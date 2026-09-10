# Temuan: empat gambar produk salah jam tangan
Ditemukan Selasa 8 September 2026, 22.30 WITA — saat memposting pin batch 01.

## Apa yang salah

Keempat berkas gambar di `website/images/products/` berisi jam tangan yang
**bukan** produk yang dinamakan. Diverifikasi dengan membaca tulisan di dial.

| Berkas | Isi sebenarnya | Seharusnya |
|---|---|---|
| `seiko-5-snxs79.jpg` | **Seiko Presage Cocktail Time** — tali kulit biru, caseback tembus pandang, dial "PRESAGE AUTOMATIC" | Seiko 5 SNXS79, rantai baja, day-date |
| `casio-a168wg-9.jpg` | **BALTANY** automatic — dial hitam, "660ft=200m" | Casio A168WG-9, digital kotak emas |
| `timex-marlin.jpg` | **AV 1956 MARINE** (About Vintage, Copenhagen) — jam selam, tali kanvas | Timex Marlin, gaun 34mm, kristal akrilik cembung |
| `tissot-prx-powermatic-80.jpg` | Tissot **Ballade** Powermatic 80 — bezel bergerigi, angka Romawi, rantai 5-mata | Tissot PRX, rantai menyatu, dial wafel, indeks batang |

## Yang TIDAK salah

**ASIN Amazon-nya benar semua.** Audit 1 September (`audit-link-amazon.md`)
mengecek link, tapi tidak pernah mengecek gambar. Itu celahnya.

- Seiko 5 SNXS79 → `B004YDLF3A` ✅
- Casio A168WG-9 → `B01M09CT2Q` ✅
- Timex Marlin → `B08K2GT7GB` ✅
- Tissot PRX → `B0CDP157F4` ✅

## Terdampak

1. **Artikel blog** `website/blog/quiet-luxury-watches-that-look-expensive/index.html`
   — memakai keempat gambar itu, dipasangkan dengan ASIN yang benar.
2. **Pinterest** — 1 pin sudah terbit dengan gambar Tissot yang salah model
   ("4 Quiet Luxury Watches That Look Expensive", 8 Sep malam).
   Dua pin terjadwal (Casio 9 Sep, Timex 10 Sep) **sudah dihapus 8 Sep 22.35**
   sebelum terbit. Scheduled Pins = 0.
3. **Kemungkinan besar penjelasan klik afiliasi = 0** di `catatan-mingguan.csv`.
   Pembaca melihat foto jam A, mengklik, mendarat di jam B.

## Risiko

Memasang foto produk yang bukan produk yang di-link termasuk menyesatkan
menurut Amazon Associates. Sejenis dengan aturan "jangan klik link afiliasi
sendiri" — penutupan akun tidak bisa dibanding.

## Belum dikerjakan

- [ ] Cari sumber gambar yang benar **dan sah dipakai** (unduh dari halaman
      Amazon juga ada aturannya — perlu jalan yang aman dan gratis)
- [ ] Periksa seluruh 27 gambar di `website/images/products/`, bukan cuma 4 ini
- [ ] Perbaiki artikel blog
- [ ] Hapus/ganti pin Tissot yang sudah terbit
- [ ] Cek board Timeless Watches — 13 pin, beberapa judul tampak muncul dua kali

---

## SELESAI — 10 September 2026

Keempat foto **tidak diganti dengan foto lain**, melainkan dengan **kartu
tipografi** buatan sendiri (`agent02-pinterest/buat-kartu-produk.py`).

**Kenapa bukan cari foto pengganti:** PA-API Amazon adalah satu-satunya sumber
foto produk yang halal dipakai penerbit Associates, dan baru terbuka sesudah
3 penjualan. Mengunduh foto dari halaman Amazon atau dari Google melanggar
syarat program dan/atau hak cipta pemiliknya. Gambar buatan sendiri adalah
satu-satunya yang aman sampai PA-API terbuka.

**Isi kartunya sengaja hanya keterangan yang sudah ada di dalam artikel** —
tidak ada spesifikasi baru yang ditambahkan, supaya tidak mengulang kesalahan
yang sama dalam bentuk lain.

Yang diperbaiki dan sudah terbit:
- `website/blog/quiet-luxury-watches-that-look-expensive/index.html` — 4 gambar + og:image + JSON-LD
- `website/index.html` — 12 rujukan di beranda
- `website/blog/index.html` — kartu artikel di index The Journal

Berkas `.jpg` yang salah **tidak dihapus** tapi **tidak lagi dirujuk dari halaman
mana pun** (diverifikasi dengan grep, hasilnya nol). Jangan dipakai lagi.
