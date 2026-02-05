def linear_search(data, target):
    for i in range (len(data)):
        if data[i] == target:
            return i # Mengembalikan indeks jika ditemukan
    return -1 # Mengembalikan -1 jika tidak ditemukan

# Contoh penggunaan
data = [4, 2, 7, 1, 9]
target = 7

hasil = linear_search(data, target)

if hasil != -1:
    print(f"Elemen {target} ditemukan pada indeks {hasil}.")
else:
    print(f"Elemen {target} tidak ditemukan dalam data.")