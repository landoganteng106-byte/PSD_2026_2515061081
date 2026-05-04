Judul : Program mengurutkan rekor angkat beban

Deskripsi :

Program ini dibuat untuk mencatat dan mengurutkan rekor beban angkatan dari yang terbesar ke yang terkecil menggunakan algoritma Selection Sort. 
Program bekerja dengan meminta input jumlah data, nama individu, dan berat beban yang diangkat, kemudian program akan mencari nilai tertinggi dalam daftar 
untuk ditempatkan di posisi teratas dengan proses penukaran dan hasilnya akhirnya adalah daftar peringkat yang rapi dan informatif, 
memudahkan pengguna untuk melihat siapa yang memegang rekor angkatan terberat secara berurutan.




![image alt](https://cdn.corenexis.com/files/c/2599666720.png)

Penjelasan :
fungsi tukar berisi Kode baris pertama digunakan untuk menginisiasi atau membuat fungsi tukar dengan arr,i dan j sebagai elemennya.
Lalu,mulai dari kode baris kedua,dimulai dengan menyimpan nilai dari indeks ke-i ke dalam variabel sementara temp, kemudian menimpah posisi indeks ke-i dengan nilai dari indeks ke-j. Terakhir, nilai asli dari indeks ke-i yang berada di dalam temp dipindahkan ke posisi indeks ke-j.
Kode def selection_sort(arr, n) berfungsi untuk menginisiasi atau membuat fungsi seletion sort dimana fungsi ini berguna untuk mengurutkan datanya.
Lalu,Alurnya dimulai dari kode bawahnya dimana  dari loop luar yang menentukan posisi target (i), kemudian loop dalam akan menyeleksi sisa elemen di sebelah kanan untuk mencari nilai yang lebih besar dari nilai di posisi pos. Jika ditemukan elemen yang lebih besar, variabel pos akan diperbarui untuk mencatat indeks elemen tersebut. Setelah penyeleksian selesai, jika indeks pos tidak lagi sama dengan i, maka fungsi tukar akan dipanggil untuk memindahkan elemen terbesar tersebut ke posisi yang seharusnya, dan proses ini terus berulang hingga seluruh data terurut secara menurun. Kode "for i in range(n - 1):" berguna untuk looping sesuai input yang diterima karena indeks di python dimulai dari 0,maka setiap hasil inputan dikurang dengan 1 agar sesuai indeksnya.
    
    
    for i in range(n - 1):
        pos = i
        for j in range(i + 1, n):
            if arr[j][1] > arr[pos][1]:
                pos = j
        if pos != i:
            tukar(arr, i, pos)

            
kode di atas adalah nested loop yang ada diloopingan sebelumnya,dimana dimulai dari arr[j] yang akan diloopig dengan total arr[i] yang ditambah satu persatu hingga sesuai inputan,lalu akan diseleksi dan dibandingkan di mana kalau arr[j] lebih besar dari arr[pos],lalu nilai tertinggi akan masuk ke
 nilai arr[pos] sebagai pivot dan ditukar,begitu terus hingga semuanya selesai sesuai inputan.kondisi   if arr[j][1] > arr[pos][1]:
dimana Indeks [1] digunakan karena data disimpan dalam format [nama, beban]. Angka 1 memastikan program hanya membandingkan nilai beban, bukan nama orangnya.



![image alt](https://cdn.corenexis.com/files/c/2314337720.png)

Penjelasan :

ada variabel data_rekor yang jadi penampung atau berisi list,lalu ada perulangan sesuai inputan yang diberikan di kode "for i in range(n):"lalu dia akan menprint   print(f"\nData ke-{i + 1}:" yang akan disesuaikan dengan i + 1 hingga sampai inputannya atau nilai n.terus juga ada kode

 
 while True:
            try:
                beban = int(input(f"Masukkan beban angkatan {nama} (Kg): "))
                data_rekor.append([nama, beban])
                break
            except ValueError:
                print("Input beban tidak valid, masukkan angka!")

    print("\n" + "="*30)
    print(f"Data sebelum diurutkan: {data_rekor}")



kode ini berfungsi sebagai pengisian datanys  yang memastikan setiap rekor beban angkatan tersimpan dengan aman dan benar.dengan perulangan while True dan kode try dan exept, program memaksa pengguna untuk memasukkan angka beban yang benar.jika terjadi kesalahan ketik seperti memasukkan huruf, program akan memberikan peringatan dan meminta input ulang tanpa menghentikan jalannya aplikasi. Setelah angka beban berhasil dikonversi menjadi integer, data tersebut digabungkan dengan nama dalam bentuk list pasangan [nama, beban] dan dimasukkan ke dalam daftar besar data_rekor lalu setelah semuanya selesai akan diprint dan ditampilkan.



![image alt](https://cdn.corenexis.com/files/c/5686641720.png)

Penjelasan :
Kode ini dimulai dengan pemanggilan  selection_sort(data_rekor, n), di mana daftar data yang tadinya acak disusun ulang berdasarkan beban angkatan
tertinggi Setelah data terurut, program menggunakan perulangan for untuk membedah kembali isi list dua dimensi tersebut; pada setiap putaran, program mengambil nama orang dari indeks [0] dan besar bebannya dari indeks [1]. Hasilnya dicetak dalam format daftar bernomor (i+1) untuk menciptakan tampilan papan peringkat atau leaderboard dan if __name__ == "__main__": memastikan bahwa seluruh rangkaian fungsi ini hanya akan berjalan secara otomatis saat file dijalankan sebagai program utama.







