class Siswa:
    def __init__(self, nama, kelas, nilai):
        self.nama = nama
        self.kelas = kelas
        self.nilai = nilai

    def tampilkan_data(self):
        print("=== DATA SISWA ===")
        print("Nama  :", self.nama)
        print("Kelas :", self.kelas)
        print("Nilai :", self.nilai)

    def status_kelulusan(self):
        if self.nilai >= 75:
            print("Status: LULUS")
        else:
            print("Status: TIDAK LULUS")


siswa1 = Siswa("phuwin", "X RPL", 80)
siswa1.tampilkan_data()
siswa1.status_kelulusan()
