class QueueArray:
    def __init__(self, max_size=100):
        self.MAXN = max_size
        self.q = [None] * self.MAXN
        self.front_idx = -1
        self.rear_idx = -1

    def is_empty(self):
        return self.front_idx == -1

    def is_full(self):
        return (self.rear_idx + 1) % self.MAXN == self.front_idx

    def get_total_elements(self):
        """Menghitung jumlah total orang yang ada di dalam antrean saat ini"""
        if self.is_empty():
            return 0
        if self.rear_idx >= self.front_idx:
            return self.rear_idx - self.front_idx + 1
        else:
            return (self.MAXN - self.front_idx) + self.rear_idx + 1

    def enqueue(self, nama_pelanggan):
        if self.is_full():
            print(" Maaf, antrean di kasir sudah penuh! Silakan tunggu beberapa saat.")
            return
        
        if self.is_empty():
            self.front_idx = 0
            self.rear_idx = 0
        else:
            self.rear_idx = (self.rear_idx + 1) % self.MAXN
            
        self.q[self.rear_idx] = nama_pelanggan
        
        
        orang_di_depan = self.get_total_elements() - 1
        estimasi_waktu = orang_di_depan * 5  
        

    def dequeue(self):
        if self.is_empty():
            print(" Antrean kosong. Semua pelanggan sudah dilayani!")
            return
        
        pelanggan_dipanggil = self.q[self.front_idx]
        print(f" Pelanggan '{pelanggan_dipanggil}', silakan menuju ke Loket Kasir!")
        
        if self.front_idx == self.rear_idx:
            self.front_idx = -1
            self.rear_idx = -1
        else:
            self.front_idx = (self.front_idx + 1) % self.MAXN

    def peek(self):
        if self.is_empty():
            print(" Antrean kosong.")
            return
        print(f" Pelanggan di antrean terdepan saat ini: {self.q[self.front_idx]}")

    def display(self):
        if self.is_empty():
            print(" Antrean kosong ")
            return
        print(" Daftar Antrean Kasir :")
        i = self.front_idx
        nomor = 1
        while True:
            print(f"   {nomor}. {self.q[i]}")
            if i == self.rear_idx:
                break
            i = (i + 1) % self.MAXN
            nomor += 1


def main():
    kasir_queue = QueueArray(max_size=5)
    pilih = 0
    
    while pilih != 5:
        print("     SISTEM ANTREAN KASIR SWALAYAN  ")
        print("1. Pelanggan Datang (Enqueue)")
        print("2. Panggil Pelanggan Berikutnya (Dequeue)")
        print("3. Lihat Pelanggan Terdepan (Peek)")
        print("4. Tampilkan Seluruh Antrean (Display)")
        print("5. Tutup Kasir (Keluar)")
        
        try:
            pilih = int(input("Pilih menu (1-5): "))
        except ValueError:
            print(" Input harus berupa angka!")
            continue
            
        if pilih == 1:
            nama = input("Masukkan nama pelanggan: ").strip()
            if nama:
                kasir_queue.enqueue(nama)
            else:
                print(" Nama pelanggan tidak boleh kosong!")
        elif pilih == 2:
            kasir_queue.dequeue()
        elif pilih == 3:
            kasir_queue.peek()
        elif pilih == 4:
            kasir_queue.display()
        elif pilih == 5:
            print(" Kasir ditutup. Program selesai.")
        else:
            print(" Pilihan menu tidak tersedia!")


if __name__ == "__main__":
    main()