from tabulate import tabulate
import datetime

daftarmobil = [
    {'Kode': '1','Merk': 'Toyota', 'Type': 'Avanza', 'Transmisi': 'Manual', 'Tarif Per Hari': 200000, 'Status': 'Available'},
    {'Kode': '2','Merk': 'Honda', 'Type': 'Civic', 'Transmisi': 'Matic', 'Tarif Per Hari': 400000, 'Status': 'Available'},
    {'Kode': '3','Merk': 'Honda', 'Type': 'Brio', 'Transmisi': 'Matic', 'Tarif Per Hari': 250000, 'Status': 'Available'},
    {'Kode': '4','Merk': 'Suzuki', 'Type': 'Swift', 'Transmisi': 'Manual', 'Tarif Per Hari': 200000, 'Status': 'Available'},
    {'Kode': '5','Merk': 'Mitsubishi', 'Type': 'Pajero', 'Transmisi': 'Matic', 'Tarif Per Hari': 600000, 'Status': 'Available'},
    {'Kode': '6','Merk': 'Toyota', 'Type': 'Innova', 'Transmisi': 'Matic', 'Tarif Per Hari': 400000, 'Status': 'Available'},
]
print(tabulate(daftarmobil, headers='keys', tablefmt='psql'))

data_peminjaman = []

def database():
    print(tabulate(daftarmobil, headers='keys', tablefmt='psql'))
def datapeminjaman():
    print(tabulate(data_peminjaman, headers='keys', tablefmt='psql'))
#ADDMORE
def addmore():
  while True:
    kode = len(daftarmobil) + 1
    merk = input('Merk: ')
    model = input('Type: ')
    transmisi = input('Transmisi: ')
    try:
        tarif = int(input('Tarif Per Hari: '))
    except ValueError:
        print('Silahkan masukkan angka')
    daftarmobil.append({'Kode': kode,'Merk': merk, 'Type': model, 'Transmisi': transmisi, 'Tarif Per Hari': tarif})
    print('Data berhasil ditambahkan')
    database()

#DEL
def delete():
  database()
  print('''
    Pilih kode yang ingin dihapus
    ''')
  kode = int(input('Kode: '))
  daftarmobil.pop(kode-1)
  for i in range(len(daftarmobil)): #kode dalam list akan menyesuaikan degan data yang dihapus
    daftarmobil[i]['Kode'] = i+1
  print('Data berhasil dihapus')
  database()

def rent():
  global data_peminjaman
  while True:
    print('''
    Masukan Nama dan Nomor Handphone Anda
    ''')
    Nama = input('Nama: ')
    CP = (input('Nomor Handphone: '))
    if len(str(CP)) < 12:
      print('Silahkan masukkan nomor handphone dengan benar')
      continue
   
    database()
    print('''
    Masukkan kode mobil yang ingin disewa
    ''')
    sewa = int(input('Kode Mobil: '))
    for i in range(len(daftarmobil)):
        if sewa == daftarmobil[i]['Kode']:  #ini harusnya dia bakal ngambil mobil sesuai kode di list
            print('Kode Mobil: ',daftarmobil[i]['Kode'])
        tanggalsewa = input('Tanggal Sewa(dd/mm/yyyy):')
        tanggalsewa = datetime.datetime.strptime(tanggalsewa, '%d/%m/%Y').date()
        if tanggalsewa < datetime.date.today():
          print('Silahkan masukkan tanggal yang benar')
          continue
        tanggalkembali = input('Tanggal Kembali(dd/mm/yyyy):')
        tanggalkembali = datetime.datetime.strptime(tanggalkembali, '%d/%m/%Y').date()
        if tanggalkembali < tanggalsewa:
          print('Silahkan masukkan tanggal yang benar')
          continue
        duration = (tanggalkembali - tanggalsewa).days + 1
        if duration == 0: #lama sewa akan terhitung 1 hari jita tanggal sewa dan tanggal kembali sama
          duration = 1


        print('''
        Detail Peminjaman
        ''')
        print('Nama: ', Nama)
        print('Nomor Handphone: ', CP)
        print({daftarmobil[i]['Merk']}, {daftarmobil[i]['Type']}, {daftarmobil[i]['Transmisi']})
        print('Lama Sewa: ', duration, 'Hari')
        print('Total Pembayaran: ', int(daftarmobil[i]['Tarif Per Hari']) * int(duration))
        print('Thank You For Booking With Easy Rental')
        daftarmobil[i]['Status'] = 'Sedang Disewa'

        # Create a copy of the car data and remove unwanted keys
        car_data_copy = daftarmobil[i].copy()
        car_data_copy.pop('Status', None)  # Remove 'status' if it exists
        car_data_copy.pop('Tarif Per Hari', None)  # Remove 'Tarif Per Hari' if it exists


        rental_data = {
            'Nama': Nama,
            'Contact Person': CP,
            'Tanggal Sewa': tanggalsewa,
            'Tanggal Kembali': tanggalkembali,
            'Lama Sewa': duration,
            'Total Pembayaran': int(daftarmobil[i]['Tarif Per Hari']) * int(duration),
            **car_data_copy  # Include the modified car data
        }
        data_peminjaman.append(rental_data)

        

        return main()
    
def admin(): #ADMIN
  while True:
    print('''
    Welcome Admin

    1. List Mobil    
    2. Add Car
    3. Delete Car
    4. Data Peminjaman
    5. Exit
    ''')
    user_input = input('Choose Action: ')
    if user_input == '1':
        database()
    elif user_input == '2':
      addmore()
    elif user_input == '3':
      delete()
    elif user_input == '4':
      datapeminjaman()
    elif user_input == '5':
      return main()
    else:
       return
    

def customer(): #CUSTOMER

    print('''
    Welcome Customer!

    1. Daftar Mobil
    2. Rent A Car
    3. Exit
    ''')
    user_input = input('Choose Action: ')
    if user_input == '1':
        database()
        return
    elif user_input == '2':
        rent()
    elif user_input == '3':
        print('Thank You For Booking With Easy Rental')
    

#main
def main():
    while True:
      print('''
        WELCOME TO EASY RENTAL

        1. ADMINISTRATOR
        2. CUSTOMER
        3. EXIT
        ''')
      user_input = input('Choose User')
      if user_input == '1':
            admin()
      elif user_input == '2':
            customer()
      elif user_input == '3':
            print('Thank You For Booking With Easy Rental') 
            break
      else:
            print('Invalid')
            break
        

main()   