def tukar(arr, i, j):
  temp = arr[i]
  arr[i] = arr[j]
  arr[j] = temp

def selection_sort(arr, n):
    for i in range(n - 1):
        pos = i
        for j in range(i + 1, n):
            if arr[j][1] > arr[pos][1]:
                pos = j
        if pos != i:
            tukar(arr, i, pos)


def main():
  n = int(input("Masukkan jumlah nama dan rekor : ")) 
  data_rekor = []
  for i in range(n):
        print(f"\nData ke-{i + 1}:")
        nama = input("Masukkan nama: ")
        while True:
            try:
                beban = int(input(f"Masukkan beban angkatan {nama} (Kg): "))
                data_rekor.append([nama, beban])
                break
            except ValueError:
                print("Input beban tidak valid, masukkan angka!")

  print("\n" + "="*30)
  print(f"Data sebelum diurutkan: {data_rekor}")


  selection_sort(data_rekor, n)

  print("\nRanking Beban Terberat :")
  for i in range(n):
        nama_orang = data_rekor[i][0]
        beban_orang = data_rekor[i][1]
        print(f"{i+1}. {nama_orang}: {beban_orang} Kg")

  print("="*30)

if __name__ == "__main__":
    main()