# MINI PROJECT LOOP PYTHON
# Kelas X RPL

nama_siswa = []
pilihan = 0

print("=== APLIKASI DATA SISWA ===")

while pilihan != 4:
    print("\nMENU")
    print("1. Tambah Data Siswa")
    print("2. Tampilkan Data Siswa")
    print("3. Hitung Jumlah Siswa")
    print("4. Keluar")

    pilihan = int(input("Pilih menu (1-4): "))

    if pilihan == 1:
        jumlah = int(input("Masukkan jumlah siswa: "))
        for i in range(jumlah):
            nama = input(f"Masukkan nama siswa ke-{i+1}: ")
            nama_siswa.append(nama)
        print("Data siswa berhasil ditambahkan")

    elif pilihan == 2:
        print("\nDaftar Nama Siswa:")
        if len(nama_siswa) == 0:
            print("Belum ada data siswa")
        else:
            for i in range(len(nama_siswa)):
                print(f"{i+1}. {nama_siswa[i]}")

    elif pilihan == 3:
        print("Jumlah siswa:", len(nama_siswa))

    elif pilihan == 4:
        print("Terima kasih, program selesai")

    else:
        print("Menu tidak tersedia")