class Lagu:
    def __init__(self, judul, artis):
        self.judul = judul
        self.artis = artis
        self.next = None

class Playlist:
    def __init__(self):
        self.head = None

    def tambah_lagu(self, judul, artis):
        baru = Lagu(judul, artis)
        if not self.head:
            self.head = baru
            return

        arus = self.head
        while arus.next:
            arus = arus.next
        arus.next = baru

    def tampilkan_playlist(self):
        if not self.head:
            print("Playlist kosong.")
            return

        print("\n--- Daftar Putar Lagu ---")
        arus = self.head
        nomor = 1
        while arus:
            print(f"{nomor}. {arus.judul} - {arus.artis}")
            arus = arus.next
            nomor += 1


    def hapus_lagu_depan(self):
        if self.head:
            print(f"\nMemutar dan menghapus: {self.head.judul}")
            self.head = self.head.next
        else:
            print("Tidak ada lagu untuk diputar.")

#contoh pemakaian untuk mengisi
my_playlist = Playlist()
my_playlist.tambah_lagu("Hana No Tou", "Sayuri")
my_playlist.tambah_lagu("Heikousen", "Sayuri")
my_playlist.tambah_lagu("Winning The Soul", "Tokai Teio")

#Memutar lagu
my_playlist.tampilkan_playlist()
my_playlist.hapus_lagu_depan()
my_playlist.tampilkan_playlist()