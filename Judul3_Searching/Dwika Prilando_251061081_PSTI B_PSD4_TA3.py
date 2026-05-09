def cps(daftar_stok, produk_dicari):
    n = len(daftar_stok)
    produk_dicari = produk_dicari.lower()
    last_item = daftar_stok[n - 1]
    daftar_stok[n - 1] = produk_dicari
    i = 0
    while daftar_stok[i].lower() != produk_dicari:
        i += 1
    daftar_stok[n - 1] = last_item
    if i < n - 1 or daftar_stok[n - 1].lower() == produk_dicari:
        return i
    return -1

stok_toko = ["Beras", "Minyak Goreng", "Gula", "Garam", "Telur", "Terigu", "Kopi", "Tempe"]

print(" SISTEM CEK STOK TOKO ")
barang = input("Masukkan nama barang yang ingin dicari: ")

indeks = cps(stok_toko, barang)

if indeks != -1:
    print(f"Barang'{stok_toko[indeks]}' tersedia di rak nomor {indeks + 1}.")
else:
    print(f"Maaf, stok barang '{barang}' sedang kosong atau tidak terdaftar.")