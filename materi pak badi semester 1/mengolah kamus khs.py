khs = { 
    1 : {'kode':'K20001','mata_kul':'Pemrograman','nilai':'A','sks':3},
    2 : {'kode':'K20002','mata_kul':'Jaringan komputer','nilai':'B','sks':2},
    3 : {'kode':'K20003','mata_kul':'Algoritma','nilai':'C','sks':3},
    4 : {'kode':'K20004','mata_kul':'Statistik','nilai':'B','sks':3},
    5 : {'kode':'K20005','mata_kul':'Matematika','nilai':'B','sks':3},
    6 : {'kode':'K20006','mata_kul':'Fisika','nilai':'B','sks':3}
}

def hitung_skor(nilai, sks):
    if nilai == 'A':
        nil = 4
    elif nilai == 'B':
        nil = 3
    elif nilai == 'C':
        nil = 2
    else:
        nil = 1
    skor = nil * sks
    return skor 

print('KODE   MATAKULIAH           NILAI SKS SKOR')
print("==========================================")
for i in range(len(khs)):
    skor=hitung_skor((khs[i+1]["nilai"]),(khs[i+1]["sks"]))
    print ("{:6s}".format(khs[i+1]['kode']),
           "{:20s}".format(khs[i+1]['mata_kul']), 
           "{:5s}".format(khs[i+1]["nilai"]),
           "{:1d}".format(khs[i+1]["sks"]),
           "{:4d}".format(skor))