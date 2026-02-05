# library_receipt.py
# Program struk peminjaman buku di perpustakaan

from datetime import datetime, timedelta

def cetak_struk_perpustakaan(nama_perpus, nama_petugas, nama_anggota, buku_list, lama_pinjam=7, tanggal_pinjam=None):
    """
    nama_perpus : str - nama perpustakaan
    nama_petugas : str - nama petugas
    nama_anggota : str - nama anggota
    buku_list : list of dict - [{'judul':..., 'pengarang':..., 'kode':...}, ...]
    lama_pinjam : int - jumlah hari peminjaman
    tanggal_pinjam : datetime - jika None, pakai waktu saat ini
    """

    if tanggal_pinjam is None:
        tanggal_pinjam = datetime.now()

    tanggal_kembali = tanggal_pinjam + timedelta(days=lama_pinjam)

    print("="*50)
    print(f"{nama_perpus:^50}")
print("="*50)
    print(f"Tanggal Pinjam : {tanggal_pinjam.strftime('%d-%m-%Y %H:%M')}")
    print(f"Tanggal Kembali: {tanggal_kembali.strftime('%d-%m-%Y')}")
    print(f"Petugas        : {nama_petugas}")
    print(f"Nama Anggota   : {nama_anggota}")
    print("-"*50)
    print(f"{'No':<4}{'Kode Buku':<12}{'Judul Buku':<22}{'Pengarang':<12}")
    print("-"*50)

    for i, b in enumerate(buku_list, 1):
        print(f"{i:<4}{b['kode']:<12}{b['judul'][:20]:<22}{b['pengarang'][:12]:<12}")

    print("-"*50)
    print("Harap mengembalikan buku tepat waktu.")
    print("Denda keterlambatan: Rp 1.000 / hari / buku")
    print("="*50)
    print("Terima kasih telah berkunjung ke perpustakaan!")
    print("="*50)


# === Contoh penggunaan ===
if _name_ == "_main_":
    nama_perpus = "PERPUSTAKAAN NEGERI CERDAS"
    nama_petugas = "Siti"
    nama_anggota = "Kasih Rizal"

    daftar_buku = [
        {'kode': 'BK001', 'judul': 'Laskar Pelangi', 'pengarang': 'Andrea Hirata'},
        {'kode': 'BK002', 'judul': 'Bumi Manusia', 'pengarang': 'Pramoedya A. Toer'},
        {'kode': 'BK003', 'judul': 'Negeri 5 Menara', 'pengarang': 'A. Fuadi'},
    ]

    cetak_struk_perpustakaan(nama_perpus, nama_petugas, nama_anggota, daftar_buku, lama_pinjam=14)