# Program Toko

print ("\n          TOKO FAIRUZ IMUT ")
print ("=====================================")

while True:
    jumlah_barang = int(input("Masukan Jumlah Barang: "))
    total_belanja = 0
    for i in range (jumlah_barang):
        harga = float(input(f"Masukan Harga Barang ke-{i+1}: Rp "))
        total_belanja += harga
    member = input("Apakah Punya Kartu Member? (y/n): ").lower()
    if total_belanja >= 200000 and member == "y":
        diskon = total_belanja*0.20
    elif total_belanja >= 20000 and member == "n":
        diskon = total_belanja*0.10
    else:
        diskon = 0
    
    bayar = total_belanja - diskon

    print ("\n===========TOTAL BELANJA==============")
    print (f"Jumlah Barang : {jumlah_barang} ")
    print (f"Total Belanja : Rp {total_belanja:,.0f}")
    print (f"Diskon        : Rp {diskon:,.0f}")
    print (f"Jumlah Bayar  : Rp {bayar:,.0f}")
    print ("\nTERIMAKASIH SUDAH BERBELANJA")
    print ("======================================")

    ulang = input("\nApakah Ingin Input Ulang? (y/n): ").lower()
    if ulang != "y":
        print ("\nPROGRAM SELESAI")
        break

    

    