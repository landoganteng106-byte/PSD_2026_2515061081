Judul : Program Putar Playlist Lagu

Deskripsi :
Program ini menggunakan struktur data Singly Linked List untuk mensimulasikan antrean lagu dengan prinsip FIFO (First In, First Out).

Source code :

![image alt](https://cdn.corenexis.com/files/c/8736163720.png)

Penjelasan
kode baris pertama berfungsi untuk mendeklarasikan class yaitu lagu
kode baris ke-2 adalah konstruktor,fungsinya adalah untuk menginisialisasi objek saat pertama kali dibuat dari sebuah kelas
kode baris ke-3 berungsi untuk menyimpan judul lagu ke dalam variabel objek
kode baris ke-4 berfungsi untuk menyimpan nama penyanyi ke dalam variabel objek
kode baris ke-5 berfungsi untuk menginisialisasi penunjuk (pointer) ke lagu berikutnya dengan nilai kosong
kode baris ke-7 berfungsi untuk mendeklarasikan kelas utama untuk mengelola daftar lagu
kode baris ke-8 berfungsi untuk menetapkan,saat playlist pertama kali dibuat, daftar dalam keadaan kosong (tidak ada lagu pertama)
kode baris ke-11 membuat fungsi untuk menambahkan lagu dengan variabel self,judul dan artis
kode baris ke-12  berfungsi untuk menciptakan sebuah node baru menggunakan kelas Lagu. Data judul dan artis yang dimasukkan akan disimpan ke dalam objek bernama baru ini
kode baris ke-13 digunakan untuk melakukan pengecekan apakah playlist masih benar-benar kosong
kode baris ke-14 digunakan jika kondisi di atas terpenuhi di mana playlist kosong, maka lagu baru tersebut langsung ditunjuk sebagai headnya
kode baris ke-15 digunakan untuk keluar dari fungsi. Hal ini dilakukan agar program tidak menjalankan baris kode di bawahnya
kode baris ke-17 digunakan untuk menyiapkan sebuah penanda  yang dimulai dari lagu paling depan
kode baris ke-18 Program melakukan pengecekan: "Apakah lagu ini punya sambungan ke lagu berikutnya?". Perulangan ini akan terus berjalan selama arus.next tidak bernilai None. Artinya, program sedang mencari lagu mana yang berada di posisi paling terakhir
kode baris ke-19 berfungsi di mana jika setelah perulangan selesai dan posisi terakhir ditemukan, baris ini bertugas menyambungkan lagu terakhir  ke lagu baru
kode baris ke-22 membuat fungsi untuk menampilkan isi playlist
