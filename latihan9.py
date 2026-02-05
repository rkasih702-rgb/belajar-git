#Program Diskon Belanja 
# Program Diskon Belanja

print("=== Program Diskon Belanja ===")

# Input total belanja
total_belanja = float(input("Masukkan total belanja (Rp): "))

# Aturan diskon
# >= 500000 → diskon 20%
# >= 300000 → diskon 15%
# >= 100000 → diskon 10%
# < 100000  → tidak ada diskon

if total_belanja >= 500000:
    diskon = 0.20
elif total_belanja >= 300000:
    diskon = 0.15
elif total_belanja >= 100000:
    diskon = 0.10
else:
    diskon = 0.0

# Hitung jumlah diskon
jumlah_diskon = total_belanja * diskon
total_bayar = total_belanja - jumlah_diskon

# Output
print(f"Total belanja : Rp {total_belanja:,.0f}")
print(f"Diskon        : {diskon*100:.10f}%")
print(f"Potongan      : Rp {jumlah_diskon:,.0f}")
print(f"Total bayar   : Rp {total_bayar:,.0f}")
