# === APLIKASI PERPUSTAKAAN MINI ===
# Dibuat untuk pembelajaran pemrograman terstruktur di SMK

# Daftar buku disimpan dalam list of dictionary
buku_list = []

# --- Fungsi dan Prosedur ---

# Prosedur menampilkan menu utama
def tampilkan_menu():
    print("\n===== MENU PERPUSTAKAAN =====")
    print("1. Tambah Buku")
    print("2. Lihat Daftar Buku")
    print("3. Cari Buku")
    print("4. Pinjam Buku")
    print("5. Kembalikan Buku")
    print("6. Keluar")

# Prosedur menambah buku baru
def tambah_buku():
    judul = input("Masukkan judul buku: ")
    penulis = input("Masukkan nama penulis: ")
    buku = {"judul": judul, "penulis": penulis, "status": "Tersedia"}
    buku_list.append(buku)
    print(f"Buku '{judul}' berhasil ditambahkan!")

# Prosedur menampilkan semua buku
def tampilkan_buku():
    if not buku_list:
        print("Belum ada buku dalam perpustakaan.")
    else:
        print("\n=== DAFTAR BUKU ===")
        for i, buku in enumerate(buku_list, start=1):
            print(f"{i}. {buku['judul']} - {buku['penulis']} ({buku['status']})")

# Fungsi mencari buku berdasarkan judul