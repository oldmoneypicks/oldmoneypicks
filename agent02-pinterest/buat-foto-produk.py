#!/usr/bin/env python3
"""Gambar produk dari FOTO RESMI merek (aturan Pak 28 Sep 2026: foto aktual, bukan kartu teks).

Membuat dua berkas per produk di website/images/products/:
  <slug>.jpg       1000x1500 (2:3) — pin Pinterest & beranda: foto besar + nama + 3 fakta
  <slug>-card.png  1400x640        — slot gambar di artikel: foto di kiri, teks di kanan
Foto sumber disimpan di foto-resmi/ bersama asal URL-nya (foto-resmi/SUMBER.md).

Pakai: python3 buat-foto-produk.py foto-produk.json
"""
import json, sys, pathlib
from PIL import Image, ImageDraw, ImageFont, ImageChops

AKAR = pathlib.Path(__file__).parent
OUT = AKAR.parent / "website" / "images" / "products"
SERIF = "/System/Library/Fonts/Supplemental/Didot.ttc"
SANS = "/System/Library/Fonts/Supplemental/Arial.ttf"
BG, INK, GOLD, GREY = (250, 248, 244), (28, 28, 28), (150, 118, 40), (95, 95, 95)


def buka(p):
    im = Image.open(AKAR / "foto-resmi" / p)
    if im.mode in ("RGBA", "LA", "P"):
        im = im.convert("RGBA"); bg = Image.new("RGB", im.size, (255, 255, 255))
        bg.paste(im, mask=im.split()[3]); im = bg
    im = im.convert("RGB")
    # pangkas latar putih/abu terang di sekeliling barang
    diff = ImageChops.difference(im, Image.new("RGB", im.size, im.getpixel((2, 2))))
    bb = diff.convert("L").point(lambda v: 255 if v > 18 else 0).getbbox()
    if bb:
        m = 20; bb = (max(0, bb[0]-m), max(0, bb[1]-m), min(im.width, bb[2]+m), min(im.height, bb[3]+m))
        im = im.crop(bb)
    return im


def pas(kanvas, im, box):
    x0, y0, x1, y1 = box
    im = im.copy(); s = min((x1-x0)/im.width, (y1-y0)/im.height); im = im.resize((int(im.width*s), int(im.height*s)), Image.LANCZOS)
    # latar putih foto dilebur ke kartu putih bersih
    kotak = Image.new("RGB", (x1-x0, y1-y0), (255, 255, 255))
    kotak.paste(im, ((x1-x0-im.width)//2, (y1-y0-im.height)//2))
    kanvas.paste(kotak, (x0, y0))


def tengah(d, y, s, f, isi, w):
    d.text(((w - d.textlength(s, font=f))/2, y), s, font=f, fill=isi)


def potret(p):
    k = Image.new("RGB", (1000, 1500), BG); d = ImageDraw.Draw(k)
    d.rectangle((40, 40, 960, 1110), fill=(255, 255, 255))
    pas(k, buka(p["foto"]), (90, 90, 910, 1060))
    tengah(d, 1150, p["merek"].upper(), ImageFont.truetype(SANS, 28), GOLD, 1000)
    tengah(d, 1195, p["model"], ImageFont.truetype(SERIF, 64), INK, 1000)
    tengah(d, 1300, "  ·  ".join(p["fakta"]), ImageFont.truetype(SANS, 27), GREY, 1000)
    tengah(d, 1420, "OLDMONEYPICKS.COM", ImageFont.truetype(SANS, 22), GOLD, 1000)
    k.save(OUT / f'{p["slug"]}.jpg', "JPEG", quality=90, optimize=True)


def lanskap(p):
    k = Image.new("RGB", (1400, 640), BG); d = ImageDraw.Draw(k)
    d.rectangle((0, 0, 700, 640), fill=(255, 255, 255))
    pas(k, buka(p["foto"]), (40, 30, 660, 610))
    d.text((760, 150), p["merek"].upper(), font=ImageFont.truetype(SANS, 26), fill=GOLD)
    d.text((760, 190), p["model"], font=ImageFont.truetype(SERIF, 56), fill=INK)
    y = 300
    for f in p["fakta"]:
        d.text((760, y), "—  " + f, font=ImageFont.truetype(SANS, 28), fill=GREY); y += 52
    k.save(OUT / f'{p["slug"]}-card.png', optimize=True)


if __name__ == "__main__":
    for p in json.loads(pathlib.Path(sys.argv[1]).read_text(encoding="utf-8")):
        potret(p); lanskap(p); print("dibuat:", p["slug"])
