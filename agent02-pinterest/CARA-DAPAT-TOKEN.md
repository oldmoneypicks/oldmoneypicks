# Cara mendapat PINTEREST_ACCESS_TOKEN yang bisa memposting

**Temuan 10 September 2026 (diperbarui, sesudah token pertama diuji):**
token yang keluar dari tombol **Generate access token** di halaman app itu
**baca-saja**. Dengan token itu:

- `GET /v5/user_account` → **200** (jalan)
- `GET /v5/boards` → **200** (6 papan terbaca)
- `POST /v5/pins` → **401**, pesannya jelas:
  `Missing: ['boards:write', 'pins:write']`

Jadi tombol Generate tidak cukup. Untuk memposting, Pinterest mewajibkan
**alur OAuth penuh** (Pak Stefanus menekan "Allow" sekali di browser).

## Langkah — sekali saja, ±5 menit

1. **developers.pinterest.com** → app `oldmoneypicks-agent` → **Redirect URIs**
   → tambahkan persis: `http://localhost:8085/callback` → Save.
2. Di Terminal:
   ```
   cd ~/affiliate-oldmoney/agent02-pinterest
   python3 ambil-token-tulis.py
   ```
   Browser terbuka sendiri → tekan **Allow**. Token ditulis sendiri ke `.env`
   (izin 600). Tidak perlu menempel apa pun ke chat.
3. Uji: `python3 kirim-pin.py pins-10-sep.json`

**App id** `1610309` dan **App secret** sudah ada di `.env` dengan nama kunci
`PINTEREST_APP_ID` dan `PINTEREST_APP_SECRET` (10 Sep: nama kuncinya sempat
tertulis `PINTEREST_App secret key`, sehingga skrip tidak menemukannya — sudah
dirapikan).

**Scope yang diminta:** `boards:read, boards:write, pins:read, pins:write`.

**Jangan tempelkan token ke kolom chat AI mana pun** — termasuk ke saya.
Cukup di `.env`; saya cukup memakainya dari berkas, tidak perlu melihat isinya.

**Token Pinterest kedaluwarsa ±30 hari.** Kalau suatu hari skripnya menjawab 401,
itu bukan kerusakan — ulangi langkah 2. (`PINTEREST_REFRESH_TOKEN` ikut disimpan,
jadi nanti bisa diperpanjang tanpa menekan Allow lagi.)

---

## Temuan lanjutan 10 Sep 2026 malam — token sudah benar, tapi app-nya belum boleh

Sesudah Allow ditekan, token tulis berhasil tersimpan:
`scope: boards:read boards:write pins:read pins:write`, berlaku 2.592.000 detik
(**30 hari — kedaluwarsa ±10 Oktober 2026**).

Tapi `POST /v5/pins` ke produksi menjawab:

```
HTTP 403 {"code":29,"message":"Apps with Trial access may not create Pins in
production https://api.pinterest.com - use API Sandbox instead."}
```

**Jadi penghalangnya bukan token lagi, melainkan tingkat akses app.** Menurut
dokumentasi Pinterest (Access tiers):

| | Trial access (sekarang) | Standard access (yang dibutuhkan) |
|---|---|---|
| Pin yang dibuat API | hanya entitas Sandbox, **hanya terlihat oleh diri sendiri** | terbit sungguhan di profil |
| Batas panggilan | per hari per app | per menit per pengguna per app |
| Kalimat kuncinya | "may not create Pins in production" | — |

### Naik ke Standard access — 5 langkah di portal

1. **My apps** → tombol **Upgrade** di kartu app
2. Periksa lagi keterangan app (use case, privacy policy)
3. **Unggah video demonstrasi** — harus memperlihatkan alur OAuth berjalan
   dan integrasi API-nya hidup
4. Kirim permintaan
5. Menunggu — Pinterest meninjau berkala, kabarnya lewat email, tanpa janji tanggal

**Syarat yang sudah dipegang:** app sudah lolos Trial; alur OAuth sudah berjalan
sungguhan (rekaman langkah tadi persis bahan videonya); halaman privasi ada di
`https://oldmoneypicks.com/privacy/` (**200**).

**Yang masih kurang:** halaman privasi itu **tidak tertaut dari beranda**.
Peninjau biasanya mencari tautannya, bukan menebak alamatnya — pasang di footer.

### Sementara Standard belum turun

- Pin sungguhan **dipasang tangan** dari HP (gambarnya sudah jadi di `pins/`).
- Pipa otomatisnya diuji lewat Sandbox:
  ```
  python3 ambil-token-tulis.py --sandbox     # token khusus sandbox
  python3 kirim-pin.py pins-10-sep.json --sandbox
  ```
  Token sandbox dan token produksi **tidak bisa saling dipakai** — disimpan
  terpisah di `.env` sebagai `PINTEREST_SANDBOX_TOKEN`.
