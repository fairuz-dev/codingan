def total_belanja(harga_list):
    total = sum(harga_list)

    if total >= 500000:
        total = total - (total * 0.10)

    return round(total)


harga_barang = [200000, 150000, 175000]

hasil = total_belanja(harga_barang)

print("Total belanja:", hasil)
