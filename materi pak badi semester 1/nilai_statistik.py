def statistik_nilai(data):
    nilai_maksimum = max(data)
    nilai_minimum = min(data)
    rata_rata = sum(data) / len(data)
    jumlah_data = len(data)

    return nilai_maksimum, nilai_minimum, rata_rata, jumlah_data


data = [80, 90, 75, 85, 95]

hasil = statistik_nilai(data)

print("Nilai maksimum:", hasil[0])
print("Nilai minimum:", hasil[1])
print("Rata-rata:", hasil[2])
print("Jumlah data:", hasil[3])

