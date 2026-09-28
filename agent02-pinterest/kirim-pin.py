#!/usr/bin/env python3
"""Memposting pin ke Pinterest lewat API resmi v5.

Pakai:  python3 kirim-pin.py pins-10-sep.json              (produksi — pin sungguhan)
        python3 kirim-pin.py pins-10-sep.json --sandbox    (uji coba — pin hanya terlihat sendiri)
Butuh:  PINTEREST_ACCESS_TOKEN (produksi) atau PINTEREST_SANDBOX_TOKEN (--sandbox) di .env,
        scope: boards:read, boards:write, pins:write.

Catatan 10 Sep 2026: selama app masih Trial access, produksi menolak dengan
HTTP 403 code 29 — pin sungguhan baru bisa dibuat sesudah app naik ke Standard
access. Sampai itu, --sandbox untuk menguji pipa, dan pin sungguhan dipasang tangan.

Gambar dikirim sebagai base64 langsung dari berkas lokal — tidak perlu gambarnya
lebih dulu terbit di internet.
"""
import base64, json, os, pathlib, re, sys, urllib.request, urllib.error

HERE = pathlib.Path(__file__).parent
SANDBOX = "--sandbox" in sys.argv
API = ("https://api-sandbox.pinterest.com/v5" if SANDBOX
       else "https://api.pinterest.com/v5")
KUNCI = "PINTEREST_SANDBOX_TOKEN" if SANDBOX else "PINTEREST_ACCESS_TOKEN"

def env():
    for baris in (HERE / ".env").read_text(encoding="utf-8").splitlines():
        if baris.startswith(KUNCI + "="):
            nilai = baris.split("=", 1)[1].strip()
            if nilai and not nilai.startswith("isi-"):
                return nilai
    sys.exit(f"{KUNCI} tidak ada di .env — lihat CARA-DAPAT-TOKEN.md")

def panggil(jalur, token, data=None):
    req = urllib.request.Request(API + jalur, method="POST" if data else "GET",
        data=json.dumps(data).encode() if data else None,
        headers={"Authorization": "Bearer " + token, "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        isi = e.read().decode()
        if e.code == 401:
            sys.exit(f"Token ditolak (401). Perbarui {KUNCI} di .env — "
                     "lihat CARA-DAPAT-TOKEN.md.")
        if e.code == 403 and '"code":29' in isi:
            sys.exit("Ditolak (403 code 29): app masih Trial access, produksi belum boleh "
                     "membuat pin. Naikkan ke Standard access, atau uji dengan --sandbox. "
                     "Langkahnya di CARA-DAPAT-TOKEN.md.")
        sys.exit(f"HTTP {e.code}: {isi[:300]}")

def norm(nama):
    """Cocokkan nama papan tanpa peduli emoji, spasi, atau huruf besar-kecil."""
    return re.sub(r"[^a-z0-9]+", "", nama.lower())

def main():
    token = env()
    berkas = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not berkas:
        sys.exit("Pakai: python3 kirim-pin.py <spec.json> [--sandbox]")
    spec = json.loads(pathlib.Path(berkas[0]).read_text(encoding="utf-8"))
    print("Lingkungan:", "SANDBOX (pin tidak terlihat orang lain)" if SANDBOX else "PRODUKSI")
    daftar = panggil("/boards?page_size=50", token)["items"]
    papan = {norm(b["name"]): b["id"] for b in daftar}
    print("Papan ditemukan:", ", ".join(b["name"] for b in daftar) or "(kosong)")

    for p in spec:
        nama = p.get("papan", "Timeless Watches")
        if norm(nama) not in papan:
            print(f"  ! papan '{nama}' tidak ada — dilewati"); continue
        png = HERE / "pins" / (p["slug"] + ".png")
        hasil = panggil("/pins", token, {
            "board_id": papan[norm(nama)],
            "title": p["judul"][:100],
            "description": p["deskripsi"],
            "link": p["tujuan"],
            "media_source": {"source_type": "image_base64", "content_type": "image/png",
                             "data": base64.b64encode(png.read_bytes()).decode()},
        })
        print(f"  ✓ {p['slug']} → https://pinterest.com/pin/{hasil['id']}")

if __name__ == "__main__":
    main()
