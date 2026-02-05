class Pegawai:
    def __init__(self, nama):
        self.nama = nama

class Guru(Pegawai):
    def __init__(self, nama, mapel):
        super().__init__(nama)
        self.mapel = mapel

    def info(self):
        print(self.nama, "mengajar", self.mapel)

g = Guru("Pak Budi", "Informatika")
g.info()
