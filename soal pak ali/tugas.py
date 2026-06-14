listkota = {}
print("1. Kelola Jaringan Hub")
print("2. Kelola Administrasi resi pengiriman")
pilihan = int(input("Masukkan pilihan: "))
if pilihan == 1:
    print("1.1) Input Hub kota baru")
    print("1.2) Tambahkan rute antar kota")
    pilihan1 = int(input("Masukkan pilihan: "))
    if pilihan1 == 1:
        kota = input("Masukkan nama kota: ")
        listkota[kota] = []
elif pilihan == 2:
    print("2.1) Input resi pengiriman baru")
    print("2.2) Lihat seluruh data resi terdaftar")
    print("2.3) Urutkan data resi berdasarkan biaya terbesar")