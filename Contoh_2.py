nama_siswa = []
nilai_siswa = []
pilihan = 0

print("=== APLIKASI DATA & NILAI SISWA ===")

while pilihan != 5:
    print("\nMENU")
    print("1. Tambah Data Siswa & Nilai")
    print("2. Tampilkan Data")
    print("3. Hitung Rata-rata Nilai")
    print("4. Hitung Jumlah Siswa")
    print("5. Keluar")

    pilihan = int(input("Pilih menu (1-5): "))

    if pilihan == 1:
        jumlah = int(input("Masukkan jumlah siswa: "))
        for i in range(jumlah):
            nama = input(f"Masukkan nama siswa ke-{i+1}: ")
            nilai = int(input(f"Masukkan nilai siswa ke-{i+1}: "))
            nama_siswa.append(nama)
            nilai_siswa.append(nilai)

    elif pilihan == 2:
        # TODO: tampilkan nama dan nilai siswa
        pass

    elif pilihan == 3:
        # TODO: hitung dan tampilkan rata-rata nilai
        pass

    elif pilihan == 4:
        # TODO: tampilkan jumlah siswa
        pass

    elif pilihan == 5:
        print("Program selesai")

    else:
        print("Menu tidak tersedia")


#DESCRIPTION OUTPUT :
# 1. Andi - Nilai: 80
# 2. Budi - Nilai: 90

# Rata-rata Nilai: 85
# Jumlah Siswa: 2
