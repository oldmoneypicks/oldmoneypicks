#!/usr/bin/env python3
"""Pembuat gambar pin Pinterest — tipografi, tanpa foto produk.

Alasannya ada di data/TEMUAN-GAMBAR-SALAH-8-SEP.md: empat foto produk di repo
berisi jam tangan yang salah, dan PA-API Amazon (satu-satunya sumber foto produk
yang halal dipakai) baru terbuka sesudah 3 penjualan. Sampai saat itu, gambar
buatan sendiri adalah satu-satunya yang aman.

Pakai:  python3 buat-pin.py pins.json
Hasil:  pins/<slug>.png  — 1000x1500, ukuran baku Pinterest 2:3
"""
import json, subprocess, sys, pathlib, html

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
HERE = pathlib.Path(__file__).parent
OUT = HERE / "pins"

TEMA = {
    # nama: (latar, tinta, aksen, garis)
    "krem":  ("#F2EFE9", "#1C1A17", "#6B5B3E", "#D6CFC2"),
    "hijau": ("#1F2A24", "#F1EDE4", "#B9A16B", "#3A4840"),
    "biru":  ("#1B2430", "#EFEDE7", "#9CB2C7", "#33404F"),
}

HTML = """<!doctype html><html><head><meta charset=utf-8>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600&family=Inter:wght@400;500;600&display=swap">
<style>
@page{{size:1000px 1500px;margin:0}}
*{{box-sizing:border-box}}
body{{margin:0;width:1000px;height:1500px;background:{bg};color:{ink};
  font-family:Inter,-apple-system,sans-serif;display:flex;flex-direction:column;
  justify-content:space-between;padding:78px 76px}}
.kop{{font-size:19px;letter-spacing:.30em;text-transform:uppercase;color:{acc};font-weight:600}}
.garis{{height:1px;background:{line};margin:26px 0 0}}
h1{{font-family:"Cormorant Garamond",Georgia,serif;font-weight:600;font-size:96px;
  line-height:1.04;margin:0;letter-spacing:-.015em;text-wrap:balance}}
.sub{{font-size:29px;line-height:1.48;color:{ink};opacity:.82;margin-top:34px;max-width:680px}}
.no{{font-family:"Cormorant Garamond",Georgia,serif;font-size:150px;line-height:1;
  color:{acc};opacity:.30;margin:0 0 14px}}
.kaki{{display:flex;justify-content:space-between;align-items:flex-end;gap:20px}}
.situs{{font-size:24px;letter-spacing:.10em;font-weight:600;text-transform:uppercase}}
.tag{{font-size:19px;color:{acc};letter-spacing:.05em;text-align:right;line-height:1.6}}
.tengah{{flex:1;display:flex;flex-direction:column;justify-content:center;padding:40px 0}}
</style></head><body>
<div><div class="kop">{kop}</div><div class="garis"></div></div>
<div class="tengah">{no}<h1>{judul}</h1><div class="sub">{sub}</div></div>
<div><div class="garis" style="margin-bottom:26px"></div>
<div class="kaki"><div class="situs">oldmoneypicks.com</div><div class="tag">{tag}</div></div></div>
</body></html>"""

def buat(p):
    bg, ink, acc, line = TEMA[p.get("tema", "krem")]
    doc = HTML.format(bg=bg, ink=ink, acc=acc, line=line,
        kop=html.escape(p["kop"]), judul=html.escape(p["judul"]),
        sub=html.escape(p["sub"]), tag=html.escape(p.get("tag", "")),
        no=f'<div class="no">{html.escape(p["no"])}</div>' if p.get("no") else "")
    OUT.mkdir(exist_ok=True)
    src = OUT / (p["slug"] + ".html"); src.write_text(doc, encoding="utf-8")
    png = OUT / (p["slug"] + ".png")
    subprocess.run([CHROME, "--headless", "--disable-gpu", f"--screenshot={png}",
                    "--window-size=1000,1500", "--hide-scrollbars",
                    f"file://{src}"], capture_output=True)
    return png

if __name__ == "__main__":
    spec = json.loads(pathlib.Path(sys.argv[1]).read_text(encoding="utf-8"))
    for p in spec:
        print("dibuat:", buat(p))
