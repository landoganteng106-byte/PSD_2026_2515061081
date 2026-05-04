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
    for j in range(i + 1, n):
      if arr[j] > arr[pos]:
        pos = j
    if pos != i:
      tukar(arr, i, pos)
kode di atas adalah nested loop yang ada diloopingan sebelumnya,dimana dimulai dari arr[j] yang akan diloopig dengan total arr[i] yang ditambah satu persatu hingga sesuai inputan,lalu akan diseleksi dan dibandingkan di mana kalau arr[j] lebih besar dari arr[pos],lalu nilai tertinggi akan masuk ke nilai arr[pos] sebagai pivot dan ditukar,begitu terus hingga semuanya selesai sesuai inputan.



![image alt](https://cdn.corenexis.com/files/c/4544171720.png)

Penjelasan :
Fungsi main() adalah pusat kendali yang mengatur jalannya program,lalu fungsi dimulai dengan meminta pengguna memasukkan jumlah rekor (n). Penggunaan blok try...except di sini sangat penting untuk menangani kesalahan (error handling); jika pengguna memasukkan huruf, bukan angka, program tidak akan langsung error, melainkan akan memberikan pesan peringatan dan menghentikan proses.lalu,Program kemudian melakukan looping sebanyak inputan n yang diberikan untuk mengambil input data beban.Setelah semua data terkumpul ke dalam arr,program akan menetak data awal,memnggil fungsi selection sort lalu menampilkan hasil akhirnya dan kode ini "if __name__ == "__main__":" berfungsi i untuk memastikan bahwa fungsi main() hanya akan berjalan jika file ini dieksekusi secara langsung sebagai program utama, dan agar tidak harus memanggil fungsinya berulang kali.



![image alt](https://cdn.corenexis.com/files/c/2599666720.png)

Penjelasan :
untuk fungsi tukar  sama saja seperti sebelumnya,untuk fungsi seletion sortnya juga kurang lebih sama sepertui sebelumnya cuma ada sedikit perbedaan dimana bagian
            if arr[j][1] > arr[pos][1]:
dimana Indeks [1] digunakan karena data disimpan dalam format [nama, beban]. Angka 1 memastikan program hanya membandingkan nilai beban, bukan nama orangnya.




![image alt](https://cdn.corenexis.com/files/c/2859644720.png)

Penjelasan :
fungsi main berguna sebagai pengendali utamanya dimana ada fungsi di dalamnya yang langsung menetak " Program Rekor Beban Angkat " 
lalu ada looping menggunakan while true, dimana akan terus melooping selama kondisi true
