#!/usr/bin/env python3
"""Demo untuk video pengajuan Standard access: membuktikan integrasi API hidup.

Menampilkan nama akun, jumlah papan, dan isi satu papan — TIDAK PERNAH
menampilkan token. Aman direkam layar.

Pakai:  python3 demo-api.py            (produksi)
        python3 demo-api.py --sandbox  (sandbox)
"""
import json, pathlib, sys, urllib.request, urllib.error

HERE = pathlib.Path(__file__).parent
SANDBOX = "--sandbox" in sys.argv
API = "https://api-sandbox.pinterest.com/v5" if SANDBOX else "https://api.pinterest.com/v5"
KUNCI = "PINTEREST_SANDBOX_TOKEN" if SANDBOX else "PINTEREST_ACCESS_TOKEN"

def token():
    for baris in (HERE / ".env").read_text(encoding="utf-8").splitlines():
        if baris.startswith(KUNCI + "="):
            return baris.split("=", 1)[1].strip()
    sys.exit(f"{KUNCI} tidak ada di .env")

def get(jalur, wajib=True):
    req = urllib.request.Request(API + jalur, headers={"Authorization": "Bearer " + token()})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        isi = e.read().decode()[:200]
        if not wajib:            # jangan mati di tengah rekaman
            print(f"   (dilewati — HTTP {e.code})")
            return None
        sys.exit(f"HTTP {e.code}: {isi}")

def main():
    print(f"Pinterest API v5 — {'SANDBOX' if SANDBOX else 'PRODUCTION'}\n")
    print("GET /user_account")
    akun = get("/user_account", wajib=False)
    if akun:
        print("   account   :", akun.get("business_name") or akun.get("username"))
        print("   type      :", akun.get("account_type"))
        print("   followers :", akun.get("follower_count"))
        print("   monthly views:", akun.get("monthly_views"))
    print()

    papan = get("/boards?page_size=25")["items"]
    print(f"GET /boards — {len(papan)} boards")
    for b in papan:
        print(f"   {b['name']:<24} {b['pin_count']:>4} pins   id {b['id']}")
    print()

    pilih = next((b for b in papan if b["name"] == "Timeless Watches"), papan[0])
    pin = get(f"/boards/{pilih['id']}/pins?page_size=3")["items"]
    print(f"GET /boards/{pilih['id']}/pins — 3 terbaru di '{pilih['name']}'")
    for p in pin:
        print("   ", (p.get("title") or "(untitled)")[:52], "|", p.get("created_at"))

if __name__ == "__main__":
    main()
