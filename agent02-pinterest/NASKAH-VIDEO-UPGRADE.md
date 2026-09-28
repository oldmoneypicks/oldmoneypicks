# Naskah rekaman video — pengajuan Standard access Pinterest

Tujuan video ini menurut syarat Pinterest: memperlihatkan **alur OAuth berjalan**
dan **integrasi API yang hidup**. Bukan iklan, bukan penjelasan bisnis — cukup
bukti bahwa app-nya betul-betul jalan. **Target 90–120 detik.**

## Sebelum merekam — 5 hal

1. **Tutup semua tab yang tidak perlu.** Bilah tab Chrome sekarang penuh sekali;
   peninjau melihat seluruh layar. Pakai jendela Chrome baru yang bersih.
2. **Jangan pernah membuka `.env` di layar.** Semua skrip di bawah sudah dibuat
   supaya tidak pernah mencetak token. Jangan menjalankan `cat .env`.
3. Perbesar huruf Terminal (⌘ +) sampai mudah terbaca di video.
4. Rekam dengan **⌘⇧5** → *Record Selected Portion* atau *Entire Screen* → Record.
5. Siapkan dua jendela berdampingan: Terminal dan Chrome.

## Urutan pengambilan

### Adegan 1 — situs yang memakai API (0:00–0:15)
Buka `https://oldmoneypicks.com`, gulir sampai footer sampai terlihat
**Privacy & Disclosure**, klik, biarkan halaman privasi terbuka 2 detik.

> Teks/ucapan: *"This is our site, oldmoneypicks.com. Privacy policy is linked in the footer."*

### Adegan 2 — app di portal (0:15–0:30)
Buka **developers.pinterest.com → My apps → oldmoneypicks-agent → Configure**.
Perlihatkan **App ID 1610309** dan daftar **Redirect URIs** yang berisi
`http://localhost:8085/callback`.

> *"Our app, with the redirect URI registered."*

### Adegan 3 — alur OAuth, ini bagian terpenting (0:30–1:10)
Di Terminal:

```
cd ~/affiliate-oldmoney/agent02-pinterest
python3 ambil-token-tulis.py
```

Yang harus terlihat berurutan, tanpa dipotong:
1. Terminal mencetak "Membuka halaman izin Pinterest…"
2. Chrome membuka **halaman izin Pinterest** — tahan 2–3 detik supaya nama app
   dan daftar izinnya terbaca kamera
3. Tekan **Allow**
4. Halaman berganti jadi **"Berhasil. Tutup tab ini…"**
5. Kembali ke Terminal — terlihat baris:
   `scope : boards:read boards:write pins:read pins:write user_accounts:read`
   dan `berlaku: 2592000 detik`

> *"The user grants consent, Pinterest redirects back to our local callback, and the app exchanges the code for a token. The token itself is never displayed."*

**Jangan dipotong di tengah.** Justru ketersambungan langkah 1→5 itu yang dinilai.

### Adegan 4 — API-nya sungguh dipakai (1:10–1:35)
```
python3 demo-api.py
```
Terlihat: nama akun, 6 papan beserta jumlah pin, lalu 3 pin terbaru di
Timeless Watches.

> *"Three live API calls: user account, boards, and pins on a board."*

### Adegan 5 — yang diminta izinnya (1:35–2:00)
```
python3 kirim-pin.py pins-10-sep.json
```
Biarkan pesan penolakannya terlihat jelas:
`403 code 29 — Apps with Trial access may not create Pins in production`

Lalu jalankan yang sandbox supaya terlihat pipanya memang lengkap:
```
python3 kirim-pin.py pins-10-sep.json --sandbox
```

> *"This is exactly why we're requesting Standard access: pin creation works,
> but production is closed to Trial apps. We publish our own guides to our own
> boards — no third-party posting."*

Adegan 5 boleh dilewati kalau videonya jadi terlalu panjang. Adegan 3 tidak boleh.

## Sesudah merekam
- Tonton sekali sampai habis, khusus mencari: apakah ada token, kata sandi, atau
  isi `.env` yang tidak sengaja terlihat. Kalau ada — ulangi, jangan diedit.
- My apps → tombol **Upgrade** di kartu app → periksa keterangan app dan privacy
  policy → unggah video → **Submit**.
- Hasilnya lewat email, tanpa janji tanggal.

## Catatan kecil tapi penting
Menjalankan `ambil-token-tulis.py` di depan kamera akan **menimpa token yang
sekarang** dengan token baru — itu justru bagus, hitungan 30 harinya mulai dari
nol lagi, dan token barunya sekaligus mendapat `user_accounts:read` yang
sebelumnya belum diminta.
