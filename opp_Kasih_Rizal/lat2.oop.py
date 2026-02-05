class Siswa:
    def __init__(self, nama, kelas, jurusan):
        self.nama = nama
        self.kelas = kelas
        self.jurusan = jurusan

    def tampilkan_data(self):
        print("=== DATA SISWA SMK ===")
        print("Nama    :", self.nama)
        print("Kelas   :", self.kelas)
        print("Jurusan :", self.jurusan)


# Membuat objek dari class Siswa
siswa1 = Siswa("joss", "X", "RPL")
siswa2 = Siswa("gawin", "X", "TKJ")

# Memanggil method
siswa1.tampilkan_data()
print()
siswa2.tampilkan_data()
