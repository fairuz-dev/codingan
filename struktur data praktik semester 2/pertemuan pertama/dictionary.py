data_olahraga = {
    "Sepak Bola": {
        1: "Jack",
        2: "Holmes",
        3: "Boby",
        4: "Patrick",
        5: "Putera"
    },
    "Bulu Tangkis": {
        1: "Putri",
        2: "Elaina",
        3: "Laila",
        4: "Inara",
        5: "Andini"
    },
    "Voli": {
        1: "Gojo",
        2: "Yamada",
        3: "Natsume",
        4: "Shinichi",
        5: "Veino"
    }
}

while True:
    print("\n=== Pilih Cabang Olahraga Favorit ===")
    print("1. Sepak Bola")
    print("2. Bulu Tangkis")
    print("3. Voli")
    print("4. Keluar")

    pilihan = input("Masukkan nomor pilihan (1/2/3/4): ")

    if pilihan == "1":
        cabang_dipilih = "Sepak Bola"
    elif pilihan == "2":
        cabang_dipilih = "Bulu Tangkis"
    elif pilihan == "3":
        cabang_dipilih = "Voli"
    elif pilihan == "4":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid.")
        continue

    while True:
        print(f"\nMenampilkan daftar pemain {cabang_dipilih}:")
        print("-" * 40)

        daftar_pemain = data_olahraga[cabang_dipilih]
        for no, nama in daftar_pemain.items():
            print(f"No. Punggung {no}: {nama}")

        print("-" * 40)

        try:
            no_pilih = int(input("Ketik Nomor Punggung: "))
            if no_pilih in daftar_pemain:
                print(f"Pemain favorit anda: {daftar_pemain[no_pilih]}")
            else:
                print("Nomor punggung tidak ditemukan.")
                continue
        except ValueError:
            print("Input harus berupa angka.")
            continue

        print("\n=== MENU LANJUTAN ===")
        print("1. Balik ke Menu Utama")
        print("2. Pilih Ulang Pemain")
        print("3. Berhentikan Program")

        lanjut = input("Masukkan pilihan (1/2/3): ")

        if lanjut == "1":
            break
        elif lanjut == "2":
            continue
        elif lanjut == "3":
            print("Program dihentikan.")
            exit()
        else:
            print("Pilihan tidak valid.")
            break
        
        
        