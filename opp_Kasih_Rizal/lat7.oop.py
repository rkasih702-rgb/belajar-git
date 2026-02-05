class Karyawan:
    def absen(self):
        print("Absen masuk")

class Admin(Karyawan):
    def data(self):
        print("Mengelola data")

class Kasir(Karyawan):
    def transaksi(self):
        print("Melakukan transaksi")
