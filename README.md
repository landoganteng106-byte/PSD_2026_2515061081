Judul : Program Putar Playlist Lagu

Deskripsi :
Program ini menggunakan struktur data Singly Linked List untuk mensimulasikan antrean lagu dengan prinsip FIFO (First In, First Out).

Source code :

![image alt](https://cdn.corenexis.com/files/c/5433456720.png)

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
kode baris ke-23 digunakan untuk melakukan pengecekan di awal,Jika variabel head masih kosong,itu artinya memang belum ada satu pun lagu yang dimasukkan ke dalam
kode baris ke-24 digunakan jika kondisi di atas kosong, program akan menampilan "Playlist Kosong"unutuk memberikan informasi kepada pengguna bahwa playlistnya kosong
kode baris ke-25 berfungsi untuk menghentikan fungsi saat itu juga
kode baris ke-27 digunakan untuk menampilkan tulisan "Dafar Putar Lagu"
kode baris ke-28 digunakan untuk menyiapkan penunjuk yang dimulai dari lagu paling depan 
kode baris ke-29 digunakan untuk membuat variabel penghitung yang dimulai dari angka 1
kode baris ke-30 dimana program akan melakukan perulangan selama variabel arus tidak kosong
kode baris ke-31 akan menampilkan tulisan lagu yang sedang ditunjuk oleh arus ke layar, lengkap dengan nomor urut, judul, dan artisnya
kode baris ke-32 akan memerintahkan variabel arus untuk melepaskan lagu yang sekarang dan memegang lagu berikutnya yang ada di sambungan (next).
kode baris ke-33 akan menambah nilai variabel nomor sebanyak 1 angka setiap kali satu lagu selesai dicetak
kode baris ke-36 membuat fungsi untuk menghapus simpul (node) pertama
kode baris ke-37 akan mengecek apakah ada lagu di dalam playlist Jika self.head berisi data (bukan None), berarti ada lagu yang bisa diputar
kode baris ke-38 akan mencetak dan memberikan informasi kepada pengguna bahwa lagu yang berada di posisi pertama (head) sedang diputar dan akan segera dikeluarkan dari daftar
kode baris ke-39 akan memindahkan penunjuk head ke lagu urutan kedua (self.head.next)
kode baris ke-40 akan dijalankan jika kondisi if self.head tidak terpenuhi, alias playlist dalam keadaan kosong
kode baris ke-41 akan mencetak "Tidak ada lagu untuk diputar." jika kondisi terpenuhi
kode baris ke-44 akan menyimpan variabel playlist
kode baris ke-45 hingga 47 berfungsi untk menambahkan lagu
kode baris ke 50 berfungsi untuk menampilkan playlist
kode baris ke-51 berfungsi untuk menghapus elemen atau lagu terdepan 

Output :



![image alt](https://cdn.corenexis.com/files/c/8182465720.png)






link video demonstrasi :
