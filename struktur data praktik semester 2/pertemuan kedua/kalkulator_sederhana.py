class KalkulatorSederhana:
    def __init__(self, bilangan1, bilangan2):
        self.bilangan1 = bilangan1
        self.bilangan2 = bilangan2

    def setBilangan1(self, bilangan1):
        self.bilangan1 = bilangan1

    def setBilangan2(self, bilangan2):
        self.bilangan2 = bilangan2

    def tambah(self):
        hasil = self.bilangan1 + self.bilangan2
        print("Hasil Penjumlahan =", hasil)

    def pangkat(self):
        hasil = 1

        for i in range(self.bilangan2):
            hasil = hasil * self.bilangan1

        print("Hasil Pangkat =", hasil)


# membuat objek
kalkulator = KalkulatorSederhana(3, 5)

# menjalankan method
kalkulator.tambah()
kalkulator.pangkat()