class SlotState:
    EMPTY = 0
    OCCUPIED = 1
    DELETED = 2


class Entry:
    def __init__(self):
        self.key = None
        self.value = None
        self.state = SlotState.EMPTY


class HashMapOpenAddressing:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [Entry() for _ in range(self.SIZE)]

    def hash_function(self, key):
        return (key % self.SIZE + self.SIZE) % self.SIZE

    def insert(self, key, value):
        idx = self.hash_function(key)
        first_deleted = -1
        for step in range(self.SIZE):
            i = (idx + step) % self.SIZE
            if self.table[i].state == SlotState.OCCUPIED:
                if self.table[i].key == key:
                    self.table[i].value = value
                    return True
            elif self.table[i].state == SlotState.DELETED:
                if first_deleted == -1:
                    first_deleted = i
            else:
                if first_deleted != -1:
                    i = first_deleted
                self.table[i].key = key
                self.table[i].value = value
                self.table[i].state = SlotState.OCCUPIED
                return True
        if first_deleted != -1:
            self.table[first_deleted].key = key
            self.table[first_deleted].value = value
            self.table[first_deleted].state = SlotState.OCCUPIED
            return True
        return False

    def search(self, key):
        idx = self.hash_function(key)
        for step in range(self.SIZE):
            i = (idx + step) % self.SIZE
            if self.table[i].state == SlotState.EMPTY:
                return None
            if self.table[i].state == SlotState.OCCUPIED and self.table[i].key == key:
                return self.table[i]
        return None

    def remove_key(self, key):
        entry = self.search(key)
        if entry is None:
            return False
        entry.state = SlotState.DELETED
        return True

    def display(self):
        print("\n[Kondisi Rak Penyimpanan Hash Table]:")
        for i in range(self.SIZE):
            print(f"Slot {i}: ", end="")
            if self.table[i].state == SlotState.EMPTY:
                print("KOSONG (EMPTY)")
            elif self.table[i].state == SlotState.DELETED:
                print("BEKAS BARANG (DELETED)")
            else:
                print(f"Barcode: {self.table[i].key} -> Barang: {self.table[i].value}")


def main():
    kasir_toko = HashMapOpenAddressing(size=10)
    
    print("==================================================")
    print("   SIMULASI SISTEM KASIR TOKO KELONTONG DIGITAL   ")
    print("==================================================")
    print("\n--- 1. Menambahkan Barang ke Sistem ---")
    kasir_toko.insert(101, "Indomie Goreng")
    kasir_toko.insert(111, "Minyak Goreng 1 Liter") 
    kasir_toko.insert(121, "Beras Premium 5 Kg")    
    kasir_toko.insert(105, "Susu Kotak UHT")
    
    kasir_toko.display()
    
    print("\n--- 2. Simulasi Pembeli Datang ke Kasir (Scan Barang) ---")
    barcode_scan = 111
    print(f"Kasir men-scan barcode: [{barcode_scan}]")
    
    item = kasir_toko.search(barcode_scan)
    if item:
        print(f"Hasil Layar Kasir: BARANG DITEMUKAN! -> {item.value}")
    else:
        print("Hasil Layar Kasir: BARANG TIDAK TERDAFTAR!")
     
    print("\n--- 3. Barang Habis, Dihapus dari Sistem ---")
    barcode_hapus = 111
    print(f"Menghapus kode [{barcode_hapus}] (Minyak Goreng) karena stok gudang kosong...")
    kasir_toko.remove_key(barcode_hapus)
    
    kasir_toko.display()
 
    print("\n--- 4. Scan Barang Lain Setelah Ada Penghapusan ---")
    barcode_beras = 121
    print(f"Kasir men-scan Beras Premium dengan kode: [{barcode_beras}]")
    
    item_beras = kasir_toko.search(barcode_beras)
    if item_beras:
        print(f"Hasil Layar Kasir: {item_beras.value} MASIH ditemukan dengan aman!")
    else:
        print("Hasil Layar Kasir: Gawat, Beras hilang dari sistem!")
    print("\n==================================================")


if __name__ == "__main__":
    main()