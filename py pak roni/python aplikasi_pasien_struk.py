# rumah sakit GMM
# rumah sakit GMM

print("=== RUMAH SAKIT GMM ===")

# 1. Data diri pasien
nama = input("Nama pasien        : ")
umur = input("Umur pasien        : ")
alamat = input("Alamat pasien      : ")
kelas_kamar = input("Kelas kamar (VIP/I/II/III) : ").upper()
gejala = input("Gejala/Sakit       : ")

# Hari rawat dan biaya pendaftaran
hari_rawat = int(input("Jumlah hari rawat             : "))
biaya_pendaftaran = float(input("Biaya pendaftaran (sesuai penyakit) : Rp "))

# 2. Biaya otomatis berdasarkan aturan
if kelas_kamar == "VIP":
    biaya_inap = 500000 * hari_rawat
elif kelas_kamar == "I":
    biaya_inap = 350000 * hari_rawat
elif kelas_kamar == "II":
    biaya_inap = 250000 * hari_rawat
elif kelas_kamar == "III":
    biaya_inap = 150000 * hari_rawat
else:
    print("Kelas kamar tidak valid, dianggap kelas III.")
    biaya_inap = 150000 * hari_rawat

biaya_pengobatan_masa_tunggu = 200000 * hari_rawat
biaya_konsultasi_dokter = 125000
biaya_tindakan_medis = 500000
biaya_makan = 300000 * hari_rawat
biaya_layanan_tambahan = 400000

# Obat-obatan (manual)
jumlah_obat = int(input("Jumlah jenis obat             : "))
harga_obat = float(input("Harga per obat (Rp)           : "))
biaya_obat = jumlah_obat * harga_obat
# BPJS
pakai_bpjs = input("Apakah pasien menggunakan BPJS? (ya/tidak): ").lower()

# Hitung total biaya
total_biaya = (
    biaya_pendaftaran
    + biaya_pengobatan_masa_tunggu
    + biaya_inap
    + biaya_konsultasi_dokter
    + biaya_tindakan_medis
    + biaya_makan
    + biaya_obat
    + biaya_layanan_tambahan
)

# Hitung potongan BPJS
if pakai_bpjs == "ya":
    tanggungan_bpjs = (
        biaya_konsultasi_dokter
        + biaya_obat
        + biaya_makan
        + biaya_inap
        + biaya_pengobatan_masa_tunggu
    )
else:
    tanggungan_bpjs = 0

total_setelah_bpjs = total_biaya - tanggungan_bpjs

# 3. Tanggal pulang atau status
tanggal_pulang = input("Tanggal pulang (YYYY-MM-DD): ")
status = input("Masih di rumah sakit? (ya/tidak): ").lower()
masih_dirumah_sakit = True if status == "ya" else False

# 4. Cetak hasil
print("\n==============================================")
print("       DATA PASIEN - RUMAH SAKIT GMM")
print("==============================================")
print(f"Nama pasien        : {nama}")
print(f"Umur               : {umur} tahun")
print(f"Alamat             : {alamat}")
print(f"Kelas kamar        : {kelas_kamar}")
print(f"Gejala/Sakit       : {gejala}")
print("----------------------------------------------")
print(f"Biaya pendaftaran              : Rp {biaya_pendaftaran:,.0f}")
print(f"Biaya pengobatan masa tunggu   : Rp {biaya_pengobatan_masa_tunggu:,.0f}")
print(f"Biaya inap ({hari_rawat} hari)            : Rp {biaya_inap:,.0f}")
print(f"Biaya konsultasi dokter        : Rp {biaya_konsultasi_dokter:,.0f}")
print(f"Biaya tindakan medis           : Rp {biaya_tindakan_medis:,.0f}")
print(f"Biaya makan ({hari_rawat} hari)           : Rp {biaya_makan:,.0f}")
print(f"Biaya obat-obatan              : Rp {biaya_obat:,.0f}")
print(f"Biaya layanan tambahan         : Rp {biaya_layanan_tambahan:,.0f}")
print("----------------------------------------------")
print(f"TOTAL BIAYA                    : Rp {total_biaya:,.0f}")
print(f"Tanggungan BPJS                : Rp {tanggungan_bpjs:,.0f}")
print("----------------------------------------------")
print(f"TOTAL DIBAYAR (setelah BPJS)   : Rp {total_setelah_bpjs:,.0f}")
print("----------------------------------------------")
print(f"Tanggal pulang                 : {tanggal_pulang}")
print(f"Masih di rumah sakit?          : {'YA' if masih_dirumah_sakit else 'TIDAK'}")
print(f"Menggunakan BPJS?              : {'YA' if pakai_bpjs == 'ya' else 'TIDAK'}")
print("==============================================")