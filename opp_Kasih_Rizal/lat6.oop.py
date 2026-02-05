class Hewan:
    def makan(self):
        print("Hewan sedang makan")

class Burung(Hewan):
    def terbang(self):
        print("Burung bisa terbang")

b = Burung()
b.makan()
b.terbang()
