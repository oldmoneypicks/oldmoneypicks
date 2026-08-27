# Prompt untuk Grok Bot — OldMoneyPicks

> Sebelum dipakai, baca `RUNBOOK.md` bagian "Aturan kredensial".
> **Jangan pernah** mengetik password Pinterest / GitHub / email ke kolom chat Grok Bot.
> Yang diberikan hanya **token** yang bisa dicabut kapan saja.

---

## Prompt A — Riset & Draft Artikel (aman, tidak menyentuh akun apa pun)

```
You are my content researcher for oldmoneypicks.com, a curated quiet-luxury
affiliate site (Amazon Associates). The site is a static HTML site — there is
NO WordPress, so do not attempt to log in to any CMS.

Your job this week:

1. Research what is trending in "quiet luxury", "old money aesthetic", and
   "classic menswear" over the last 14 days. Use Pinterest Trends, Google
   Trends, and Reddit (r/malefashionadvice, r/Watches).

2. Give me the 5 highest-opportunity article topics: high search interest,
   low competition, and mappable to products I already sell. My current
   categories are: Timeless Watches, Quiet Luxury Leather, Signature Scents,
   Quiet Luxury Fashion, Elegant Living.

3. For the single best topic, write a complete 800-word article in the house
   voice: understated, declarative, no hype, no exclamation marks, British-ish
   restraint. Structure: intro, 5 numbered picks, a short "how to choose"
   closing. For each pick include a one-line "Best for:" verdict.

4. For product links, use the placeholder [AFFILIATE_LINK: <product name>].
   Do NOT invent Amazon URLs. Do NOT state specific dollar prices — Amazon
   prices change and the Associates programme restricts quoting them.

5. Output the article as raw markdown in the chat. Do not publish anywhere.
```

## Prompt B — Pinterest Pin Copy (aman, tidak menyentuh akun apa pun)

```
Write 5 Pinterest pin descriptions for this article: <paste article URL>.

Rules:
- Each description max 480 characters.
- Front-load the hook in the first 60 characters (that is all that shows in feed).
- End each with 5 hashtags drawn from: #quietluxury #oldmoneyaesthetic
  #oldmoneystyle #classicmenswear #minimaliststyle #gentlemanstyle #timelessstyle
- No emoji. No "click here". Write like a magazine caption, not an ad.
- Output as CSV with columns: Pin Title, Pin Description, Image URL, Destination Link.
- Destination Link is always the article URL above.
```

## Prompt C — Laporan Harian (butuh akses akun — lakukan SETELAH langkah keamanan di RUNBOOK)

```
Every day at 20:00 Asia/Jakarta, produce a one-screen report for me:

1. Google Analytics (property G-5MXY6JHJLC): sessions yesterday, top 5 landing
   pages, and the number of 'affiliate' category click events.
2. Pinterest business account @theoldmoneypicks: impressions and outbound
   clicks for the last 7 days, and which pin performed best.
3. Amazon Associates dashboard: clicks, ordered items, and estimated earnings
   for the current month to date.

Format: bullet points, under 150 words, numbers only — no commentary unless
something dropped more than 30% versus the previous week. Send it to me and
stop. Do not take any other action.
```

---

## Yang TIDAK boleh diberikan ke Grok Bot

| Jangan | Pakai ini sebagai gantinya |
|---|---|
| Password Pinterest | `PINTEREST_ACCESS_TOKEN` (sudah ada di `agent02-pinterest/.env`) |
| Password GitHub | Fine-grained PAT, scope: repo `oldmoneypicks/oldmoneypicks` saja |
| Password email / WhatsApp | Tidak usah sama sekali — Grok Bot tidak menyentuh chat pasien |
| Login Amazon Associates | Read-only report saja, dan cabut aksesnya setelah selesai |
