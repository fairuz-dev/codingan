antrian = []
terlayani = []

def tambah_antrian():
    nim = input("Masukkan NIM: ")
    antrian.append(nim)
    print("Berhasil ditambahkan")

def cetak_antrian():
    if antrian == []:
        print("Antrian kosong")
    else:
        print("Daftar antrian:")
        for i in antrian:
            print(i)

def panggil_mahasiswa():
    if antrian == []:
        print("Antrian kosong")
    else:
        ambil = antrian.pop(0)
        terlayani.append(ambil)
        print("Mahasiswa dengan NIM", ambil, "dipanggil")

def cetak_terlayani():
    if terlayani == []:
        print("Belum ada yang dilayani")
    else:
        print("Yang sudah dilayani:")
        data = sorted(terlayani)  
        for i in data:
            print(i)

while True:
    print("\n====== Sistem antrian mahasiswa bimbingan ====")
    print("1. Tambah antrian mahasiswa")
    print("2. Cetak daftar mahasiswa yang mengantri")
    print("3. Panggil 1 mahasiswa dari antrian untuk dilayani")
    print("4. Cetak mahasiswa yang sudah dilayani dengan metode sorting")
    print("5. Keluar")


    pilih = input("Pilih: ")

    if pilih == "1":
        tambah_antrian()
    elif pilih == "2":
        cetak_antrian()
    elif pilih == "3":
        panggil_mahasiswa()
    elif pilih == "4":
        cetak_terlayani()
    elif pilih == "5":
        break
    else:
        print("Pilihan salah")