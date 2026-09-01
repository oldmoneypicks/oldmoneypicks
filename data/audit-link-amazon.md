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
| 13 | Dior Sauvage | — | **link sengaja dicabut, kartu tanpa tombol** |
| 14 | Creed Aventus Sample | — | **link sengaja dicabut, kartu tanpa tombol** |
| 15 | Jo Malone Wood Sage & Sea Salt | B00VL1H4KQ | Jo Malone Wood Sage & Sea Salt Eau De Cologne Spray, 3.4 Oz |
| 16 | Polo RL Oxford White | B0D15F8XZY | POLO RALPH LAUREN Men's Classic Fit Iconic Oxford Shirt, White |
| 17 | Brooks Brothers Non-Iron Slim Fit | B074R5GC2V | Brooks Brothers Men's Regent Slim Fit Non Iron Oxford Button Down Shirt White ⚠️ |
| 18 | Linen Shirt — Cream | — | **BELUM DIPERBAIKI — perlu keputusan pemilik** |
| 19 | Cashmere V-Neck Navy | B00WSAYH9K | Citizen Cashmere Men's V-Neck Sweater 100% Cashmere, Navy Blue |
| 20 | Uniqlo Linen Blazer — Beige | — | **BELUM DIPERBAIKI — Uniqlo tidak dijual di Amazon** |
| 21 | LAFCO Chamomile Lavender Candle | B002LK414S | LAFCO New York Signature Candle, Chamomile Lavender, 15.5 oz |
| 22 | Waterford Lismore Tumbler | B000SMQ7JS | Waterford Lismore Tumbler |
| 23 | Marble & Brass Bookends | B08NFHN5PQ | Cork & Mill Marble Bookends with Gold Brass, Grey and White, Set of 2 |
| 24 | Ralph Lauren Cashmere Throw | B01MR6KQ4E | Ralph Lauren Home Luxury Cashmere Piqué Throw Blanket, Heather Light Gray 50"x70" |
| 25 | Diptyque Baies Scented Oval | B004RVBSKE | Diptyque BAIES Scented Oval |

⚠️ **No. 17 (Brooks Brothers)** adalah satu-satunya yang judulnya dipastikan dari
indeks pencarian Amazon, bukan dari membaca halamannya langsung — halaman itu menolak
dibaca berulang kali (robot check). Sebaiknya dibuka sekali secara manual di
`https://www.amazon.com/dp/B074R5GC2V` (tanpa tag) untuk memastikan.

## Dua yang belum selesai

**No. 18 — "Linen Shirt — Cream".** Judul kartunya tidak menyebut merek, jadi tidak ada
satu produk "yang benar". Kandidat terdekat yang sudah diverifikasi ada:
`B075CRJCLD` (Isle Bay Linens, 100% linen, long sleeve button-down) — tapi warna krem
tidak bisa dipastikan dari judul halamannya. **Perlu pemilik memilih produknya.**

**No. 20 — "Uniqlo Linen Blazer — Beige".** Uniqlo **tidak menjual produknya di Amazon.**
Kartu ini tidak bisa diperbaiki apa adanya. Tiga pilihan: (a) ganti judul kartu ke blazer
linen merek lain yang ada di Amazon, (b) hapus kartunya, (c) biarkan tanpa tombol seperti
kartu 13 dan 14.

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
