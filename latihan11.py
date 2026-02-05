# Fungsi pertama untuk menjumlahkan dua angka
def jumlahkan(a, b):
    return a + b

# Fungsi kedua untuk menampilkan hasil penjumlah
def tampilkan_hasil(angka1,angka2):
    hasil=jumlahkan(angka1,angka2)# Memanggil fungsi jumlahkan
    print(f"Hasil dari{angka1}+{angka2}adalah:{hasil}")

    # Panggil fungsi tampilkan_hasil untuk menjalankan program
    tampilkan_hasil(10,5)
    tampilkan_hasil(25,7)