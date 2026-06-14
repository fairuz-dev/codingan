# SOAL 1 - Hospital Queue (Circular Buffer) O(1)

class HospitalQueue:
    def __init__(self, max_capacity):
        self.kapasitas = max_capacity + 1
        self.buffer = [None] * self.kapasitas
        self.head = 0
        self.tail = 0

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.tail + 1) % self.kapasitas == self.head

    def enqueue(self, nama):
        # O(1) - langsung tulis di posisi tail
        if self.is_full():
            print("Antrean penuh!")
            return
        self.buffer[self.tail] = nama
        self.tail = (self.tail + 1) % self.kapasitas
        print(f"{nama} masuk antrean.")

    def dequeue(self):
        # O(1) - langsung ambil dari head, tanpa geser elemen lain
        if self.is_empty():
            print("Antrean kosong.")
            return None
        pasien = self.buffer[self.head]
        self.head = (self.head + 1) % self.kapasitas
        print(f"{pasien} dipanggil.")
        return pasien


# --- Simulasi Soal 1 ---
antrian = HospitalQueue(3)
antrian.enqueue("Budi")
antrian.enqueue("Siti")
antrian.enqueue("Andi")
antrian.enqueue("Rizky")  # penuh
antrian.dequeue()
antrian.enqueue("Rizky")  # berhasil

# SOAL 2 - Browser History (Doubly Linked List)

class Node:
    def __init__(self, url):
        self.url = url
        self.prev = None  # pointer ke halaman sebelumnya
        self.next = None  # pointer ke halaman sesudahnya


class BrowserHistory:
    def __init__(self, homepage):
        self.current = Node(homepage)

    def visit_page(self, url):
        # Saat visit_page dipanggil setelah go_back():
        # - current.next diarahkan ke node baru (forward history lama terputus)
        # - node baru.prev diarahkan ke current
        # - node lama di depan otomatis dihapus oleh Garbage Collector
        baru = Node(url)
        self.current.next = baru   # putus forward history lama
        baru.prev = self.current   # hubungkan balik ke halaman sekarang
        self.current = baru
        print(f"Kunjungi: {self.current.url}")

    def go_back(self):
        if self.current.prev:
            self.current = self.current.prev
            print(f"Back: {self.current.url}")
        else:
            print("Sudah di halaman awal.")
        return self.current.url

    def go_forward(self):
        if self.current.next:
            self.current = self.current.next
            print(f"Forward: {self.current.url}")
        else:
            print("Tidak ada halaman ke depan.")
        return self.current.url


# --- Simulasi Soal 2 ---
browser = BrowserHistory("Halaman A")
browser.visit_page("Halaman B")
browser.visit_page("Halaman C")
browser.go_back()           # kembali ke B
browser.visit_page("Halaman X")  # C terhapus permanen
browser.go_forward()        # tidak bisa, C sudah hilang
browser.go_back()           # kembali ke B
