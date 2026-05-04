Judul : Program mengurutkan rekor angkat beban

Deskripsi :

Program ini dibuat untuk mencatat dan mengurutkan rekor beban angkatan dari yang terbesar ke yang terkecil menggunakan algoritma Selection Sort. 
Program bekerja dengan meminta input jumlah data, nama individu, dan berat beban yang diangkat, kemudian program akan mencari nilai tertinggi dalam daftar 
untuk ditempatkan di posisi teratas dengan proses penukaran dan hasilnya akhirnya adalah daftar peringkat yang rapi dan informatif, 
memudahkan pengguna untuk melihat siapa yang memegang rekor angkatan terberat secara berurutan.



![image alt](https://cdn.corenexis.com/files/c/1142962720.png)

Penjelasan :
Kode baris pertama digunaka untuk menginisiasi atau membuat fungsi tukar dengan arr,i dan j sebagai elemennya.
Lalu,mulai dari kode baris kedua,dimulai dengan menyimpan nilai dari indeks ke-i ke dalam variabel sementara temp, kemudian menimpah posisi indeks ke-i dengan nilai dari indeks ke-j. Terakhir, nilai asli dari indeks ke-i yang berada di dalam temp dipindahkan ke posisi indeks ke-j.



![image alt](https://cdn.corenexis.com/files/c/4519233720.png)

Penjelasan :
Kode def selection_sort(arr, n) berfungsi untuk menginisiasi atau membuat fungsi seletion sort dimana fungsi ini berguna untuk mengurutkan datanya.
Lalu,Alurnya dimulai dari kode bawahnya dimana  dari loop luar yang menentukan posisi target (i), kemudian loop dalam akan menyeleksi sisa elemen di sebelah kanan untuk mencari nilai yang lebih besar dari nilai di posisi pos. Jika ditemukan elemen yang lebih besar, variabel pos akan diperbarui untuk mencatat indeks elemen tersebut. Setelah penyeleksian selesai, jika indeks pos tidak lagi sama dengan i, maka fungsi tukar akan dipanggil untuk memindahkan elemen terbesar tersebut ke posisi yang seharusnya, dan proses ini terus berulang hingga seluruh data terurut secara menurun. Kode "for i in range(n - 1):" berguna untuk looping sesuai input yang diterima karena indeks di python dimulai dari 0,maka setiap hasil inputan dikurang dengan 1 agar sesuai indeksnya.

