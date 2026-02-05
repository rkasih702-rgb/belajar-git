#  Program: Rapor Siswa (Versi Sederhana)
# Dibuat oleh Kasih Rijalllll

def hitung_rata(nilai):
    return sum(nilai) / len(nilai)

def get_predikat(rata):
    if rata >= 90:
        return "A (Sangat Baik)"
    elif rata >= 80:
        return "B (Baik)"
    elif rata >= 70:
        return "C (Cukup)"
    elif rata >= 60:
        return "D (Kurang)"
    else:
        return "E (Sangat Kurang)"

def tampilkan_rapor(nama, kelas, daftar_nilai):
    print("\n==== RAPOR SISWA ====")
    print(f"Nama  : {nama}")
    print(f"Kelas : {kelas}")
    print("------------------------------")

    total = 0
    for pelajaran, nilai in daftar_nilai.items():
        print(f"{pelajaran:15s} : {nilai}")
        total += nilai

    rata = total / len(daftar_nilai)
    print("------------------------------")
    print(f"Rata-rata : {rata:.2f}")
    print(f"Predikat  : {get_predikat(rata)}")
    print("==============================\n")

# ==== Main Program ====
print("=== Program Input Rapor Siswa ===")
nama = input("Masukkan nama siswa: ")
kelas = input("Masukkan kelas: ")

# Daftar mata pelajaran (bisa diubah)
mapel = ["Matematika", "Bahasa Indonesia", "Bahasa Inggris", "IPA", "IPS"]
nilai_mapel = {}

for pelajaran in mapel:
    while True:
        nilai = float(input(f"Masukkan nilai{pelajaran}: "))
        if nilai > 100:
            print("melebihi batas")
        else:
            break
    nilai_mapel[pelajaran] = nilai

# Tampilkan hasil rapor
tampilkan_rapor(nama, kelas,nilai_mapel)