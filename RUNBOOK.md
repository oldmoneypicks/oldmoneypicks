# RUNBOOK — Mengelola Klinik + OldMoneyPicks + YouTube

Terakhir diperbarui: 30 Agustus 2026

---

## 0. Koreksi penting dari percakapan AI sebelumnya

Sebelum mengeksekusi apa pun, tiga hal ini perlu diluruskan — kalau tidak,
Anda akan buang waktu:

**1. Situs Anda BUKAN WordPress.**
`oldmoneypicks.com` adalah situs HTML statis, di-deploy dari repo GitHub
`oldmoneypicks/oldmoneypicks` ke **Vercel**. Tidak ada dashboard WordPress,
tidak ada halaman login CMS. Semua prompt di percakapan itu yang berbunyi
*"log in to the WordPress dashboard"* akan gagal total — Grok Bot akan
berputar-putar mencari halaman login yang tidak pernah ada.

Artinya: menambah artikel = menambah file HTML di repo, lalu `git push`.
Vercel otomatis deploy. Itu saja.

**2. Jangan berikan password ke kolom chat AI mana pun.**
Saran *"masukkan username dan password Pinterest, Grok Bot mengamankan sesi ini"*
itu keliru dan berbahaya. Password yang diketik ke chat masuk ke riwayat
percakapan dan tidak bisa dicabut. Yang benar: pakai **token** yang scope-nya
sempit dan bisa dicabut kapan saja (caranya di Langkah 3).

Kabar baiknya, Anda sudah punya `PINTEREST_ACCESS_TOKEN` di
`agent02-pinterest/.env` — jadi Pinterest bisa diposting lewat API resmi,
tanpa browser automation, tanpa risiko akun kena flag.

**3. Soal Grok Bot dan Cursor Pro.**
Grok Bot memang nyata (rilis 11 Agustus 2026) dan menurut halaman resmi xAI
memang termasuk di paket SuperGrok dan Cursor Pro ke atas — **tapi kuotanya
terpisah** dari kuota Grok/Cursor biasa. Yang keliru adalah saran
*"pindahkan Claude Pro ke Cursor Pro, Anda dapat Claude sekaligus"*: Cursor Pro
adalah langganan IDE, bukan pengganti Claude Pro. Jangan batalkan apa pun dulu.
Coba Grok Bot dengan kuota yang sudah ada, ukur hasilnya sebulan, baru putuskan.

---

## 1. HARI INI — 20 menit: publikasikan blog

Saya sudah membuatkan fondasinya. Yang tersisa hanya di-deploy.

**Yang sudah jadi di repo Anda:**

| File | Isi |
|---|---|
| `website/blog/index.html` | Halaman index "The Journal" |
| `website/blog/quiet-luxury-watches-that-look-expensive/index.html` | Artikel 800 kata, 4 produk jam tangan, 4 link afiliasi asli Anda |
| `website/index.html` | Nav bar ditambah link ✒️ Journal |
| `website/sitemap.xml` | Ditambah 2 URL baru |
| `data/pins-blog-batch-01.csv` | 4 naskah pin Pinterest siap posting |

**Cek dulu di laptop:**

```bash
cd ~/affiliate-oldmoney/website
python3 -m http.server 8080
```

Buka `http://localhost:8080/blog/` di browser. Pastikan gambar muncul dan
tombol "Shop Now" mengarah ke `amazon.com/dp/...?tag=oldmoneypicks-20`.
Tag `oldmoneypicks-20` itulah yang membawa komisi — bukan bentuk `amzn.to/...`
yang disebut versi lama runbook ini. Keduanya sah, situs Anda memakai URL penuh.
Tekan Ctrl+C untuk berhenti.

**Kalau sudah cocok, deploy:**

```bash
cd ~/affiliate-oldmoney
git add website/ data/pins-blog-batch-01.csv RUNBOOK.md GROKBOT-PROMPT.md
git commit -m "Add blog section with first quiet luxury watches article"
git push
```

Vercel akan deploy sendiri dalam ~30 detik. Cek di
`https://oldmoneypicks.com/blog/`.

> ⚠️ Jangan `git add .` — folder `agent02-pinterest/` berisi `.env` dengan
> API key Anda. Sudah ada di `.gitignore`, tapi lebih aman menyebut file
> satu per satu.

**Terakhir, daftarkan ke Google:**
Buka Google Search Console → URL Inspection → tempel
`https://oldmoneypicks.com/blog/quiet-luxury-watches-that-look-expensive/` →
"Request Indexing". Ini mempercepat indexing dari berminggu-minggu jadi
beberapa hari.

---

## 2. HARI INI — 15 menit: posting Pinterest

Naskah 4 pin sudah siap di `data/pins-blog-batch-01.csv`. Semua mengarah ke
artikel baru, bukan ke homepage — ini penting, karena Pinterest memberi
jangkauan lebih besar ke link yang halamannya berisi konten, bukan sekadar
daftar produk.

**Cara cepat (manual, 15 menit, paling aman):**
Buka Pinterest → Create Pin → upload gambar dari
`website/images/products/` → copy-paste judul dan deskripsi dari CSV →
tempel Destination Link → Schedule.

Jadwalkan **1 pin per hari selama 4 hari**, jangan 4 sekaligus. Pinterest
menghukum posting yang menumpuk.

**Kalau mau otomatis:** token Pinterest Anda sudah ada. Bilang ke saya
*"buatkan script posting Pinterest dari CSV"* dan saya buatkan — pakai API
resmi, bukan browser automation, jadi tidak ada risiko akun kena blokir.

---

## 3. AKHIR PEKAN — 30 menit: siapkan Grok Bot dengan aman

Lakukan **berurutan**. Jangan lompat ke langkah 3c sebelum 3a dan 3b selesai.

### 3a. Buat token GitHub khusus (bukan password)

1. GitHub → Settings → Developer settings → **Fine-grained personal access tokens**
2. Generate new token:
   - Repository access: **Only select repositories** → `oldmoneypicks/oldmoneypicks`
   - Permissions → Contents: **Read and write**
   - Expiration: **30 hari**
3. Simpan token itu. Inilah satu-satunya yang boleh diberikan ke Grok Bot.

Kenapa: kalau Grok Bot berperilaku aneh atau tokennya bocor, Anda cabut satu
token — akun GitHub, email, dan repo lain Anda tetap aman. Kalau yang bocor
password, semuanya jatuh sekaligus.

### 3b. Batasi ruang geraknya

Di pengaturan Grok Bot, **jangan** hubungkan: WhatsApp, akun email utama,
akun bank, dashboard klinik. Grok Bot hanya boleh menyentuh tiga hal:
repo GitHub `oldmoneypicks`, Pinterest, dan Google Analytics (read-only).

### 3c. Mulai dengan tugas yang tidak bisa merusak apa pun

Minggu pertama, jalankan **Prompt A dan Prompt B saja** dari
`GROKBOT-PROMPT.md`. Keduanya cuma riset dan menulis — outputnya masuk ke
chat, tidak menyentuh akun apa pun. Anda yang menilai kualitasnya.

Kalau setelah 1–2 minggu hasilnya konsisten bagus, baru naikkan ke Prompt C
(laporan harian). Beri akses publish penuh hanya kalau Anda sudah benar-benar
percaya — dan itu keputusan bulan depan, bukan minggu ini.

---

## 4. KLINIK — 45 menit: chat pasien (ini yang paling mendesak)

Poin paling benar dari percakapan sebelumnya: **Grok Bot tidak cocok untuk
balas chat pasien.** Dia bekerja per-tugas, bukan real-time. Pasien yang
menunggu 2 jam akan pindah ke klinik lain.

Solusinya tidak butuh AI sama sekali:

**WhatsApp Business → Menu → Alat Bisnis → Balasan Cepat.**
Buat 6 template ini (ketik `/` lalu shortcut-nya untuk memanggil):

| Shortcut | Isi |
|---|---|
| `/jam` | Jam praktik, alamat, link Google Maps |
| `/harga` | Rentang biaya per sesi + apa yang termasuk |
| `/booking` | Slot kosong minggu ini + cara konfirmasi |
| `/keluhan` | 3 pertanyaan penyaring: lokasi nyeri, sudah berapa lama, riwayat cedera |
| `/persiapan` | Apa yang perlu dibawa & dipakai saat datang |
| `/followup` | Pesan pasca-terapi + kapan sesi berikutnya |

Lalu nyalakan **Pesan Salam** (otomatis untuk chat pertama) dan **Pesan Di Luar
Jam** (menyebut jam Anda kembali online). Ini menghilangkan sekitar 70%
pengetikan berulang, dan pasien tetap dibalas dalam hitungan detik.

---

## 5. Ritme mingguan

| Waktu | Fokus | Durasi |
|---|---|---|
| Senin–Jumat, jam kerja | Klinik. HP di mode Balasan Cepat. Nol urusan affiliate. | — |
| Selasa & Kamis malam | Jadwalkan pin Pinterest untuk 3 hari ke depan | 15 mnt |
| Sabtu pagi | Jalankan Prompt A di Grok Bot, review draft artikel | 45 mnt |
| Sabtu siang | Edit draft jadi HTML, `git push` | 45 mnt |
| Minggu malam | Cek Analytics + Amazon. Catat 1 angka: klik afiliasi minggu ini. | 15 mnt |

Total di luar jam klinik: **sekitar 2 jam per minggu.** Kalau lebih dari itu,
ada yang salah dengan alurnya — bukan dengan Anda.

---

## 6. Ukuran keberhasilan (jangan ukur yang lain dulu)

Bulan pertama, satu angka saja yang penting: **jumlah klik afiliasi per minggu**
(event `affiliate` di Google Analytics, sudah terpasang di situs Anda).

Traffic tanpa klik = konten salah sasaran.
Klik tanpa order = produk salah pilih.
Baru setelah klik naik konsisten, mulai perhatikan konversi.

Target realistis: 10 artikel dan 100 pin sebelum berharap pendapatan berarti.
Anda baru di artikel 1 dan pin 0 terposting (4 naskah siap, belum ada yang
terbit). Itu normal — yang penting jangan berhenti di angka 3.

---

## 7. Uang Rp 450.000

Biarkan utuh. Semua di runbook ini gratis: GitHub gratis, Vercel gratis,
Pinterest gratis, WhatsApp Business gratis, Google Analytics gratis, dan
Grok Bot sudah termasuk di langganan yang Anda punya.

Pengeluaran pertama yang layak — kalau nanti klik afiliasi sudah tumbuh —
adalah domain email profesional untuk `oldmoneypicks.com`, sekitar Rp 30rb/bulan.
Bukan sekarang.
