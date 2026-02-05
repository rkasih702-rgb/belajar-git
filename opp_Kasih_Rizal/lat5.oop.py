class Siswa:
    def __init__(self, nama, kelas, nilai):
        self.nama = nama
        self.kelas = kelas
        self.nilai = nilai

    def tampilkan_data(self):
        print("\n=== DATA SISWA ===")
        print("Nama  :", self.nama)
        print("Kelas :", self.kelas)
        print("Nilai :", self.nilai)

    def status_kelulusan(self):
        if self.nilai >= 75:
            print("Status: LULUS")
        else:
            print("Status: TIDAK LULUS")


# Input dari pengguna
nama = input("Masukkan nama siswa   : ")
kelas = input("Masukkan kelas siswa  : ")
nilai = int(input("Masukkan nilai siswa  : "))

siswa = Siswa(nama, kelas, nilai)
siswa.tampilkan_data()
siswa.status_kelulusan()
