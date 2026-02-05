# ======================================================
# APLIKASI PERPUSTAKAAN MINI
# ======================================================

buku = [
    {"kode": "B001", "judul": "Laskar Pelangi", "penulis": "Andrea Hirata", "status": "Tersedia"},
    {"kode": "B002", "judul": "Bumi Manusia", "penulis": "Pramoedya A. Toer", "status": "Tersedia"},
    {"kode": "B003", "judul": "Negeri 5 Menara", "penulis": "Ahmad Fuadi", "status": "Tersedia"}
]

# ------------------------------------------------------
def tampilkan_buku():
    print("\n=== DAFTAR BUKU PERPUSTAKAAN ===")
    print("{:<6} {:<25} {:<20} {:<10}".format("Kode", "Judul", "Penulis", "Status"))
    print("-" * 65)
    for b in buku:
        print("{:<6} {:<25} {:<20} {:<10}".format(b["kode"], b["judul"], b["penulis"], b["status"]))
    print("-" * 65)

# ------------------------------------------------------
def tambah_buku():
    kode = input("Masukkan kode buku baru: ").upper()
    for b in buku:
        if b["kode"] == kode:
            print("❌ Kode buku sudah ada!")
            return
    judul = input("Masukkan judul buku: ")
    penulis = input("Masukkan nama penulis: ")
    buku.append({"kode": kode, "judul": judul, "penulis": penulis, "status": "Tersedia"})
    print("✅ Buku berhasil ditambahkan!")

# ------------------------------------------------------
def pinjam_buku():
    kode = input("Masukkan kode buku yang ingin dipinjam: ").upper()
    for b in buku:
        if b["kode"] == kode:
            if b["status"] == "Tersedia":
                b["status"] = "Dipinjam"
                print(f"✅ Buku '{b['judul']}' berhasil dipinjam.")
            else:
                print("❌ Buku sedang dipinjam orang lain.")
            return
    print("❌ Kode buku tidak ditemukan!")

# ------------------------------------------------------
def kembalikan_buku():
    kode = input("Masukkan kode buku yang ingin dikembalikan: ").upper()
    for b in buku:
        if b["kode"] == kode:
            if b["status"] == "Dipinjam":
                b["status"] = "Tersedia"
                print(f"✅ Buku '{b['judul']}' berhasil dikembalikan.")
            else:
                print("❌ Buku ini belum dipinjam.")
            return
    print("❌ Kode buku tidak ditemukan!")

# ------------------------------------------------------
def cari_buku():
    kata = input("Masukkan kata kunci judul/penulis: ").lower()
    hasil = [b for b in buku if kata in b["judul"].lower() or kata in b["penulis"].lower()]
    if hasil:
        print("\n=== HASIL PENCARIAN ===")
        print("{:<6} {:<25} {:<20} {:<10}".format("Kode", "Judul", "Penulis", "Status"))
        print("-" * 65)
        for b in hasil:
            print("{:<6} {:<25} {:<20} {:<10}".format(b["kode"], b["judul"], b["penulis"], b["status"]))
        print("-" * 65)
    else:
        print("❌ Tidak ada buku yang cocok dengan pencarianmu.")

# ------------------------------------------------------
def menu():
    while True:
        print("""
=== MENU PERPUSTAKAAN MINI ===
1. Tampilkan Semua Buku
2. Tambah Buku Baru
3. Pinjam Buku
4. Kembalikan Buku
5. Cari Buku
6. Keluar
""")
        pilihan = input("Pilih menu (1-6): ")

        if pilihan == "1":
            tampilkan_buku()
        elif pilihan == "2":
            tambah_buku()
        elif pilihan == "3":
            pinjam_buku()
        elif pilihan == "4":
            kembalikan_buku()
        elif pilihan == "5":
            cari_buku()
        elif pilihan == "6":
            print("📚 Terima kasih telah menggunakan Aplikasi Perpustakaan Mini!")
            break
        else:
            print("❌ Pilihan tidak valid, coba lagi!")

# ------------------------------------------------------
menu()
