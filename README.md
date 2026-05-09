Judul : Program Cek Stok Toko

Deskripsi    :
Program ini dibuat untuk mensimulasikan pencarian barang di dalam gudang atau rak toko dengan algoritma yang efisien dan sederhana denga menggunakan
Sentinel Linear Searching untuk meningkatkan efisiensi dalam pencarian produk.



[![image alt]](https://cdn.corenexis.com/files/c/9337662720.png)





Pada kode ke-1 dibuat def cps dengan parameter daftar_stok, produk_dicari
Kode ke-2 berguna untuk menghitung jumlah total barang yang ada di dalam daftar_stok
Pada kode ke-3,produk_dicari.lower() digunakan untuk mengubah input nama barang menjadi huruf kecil agar pencarian tidak error hanya karena perbedaan huruf kapital ,misalnya "Beras" tetap ditemukan meski mengetik "beras".
Pada kode daftar_stok[n - 1]: Menyimpan nama barang terakhir yang asli agar tidak hilang,digunakan n - 1 untuk menyesuaikan input karena indeks dimulai dari 0.
Pade kode daftar_stok[n - 1] = produk_dicari:, digunakan untuk mengganti barang terakhir dengan barang yang sedang kita cari,Tujuannya agar perulangan (while) pasti akan menemukan barang tersebut dan berhenti, sehingga komputer tidak perlu terus-menerus mengecek apakah daftar sudah habis atau belum.
kode i = 0 digunakan untuk menyatakan bahwa indeks dimulai dari 0
while daftar_stok[i].lower() != produk_dicari:: Program akan terus berlanjut ke barang berikutnya (i += 1) selama barang yang diperiksa belum cocok dengan yang dicari.
kode ke-9 berfungsi untuk ketika looping berhenti, kita mengembalikan barang terakhir yang asli ke tempatnya semula.
kode ke-10, digunakan untuk mengecek di mana barang itu ditemukan,Jika ditemukan di indeks i yang lebih kecil dari posisi terakhir, berarti barang itu memang ada di daftar asli,Jika ditemukan di posisi terakhir, bakal dicek lagi apakah itu memang barang yang sama atau hanya kebetulan saja Jika ditemukan, kirimkan nomor indeksnya pada kode return i, Jika sampai akhir tidak ditemukan , kirimkan angka -1 sebagai tanda barang tidak ada dengan kode return -1.



[![image alt]] (https://cdn.corenexis.com/files/c/8687126720.png)



Pada kode 14 dibuat list stok_toko dengan isinya "Beras", "Minyak Goreng", "Gula", "Garam", "Telur", "Terigu", "Kopi", "Tempe".
