# Project Array + Class Python
# Kelas X RPL 2

class Siswa:
    def __init__(self):
        self.nama_siswa = []
        self.nilai_siswa = []

    def tambah_siswa(self, nama, nilai):
        self.nama_siswa.append(nama)
        self.nilai_siswa.append(nilai)

    def tampilkan_siswa(self):
        print("\nDaftar Data Siswa:")
        for i in range(len(self.nama_siswa)):
            print(f"Siswa ke-{i+1}: {self.nama_siswa[i]} | Nilai: {self.nilai_siswa[i]}")

    def jumlah_siswa(self):
        print("\nJumlah siswa:", len(self.nama_siswa))

    def rata_rata_nilai(self):
        total = sum(self.nilai_siswa)
        rata_rata = total / len(self.nilai_siswa)
        print("Rata-rata nilai siswa:", rata_rata)



print("=== SISTEM DATA SISWA ===")

data = Siswa()

jumlah = int(input("Masukkan jumlah siswa: "))

for i in range(jumlah):
    nama = input(f"Masukkan nama siswa ke-{i+1}: ")
    nilai = int(input(f"Masukkan nilai siswa ke-{i+1}: "))
    data.tambah_siswa(nama, nilai)

data.tampilkan_siswa()
data.jumlah_siswa()
data.rata_rata_nilai()