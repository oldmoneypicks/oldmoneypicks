# Panduan Pinterest — 10 September 2026

Tiga bagian. **Bagian 1 dulu** (posting dua pin, 5 menit), baru Bagian 2
(token, 10 menit) kalau Bapak sempat. Bagian 3 cuma untuk berjaga-jaga.

---

# BAGIAN 1 · Posting dua pin — tinggal ketuk

Gambar pinnya **sudah terbit di situs sendiri**, jadi tautan di bawah membawa
gambar, deskripsi, dan tautan tujuan sekaligus. Judul saja yang perlu diketik —
sudah saya siapkan untuk disalin.

> Kalau di HP tautan ini membuka aplikasi Pinterest dan tampilannya kosong,
> jangan dipaksa: tutup, lalu **buka tautannya di Chrome** dan pilih
> *"Buka di browser"* / *"Desktop site"*. Tombol Save versi web inilah yang
> membawa isian otomatis; aplikasi HP sering mengabaikannya.

## Pin 3 — papan ⌚ Timeless Watches

**Judul (salin ini):**
```
The Most Self-Assured Watch You Can Wear
```

**[→ KETUK: simpan Pin 3 ke Pinterest](https://www.pinterest.com/pin/create/button/?url=https%3A%2F%2Foldmoneypicks.com%2Fblog%2Fquiet-luxury-watches-that-look-expensive%2F&media=https%3A%2F%2Foldmoneypicks.com%2Fimages%2Fpins%2F03-casio-a168.png&description=It+costs+less+than+dinner+and+outlasts+every+trend.+Why+the+gold+digital+square+reads+as+old+money+%E2%80%94+and+the+four+watches+that+do+the+same.+%23quietluxury+%23oldmoneyaesthetic+%23watchesformen+%23minimaliststyle+%23timelessstyle)**

## Pin 4 — papan yang sama

**Judul (salin ini):**
```
Mid-Century Character, No Vintage Repair Bills
```

**[→ KETUK: simpan Pin 4 ke Pinterest](https://www.pinterest.com/pin/create/button/?url=https%3A%2F%2Foldmoneypicks.com%2Fblog%2Fquiet-luxury-watches-that-look-expensive%2F&media=https%3A%2F%2Foldmoneypicks.com%2Fimages%2Fpins%2F04-timex-marlin.png&description=A+hand-wound+dress+watch+with+a+domed+acrylic+crystal+%E2%80%94+the+1960s+silhouette%2C+without+a+60-year-old+movement+to+service.+Four+quiet+luxury+watches+on+the+blog.+%23oldmoneystyle+%23dresswatch+%23quietluxurywatch+%23mensaccessories+%23vintagestyle)**

Sesudah tersimpan, periksa satu hal saja: **tautan tujuan pin** harus
`oldmoneypicks.com/blog/quiet-luxury-watches-that-look-expensive/`.
Kalau kosong, pinnya tidak membawa siapa pun ke situs — dan itu satu-satunya
gunanya pin ini ada.

---

# BAGIAN 2 · Mendapat Pinterest Access Token — langkah demi langkah

Sesudah ini selesai, saya bisa memposting pin sendiri dari laptop tanpa Bapak
menyentuh apa pun. **Lakukan di laptop**, bukan HP — halaman developer Pinterest
sulit dipakai di layar kecil, dan tokennya harus disalin ke berkas di laptop.

### Langkah 1 — buka halaman developer
Buka **https://developers.pinterest.com/apps/** di Chrome laptop.
Pastikan yang login akun **@theoldmoneypicks** (cek foto profil di pojok kanan atas).

### Langkah 2 — buat app
Klik **Create app** (atau *Connect app* kalau itu yang muncul).

| Kolom | Isi |
|---|---|
| App name | `oldmoneypicks-agent` |
| App description | `Posting pin otomatis untuk blog oldmoneypicks.com` |
| Website URL | `https://oldmoneypicks.com` |

Kalau diminta memilih jenis akses: pilih **Standard access** / *Trial access*.
**Jangan** mengajukan app review — itu untuk yang memposting ke akun orang lain.
Untuk akun sendiri, akses standar sudah cukup.

### Langkah 3 — pilih izin yang sesempit mungkin
Di halaman app, cari bagian **Scopes** / *Permissions*. Centang **dua saja**:

- `boards:read` — supaya agen tahu id papan ⌚ Timeless Watches
- `pins:write` — supaya agen bisa memposting

Jangan centang yang lain. Makin sempit izinnya, makin kecil kerugiannya
kalau suatu saat tokennya bocor.

### Langkah 4 — buat tokennya
Klik **Generate access token**. Akan muncul teks panjang (biasanya diawali
`pina_`). **Salin sekarang juga** — Pinterest hanya menampilkannya satu kali.

### Langkah 5 — tempel ke laptop
Di Terminal:

```
nano ~/affiliate-oldmoney/agent02-pinterest/.env
```

Ganti baris `PINTEREST_ACCESS_TOKEN=isi-...` menjadi token yang tadi disalin.
Simpan dengan `Ctrl+O`, `Enter`, lalu `Ctrl+X`. Lalu kunci berkasnya:

```
chmod 600 ~/affiliate-oldmoney/agent02-pinterest/.env
```

### Langkah 6 — uji
```
cd ~/affiliate-oldmoney/agent02-pinterest && python3 kirim-pin.py pins-10-sep.json
```
Kalau berhasil, dia mencetak tautan pin yang baru terbit.

> **Jangan pernah menempelkan tokennya ke kolom chat AI mana pun, termasuk ke saya.**
> Saya membacanya langsung dari `.env` — saya tidak perlu melihat isinya.
>
> **Token Pinterest kedaluwarsa ±30 hari.** Kalau suatu hari skripnya menjawab
> `401`, itu bukan kerusakan: ulangi Langkah 4 dan 5.

---

# BAGIAN 3 · Kalau tautan ketuk gagal — posting manual dari HP

Bapak biasa lewat laptop, jadi ini urutannya di HP:

1. Buka aplikasi **Pinterest** → ketuk foto profil (kanan bawah).
2. Ketuk tanda **+** besar → pilih **Pin**.
3. Ketuk kotak gambar → **Galeri/Photos** → pilih gambar pin yang saya kirim
   (cari di album *Recents*, gambar tulisan berlatar krem dan hijau tua).
4. **Title** → tempel judul dari Bagian 1.
5. **Description** → tempel deskripsi dari Bagian 1.
6. **Add a destination link** → ini yang **paling sering terlupa**. Tempel:
   ```
   https://oldmoneypicks.com/blog/quiet-luxury-watches-that-look-expensive/
   ```
7. **Choose board** → ⌚ Timeless Watches.
8. Ketuk **Publish** / *Simpan*.

Pin tanpa destination link tetap terlihat bagus tapi **tidak menghasilkan
apa-apa** — tidak ada jalan dari pin ke situs, dan tidak ada jalan dari situs
ke Amazon. Itu satu-satunya langkah yang tidak boleh dilewati.
