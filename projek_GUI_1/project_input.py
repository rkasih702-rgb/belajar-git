import tkinter as tk
from tkinter import ttk, messagebox

# ---------------------------
#  FUNGSI
# ---------------------------
def tambah_data():
    nama = entry_nama.get()
    kelas = entry_kelas.get()

    if not nama or not kelas:
        messagebox.showwarning("Peringatan", "Semua data harus diisi!")
        return

    tabel.insert("", "end", values=(nama, kelas,))

    entry_nama.delete(0, tk.END)
    entry_kelas.delete(0, tk.END)

def hapus_data():
    selected = tabel.selection()
    if not selected:
        messagebox.showwarning("Peringatan", "Pilih data yang ingin dihapus!")
        return

    tabel.delete(selected)

# ---------------------------
#  GUI UTAMA
# ---------------------------
root = tk.Tk()
root.title("Aplikasi Data Siswa")
root.geometry("600x400")

# ---------------------------
#  LABEL & ENTRY
# ---------------------------
tk.Label(root, text="Nama Siswa").grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_nama = tk.Entry(root, width=40)
entry_nama.grid(row=0, column=1, padx=10)

tk.Label(root, text="Kelas").grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_kelas = tk.Entry(root, width=40)
entry_kelas.grid(row=1, column=1, padx=10)

# ---------------------------
#  TOMBOL
# ---------------------------
tk.Button(root, text="Tambah Data", command=tambah_data).grid(row=3, column=1, pady=10, sticky="w")
tk.Button(root, text="Hapus Data", command=hapus_data).grid(row=3, column=1, pady=10, sticky="e")

# ---------------------------
#  TABEL
# ---------------------------
columns = ("nama", "kelas")
tabel = ttk.Treeview(root, columns=columns, show="headings", height=10)
tabel.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

tabel.heading("nama", text="Nama Siswa")
tabel.heading("kelas", text="Kelas")

tabel.column("nama", width=150)
tabel.column("kelas", width=100)

root.mainloop()
