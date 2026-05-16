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

fungsi pada baris ke-14 Fungsi get_total_elements(self) ini berguna untuk menghitung secara akurat berapa banyak orang yang sedang mengantre saat ini.
kalau array kosong dia akan mengembalikkan 0,dan ada kondisi if self.rear_idx >= self.front_idx: 
Kondisi if ini berjalan jika posisi orang paling belakang memiliki nomor indeks yang lebih besar atau sama dengan orang paling depan . Ini terjadi saat antrean bertambah secara normal dari kiri ke kanan dan kondisi elsenya terjadi ketika rear_idx < front_idx. Ini terjadi jika beberapa pelanggan di depan sudah selesai dilayani dan pulang , lalu ada pelanggan baru berdatangan hingga posisinya berputar kembali ke indeks awal



![img alt](https://cdn.corenexis.com/files/c/9489282720.png)

untuk fungsi enqueue,kalau array penuh,dia akan mengembalikan dan memprint "Maaf, antrean di kasir sudah penuh! Silakan tunggu beberapa saat."
untuk kode  if self.is_empty():
            self.front_idx = 0
            self.rear_idx = 0
berguna untuk ketika array kosong,nilai front and rearnya aka diubah ke 0,dn elemennya akan dimasukkan dimulai dari indeks 0.
else:
            self.rear_idx = (self.rear_idx + 1) % self.MAXN
kode di atas berjalan ketika kondisinya tidak terpenuhi dan karena elemen pertamanya tidak kosong,elemen berikutnya yang mau dimasukkin akan dilanjutkan ke indeks berikutnya untuk disambung dan dilingkarkan lagi.
kode self.q[self.rear_idx] = nama_pelanggan,digunakan untuk mengisi array dengan menandai yang kosong lalu diisi.
 orang_di_depan = self.get_total_elements() - 1 digunakan untuk menampilkan total jumlah orang yag ada di depan
estimasi_waktu = orang_di_depan * 5  digunakan untuk memberi estimasi waktu 5 menit perorang

funsgi dequeue berguna untuk kalau array kosong semua,dia akan memprint" Antrean kosong. Semua pelanggan sudah dilayani!",dan setiap ada pelanggan yang sudah dipanggil,indeksnya akan dikurangi 1,dan lanjut isambung untuk dilingkarkan kembali.



![img alt](https://cdn.corenexis.com/files/c/5224574720.png)

fungsi peek berguna untuk melihat antrean terdepan dan fungsi display berguna untuk menampilkan seluruh daftar antrean kalau tidak kosong.

![img alt](https://cdn.corenexis.com/files/c/7968441720.png)

def main berguna untuk menampilkan seluruh fungsi dan opsinya,disitu ada batasannya yaitu maksimal 5,dan ada perulangan while dimana akan mengulang terus jika angka tidak sama dengan 5.ada juga try dan error berguna kalau terjadi keslahan,sistem tidak akan langsung mengerrorkannya.Ada juga kode
if __name__ == "__main__":
    main()
untuk mengatur agar fungsi main() hanya dijalankan jika file Python tersebut dieksekusi secara langsung, dan tidak ikut berjalan jika file tersebut diimpor oleh file Python lain dan berjalan tanpa perlu memberikan memanggil fungsinya seara manual


link youtube :
https://youtu.be/w8MXgus89kQ


