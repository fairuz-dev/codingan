"""
SILOG - Sistem Informasi Logistik
Tugas Final Struktur Data - Semester Genap T.A. 2025/2026

Nama Mahasiswa : Fairuz Ramadhani
NPM            : 5250411241
Digit Terakhir NIM: 1 (GANJIL)
  -> Algoritma Sorting : Quick Sort
  -> Format No. Resi   : Diawali angka '1' (4 digit)
  -> Kota Hub Default  : Mengandung 3 huruf pertama nama depan (FAI)
"""

# ── STRUKTUR DATA GLOBAL ──────────────────────────────────────
graph = {}; bst_root = None; kurir_list = []; manifest = {}
SEPARATOR = "=" * 60; SEP_THIN = "-" * 60

class BSTNode:
    def __init__(self, no_resi, nama_pengirim, kota_asal, kota_tujuan, berat, total_biaya):
        self.no_resi, self.nama_pengirim = no_resi, nama_pengirim
        self.kota_asal, self.kota_tujuan = kota_asal, kota_tujuan
        self.berat, self.total_biaya = berat, total_biaya
        self.left = self.right = None

# ── GRAPH ─────────────────────────────────────────────────────
def tambah_hub(k):
    k = k.strip()
    if k in graph: print(f"  [!] Kota '{k}' sudah terdaftar."); return False
    graph[k] = {}; print(f"  [+] Hub kota '{k}' berhasil ditambahkan."); return True

def tambah_rute(a, b, j):
    a, b = a.strip(), b.strip()
    if a not in graph: print(f"  [!] Kota '{a}' belum terdaftar di graph."); return False
    if b not in graph: print(f"  [!] Kota '{b}' belum terdaftar di graph."); return False
    if a == b: print("  [!] Kota asal dan tujuan tidak boleh sama."); return False
    graph[a][b] = graph[b][a] = j
    print(f"  [+] Rute {a} <-> {b} sejauh {j} KM berhasil ditambahkan."); return True

def cek_rute_tersedia(a, b): return a in graph and b in graph and b in graph[a]
def get_jarak(a, b): return graph[a][b]

# ── BST ───────────────────────────────────────────────────────
def bst_insert(root, node):
    if root is None: return node
    if node.no_resi < root.no_resi: root.left = bst_insert(root.left, node)
    elif node.no_resi > root.no_resi: root.right = bst_insert(root.right, node)
    else: print(f"  [!] No. Resi '{node.no_resi}' sudah terdaftar.")
    return root

def bst_cari(root, nr):
    if root is None: return None
    if nr == root.no_resi: return root
    return bst_cari(root.left if nr < root.no_resi else root.right, nr)

def bst_inorder(root, h=None):
    if h is None: h = []
    if root: bst_inorder(root.left, h); h.append(root); bst_inorder(root.right, h)
    return h

# ── QUICK SORT (descending by total_biaya) ────────────────────
def quick_sort_biaya(arr):
    if len(arr) <= 1: return arr
    p = arr[len(arr) // 2].total_biaya
    return quick_sort_biaya([x for x in arr if x.total_biaya > p]) + \
           [x for x in arr if x.total_biaya == p] + \
           quick_sort_biaya([x for x in arr if x.total_biaya < p])

# ── UTILITAS TAMPILAN ─────────────────────────────────────────
def header(j): print(f"\n{SEPARATOR}\n  {j}\n{SEPARATOR}")
def err(m): print(f"  [!] {m}")
def ok(m):  print(f"  [+] {m}")

def cetak_node_resi(node, nomor=None):
    p = f"  {nomor}. " if nomor else "  "
    print(f"{p}No. Resi      : {node.no_resi}\n"
          f"     Pengirim    : {node.nama_pengirim}\n"
          f"     Kota Asal   : {node.kota_asal}\n"
          f"     Kota Tujuan : {node.kota_tujuan}\n"
          f"     Berat       : {node.berat} Kg\n"
          f"     Total Biaya : Rp {node.total_biaya:,}\n  {SEP_THIN}")

def cetak_kurir(k, nomor=None):
    p = f"  {nomor}. " if nomor else "  "
    print(f"{p}ID Kurir     : {k['id']}\n"
          f"     Nama Kurir  : {k['nama']}\n"
          f"     Kendaraan   : {k['kendaraan']}\n  {SEP_THIN}")

def tampil_semua_hub():
    if not graph: err("Belum ada kota hub yang terdaftar."); return
    print("  Daftar Kota Hub:")
    for i, kota in enumerate(graph, 1):
        t = ", ".join(f"{x}({j}KM)" for x, j in graph[kota].items()) or "-"
        print(f"  {i}. {kota}  |  Terhubung ke: {t}")

def get_nodes():
    nodes = bst_inorder(bst_root)
    if not nodes: err("Belum ada data resi terdaftar.")
    return nodes

def sudah_assign(nr): return any(nr in manifest[k] for k in manifest)

# ── MENU 1 ────────────────────────────────────────────────────
def menu_1_1_input_hub():
    header("MENU 1.1 - Input Hub Kota Baru"); tampil_semua_hub()
    nama = input("\n  Masukkan nama kota baru: ").strip()
    if not nama: err("Nama kota tidak boleh kosong."); return
    tambah_hub(nama)

def menu_1_2_input_rute():
    header("MENU 1.2 - Input Rute Antar-Kota")
    if len(graph) < 2: err("Dibutuhkan minimal 2 kota hub. Silakan tambah kota terlebih dahulu."); return
    tampil_semua_hub()
    a = input("\n  Kota Asal  : ").strip(); b = input("  Kota Tujuan: ").strip()
    try:
        j = float(input("  Jarak (KM) : ").strip())
        if j <= 0: err("Jarak harus lebih dari 0 KM."); return
    except ValueError: err("Jarak harus berupa angka."); return
    tambah_rute(a, b, j)

def menu_kelola_jaringan():
    while True:
        header("MENU 1 - KELOLA JARINGAN HUB DAN RUTE LOGISTIK")
        print("  1.1) Input Hub Kota Baru\n  1.2) Input Rute Antar-Kota\n  0)   Kembali ke Menu Utama")
        p = input("\n  Pilih menu: ").strip()
        if p in ("1.1","1"): menu_1_1_input_hub()
        elif p in ("1.2","2"): menu_1_2_input_rute()
        elif p == "0": break
        else: err("Pilihan tidak valid.")

# ── MENU 2 ────────────────────────────────────────────────────
def menu_2_1_input_resi():
    global bst_root
    header("MENU 2.1 - Input Resi Pengiriman Baru")
    while True:
        print()
        s = input("  No. Resi (4 digit, diawali '1'): ").strip()
        if not (len(s)==4 and s.isdigit() and s[0]=='1'): err("No. Resi harus 4 digit angka dan diawali angka '1'."); continue
        nr = int(s)
        if bst_cari(bst_root, nr): err(f"No. Resi '{nr}' sudah terdaftar."); continue
        nama = input("  Nama Pengirim: ").strip()
        if not nama: err("Nama pengirim tidak boleh kosong."); continue
        if not graph: err("Belum ada kota hub terdaftar. Tambah kota dulu di Menu 1."); return
        print("\n  Kota yang tersedia:", ", ".join(graph))
        ka = input("  Kota Asal   : ").strip()
        if ka not in graph: err(f"Kota '{ka}' tidak terdaftar di jaringan."); continue
        kt = input("  Kota Tujuan : ").strip()
        if kt not in graph: err(f"Kota '{kt}' tidak terdaftar di jaringan."); continue
        if ka == kt: err("Kota asal dan tujuan tidak boleh sama."); continue
        if not cek_rute_tersedia(ka, kt): err("Rute pengiriman belum tersedia dalam jaringan!"); continue
        try:
            brt = float(input("  Berat Paket (Kg): ").strip())
            if brt <= 0: err("Berat harus lebih dari 0 Kg."); continue
        except ValueError: err("Berat harus berupa angka."); continue
        j = get_jarak(ka, kt); biaya = int(j*2000 + brt*5000)
        print(f"\n  --- Kalkulasi Biaya ---\n  Jarak Rute  : {j} KM")
        print(f"  Rumus       : ({j} x Rp2.000) + ({brt} x Rp5.000)")
        print(f"  Total Biaya : Rp {biaya:,}\n  -----------------------")
        bst_root = bst_insert(bst_root, BSTNode(nr, nama, ka, kt, brt, biaya))
        ok("Input Resi Berhasil!")
        if input("  Apakah ingin melakukan input resi lagi (Y/N)? ").strip().upper() != 'Y': break

def menu_2_2_lihat_resi():
    header("MENU 2.2 - Lihat Seluruh Data Resi Terdaftar")
    nodes = get_nodes()
    if not nodes: return
    print(f"  Total Resi: {len(nodes)}\n  {SEP_THIN}")
    for i, n in enumerate(nodes, 1): cetak_node_resi(n, i)

def menu_2_3_urutkan_biaya():
    header("MENU 2.3 - Urutkan Transaksi Resi Berdasarkan Biaya Terbesar")
    nodes = get_nodes()
    if not nodes: return
    arr = quick_sort_biaya(list(nodes))
    print(f"  Algoritma  : Quick Sort (Descending by Total Biaya)\n  Total Resi : {len(arr)}\n  {SEP_THIN}")
    for i, n in enumerate(arr, 1): cetak_node_resi(n, i)

def menu_kelola_resi():
    while True:
        header("MENU 2 - KELOLA ADMINISTRASI RESI PENGIRIMAN")
        print("  2.1) Input Resi Pengiriman Baru\n  2.2) Lihat Seluruh Data Resi Terdaftar")
        print("  2.3) Urutkan Transaksi Resi Berdasarkan Biaya Terbesar\n  0)   Kembali ke Menu Utama")
        p = input("\n  Pilih menu: ").strip()
        if p in ("2.1","1"): menu_2_1_input_resi()
        elif p in ("2.2","2"): menu_2_2_lihat_resi()
        elif p in ("2.3","3"): menu_2_3_urutkan_biaya()
        elif p == "0": break
        else: err("Pilihan tidak valid.")

# ── MENU 3 (EC) ───────────────────────────────────────────────
def menu_3_1_input_kurir():
    header("MENU 3.1 - Input Data Kurir")
    KDR = ["Motor", "Mobil", "Truck"]
    while True:
        print()
        id_k = input("  ID Kurir   : ").strip()
        if not id_k: err("ID Kurir tidak boleh kosong."); continue
        if any(k['id'] == id_k for k in kurir_list): err(f"ID Kurir '{id_k}' sudah terdaftar."); continue
        nama = input("  Nama Kurir : ").strip()
        if not nama: err("Nama kurir tidak boleh kosong."); continue
        print("  Jenis Kendaraan: 1) Motor  2) Mobil  3) Truck")
        pk = input("  Pilih (1/2/3): ").strip()
        if pk not in ("1","2","3"): err("Pilihan kendaraan tidak valid."); continue
        kurir_list.append({'id': id_k, 'nama': nama, 'kendaraan': KDR[int(pk)-1]})
        ok("Data Kurir Berhasil Diinputkan!")
        if input("  Apakah ingin menambahkan data Kurir lagi (Y/N)? ").strip().upper() != 'Y': break

def menu_3_2_plotting_manifest():
    header("MENU 3.2 - Plotting Penugasan Manifest")
    if not kurir_list: err("Belum ada data kurir. Tambah kurir dulu di Menu 3.1."); return
    nodes = bst_inorder(bst_root)
    if not nodes: err("Belum ada data resi. Tambah resi dulu di Menu 2.1."); return
    print("\n  === Daftar Kurir ===")
    for i, k in enumerate(kurir_list, 1): cetak_kurir(k, i)
    id_k = input("  Masukkan ID Kurir yang akan ditugaskan: ").strip()
    kd = next((k for k in kurir_list if k['id'] == id_k), None)
    if not kd: err(f"ID Kurir '{id_k}' tidak ditemukan."); return
    if id_k not in manifest: manifest[id_k] = []
    print(f"\n  Kurir terpilih: {kd['nama']} ({kd['kendaraan']})")
    print("\n  === Daftar Seluruh Resi dalam Sistem ===")
    for i, n in enumerate(nodes, 1):
        st = "[SUDAH DIASSIGN]" if sudah_assign(n.no_resi) else "[TERSEDIA]"
        print(f"  {i}. {n.no_resi} - {n.nama_pengirim} ({n.kota_asal} -> {n.kota_tujuan}) | Rp {n.total_biaya:,} {st}")
    print()
    while True:
        s = input("  Masukkan No. Resi untuk ditugaskan (atau '0' untuk selesai): ").strip()
        if s == '0': break
        if not s.isdigit(): err("Input tidak valid."); continue
        nr = int(s)
        if not bst_cari(bst_root, nr): err(f"No. Resi '{nr}' tidak terdaftar."); continue
        if sudah_assign(nr): err(f"No. Resi '{nr}' sudah diassign ke kurir lain."); continue
        manifest[id_k].append(nr); ok(f"No. Resi {nr} berhasil ditambahkan ke manifest kurir {kd['nama']}.")
    print(f"\n  [+] Plotting selesai. Total resi untuk kurir {kd['nama']}: {len(manifest[id_k])} paket.")

def menu_3_3_tampil_manifest():
    header("MENU 3.3 - Tampil Manifest & Aturan Bonus Insentif")
    if not kurir_list: err("Belum ada data kurir."); return
    def lencana(n):
        if n == 0: return "Kurir Santai", 0
        elif n <= 3: return "Kurir Reguler", 25000
        elif n <= 6: return "Kurir Produktif", 60000
        else: return "Kurir Elite", 120000
    for k in kurir_list:
        rids = manifest.get(k['id'], [])
        lnc, kom = lencana(len(rids))
        print(f"\n  {'='*50}\n  ID Kurir    : {k['id']}\n  Nama Kurir  : {k['nama']}")
        print(f"  Kendaraan   : {k['kendaraan']}\n  Lencana     : {lnc}")
        print(f"  Bonus Komisi: Rp {kom:,}\n  Jml Paket   : {len(rids)} paket\n  {'-'*50}")
        if rids:
            print("  Detail Resi yang Dibawa:")
            for j, nr in enumerate(rids, 1):
                n = bst_cari(bst_root, nr)
                if n: print(f"    {j}. Resi #{n.no_resi} | {n.nama_pengirim} | "
                            f"{n.kota_asal} -> {n.kota_tujuan} | {n.berat}Kg | Rp {n.total_biaya:,}")
        else: print("  [Tidak ada resi yang diassign]")

def menu_kelola_kurir():
    while True:
        header("MENU 3 - KELOLA KURIR DAN MANIFEST PENGANTARAN")
        print("  3.1) Input Data Kurir\n  3.2) Plotting Penugasan Manifest")
        print("  3.3) Tampil Manifest & Aturan Bonus Insentif\n  0)   Kembali ke Menu Utama")
        p = input("\n  Pilih menu: ").strip()
        if p in ("3.1","1"): menu_3_1_input_kurir()
        elif p in ("3.2","2"): menu_3_2_plotting_manifest()
        elif p in ("3.3","3"): menu_3_3_tampil_manifest()
        elif p == "0": break
        else: err("Pilihan tidak valid.")

# ── INISIALISASI & MAIN ───────────────────────────────────────
def inisialisasi_data_default():
    """
    Memuat data kota hub dan rute default ke dalam sistem.
    Kota hub pertama (Faikah) mengandung 3 huruf pertama nama depan mahasiswa: 'FAI' (Fairuz).
    """
    for k in ["Faikah","Yogyakarta","Jakarta","Bandung","Surabaya","Semarang"]: tambah_hub(k)
    for a,b,j in [("Faikah","Yogyakarta",120),("Yogyakarta","Jakarta",560),
                  ("Jakarta","Bandung",150),("Jakarta","Surabaya",780),
                  ("Bandung","Semarang",300),("Semarang","Surabaya",320),
                  ("Yogyakarta","Semarang",120),("Faikah","Semarang",130)]: tambah_rute(a,b,j)

def main():
    print(f"\n{'='*60}\n   SILOG - SISTEM INFORMASI LOGISTIK")
    print("   Tugas Final Struktur Data - Sem. Genap 2025/2026")
    print(f"   Nama : Fairuz Ramadhani\n   NPM  : 5250411241\n{'='*60}")
    print("\n  [*] Memuat data default sistem...")
    inisialisasi_data_default()
    print("  [*] Data default berhasil dimuat.\n")
    while True:
        print(f"\n{SEPARATOR}\n   MENU UTAMA - SILOG\n{SEPARATOR}")
        print("  1) Kelola Jaringan Hub dan Rute Logistik")
        print("  2) Kelola Administrasi Resi Pengiriman")
        print(f"  3) Kelola Kurir dan Manifest Pengantaran  [EC]\n  0) Exit Program\n{SEPARATOR}")
        p = input("  Pilih menu: ").strip()
        if p == "1": menu_kelola_jaringan()
        elif p == "2": menu_kelola_resi()
        elif p == "3": menu_kelola_kurir()
        elif p == "0": print("\n  [*] Terima kasih telah menggunakan SILOG. Program berhenti."); print(SEPARATOR); break
        else: err("Pilihan tidak valid. Masukkan 0, 1, 2, atau 3.")

if __name__ == "__main__":
    main()