#!/usr/bin/env python3
"""Kartu produk tipografi 2:3 (1000x1500) — PENGGANTI foto produk yang salah.

Empat berkas foto di website/images/products/ berisi jam tangan yang bukan
produknya (data/TEMUAN-GAMBAR-SALAH-8-SEP.md). Berkas itu masih hidup di
situs dan masih dipakai otomasi Make.com untuk memposting pin mingguan —
artinya foto yang salah terus terbit dengan link afiliasi yang benar.

Skrip ini menimpa berkas .jpg itu dengan kartu tipografi buatan sendiri,
rasio 2:3 sesuai syarat Pinterest. Aslinya diarsipkan ke data/gambar-salah-arsip/.

Pakai:  python3 buat-kartu-potret.py kartu-produk.json
"""
import json, subprocess, sys, pathlib, html, shutil

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
AKAR = pathlib.Path(__file__).parent.parent
OUT = AKAR / "website" / "images" / "products"
ARSIP = AKAR / "data" / "gambar-salah-arsip"

DOC = """<!doctype html><html><head><meta charset=utf-8>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600&family=Inter:wght@400;500;600&display=swap">
<style>
*{{box-sizing:border-box}}
body{{margin:0;width:1000px;height:1500px;background:#141414;color:#f2f2f2;
 font-family:Inter,sans-serif;padding:96px 84px;display:flex;flex-direction:column;
 justify-content:space-between;
 background-image:radial-gradient(circle at 78% 16%,rgba(212,175,55,.12),transparent 48%)}}
.kick{{font-size:25px;letter-spacing:.26em;text-transform:uppercase;color:#d4af37;font-weight:600}}
.merek{{font-size:31px;letter-spacing:.22em;text-transform:uppercase;color:#a6a6a6;margin-bottom:20px}}
h1{{font-family:"Cormorant Garamond",Georgia,serif;font-size:116px;line-height:1.02;
 margin:0;font-weight:600;letter-spacing:-.01em}}
.spek div{{border-top:1px solid #262626;padding:26px 0;font-size:27px;color:#a6a6a6;line-height:1.35}}
.spek b{{display:block;color:#f2f2f2;font-weight:600;font-size:31px;margin-bottom:7px}}
.kaki{{display:flex;justify-content:space-between;align-items:center;
 border-top:1px solid #262626;padding-top:28px;font-size:22px;color:#808080;letter-spacing:.09em}}
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
    src = OUT / (p["slug"] + "-potret.html"); src.write_text(doc, encoding="utf-8")
    png = OUT / (p["slug"] + "-potret.png")
    subprocess.run([CHROME, "--headless", "--disable-gpu", f"--screenshot={png}",
                    "--window-size=1000,1500", "--hide-scrollbars", f"file://{src}"],
                   capture_output=True)
    src.unlink()

    sasaran = OUT / (p["slug"] + ".jpg")
    if sasaran.exists():
        ARSIP.mkdir(parents=True, exist_ok=True)
        shutil.move(str(sasaran), str(ARSIP / sasaran.name))
    from PIL import Image
    Image.open(png).convert("RGB").save(sasaran, "JPEG", quality=88, optimize=True)
    png.unlink()
    return sasaran


if __name__ == "__main__":
    for p in json.loads(pathlib.Path(sys.argv[1]).read_text(encoding="utf-8")):
        print("ditimpa:", buat(p))
