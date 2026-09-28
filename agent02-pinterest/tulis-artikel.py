#!/usr/bin/env python3
"""Tulis ulang isi artikel blog dari berkas spesifikasi JSON (aturan 5 tahap, 28 Sep 2026).

Kepala halaman, gaya, navigasi dan kaki tetap; yang diganti hanya <title>, meta
description, JSON-LD (headline/description/image/dateModified) dan isi <article>.

Pakai: python3 tulis-artikel.py artikel/<slug>.json
Spesifikasi: slug, eyebrow, title, description, date, minutes, intro[], picks[
  {name, kicker, img, alt, paras[], asin, brand, category, verdict}], closing[]
"""
import json, re, sys, pathlib, html

BLOG = pathlib.Path(__file__).resolve().parent.parent / "website" / "blog"
TAG = "oldmoneypicks-20"
IMG = "https://oldmoneypicks.com/images/products/"


def e(s):
    return html.escape(s, quote=True)


def pick(n, p):
    url = f"https://www.amazon.com/dp/{p['asin']}?tag={TAG}"
    js = ("gtag('event','affiliate_click',{'item_name':'%s','item_brand':'%s','item_category':'%s',"
          "'link_url':'%s','page_type':'blog'});") % tuple(
        e(x).replace("'", "\\'") for x in (p["name"], p["brand"], p["category"], url))
    paras = "\n".join(f"                <p>{x}</p>" for x in p["paras"])
    return f"""        <h2><span class="rank">{n:02d}</span>{e(p['name'])}</h2>
        <p class="kicker">{e(p['kicker'])}</p>
        <div class="pick">
            <img src="{IMG}{p['img']}" alt="{e(p['alt'])}" loading="lazy">
            <div class="pick-body">
{paras}
                <a href="{url}" target="_blank" rel="nofollow sponsored" class="btn-shop" onclick="{js}">Shop Now</a>
                <p class="verdict">Best for: {p['verdict']}</p>
            </div>
        </div>
"""


def main(spec_path):
    s = json.loads(pathlib.Path(spec_path).read_text(encoding="utf-8"))
    f = BLOG / s["slug"] / "index.html"
    t = f.read_text(encoding="utf-8")
    body = [f'<article class="article">',
            f'        <span class="eyebrow">{e(s["eyebrow"])}</span>',
            f'        <h1>{e(s["title"])}</h1>',
            f'        <p class="meta">{s["date"]} · {s["minutes"]} min read</p>', "",
            '        <p class="disclosure">As an Amazon Associate, we earn from qualifying purchases. '
            'Every pick below is independently curated — prices and stock change on Amazon, so check the listing before you buy.</p>', ""]
    body += [f"        <p>{x}</p>\n" for x in s["intro"]]
    body += [pick(i, p) for i, p in enumerate(s["picks"], 1)]
    body += [f"        <p>{x}</p>\n" for x in s["closing"]]
    body.append("    </article>")
    t = re.sub(r'<article class="article">.*?</article>', lambda m: "\n".join(body), t, count=1, flags=re.S)
    t = re.sub(r"<title>.*?</title>", f"<title>{e(s['title'])} — The Old Money Picks</title>", t, count=1)
    t = re.sub(r'(<meta name="description" content=")[^"]*(")', lambda m: m.group(1) + e(s["description"]) + m.group(2), t, count=1)
    t = re.sub(r'("headline": ")[^"]*(")', lambda m: m.group(1) + s["title"] + m.group(2), t, count=1)
    t = re.sub(r'("description": ")[^"]*(")', lambda m: m.group(1) + s["description"].replace('"', "'") + m.group(2), t, count=1)
    t = re.sub(r'("image": ")[^"]*(")', lambda m: m.group(1) + IMG + s["picks"][0]["img"] + m.group(2), t, count=1)
    t = re.sub(r'("dateModified": ")[^"]*(")', lambda m: m.group(1) + s["modified"] + m.group(2), t, count=1)
    for k in ("og:title", "twitter:title"):
        t = re.sub(rf'(<meta (?:property|name)="{k}" content=")[^"]*(")', lambda m: m.group(1) + e(s["title"]) + m.group(2), t)
    for k in ("og:description", "twitter:description"):
        t = re.sub(rf'(<meta (?:property|name)="{k}" content=")[^"]*(")', lambda m: m.group(1) + e(s["description"]) + m.group(2), t)
    f.write_text(t, encoding="utf-8")
    kata = len(re.sub(r"<[^>]+>", " ", "\n".join(body)).split())
    print(f"ditulis: {f}  ({kata} kata, {len(s['picks'])} produk)")


if __name__ == "__main__":
    main(sys.argv[1])
