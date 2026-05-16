Judul : Sistem Antrian Kasir Swalayan

Deskripsi :
Program ini adalah simulasi sistem antrean kasir berbasis teks yang menggunakan struktur data Circular Queue  berbasis Array. 
Dengan menerapkan prinsip FIFO (First In, First Out), pelanggan yang datang lebih awal akan dilayani terlebih dahulu, 
sementara pelanggan baru yang masuk (enqueue) akan ditempatkan di posisi belakang. Program ini juga dilengkapi dengan fitur interaktif untuk
memanggil pelanggan berikutnya (dequeue), melihat pelanggan terdepan (peek), serta menampilkan seluruh daftar antrean secara real-time. 
Keunggulan dari program ini adalah kemampuannya menghitung jumlah orang di depan pelanggan serta estimasi waktu tunggu secara akurat, 
memanfaatkan manajemen indeks melingkar yang mencegah pemborosan memori pada array


![img alt](https://cdn.corenexis.com/files/c/5322686720.png)


Pada gambar tersebut pada di kode pertama digunakan class untuk menyatakan kelasnya yaitu QueueArray

pada kode ke 2 def __init__(self, max_size=100):
Saat  membuat objek antrean , fungsi ini otomatis berjalan. Parameter max_size menentukan kapasitas maksimal antrean. Jika tidak diisi, ukuran defaultnya adalah 100.

Pada kode ke 3 self.MAXN = max_size
Program menyimpan kapasitas maksimal antrean tersebut ke dalam variabel self.MAXN. digunakan untuk membatasi jumlah elemen dan melakukan operasi modulo agar indeksnya bisa berputar.

Kode self.q = [None] * self.MAXN
Di baris ini, Python langsung memesan slot memori di komputer berupa list kosong yang diisi nilai None sebanyak max_size.

self.front_idx = -1 dan self.rear_idx = -1 digunakan untuk membatasi indeks front dan rear ke -1 karena maksimum indeks adalah karena indeks awal adalah 0 dan agar komputer tidak mengira indeks itu sudah terisi kalau belum digunakan.

untuk kode : def is_empty(self):
        return self.front_idx == -1
digunakan untuk memeriksa apakah elemen di dalam indeks koson atau tidak.Jika kosong fungsi ini akan mengembalikan -1.

kode  : def is_full(self):
         return (self.rear_idx + 1) % self.MAXN == self.front_idx
berfungsi untuk kalau seandainya array full,fungsi akan menghentikan input baru dan melingkarkan dan menyambung lagi keujung antrean.
