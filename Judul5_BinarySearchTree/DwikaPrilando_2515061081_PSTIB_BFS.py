class MemberNode:
    def __init__(self, member_id, nama):
        self.member_id = member_id
        self.nama = nama
        self.left = None
        self.right = None

class GymMemberSystem:
    def __init__(self):
        self.root = None

    def tambah_member(self, member_id, nama):
        if not self.root:
            self.root = MemberNode(member_id, nama)
        else:
            self._insert(self.root, member_id, nama)
        print(f"-> Member {nama} (ID: {member_id}) berhasil ditambahkan.")

    def _insert(self, current, member_id, nama):
        if member_id < current.member_id:
            if current.left is None:
                current.left = MemberNode(member_id, nama)
            else:
                self._insert(current.left, member_id, nama)
        else:
            if current.right is None:
                current.right = MemberNode(member_id, nama)
            else:
                self._insert(current.right, member_id, nama)

    def cari_member(self, member_id):
        return self._search(self.root, member_id)

    def _search(self, current, member_id):
        if current is None:
            return None
        if current.member_id == member_id:
            return current.nama
        if member_id < current.member_id:
            return self._search(current.left, member_id)
        return self._search(current.right, member_id)


def main():
    gym = GymMemberSystem()
    while True:
        print("MENU PENGELOLAAN MEMBER GYM ")
        print("1. Tambah Member")
        print("2. Cari Data Member (berdasarkan ID)")
        print("3. Keluar")
        pilihan = input("Pilih menu : ")

        if pilihan == '1':
            try:
                id_member = int(input("Masukkan ID Member: "))
                nama = input("Masukkan Nama Member: ")
                gym.tambah_member(id_member, nama)
            except ValueError:
                print("ID harus berupa angka!")
        
        elif pilihan == '2':
            try:
                id_cari = int(input("Masukkan ID yang dicari: "))
                hasil = gym.cari_member(id_cari)
                if hasil:
                    print(f"Hasil: Member dengan ID {id_cari} adalah {hasil}.")
                else:
                    print("Status: Member tidak ditemukan.")            
            except ValueError:
                print("ID harus berupa angka!")

        elif pilihan == '3':
            print("Keluar dari sistem. Selamat beraktivitas!")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()