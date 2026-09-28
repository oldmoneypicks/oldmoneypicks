#!/usr/bin/env python3
"""Kartu produk tipografi untuk artikel blog — pengganti foto produk.

Dipakai karena empat foto produk di repo berisi jam tangan yang salah
(data/TEMUAN-GAMBAR-SALAH-8-SEP.md) dan PA-API Amazon baru terbuka sesudah
3 penjualan. Kartu ini hanya memuat keterangan yang SUDAH ada di artikel —
tidak menambah klaim baru yang bisa salah lagi.

Pakai:  python3 buat-kartu-produk.py kartu-produk.json
Hasil:  ../website/images/products/<slug>-card.png  (1400x640, ikut .pick img)
"""
import json, subprocess, sys, pathlib, html

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
OUT = pathlib.Path(__file__).parent.parent / "website" / "images" / "products"

DOC = """<!doctype html><html><head><meta charset=utf-8>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600&family=Inter:wght@400;500;600&display=swap">
<style>
*{{box-sizing:border-box}}
body{{margin:0;width:1400px;height:640px;background:#141414;color:#f2f2f2;
 font-family:Inter,sans-serif;padding:66px 74px;display:flex;flex-direction:column;
 justify-content:space-between;
 background-image:radial-gradient(circle at 82% 22%,rgba(212,175,55,.10),transparent 46%)}}
.kick{{font-size:20px;letter-spacing:.26em;text-transform:uppercase;color:#d4af37;font-weight:600}}
.merek{{font-size:25px;letter-spacing:.20em;text-transform:uppercase;color:#a6a6a6;margin-bottom:14px}}
h1{{font-family:"Cormorant Garamond",Georgia,serif;font-size:82px;line-height:1.03;
 margin:0;font-weight:600;letter-spacing:-.01em}}
.spek{{display:flex;gap:0;margin-top:6px}}
.spek div{{padding-right:44px;margin-right:44px;border-right:1px solid #262626;
 font-size:23px;color:#a6a6a6;line-height:1.35}}
.spek div:last-child{{border-right:none;margin-right:0;padding-right:0}}
.spek b{{display:block;color:#f2f2f2;font-weight:600;font-size:25px;margin-bottom:5px}}
.kaki{{display:flex;justify-content:space-between;align-items:center;
 border-top:1px solid #262626;padding-top:22px;font-size:19px;color:#808080;letter-spacing:.09em}}
.kaki b{{color:#d4af37;font-weight:600;letter-spacing:.14em;text-transform:uppercase}}
</style></head><body>
<div class="kick">{kick}</div>
<div><div class="merek">{merek}</div><h1>{model}</h1></div>
<div class="spek">{spek}</div>
<div class="kaki"><span>OLDMONEYPICKS.COM</span><b>{tag}</b></div>
</body></html>"""

def buat(p):
    spek = "".join(f"<div><b>{html.escape(n)}</b>{html.escape(v)}</div>"
                   for n, v in p["spek"])
    doc = DOC.format(kick=html.escape(p["kick"]), merek=html.escape(p["merek"]),
                     model=html.escape(p["model"]), spek=spek, tag=html.escape(p["tag"]))
    OUT.mkdir(parents=True, exist_ok=True)
    src = OUT / (p["slug"] + "-card.html"); src.write_text(doc, encoding="utf-8")
    png = OUT / (p["slug"] + "-card.png")
    subprocess.run([CHROME, "--headless", "--disable-gpu", f"--screenshot={png}",
                    "--window-size=1400,640", "--hide-scrollbars", f"file://{src}"],
                   capture_output=True)
    src.unlink()
    return png

if __name__ == "__main__":
    for p in json.loads(pathlib.Path(sys.argv[1]).read_text(encoding="utf-8")):
        print("dibuat:", buat(p))
