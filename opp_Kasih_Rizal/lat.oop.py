class Siswa:
    def __init__(self, nama, jurusan):
        self.nama = nama
        self.jurusan = jurusan

    def info(self):
        print("Nama:", self.nama)
        print("Jurusan:", self.jurusan)

siswa1 = Siswa("Kasih Rizal", "RPL")
siswa1.info()
