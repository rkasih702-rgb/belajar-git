class siswa:
    def __init__(self, nama, kelas):
        self.nama = nama
        self.kelas = kelas

    def tampilkan_info (self):
        print ("Nama : ", self.nama)
        print ("Kelas :", self.kelas)

S1 = siswa ("kasih","x pplg 1")
S1.tampilkan_info()