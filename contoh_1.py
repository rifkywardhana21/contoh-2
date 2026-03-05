nama = input("Masukkan nama: ")
print("Halo", nama)


class Buku:
    def __init__(self, judul, penulis, tahun):
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun
        self.kiri = None
        self.kanan = None


#menambahkan buku

def tambah_buku(root, judul, penulis, tahun):

    if root is None:
        return Buku(judul, penulis, tahun)

    if judul.lower() < root.judul.lower():
        root.kiri = tambah_buku(root.kiri, judul, penulis, tahun)

    elif judul.lower() > root.judul.lower():
        root.kanan = tambah_buku(root.kanan, judul, penulis, tahun)

    return root


#pencarian data buku

def cari_buku(root, judul):

    if root is None:
        return None

    if root.judul.lower() == judul.lower():
        return root

    elif judul.lower() < root.judul.lower():
        return cari_buku(root.kiri, judul)

    else:
        return cari_buku(root.kanan, judul)


#menampilkan semua data buku

def tampilkan_buku(root):

    if root is not None:

        tampilkan_buku(root.kiri)

        print("---------------------------")
        print("Judul   :", root.judul)
        print("Penulis :", root.penulis)
        print("Tahun   :", root.tahun)

        tampilkan_buku(root.kanan)


#menu system perpus

def menu():

    root = None

    while True:

        print("\n===== SISTEM PERPUSTAKAAN =====")
        print("1. Tambah Buku")
        print("2. Cari Buku")
        print("3. Tampilkan Semua Buku")
        print("4. Keluar")

        pilihan = input("Pilih menu: ")

        
        if pilihan == "1":

            judul = input("Masukkan Judul Buku : ")
            penulis = input("Masukkan Penulis : ")
            tahun = input("Masukkan Tahun : ")

            root = tambah_buku(root, judul, penulis, tahun)

            print("Buku berhasil ditambahkan!")

        
        elif pilihan == "2":

            judul = input("Masukkan Judul Buku yang dicari: ")

            hasil = cari_buku(root, judul)

            if hasil:
                print("\nBuku ditemukan!")
                print("Judul   :", hasil.judul)
                print("Penulis :", hasil.penulis)
                print("Tahun   :", hasil.tahun)
            else:
                print("Buku tidak ditemukan")

       
        elif pilihan == "3":

            if root is None:
                print("Belum ada buku dalam perpustakaan")

            else:
                print("\nDaftar Buku Perpustakaan")
                tampilkan_buku(root)

  
        elif pilihan == "4":

            print("Program selesai")
            break

        else:
            print("Menu tidak tersedia")


# MENJALANKAN PROGRAM


menu()