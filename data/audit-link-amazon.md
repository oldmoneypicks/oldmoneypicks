# Audit link afiliasi homepage — 1 September 2026

Sebelum audit ini, **25 produk homepage memakai shortlink `amzn.to`** yang tujuannya
tidak bisa dibaca tanpa membukanya. Itu sebabnya ±18 di antaranya mendarat di produk
yang berbeda dari judul kartunya tanpa ketahuan.

**Keputusan: shortlink `amzn.to` tidak dipakai lagi.** Semua diganti bentuk penuh
`https://www.amazon.com/dp/<ASIN>?tag=oldmoneypicks-20`, sama seperti yang sudah
dipakai di artikel blog. Bentuk ini bisa dibaca mata telanjang, jadi masalah yang
sama tidak bisa terulang diam-diam.

## Cara link diverifikasi — TANPA melanggar aturan Amazon

Setiap ASIN dicek dengan membuka `https://www.amazon.com/dp/<ASIN>` **tanpa tag
afiliasi**, lalu judul halamannya dicocokkan dengan judul kartu. Halaman Amazon polos
bukan link afiliasi, jadi ini **bukan** klik afiliasi sendiri.

> ⛔ Shortlink `amzn.to` yang lama **tidak pernah dibuka** selama audit ini — di
> dalamnya sudah tertanam tag `oldmoneypicks-20`, dan membukanya sama dengan mengklik
> link afiliasi sendiri. Aturan itu tidak dilanggar sekali pun.

Skrip pengecek: `cek-asin.sh` (dibuat di folder sementara, tidak ikut disimpan di repo).

## Hasil

| # | Kartu | ASIN | Judul halaman Amazon (terverifikasi) |
|---|---|---|---|
| 1 | Seiko 5 SNXS79 | B004YDLF3A | SEIKO 5 Mens Automatic Watch SNXS79 |
| 2 | Casio A168WG-9 | B01M09CT2Q | *(dari artikel blog, sudah diverifikasi pemilik)* |
| 3 | Timex Marlin | B08K2GT7GB | *(dari artikel blog, sudah diverifikasi pemilik)* |
| 4 | Tissot PRX Powermatic 80 | B0CDP157F4 | *(dari artikel blog, sudah diverifikasi pemilik)* |
| 5 | Orient Bambino Small Seconds | B078BY3B1B | Orient Bambino Mechanical Classic Vintage Small Sub Seconds Champagne AP0003S |
| 6 | Coach Pebbled Leather Card Holder | B07PJFNTHT | Coach Multiway Zip Card Case in Black Pebbled Leather F66550 |
| 7 | Fossil Minimalist Slim Wallet | B0BJ7T1BS7 | Fossil Men's Ryan Leather RFID-Blocking Slim Minimalist Bifold, Dark Brown |
| 8 | Leatherology Leather Desk Pad | B01N2AL2MK | Leatherology Black Onyx Laptop Desk Pad |
| 9 | Hide & Drink Leather Watch Roll | B07L15L48X | Hide & Drink Leather Watch Roll Organizer, Holds Up to 4 Watches (Bourbon Brown) |
| 10 | Royce Leather Valet Tray | B00WKL39ZA | Royce Leather Men's Stylish Leather Valet Tray with 6 Compartments, Tan |
| 11 | Nautica Voyage EDT | B000P22TIY | Nautica Voyage Eau de Toilette, Men's Fragrance, 3.3 fl oz |
| 12 | CK One | B000E7WFX4 | Calvin Klein CK One Eau de Toilette – Citrus Unisex Fragrance |
| 13 | ~~Dior Sauvage~~ → **Givenchy Gentleman Boisée EDP** | B0855L81LL | Givenchy Gentleman Boisee For Men Eau De Parfume Spray 3.4 Ounce |
| 14 | ~~Creed Aventus~~ → **Versace Eros Parfum 6.7 oz** | B0BBR9LQV3 | Versace Eros by Versace for Men - 6.7 oz Parfum Spray |
| 15 | Jo Malone Wood Sage & Sea Salt | B00VL1H4KQ | Jo Malone Wood Sage & Sea Salt Eau De Cologne Spray, 3.4 Oz |
| 16 | Polo RL Oxford White | B0D15F8XZY | POLO RALPH LAUREN Men's Classic Fit Iconic Oxford Shirt, White |
| 17 | Brooks Brothers Non-Iron Slim Fit | B074R5GC2V | Brooks Brothers Men's Regent Slim Fit Non Iron Oxford Button Down Shirt White ⚠️ |
| 18 | ~~Linen Shirt — Cream~~ → **J.VER Linen Blend Shirt — White** | B0CFHLCPZP | J.VER Men's Long Sleeve Cotton Linen Button Down Shirts Casual Beach Wedding Shirt with Pocket White |
| 19 | Cashmere V-Neck Navy | B00WSAYH9K | Citizen Cashmere Men's V-Neck Sweater 100% Cashmere, Navy Blue |
| 20 | ~~Uniqlo Linen Blazer — Beige~~ → **Perry Ellis Linen Blazer — Natural** | B0CNKXL8ZN | Perry Ellis Men's Linen-Blend Suit Jacket with Chest Pocket, Breathable & Lightweight, Regular Fit, Natural Linen Herringbone |
| 21 | LAFCO Chamomile Lavender Candle | B002LK414S | LAFCO New York Signature Candle, Chamomile Lavender, 15.5 oz |
| 22 | Waterford Lismore Tumbler | B000SMQ7JS | Waterford Lismore Tumbler |
| 23 | Marble & Brass Bookends | B08NFHN5PQ | Cork & Mill Marble Bookends with Gold Brass, Grey and White, Set of 2 |
| 24 | Ralph Lauren Cashmere Throw | B01MR6KQ4E | Ralph Lauren Home Luxury Cashmere Piqué Throw Blanket, Heather Light Gray 50"x70" |
| 25 | Diptyque Baies Scented Oval | B004RVBSKE | Diptyque BAIES Scented Oval |

⚠️ **No. 17 (Brooks Brothers)** adalah satu-satunya yang judulnya dipastikan dari
indeks pencarian Amazon, bukan dari membaca halamannya langsung — halaman itu menolak
dibaca berulang kali (robot check). Sebaiknya dibuka sekali secara manual di
`https://www.amazon.com/dp/B074R5GC2V` (tanpa tag) untuk memastikan.

## Dua kartu terakhir — SELESAI 1 September, 17.40

Keduanya sudah diputuskan pemilik dan dikerjakan. Homepage kini **25 dari 25 link
bentuk penuh, nol shortlink `amzn.to`.**

### No. 18 — dulu "Linen Shirt — Cream", kini J.VER Linen Blend Shirt — White

Judul lamanya tidak menyebut merek, jadi tidak ada satu produk "yang benar". Yang
membuat keputusannya jelas: **fotonya sendiri menampilkan kemeja PUTIH, bukan krem** —
jadi judul lamanya sudah salah sejak awal, terlepas dari urusan link.

Kandidat lama `B075CRJCLD` (Isle Bay Linens) **ditolak.** Halamannya memang hidup, tapi
foto listing-nya kemeja **ungu** — variasi warnanya tidak bisa dipastikan lewat URL,
jadi tidak aman dipakai. Kandidat `B0DRP8C97G` (Isle Bay putih) juga ditolak: ASIN-nya
mengembalikan **Page Not Found**, listing-nya sudah mati.

`B0CFHLCPZP` dipilih karena cocok bertiga: putih, lengan panjang, ada saku dada —
sama seperti foto kartunya. Satu catatan jujur: bahannya **campuran katun-linen**,
bukan 100% linen. Karena itu judul kartunya ditulis "Linen Blend", bukan "Linen".

Berkas foto diganti nama `linen-shirt-cream.jpg` → `linen-shirt-white.jpg`.

### No. 20 — dulu "Uniqlo Linen Blazer — Beige", kini Perry Ellis Linen Blazer — Natural

Uniqlo memang tidak menjual produknya di Amazon. Tapi saat mencari penggantinya,
ketahuan hal yang lebih penting: **foto kartunya adalah foto listing resmi Perry Ellis
`B0CNKXL8ZN`** — sama persis sampai ke rompi dan celana setelannya.

Jadi kartu ini sebenarnya tidak pernah menampilkan produk Uniqlo. Ia menampilkan
blazer Perry Ellis yang salah diberi nama. Memberi link ke `B0CNKXL8ZN` bukan mengganti
produknya — itu **mengembalikan kartu ke produk yang fotonya memang dipakai.**

Berkas foto diganti nama `uniqlo-linen-blazer.jpg` → `perry-ellis-linen-blazer.jpg`,
dan nama Uniqlo dihapus dari judul kartu, blok JSON-LD, parameter GA4, serta keempat CSV.

> ⚠️ **Konsekuensi untuk Google Sheet:** dua baris ini berubah di **tiga kolom**
> sekaligus — Pin Title, Image URL, dan Amazon Affiliate Link. Menempel kolom link saja
> tidak cukup untuk baris 19 dan 21; ketiganya harus diperbarui.

## Catatan terpisah: foto kartu tidak selalu menggambarkan produknya

Foto produk adalah foto stok umum, bukan foto listing Amazon. Beberapa jelas tidak cocok
dengan judulnya sendiri — contoh paling nyata: `marble-brass-bookends.jpg` menampilkan
sepasang bookend batu krem **tanpa kuningan sama sekali**, dan `fossil-slim-wallet.jpg`
adalah dompet cokelat tanpa merek Fossil. Ini isu terpisah dari link, tapi risikonya
mirip: pengunjung mengklik karena foto, lalu mendarat di barang yang berbeda.

---

# CSV untuk Google Sheets Make.com — 1 September 2026

Tiga berkas dibuat dari `data/produk.csv` yang sudah diperbaiki. Pilih **satu** sesuai
cara Bapak memperbarui Sheet:

| Berkas | Isi | Dipakai kalau |
|---|---|---|
| `sheet-make-link-baru.csv` | 2 kolom: Pin Title + link baru, 25 baris | Mau menimpa **kolom link saja**, kolom lain tidak disentuh |
| `sheet-make-siap-pakai.csv` | 4 kolom, **21 baris** — hanya yang linknya sudah benar | Mau mengganti isi Sheet dan membuang baris bermasalah |
| `sheet-make-lengkap.csv` | 4 kolom, 25 baris apa adanya | Mau salinan persis `produk.csv` |

## ⚠️ Tiga hal yang harus diperiksa sebelum menempel

**1. Kolom "Last Posted" akan hilang kalau seluruh Sheet ditimpa.**
Rotasi produk bergantung pada kolom itu (sort ascending, limit 1). Kalau seluruh isi
Sheet diganti, semua nilai Last Posted kosong dan rotasi mengulang dari awal — beberapa
produk bisa diposting dua kali berturut-turut. **Cara paling aman: tempel hanya kolom
link.**

**2. Dior Sauvage dan Creed Aventus masih membawa link afiliasi hidup di Sheet.**
Dua produk ini **sudah dicabut dari situs** (kartunya tanpa tombol), tapi barisnya masih
ada di `produk.csv` dengan shortlink lama `amzn.to/4bIkXKB` dan `amzn.to/4fQJdN8`. Kalau
Make.com masih merotasi 25 baris, dua produk yang sudah ditarik itu **masih ikut
diposting**. Perlu diputuskan: hapus barisnya dari Sheet, atau kembalikan produknya ke
situs.

**3. Pertanyaan terbuka: apa yang dipakai Make.com sebagai tujuan pin?**
Aturan yang sudah ditetapkan: **Pinterest tidak pernah link Amazon langsung — pin
mengarah ke artikel, link Amazon ada di dalam artikel.** Berkas `pins-blog-batch-01.csv`
mengikuti aturan itu (kolomnya `Destination Link` → URL artikel blog). Tapi `produk.csv`
hanya punya kolom `Amazon Affiliate Link`.

Kalau skenario Make.com memakai kolom itu sebagai tujuan pin, berarti 25 pin produk
mengarah langsung ke Amazon — melanggar aturan sendiri dan berisiko di sisi Amazon
Associates. **Buka skenario "Integration Pinterest" di Make.com dan periksa kolom mana
yang dipetakan ke field "link" modul Pinterest** sebelum rotasi berikutnya jalan
(Minggu 17:03 WIB).

---

# Penggantian dua produk — 1 September 2026 (sore)

Dior Sauvage dan Creed Aventus **diganti**, bukan sekadar dicabut. Pemilik memilih
penggantinya lewat Google Sheet (baris 14 dan 15), lalu situs disesuaikan.

| Posisi | Dulu | Sekarang | ASIN |
|---|---|---|---|
| 13 | Dior Sauvage Eau de Toilette | Givenchy Gentleman Boisée Eau de Parfum | `B0855L81LL` |
| 14 | Creed Aventus — Sample Vial | Versace Eros Parfum — 6.7 oz | `B0BBR9LQV3` |

**Versace terkonfirmasi ganda.** Judul di Sheet ("Versace Eros by Versace for Men - 6.7 oz
Parfum Spray") sama persis dengan judul listing `B0BBR9LQV3`, dan foto produknya sendiri
bertuliskan **PARFUM · 200 ML · 6.7 US FL.Oz** — cocok sampai ke variannya. Versace Eros
punya versi EDT, EDP, dan Parfum; yang dipakai adalah Parfum.

**Givenchy dipilih dengan satu asumsi.** Judul di Sheet tidak menyebut ukuran. Botol di
foto bertuliskan 100 ML / 3.3 FL.OZ, dan `B0855L81LL` adalah listing 100 ml (ditulis
"3.4 Ounce" oleh penjual — 100 ml memang dibulatkan 3,3 atau 3,4 tergantung listing).
Ada listing 100 ml lain, `B0DZLMTH4Y`, yang menulisnya "3.3 Ounce". Kalau yang dimaksud
justru listing itu, tinggal ganti ASIN-nya.

## Yang ikut diperbarui selain link

1. **Kartu HTML** — judul, gambar, tombol Shop Now (sebelumnya "Currently Unavailable"),
   event GA4 `affiliate_click`, dan tombol Save to Pinterest.
2. **JSON-LD data terstruktur** posisi 13 & 14 — nama, gambar, deskripsi, dan merek.
   Ini gampang terlewat: kalau hanya kartunya diganti, data terstruktur untuk Google
   masih menyebut Dior dan Creed sementara halamannya menampilkan Givenchy dan Versace.
3. **`data/produk.csv`** dan ketiga CSV Sheet, dibuat ulang.

## Foto produk

Foto disediakan pemilik, aslinya persegi (Givenchy 1000×1000, Versace 1500×1500).
Diubah ke **1000×1500 (2:3)** seperti semua foto lain dengan menambah ruang putih
atas-bawah — bukan dipotong, supaya botolnya tetap utuh. Latar aslinya sudah putih,
jadi sambungannya tidak terlihat.

> ⚠️ **Perlu dipastikan asal fotonya.** Keduanya tampak seperti foto produk resmi yang
> dipakai di listing Amazon. Perjanjian Amazon Associates mensyaratkan gambar produk
> diambil lewat Product Advertising API, bukan diunduh dari halaman listing. Kalau foto
> ini diunduh dari Amazon, sebaiknya diganti dengan foto dari situs resmi merek, foto
> sendiri, atau lewat API. Foto produk lain di situs ini adalah foto stok umum, jadi
> tidak terkena isu yang sama.

Berkas lama `dior-sauvage.jpg` dan `creed-aventus-sample.jpg` dibiarkan di repo — tidak
lagi dirujuk dari mana pun, aman untuk dihapus kapan saja.
