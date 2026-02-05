# Akses elemen (indexing)
buah = ("apel", "mangga", "jeruk", "pisang")
print("Elemen pertama:", buah[0]) # Output: apel
print("Elemen terakhir:", buah[-1]) # Output: pisang

# Slicing (memotong tuple)
print("Dua elemen pertama:", buah[0:2]) # Output (apel, mangga)

# panjang tuple
print("Jumlah buah:", len(buah)) # Output: 4

# Mengecek keberadaan elemen
print("Apakah 'durian' ada?", "durian" in buah)