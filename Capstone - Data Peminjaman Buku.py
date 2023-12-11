from tabulate import tabulate
from datetime import datetime, date, timedelta
import math as ma
import random as rd

# DATA MENU
def list_menu_admin (): #def menu awal
    print("Peminjaman Buku Icha's Library \n")
    print("List Menu:"
          "\n 1.Menampilkan Daftar Buku"
          "\n 2.Menambah Daftar Buku"
          "\n 3.Menghapus Daftar Buku"
          "\n 4.Data Peminjaman Buku"
          "\n 5.Data Pengembalian Buku"
          "\n 6.Exit Program")
    
def list_menu_umum (): #def menu awal
    print("Peminjaman Buku Icha's Library \n")
    print("List Menu:"
          "\n 1.Menampilkan Daftar Buku"
          "\n 2.Data Peminjaman Buku"
          "\n 3.Data Pengembalian Buku"
          "\n 4.Exit Program")

# DATA KODE GENRE
kode_genre = [
            {'Kode Genre':100,'Genre Buku': 'Filsafat & Psikologi'},
            {'Kode Genre':200,'Genre Buku':'Agama'},
            {'Kode Genre':300,'Genre Buku':'Ilmu Sosial'},
            {'Kode Genre':400,'Genre Buku':'Bahasa'},
            {'Kode Genre':500,'Genre Buku':'Sains & Matematika'},
            {'Kode Genre':600,'Genre Buku':'Teknologi'},
            {'Kode Genre':700,'Genre Buku':'Kesenian & Hiburan'},
            {'Kode Genre':800,'Genre Buku':'Literatur & Sastra'},
            {'Kode Genre':900,'Genre Buku':'Sejarah & Geografi'},
            {'Kode Genre':1 ,'Genre Buku':'Keseluruhan Daftar Buku'}]
def genre_buku(): #BISA DI IF ELSE
    print(tabulate(kode_genre, headers='keys', tablefmt="grid"))
    
# DATA LIST BUKU
list_buku= [
            {'Kode Buku': 10010, 'Genre Buku' : 100,'Judul Buku' :'Studi Dasar Filsafat','Penulis' :'Tazkiyah Basad','Penerbit' :'Deepublish','Jumlah Eksemplar' : 197},
           
            {'Kode Buku': 10034,'Genre Buku' : 100,'Judul Buku' :'Filsafat Pendidikan Operasional','Penulis' :'Aswasulasikin','Penerbit' :'Alfabeta','Jumlah Eksemplar' : 151},
            
            {'Kode Buku': 20053,'Genre Buku' : 200,'Judul Buku' :'Sejarah Peradaban Islam','Penulis' :'H. Syamruddin Nasution','Penerbit' :'Raja Grafindo','Jumlah Eksemplar' : 314},
     
            {'Kode Buku': 20036,'Genre Buku' : 200,'Judul Buku' :'Ibrahim Bapak Semua Agama','Penulis' :'Iqbal Harahap','Penerbit' :'Lentera Hati','Jumlah Eksemplar' : 271},
           
            {'Kode Buku': 30024,'Genre Buku' : 300,'Judul Buku' :'Ilmu Sosial Budaya Dasar','Penulis' :'Abdulkadir Muhammad','Penerbit' :'Citra Aditya Bakti','Jumlah Eksemplar':388},
            
            {'Kode Buku': 30045,'Genre Buku' : 300,'Judul Buku' :'Ilmu Sosial dan Budaya Dasar dalam Keislaman','Penulis' :'Mohammad Kamaludin','Penerbit' :'UMM Press','Jumlah Eksemplar' : 188},

            {'Kode Buku': 40034,'Genre Buku' : 400,'Judul Buku' :'Trik Cepat Kuasai Bhasa Korea','Penulis' :'Melia Lee','Penerbit' :'Thema Publishing','Jumlah Eksemplar' : 168},
           
            {'Kode Buku': 40056,'Genre Buku' : 400,'Judul Buku' :'Super Easy Cara Mudah Belajar Bahasa Jerman','Penulis' :'Dian Dwi Anisa','Penerbit' :'Solusi Distribusi','Jumlah Eksemplar' :284},
     
            {'Kode Buku': 50098,'Genre Buku' : 500,'Judul Buku' :'Matematika Diskrit Dan Aplikasinya','Penulis' :'Adiwijaya','Penerbit' :'Alfabeta','Jumlah Eksemplar' : 200},
           
            {'Kode Buku': 50065,'Genre Buku' : 500,'Judul Buku' :'Analisis Data Kuantitatif dengan Statistika Deskriptif','Penulis' :'Nar Herrhyanto','Penerbit' :'Yrama Widya','Jumlah Eksemplar' : 194},
           
            {'Kode Buku': 60046,'Genre Buku' : 600,'Judul Buku' :'Manajemen Audit Teknologi','Penulis' :'Yanto Sugiharto','Penerbit' :'Kanisius','Jumlah Eksemplar' : 98},
           
            {'Kode Buku': 60097,'Genre Buku' : 600,'Judul Buku' :'Konsep Teknologi Seluler','Penulis' :'Gunawan Wibisono','Penerbit' :'Informatika','Jumlah Eksemplar' : 102},
           
            {'Kode Buku': 70076,'Genre Buku' : 700,'Judul Buku' :'Pintar Bermain Harmonika','Penulis' :'Danar Bayuardi','Penerbit' :'Flashbooks','Jumlah Eksemplar' : 92},

            {'Kode Buku': 70058,'Genre Buku' : 700,'Judul Buku' :'Blackpink Daebak','Penulis' :'Summer Chu','Penerbit' :'Histeria','Jumlah Eksemplar' : 208},
           
            {'Kode Buku': 80047,'Genre Buku' : 800,'Judul Buku' :'A History of Classical Malay Literature','Penulis' :'Liaw Yock Fang','Penerbit' :'Yayasan Pustaka Obor','Jumlah Eksemplar' : 516},
        
            {'Kode Buku': 80067,'Genre Buku' : 800,'Judul Buku' :'Literature Through the Eyes of Faith','Penulis' :'Susan V. Gallagher','Penerbit' :'Harper Collins','Jumlah Eksemplar' : 67},
        
            {'Kode Buku': 90073,'Genre Buku' : 900,'Judul Buku' :'Sejarah dan Peradaban Mesir Kuno','Penulis' :'Jonar T.h Situmorang','Penerbit' :'Andi Offset','Jumlah Eksemplar' : 214},
         
            {'Kode Buku': 90087,'Genre Buku' : 900,'Judul Buku' :'Sejarah Ringkas Terbaik Dunia Kuno Empat Benua','Penulis' :'Anisa Septianingrum','Penerbit' :'Anak Hebat Indonesia','Jumlah Eksemplar' : 188}
            ]
def daftar_buku():
    print(tabulate(list_buku, headers='keys', tablefmt='grid'))
    
# DATA INPUT GENRE   
def input_genre():
    while True:
        genre_buku()
        input_genre = int(input('Masukkan Kode Genre Buku: '))
        if input_genre == 1:
            print('Keseluruhan Data Buku')
            daftar_buku()
        else: #INI HRSNYA ELIF TP SYARATNYA APA?
            list_genre_buku = []
            for i in range(len(list_buku)):
                if list_buku[i]['Genre Buku'] == input_genre:
                    list_genre_buku.append(list_buku[i])
            print(tabulate(list_genre_buku, headers = 'keys', tablefmt='grid'))      
        stop = (input('Ingin Balik ke Menu?(ya/tidak)')).lower()
        if stop == 'ya':
            break
        
# MENAMBAH DAFTAR BUKU
def menambah_buku():
    kode_genre.pop()
    print(tabulate(kode_genre, headers='keys', tablefmt='grid'))
    list_buku_baru= []
    while True: 
        data= {}
        print('Masukkan Data Buku Baru!')
        input_kode_genre = input('Masukkan Kode Genre: ')
        data['Kode Buku'] = input_kode_genre + str(rd.randint(10,99))
        data['Genre Buku'] = input_kode_genre
        data['Judul Buku'] = input('Masukkan Judul Buku: ')
        data['Penulis'] = input('Masukkan Penulis Buku: ')
        data['Penerbit'] = input('Masukkan Penerbit Buku: ')
        data['Jumlah Eksemplar'] = int(input(f'Masukkan Jumlah Eksemplar: '))

        list_buku_baru.append(data)
        print(tabulate(list_buku_baru, headers = 'keys', tablefmt='grid'))
        stop = input('Ingin menambahkan Buku Lagi?(ya/tidak): ')
        if stop == 'tidak':
            list_buku.extend(list_buku_baru)
            print(tabulate(list_buku,headers='keys',tablefmt='grid'))
            print('Buku Berhasil Ditambahkan!')
            break
        continue

# DATA HAPUS BUKU        
def hapus_buku ():
    while True:
        kode_buku = int(input('Masukkan kode buku yang ingin dihapus: '))
        for buku in list_buku:
            if buku ['Kode Buku'] == kode_buku:
                list_buku.remove(buku)
        print(tabulate(list_buku, headers='keys', tablefmt='grid'))
        print(f'Buku dengan kode {kode_buku} berhasil dihapus!')
        stop = (input('Ingin Balik ke Menu?(ya/tidak)')).lower()
        if stop == 'ya':
            break 
        
# DATA PEMINJAMAN BUKU         
def data_pinjam(): #BISA MENGGUNAKAN FOR i UNTUK BUKU KE 1 DAN KE 2
    buku_1= None
    buku_2 = None
    while True:
        daftar_buku()
        input_pinjam = int(input('Masukkan Kode Buku 1: '))
        list_pinjam_buku_1 = []
        index_buku_1 = None
        for i in range(len(list_buku)):
            if list_buku[i]['Kode Buku'] == input_pinjam:
                list_pinjam_buku_1.append(list_buku[i])
                index_buku_1 = i
        buku_1 = tabulate(list_pinjam_buku_1, headers='keys', tablefmt='grid')
        print(buku_1)
        del list_buku[index_buku_1]
        stop = (input('Ingin menambah buku untuk dipinjam? (ya/tidak) ')).lower()
        if stop == 'ya':
            while True:
                daftar_buku()
                input_pinjam = int(input('Masukkan Kode Buku 2: '))
                list_pinjam_buku_2 = []
                index_buku_2 = None
                for i in range(len(list_buku)):
                    if list_buku[i]['Kode Buku'] == input_pinjam:
                        list_pinjam_buku_2.append(list_buku[i])
                        index_buku_2 = i
                buku_2 = tabulate(list_pinjam_buku_2, headers='keys', tablefmt='grid')
                print(tabulate([list_pinjam_buku_1[0], list_pinjam_buku_2[0]], headers='keys', tablefmt='grid'))
                del list_buku[index_buku_2]
                print('Berhasil! \n Peminjaman buku maksimal hanya 2 buku')
                hari_ini = date.today()
                tujuh_hari_ke_depan = timedelta(days=7)
                hasil = hari_ini + tujuh_hari_ke_depan
                hasil_1 = hasil.strftime("%d-%m-%Y")
                print(f"Batas pengembalian buku: \n {hasil_1}" "\n Harap dikembalikan tepat waktu," "\n sesuai tanggal batas buku pengembalian")
                break
            break    
        elif stop == 'tidak':
            print('Peminjaman buku berhasil')
            hari_ini = date.today()
            tujuh_hari_ke_depan = timedelta(days=7)
            hasil = hari_ini + tujuh_hari_ke_depan
            hasil_2 = hasil.strftime("%d-%m-%Y")
            print(f"Batas buku pengembalian buku: \n {hasil_2}" "\n Harap dikembalikan tepat waktu," "\n sesuai tanggal batas buku pengembalian")
            break   
        else:
            print('Masukkan jawaban ya/tidak')
    return buku_1,buku_2
        
#DATA PENGEMBALIAN BUKU
import datetime
def data_pengembalian():
    buku_pengembalian = []
    while True:
        pengembalian = {}
        print('Masukkan data buku pengembalian')
        pengembalian['Kode Buku'] = input('Masukkan kode buku: ')
        pengembalian['Kode Genre'] = input('Masukkan kode genre buku: ')
        pengembalian['Judul Buku'] = input('Masukkan judul buku: ')
        pengembalian['Penulis'] = input('Masukkan penulis buku: ')
        pengembalian['Penerbit'] = input('Masukkan penerbit buku: ')
        pengembalian['Jumlah Eksemplar'] = int(input('Masukkan jumlah eksemplar: '))
        buku_pengembalian.append(pengembalian)
        print(tabulate(buku_pengembalian,headers='keys',tablefmt='grid'))
        due_date = input('Masukkan tanggal batas pengembalian buku (DD-MM-YYYY): ')
        due_date = datetime.datetime.strptime(due_date, "%d-%m-%Y").date()
        today = date.today()
        try:
            remaining_days = (due_date - today).days
            total_denda = int (abs(remaining_days) * 2000)
            if remaining_days >=0:
                print('Buku berhasil dikembalikan!''\nTerimakasih:)')
            else:
                print(f"Telat mengembalikan buku selama {abs(remaining_days)} hari")
                print(f"Dikenakan denda sebesar Rp.{abs(total_denda)}")
                while True:
                    uang = int(input('Masukkan nominal uang untuk membayar denda Rp. '))
                    if total_denda > uang:
                        print(f'Jumlah uang kurang sebesar: {abs(total_denda-uang)}')
                    else:
                        break
                kembalian = abs(uang - total_denda)
                print("Terimakasih telah melakukan pembayaran denda")
                print(f"Uang kembalian anda Rp.{kembalian}")
            return date
        except ValueError:
            print('Format tanggal salah. Silakan coba lagi.')
    
#KESELURUHAN CODING#
username = (input("Masukkan Nama: ")).upper()
while True:
    role = str(input("Masukkan peran (admin/umum) : ")).lower()
    if role == "admin":
        try:
            password = input("Masukkan password : ")
            if password == "12345":
                print("Selamat datang, ", username)
                print("Anda dapat mengakses semua fitur aplikasi")
                while True:
                    list_menu_admin ()
                    angka_menu= int(input('Masukkan Nomor List yang Ingin Diakses: '))
                    if angka_menu == 1:
                        print('Menampilkan Daftar Buku:\n')
                        input_genre()
                        
                    elif angka_menu == 2:
                        print('Menambah Daftar Buku:')
                        while True:
                            menambah_buku()
                            break
                    
                    elif angka_menu == 3:
                        print('Menghapus Daftar Buku:')
                        while True:
                            daftar_buku()
                            hapus_buku()
                            break 
                                            
                    elif angka_menu == 4:
                        print('Data Peminjaman Buku:')
                        while True:
                            data_pinjam()
                            break
                            
                    elif angka_menu == 5:
                        while True:
                            data_pengembalian()
                            break
                        
                    elif angka_menu == 6:
                        print('Terima Kasih, Selamat Berjumpa Kembali <3')
                        break
                    
                    else:
                        print('Masukkan angka menu 1-6')

            else:
                print("Password salah. Akses ditolak")
        except:
            break
        
    elif role == "umum":
        while True:
            print("Selamat datang, ", username)
            list_menu_umum ()
            while True:
                angka_menu= int(input('Masukkan Nomor List yang Ingin Diakses: '))
                if angka_menu == 1:
                    print('Menampilkan Daftar Buku:\n')
                    input_genre()
                
                elif angka_menu == 2:
                    print('Data Peminjaman Buku:')
                    while True:
                        data_pinjam()
                        break
                        
                elif angka_menu == 3:
                    while True:
                        data_pengembalian()
                        break
                    
                elif angka_menu == 4:
                    print('Terima Kasih, Selamat Berjumpa Kembali <3')
                    break
                
                else:
                    print('Masukkan angka menu 1-6')
                break
            break
        break
    else:
        print("Peran yang dimasukkan tidak valid")