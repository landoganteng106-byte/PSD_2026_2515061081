Judul : Penyimpanan Toko kelontong

Deskripsi :
Program ini adalah program simulasi sistem kasir toko kelontong digital yang mengimplementasikan struktur data Hash Map menggunakan metode Open Addressing (Linear Probing). Program ini dirancang untuk mengelola inventaris produk secara efisien, di mana nomor barcode unik bertindak sebagai kunci (key) untuk menyimpan, mencari, dan menghapus nama barang (value) pada slot tabel memori yang terbatas. Melalui skenario dalam fungsi utama, kode ini mendemonstrasikan cara kerja sistem dalam mengatasi tabrakan data (collision) ketika beberapa barcode menghasilkan indeks yang sama, sekaligus memanfaatkan status khusus 
DELETED untuk menjamin rantai pencarian barang lain di sekitarnya tidak terputus setelah terjadi penghapusan stok.

![img alt](https://cdn.corenexis.com/files/c/9469273720.png)


Baris ke-1 menjelaskan tentang pembuatan kelas baru bernama SlotState. Kelas ini berfungsi sebagai pengelompok wilayah (namespace) untuk mendefinisikan konstanta status atau kondisi dari setiap slot yang ada di dalam hash table.

Baris ke-2 menjelaskan tentang pembuatan konstanta bernama EMPTY yang diberi nilai 0. Konstanta ini digunakan sebagai penanda bahwa slot di dalam tabel benar-benar kosong dan belum pernah diisi data sama sekali sejak awal.

Baris ke-3 menjelaskan tentang pembuatan konstanta bernama OCCUPIED yang diberi nilai 1. Konstanta ini digunakan sebagai penanda bahwa slot tersebut sedang terisi oleh data aktif.

Baris ke-4 menjelaskan tentang pembuatan konstanta bernama DELETED yang diberi nilai 2. Konstanta ini digunakan sebagai penanda bahwa data di slot tersebut sudah dihapus. Penanda ini sangat penting dalam Open Addressing agar proses pencarian data lain tidak terputus di tengah jalan akibat adanya slot yang kosong pasca-penghapusan.

Baris ke-7 menjelaskan tentang pembuatan kelas baru bernama Entry. Kelas ini bertindak sebagai cetakan (blueprint) objek untuk menyimpan satu paket data tunggal yang akan dimasukkan ke dalam hash table.

Baris ke-8 menjelaskan tentang pendefinisian fungsi konstruktor khusus bawaan Python bernama __init__. Fungsi ini akan otomatis berjalan setiap kali ada objek baru yang dibuat dari kelas Entry untuk menyiapkan nilai-nilai awalnya.

Baris ke-9 menjelaskan tentang pembuatan variabel (atribut) objek bernama self.key dengan nilai awal None (kosong). Atribut ini nantinya digunakan untuk menyimpan kunci unik data, contohnya seperti nomor ID atau barcode barang.

Baris ke-10 menjelaskan tentang pembuatan variabel (atribut) objek bernama self.value dengan nilai awal None (kosong). Atribut ini nantinya digunakan untuk menyimpan nilai/isi data asli yang berpasangan dengan kunci tersebut, contohnya seperti nama barang atau harga.

Baris ke-11 menjelaskan tentang pembuatan variabel (atribut) objek bernama self.state yang nilai awalnya diset langsung ke SlotState.EMPTY. Ini memastikan bahwa setiap kali wadah data (Entry) baru dibuat, statusnya akan otomatis terdeteksi sebagai slot yang kosong sebelum nantinya diisi data sungguhan oleh sistem.

![img alt](https://cdn.corenexis.com/files/c/2758635720.png)

Baris ke-14 menjelaskan tentang pendefinisian kelas utama bernama HashMapOpenAddressing yang berfungsi untuk mengimplementasikan struktur data Hash Map menggunakan metode penanganan tabrakan data Open Addressing (Linear Probing).

Baris ke-15 menjelaskan tentang pendefinisian fungsi konstruktor khusus __init__ yang menerima parameter opsional size dengan nilai bawaan (default) sebesar 10 untuk menentukan kapasitas awal tabel.

Baris ke-16 menjelaskan tentang pembuatan variabel objek self.SIZE untuk menyimpan informasi kapasitas maksimal dari hash table.

Baris ke-17 menjelaskan tentang pembuatan tabel utama bernama self.table menggunakan teknik list comprehension untuk membuat wadah berisi objek Entry kosong sebanyak ukuran self.SIZE.

Baris ke-19 menjelaskan tentang pendefinisian fungsi bernama hash_function yang menerima parameter key untuk menghitung dan menentukan indeks posisi penempatan data di dalam tabel.

Baris ke-20 menjelaskan tentang proses perhitungan indeks menggunakan rumus operasi modulus (%) agar nilai key dipetakan secara aman ke dalam rentang indeks tabel, sekaligus memastikan nilai negatif tetap menghasilkan indeks positif yang valid.


Baris ke-22 menjelaskan tentang pendefinisian fungsi insert yang digunakan untuk memasukkan atau menambahkan pasangan data baru berupa key (kunci) dan value (nilai) ke dalam hash table.

Baris ke-23 menjelaskan tentang pencarian posisi indeks awal (home slot) untuk data baru dengan cara memanggil fungsi hash_function(key) dan menyimpannya ke dalam variabel idx.

Baris ke-24 menjelaskan tentang inisialisasi variabel first_deleted dengan nilai awal -1. Variabel ini bertugas mencatat posisi indeks pertama yang berstatus DELETED yang ditemui selama proses pencarian slot.

Baris ke-25 menjelaskan tentang pembuatan perulangan for sebanyak ukuran tabel (self.SIZE) untuk melakukan pencarian linier (probing) jika indeks awal yang dituju sudah terisi data lain.

Baris ke-26 menjelaskan tentang perhitungan indeks pergeseran i pada setiap langkah (step) pencarian menggunakan rumus Linear Probing: (idx + step) % self.SIZE.

Baris ke-27 menjelaskan tentang pemeriksaan kondisi apakah slot pada indeks i saat ini berstatus OCCUPIED (sedang terisi oleh data aktif lain).

Baris ke-28 menjelaskan tentang pemeriksaan lanjutan di dalam slot yang terisi, untuk mengecek apakah kunci (key) di slot tersebut sama dengan kunci baru yang ingin dimasukkan (kondisi update data).

Baris ke-29 menjelaskan tentang proses memperbarui atau menimpa nilai lama di dalam slot tersebut dengan nilai value yang baru karena kuncinya cocok.

Baris ke-30 menjelaskan tentang pengembalian nilai True untuk menghentikan fungsi dan menandakan bahwa proses pembaruan data berhasil dilakukan.

Baris ke-31 menjelaskan tentang pemeriksaan kondisi alternatif (elif) jika ternyata slot pada indeks i berstatus DELETED (bekas data yang sudah dihapus).

Baris ke-32 menjelaskan tentang pengecekan apakah ini merupakan slot berstatus DELETED pertama yang ditemukan (ditandai dengan nilai first_deleted yang masih -1).

Baris ke-33 menjelaskan tentang penyimpanan posisi indeks i tersebut ke dalam variabel first_deleted agar bisa digunakan sebagai tempat menyimpan data baru jika tidak ditemukan kunci ganda di dalam tabel.

Baris ke-34 menjelaskan tentang blok kondisi else yang akan dieksekusi jika slot pada indeks i tidak berstatus OCCUPIED maupun DELETED, yang berarti slot tersebut berstatus EMPTY (benar-benar kosong).

Baris ke-35 menjelaskan tentang pengecekan apakah sebelum mencapai slot kosong ini, sistem sempat menemukan slot berstatus DELETED (ditandai dengan nilai first_deleted tidak sama dengan -1).

Baris ke-36 menjelaskan tentang pengalihan target indeks penyimpanan dari slot kosong saat ini (i) ke indeks slot bekas yang aman ditemukan sebelumnya (first_deleted) demi menghemat ruang penyimpanan.

Baris ke-37 menjelaskan tentang pengisian data kunci baru ke dalam atribut key pada slot tabel yang telah ditentukan.

Baris ke-38 menjelaskan tentang pengisian data nilai baru ke dalam atribut value pada slot tabel tersebut.

Baris ke-39 menjelaskan tentang pengubahan status slot tabel tersebut menjadi SlotState.OCCUPIED karena kini telah resmi terisi oleh data baru.

Baris ke-40 menjelaskan tentang pengembalian nilai True untuk menghentikan fungsi dan menyatakan bahwa proses penyisipan data baru berhasil.

Baris ke-41 menjelaskan tentang pemeriksaan di luar perulangan (setelah seluruh tabel diperiksa) untuk mengecek apakah ada slot berstatus DELETED yang sempat dicatat dan bisa digunakan (first_deleted != -1).

Baris ke-42 menjelaskan tentang pengisian kunci data baru ke dalam slot berstatus DELETED pertama yang ditemukan setelah perulangan penuh selesai dijalankan.

Baris ke-43 menjelaskan tentang pengisian nilai data baru ke dalam slot berstatus DELETED tersebut.

Baris ke-44 menjelaskan tentang pembaruan status slot tersebut menjadi SlotState.OCCUPIED agar terproteksi dari penimpaan data lain di kemudian hari.

Baris ke-45 menjelaskan tentang pengembalian nilai True untuk menyatakan bahwa data berhasil disisipkan pada slot bekas yang tersedia setelah pencarian panjang.

Baris ke-46 menjelaskan tentang pengembalian nilai False yang berarti data gagal dimasukkan ke dalam sistem karena seluruh kapasitas hash table sudah benar-benar penuh dan tidak ada slot kosong maupun slot bekas yang tersisa.


![img alt](https://cdn.corenexis.com/files/c/8365338720.png)

Baris ke-48 menjelaskan tentang pendefinisian fungsi bernama search yang menerima parameter key (kunci), yang bertugas untuk mencari data di dalam hash table.

Baris ke-49 menjelaskan tentang proses menghitung indeks awal (home slot) lokasi data dengan memanggil fungsi hash_function(key) dan menyimpannya ke dalam variabel idx.

Baris ke-50 menjelaskan tentang pembuatan perulangan for sebanyak ukuran kapasitas tabel (self.SIZE) untuk menyusuri slot-slot tabel secara linier (linear probing).

Baris ke-51 menjelaskan tentang perhitungan indeks pergeseran i di setiap langkah pencarian dengan rumus Linear Probing: (idx + step) % self.SIZE.

Baris ke-52 menjelaskan tentang pemeriksaan kondisi apakah slot pada indeks i yang sedang dicek berstatus EMPTY (kosong asli).

Baris ke-53 menjelaskan tentang pengembalian nilai None untuk menghentikan pencarian, karena jika sistem menemukan slot EMPTY sebelum menemukan kunci, berarti data tersebut memang tidak pernah ada di dalam tabel.

Baris ke-54 menjelaskan tentang pemeriksaan kondisi apakah slot tersebut berstatus OCCUPIED (terisi) dan kunci (key) yang tersimpan di slot itu cocok dengan kunci yang sedang dicari.

Baris ke-55 menjelaskan tentang pengembalian objek data self.table[i] yang ditemukan karena kuncinya telah cocok.

Baris ke-56 menjelaskan tentang pengembalian nilai None di luar perulangan, yang akan dieksekusi jika seluruh tabel sudah diperiksa (kasus tabel penuh) namun kunci tetap tidak ditemukan.

Baris ke-58 menjelaskan tentang pendefinisian fungsi bernama remove_key yang menerima parameter key untuk menghapus data dari dalam tabel.

Baris ke-59 menjelaskan tentang pemanggilan fungsi search(key) untuk mencari keberadaan objek data yang ingin dihapus, lalu hasilnya disimpan ke variabel entry.

Baris ke-60 menjelaskan tentang pemeriksaan kondisi jika hasil pencarian variabel entry bernilai None (data tidak ditemukan).

Baris ke-61 menjelaskan tentang pengembalian nilai False yang menandakan proses penghapusan gagal karena data yang dimaksud tidak ada di dalam sistem.

Baris ke-62 menjelaskan tentang proses mengubah status slot data yang ditemukan tersebut menjadi SlotState.DELETED (menandainya sebagai bekas barang).

Baris ke-63 menjelaskan tentang pengembalian nilai True yang menandakan bahwa proses penghapusan data telah berhasil dilakukan.

Baris ke-65 menjelaskan tentang pendefinisian fungsi bernama display yang digunakan untuk mencetak seluruh isi dan status hash table ke layar.

Baris ke-66 menjelaskan tentang pencetakan teks judul atau header pembuka tabel yaitu [Kondisi Rak Penyimpanan Hash Table]: ke layar.

Baris ke-67 menjelaskan tentang pembuatan perulangan for untuk menyusuri setiap indeks dari 0 hingga batas kapasitas tabel (self.SIZE).

Baris ke-68 menjelaskan tentang pencetakan label nomor slot (contoh: Slot 0: ) dengan parameter end="" agar cetakan berikutnya tetap berada di baris yang sama.

Baris ke-69 menjelaskan tentang pemeriksaan kondisi apakah slot pada indeks i saat ini berstatus EMPTY.

Baris ke-70 menjelaskan tentang pencetakan teks "KOSONG (EMPTY)" jika kondisi pada baris ke-69 terpenuhi.

Baris ke-71 menjelaskan tentang pemeriksaan kondisi alternatif (elif) apakah slot pada indeks i tersebut berstatus DELETED.

Baris ke-72 menjelaskan tentang pencetakan teks "BEKAS BARANG (DELETED)" jika kondisi pada baris ke-71 terpenuhi.

Baris ke-73 menjelaskan tentang blok kondisi terakhir (else) yang akan berjalan jika slot tersebut tidak kosong dan tidak dihapus (artinya berstatus OCCUPIED).

Baris ke-74 menjelaskan tentang pencetakan informasi lengkap data berupa nilai key (Barcode) dan nilai value (Nama Barang) yang tersimpan aktif di dalam slot tersebut.
