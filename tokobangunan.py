#2309116002_NYOMAN ARINI TRIRAHAYU
#posttest tema Toko Bangunan

# import untuk membersihkan terminal
import os 
os.system('cls')

from prettytable import PrettyTable

# masukkan data admin
admin={"username" : ["arini", "sehun",],
     "password" : ["123", "456",],
    }

# Inisialisasi data toko bangunan
toko_bangunan = [
    {"Kode Barang": "001", "Nama Barang": "Semen", "Stok": 50, "Harga": 68000},
    {"Kode Barang": "002", "Nama Barang": "Paku", "Stok": 2000, "Harga": 1000},
    {"Kode Barang": "003", "Nama Barang": "Besi Beton", "Stok": 20, "Harga": 12000},
    {"Kode Barang": "004", "Nama Barang": "Genteng", "Stok": 100, "Harga": 20000},
    {"Kode Barang": "005", "Nama Barang": "Pipa PVC", "Stok": 50, "Harga": 20000},
]

# Fungsi untuk menampilkan data toko bangunan
def tampilkan_toko():
    table = PrettyTable()
    table.field_names = ["Kode Barang", "Nama Barang", "Stok", "Harga"]
    for item in toko_bangunan:
        table.add_row([item["Kode Barang"], item["Nama Barang"], item["Stok"], item["Harga"]])
    print(table)

# Fungsi untuk menambahkan barang ke data toko
def tambahkan_barang():
    kode_barang = input("Masukkan Kode Barang: ")
    nama_barang = input("Masukkan Nama Barang: ")
    stok = int(input("Masukkan Stok: "))
    harga = int(input("Masukkan Harga: "))
    toko_bangunan.append({"Kode Barang": kode_barang, "Nama Barang": nama_barang, "Stok": stok, "Harga": harga})
    print("Barang berhasil ditambahkan!")

# Fungsi untuk mengupdate data barang di toko
def update_barang(kode_barang):
    for item in toko_bangunan:
        if item["Kode Barang"] == kode_barang:
            item["Nama Barang"] = input("Masukkan Nama Barang Baru: ")
            item["Stok"] = int(input("Masukkan Stok Baru: "))
            item["Harga"] = int(input("Masukkan Harga Baru: "))
            print("Barang berhasil diupdate!")
            return
    print("Barang tidak ditemukan.")

# Fungsi untuk menghapus barang atau data dari toko
def hapus_barang(kode_barang):
    for item in toko_bangunan:
        if item["Kode Barang"] == kode_barang:
            toko_bangunan.remove(item)
            print("Barang berhasil dihapus!")
            return
    print("Barang tidak ditemukan.")

# Fungsi untuk melakukan transaksi pembelian
def transaksi_pembelian():
    tampilkan_toko()
    kode_barang = input("Masukkan Kode Barang yang akan dibeli: ") # pembeli memasukkan kode barang yang akan dibeli
    for item in toko_bangunan:
        if item["Kode Barang"] == kode_barang:
            jumlah_beli = int(input("Masukkan Jumlah yang akan dibeli: ")) # pembeli memasukkan jumlah barang yang akan di beli
            if jumlah_beli <= item["Stok"]:
                total_harga = jumlah_beli * item["Harga"]
                print(f"Total Harga: Rp {total_harga}")
                item["Stok"] -= jumlah_beli
                print("Transaksi berhasil!")
            else:
                print("Stok tidak mencukupi.")
            return
    print("Barang tidak ditemukan.")

# Fungsi utama program
def main():
    while True:
        # user menentukan pilihan role
        print("==========|Selamat datang di Toko Bangunan|==========")
        print("1. Admin")
        print("2. Pembeli")
        print("3. Keluar")
        pilihan = input("Pilih Role Anda (1/2/3): ")
        if pilihan == "1":
            #jika memilih role admin masukkan username dan password
            username = input ("masukkan username: ")
            password = input ("masukkan password: ")
            cariin = admin.get("username").index(username)
            if username == admin.get("username")[cariin] and password == admin.get("password")[cariin] :
                print("Login Berhasil") #jika admin memasukkan username dan password yang benar maka login berhasil
                #tampilan menu admin
                print("                      ! PERHATIAN !           ")
                print("       akses hanya untuk karyawan 'TOKO BANGUNAN'             ")
                print("==========|Menu Admin::==========")
                print(f'''
=======================================
|       NO.|       MENU                |
=======================================
|       1.| Tampilkan Data Toko        |
|       2.| Tambahkan Barang           |
|       3.| Update Barang              |
|       4.| Hapus Barang               |
|       5.| Kembali ke Menu Utama      |
=======================================''')
                admin_pilihan = input("Pilih Menu Admin (1/2/3/4/5): ")
                if admin_pilihan == "1": 
                    tampilkan_toko() #jika admin memilih 1 maka akan menampilkan data toko
                elif admin_pilihan == "2":
                    tambahkan_barang() #jika admin memilih 2 maka admin diminta menambahkan data toko
                elif admin_pilihan == "3":
                    kode_barang = input("Masukkan Kode Barang yang akan diupdate: ")
                    update_barang(kode_barang) #jika admin memilih 3 maka admin diminta memasukkan kode barang yang akan diupdate
                elif admin_pilihan == "4":
                    kode_barang = input("Masukkan Kode Barang yang akan dihapus: ")
                    hapus_barang(kode_barang) #jika admin memilih 4 maka admin diminta memasukkan kode barang yang akan dihapus
                elif admin_pilihan == "5":
                    print(f'''
==================================
SELAMAT BEKERJA DAN TETAP SEMANGAT
==================================''')
                else:
                    print("Pilihan tidak valid.") #Jika admin tidak memilih maka 'hasil' tidak muncul atau tidak valid
            else:
                print("Login gagal, Password anda salah") 
                print("Periksa kembali Password anda, Terimakasih :") #Jika admin salah memasukan username dan password maka login gagal
        #pilihan role pembeli
        elif pilihan == "2":
            print("Menu Pembeli:")
            transaksi_pembelian()

        elif pilihan == "3":
            print("Terima kasih telah menggunakan program ini.") #Jika admin 3 memilih maka program selesai atau berhenti
            break

        else:
            print("Pilihan tidak valid.") #Jika admin tidak memilih maka 'hasil' tidak muncul atau pilihan tidak valid

if __name__ == "__main__":
    main()