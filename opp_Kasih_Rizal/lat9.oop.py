class NilaiSiswa:
    def __init__(self, nama):
        self.nama = nama

    def hitung_nilai(self, *nilai):
        if len(nilai) == 0:
            return "Tidak ada nilai yang dimasukkan"

        total = 0
        for n in nilai:
            total += n

        rata_rata = total / len(nilai)

        if rata_rata >= 85:
            grade = "A"
        elif rata_rata >= 75:
            grade = "B"
        elif rata_rata >= 65:
            grade = "C"
        else:
            grade = "D"

        return f"""
Nama Siswa : {self.nama}
Jumlah Nilai : {len(nilai)}
Total Nilai  : {total}
Rata-rata    : {rata_rata:.2f}
Grade       : {grade}
"""

# objek
siswa1 = NilaiSiswa("Andi")

print(siswa1.hitung_nilai(80))
print(siswa1.hitung_nilai(75, 85))
print(siswa1.hitung_nilai(70, 80, 90, 85))
