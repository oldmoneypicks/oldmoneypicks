#!/usr/bin/env python3
"""Mengambil access token Pinterest yang BISA MEMPOSTING (scope pins:write).

Kenapa perlu skrip ini: tombol "Generate token" di halaman app hanya memberi
token BACA SAJA — halamannya sendiri menulis "Provides limited access to
3 scopes (pins:read, boards:read, user_accounts:read, ads:read, catalogs:read)".
Tidak ada pins:write di situ, jadi token itu tidak bisa membuat pin.

Untuk pins:write, Pinterest mewajibkan alur OAuth penuh: buka halaman izin,
Pak Stefanus menekan "Allow", Pinterest mengirim balik sebuah kode ke alamat
localhost, lalu kode itu ditukar jadi token memakai App id + App secret.
Skrip ini menjalankan seluruh alur itu sendiri.

SIAPKAN DULU — dua-duanya sekali saja:
  1. Di halaman app → Redirect URIs → tambahkan persis:
         http://localhost:8085/callback
  2. Di .env, tambahkan dua baris (App secret disalin dari halaman app):
         PINTEREST_APP_ID=1610309
         PINTEREST_APP_SECRET=<tempel di sini>

JALANKAN:
     python3 ambil-token-tulis.py

Token hasilnya ditulis sendiri ke .env. Tidak perlu menempel apa pun ke chat.
"""
import base64, http.server, json, pathlib, secrets, threading, urllib.parse
import urllib.request, urllib.error, webbrowser, sys

HERE = pathlib.Path(__file__).parent
ENV = HERE / ".env"
SANDBOX = "--sandbox" in sys.argv
TOKEN_URL = ("https://api-sandbox.pinterest.com/v5/oauth/token" if SANDBOX
             else "https://api.pinterest.com/v5/oauth/token")
KUNCI_TOKEN = "PINTEREST_SANDBOX_TOKEN" if SANDBOX else "PINTEREST_ACCESS_TOKEN"
PORT = 8085
REDIRECT = f"http://localhost:{PORT}/callback"
SCOPE = "boards:read,boards:write,pins:read,pins:write,user_accounts:read"

def baca_env():
    isi = {}
    if ENV.exists():
        for baris in ENV.read_text(encoding="utf-8").splitlines():
            if "=" in baris and not baris.strip().startswith("#"):
                k, v = baris.split("=", 1)
                isi[k.strip()] = v.strip()
    return isi

def tulis_env(kunci, nilai):
    baris = ENV.read_text(encoding="utf-8").splitlines() if ENV.exists() else []
    ketemu = False
    for i, b in enumerate(baris):
        if b.startswith(kunci + "="):
            baris[i] = f"{kunci}={nilai}"; ketemu = True
    if not ketemu:
        baris.append(f"{kunci}={nilai}")
    ENV.write_text("\n".join(baris) + "\n", encoding="utf-8")
    ENV.chmod(0o600)

class Tangkap(http.server.BaseHTTPRequestHandler):
    kode = None
    state = None
    def do_GET(self):
        url = urllib.parse.urlparse(self.path)
        q = urllib.parse.parse_qs(url.query)
        kode = (q.get("code") or [None])[0]
        if kode:                      # jangan tertimpa oleh /favicon.ico dsb.
            Tangkap.kode = kode
            Tangkap.state = (q.get("state") or [None])[0]
        elif url.path != "/callback":
            self.send_response(204); self.end_headers(); return
        pesan = "Berhasil. Tutup tab ini dan kembali ke Terminal." if kode \
                else "Gagal: Pinterest tidak mengirim kode. Coba lagi."
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(f"<html><body style='font:16px system-ui;padding:40px'>"
                         f"<h2>{pesan}</h2></body></html>".encode())
    def log_message(self, *a):
        pass

def main():
    env = baca_env()
    app_id = env.get("PINTEREST_APP_ID")
    rahasia = env.get("PINTEREST_APP_SECRET")
    if not app_id or not rahasia or rahasia.startswith("isi-"):
        sys.exit("PINTEREST_APP_ID atau PINTEREST_APP_SECRET belum ada di .env.\n"
                 "Baca bagian SIAPKAN DULU di atas berkas ini.")

    state = secrets.token_urlsafe(16)
    izin = "https://www.pinterest.com/oauth/?" + urllib.parse.urlencode({
        "client_id": app_id, "redirect_uri": REDIRECT, "response_type": "code",
        "scope": SCOPE, "state": state,
    })

    server = http.server.HTTPServer(("localhost", PORT), Tangkap)
    threading.Thread(target=server.serve_forever, daemon=True).start()

    print("Membuka halaman izin Pinterest di browser…")
    print("Kalau tidak terbuka sendiri, salin alamat ini:\n\n" + izin + "\n")
    webbrowser.open(izin)
    print("Menunggu Pak Stefanus menekan Allow…")

    for _ in range(900):
        if Tangkap.kode:
            break
        import time; time.sleep(1)
    server.shutdown()
    if not Tangkap.kode:
        sys.exit("Tidak ada kode yang masuk dalam 15 menit. Jalankan ulang.")
    if Tangkap.state != state:
        sys.exit("State tidak cocok — hentikan, jangan dilanjutkan.")

    basic = base64.b64encode(f"{app_id}:{rahasia}".encode()).decode()
    data = urllib.parse.urlencode({
        "grant_type": "authorization_code",
        "code": Tangkap.kode,
        "redirect_uri": REDIRECT,
    }).encode()
    req = urllib.request.Request(
        TOKEN_URL, data=data,
        headers={"Authorization": "Basic " + basic,
                 "Content-Type": "application/x-www-form-urlencoded"})
    try:
        with urllib.request.urlopen(req) as r:
            hasil = json.load(r)
    except urllib.error.HTTPError as e:
        sys.exit(f"Penukaran kode gagal — HTTP {e.code}: {e.read().decode()[:300]}")

    tulis_env(KUNCI_TOKEN, hasil["access_token"])
    if hasil.get("refresh_token"):
        tulis_env("PINTEREST_REFRESH_TOKEN" + ("_SANDBOX" if SANDBOX else ""),
                  hasil["refresh_token"])

    print(f"\n✓ {KUNCI_TOKEN} tersimpan ke .env (izin 600).")
    print("  scope :", hasil.get("scope", "(tidak disebut)"))
    print("  berlaku:", hasil.get("expires_in", "?"), "detik")
    print("\nSekarang bilang ke Claude: token sudah masuk.")

if __name__ == "__main__":
    main()
