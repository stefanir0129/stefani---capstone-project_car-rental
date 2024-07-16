from tabulate import tabulate
import datetime

#database

daftarmobil = [
    {'Kode': '1','Merk': 'Toyota', 'Type': 'Avanza', 'Transmisi': 'Manual', 'Tarif Per Hari': 200000, 'Status': 'Available'},
    {'Kode': '2','Merk': 'Honda', 'Type': 'Civic', 'Transmisi': 'Matic', 'Tarif Per Hari': 400000, 'Status': 'Available'},
    {'Kode': '3','Merk': 'Honda', 'Type': 'Brio', 'Transmisi': 'Matic', 'Tarif Per Hari': 250000, 'Status': 'Available'},
    {'Kode': '4','Merk': 'Suzuki', 'Type': 'Swift', 'Transmisi': 'Manual', 'Tarif Per Hari': 200000, 'Status': 'Available'},
    {'Kode': '5','Merk': 'Mitsubishi', 'Type': 'Pajero', 'Transmisi': 'Matic', 'Tarif Per Hari': 600000, 'Status': 'Available'},
    {'Kode': '6','Merk': 'Toyota', 'Type': 'Innova', 'Transmisi': 'Matic', 'Tarif Per Hari': 400000, 'Status': 'Available'}
]

data_peminjaman = []
deleted_data = []

def database():
    print(tabulate(daftarmobil, headers='keys', tablefmt='psql'))
def datapeminjaman():
    print(tabulate(data_peminjaman, headers='keys', tablefmt='psql'))

def filter_available():
    available_cars = [car for car in daftarmobil if car['Status'] == 'Available']
    if not available_cars:
        print("Tidak ada mobil yang tersedia.")
    else:
        print("Mobil yang tersedia:")
        for car in available_cars:
            print(tabulate([car], headers='keys', tablefmt='psql'))
            

def filter_matic():
    matic_cars = [car for car in daftarmobil if car['Transmisi'] == 'Matic']
    if not matic_cars:
        print("Tidak ada mobil matic.")
    else:
        print("Mobil matic:")
        for car in matic_cars:
            print(tabulate([car], headers='keys', tablefmt='psql'))
            

def filter_manual():
    manual_cars = [car for car in daftarmobil if car['Transmisi'] == 'Manual']
    if not manual_cars:
        print("Tidak ada mobil manual.")
    else:
          for car in manual_cars:
            print(tabulate([car], headers='keys', tablefmt='psql'))
            

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
    status = input('Status: ')
    daftarmobil.append({'Kode': kode,'Merk': merk, 'Type': model, 'Transmisi': transmisi, 'Tarif Per Hari': tarif, 'Status': 'Available'})
    print('Data berhasil ditambahkan')
    database()
    return admin()

#DEL
def delete():
  database()
  print('''
    Pilih kode yang ingin dihapus
    ''')
  kode = int(input('Kode: '))
  deleted_item = daftarmobil.pop(kode-1)
  for i in range(len(daftarmobil)): #kode dalam list akan menyesuaikan degan data yang dihapus
    daftarmobil[i]['Kode'] = i+1

  deleted_data.append(deleted_item)
  print('Data berhasil dihapus')
  database()
  return admin()

def restore():
  if not deleted_data:
    print('Tidak ada data yang dihapus')
    return

  else:
    print(tabulate(deleted_data, headers='keys', tablefmt='psql'))

  while True:
    kode = input('Masukkan Kode: ')
    for i in range(len(deleted_data)): # iterate through the list to find the item with matching Kode
        if deleted_data[i]['Kode'] == kode:
            daftarmobil.append(deleted_data[i])
            deleted_data.pop(i)
            print('Data berhasil direstore')  
            print(tabulate(deleted_data, headers='keys', tablefmt='psql'))
            database()
            return admin()



def rent():
  global data_peminjaman
  global daftarmobil
  while True:
    print('''
    Pilih Mobil
    1. Tampilkan semua mobil
    2. Tampilkan mobil yang tersedia
    3. Tampilkan transmisi matic
    4. Tampilkan transmisi manual
    ''')
    user_input = input('Choose Action: ')
    if user_input == '1':
      database()
      return rent()
    elif user_input == '2':
      filter_available()    
    elif user_input == '3':
      filter_matic()
    elif user_input == '4':
      filter_manual()


    Kode = (input('Masukkan Kode Mobil: ''tekan enter untuk kembali ke menu sebelumnya'))
    if Kode not in [i['Kode'] for i in daftarmobil]:
      print('Kode tidak ditemukan')
      return rent()
    elif Kode == '':
      return rent()
    for index, car in enumerate(daftarmobil):
      if car['Kode'] == Kode:
            break  # Exit the loop once the car is found
    else:
        continue  # Continue to the next iteration of the while loop
    
    print('''
    Lengkapi Data Anda
    ''')
    Name = input('Nama: ')
    Phone = input('Nomor Telepon: ')
    if not Phone.isdigit():
      print('Nomor Telepon harus berupa angka')
      continue    

    while True:
      try:
          tanggalsewa = input('Tanggal sewa (dd/mm/yy): ')
          tanggalsewa = datetime.datetime.strptime(tanggalsewa, '%d/%m/%y').date()
          if tanggalsewa < datetime.date.today():
            print('Tanggal tidak boleh kurang dari hari ini')
          else:
              break
      except ValueError:
        print('Silahkan masukkan tanggal dengan format dd/mm/yy')

    while True:     
      try:
        tanggalkembali = input('Tanggal kembali (dd/mm/yy): ')
        tanggalkembali = datetime.datetime.strptime(tanggalkembali, '%d/%m/%y').date()
        if tanggalkembali < tanggalsewa:
          print('Tanggal tidak boleh kurang dari tanggal sewa')
        else:
          break
      except ValueError:
        print('Silahkan masukkan tanggal dengan format dd/mm/yy')

    durasi = (tanggalkembali - tanggalsewa).days +1
    if durasi == 0:
       durasi = 1

    print('''
    Detail Peminjaman
    ''')
    print(f'Nama: {Name}')
    print(f'Nomor Telepon: {Phone}')
    print(f'Kode Mobil: {Kode}')
    print(f'Merk: {car["Merk"]}')
    print(f'Type: {car["Type"]}')
    print(f'Transmisi: {car["Transmisi"]}')
    print(f'Tarif Per Hari: {car["Tarif Per Hari"]}')
    print(f'Tanggal Sewa: {tanggalsewa}')
    print(f'Tanggal Kembali: {tanggalkembali}')
    print(f'Durasi: {durasi} hari')
    print(f'Total: {durasi * car["Tarif Per Hari"]}')
    print('Terima Kasih')

    rent_data_copy = daftarmobil[index].copy()
    rent_data_copy.pop('Status', None)  # Remove 'status' if it exists
    rent_data_copy.pop('Tarif Per Hari', None)  # Remove 'Tarif Per Hari' if it exists

    rental = {
        'Name': Name,
        'Phone': Phone,
        'Tanggal Sewa': tanggalsewa,
        'Tanggal Kembali': tanggalkembali,
        'Durasi': durasi,
        'Total': durasi * car['Tarif Per Hari'],
        **rent_data_copy
    }

    data_peminjaman.append(rental)
    daftarmobil[index]['Status'] = 'Rented'
    break
  return main()

def admin(): #ADMIN
  print('''
    Welcome Admin

    1. Delete Car
    2. Add Car
    3. Data Peminjaman
    4. Restore Data
    5. Exit
    ''')
  user_input = input('Choose Action: ')
  if user_input == '1':
      delete()
  elif user_input == '2':
      addmore()
  elif user_input == '3':
      datapeminjaman()
  elif user_input == '4':
      restore()
  elif user_input == '5':
      return print('Thank You For Booking With Easy Rental')

def customer(): #CUSTOMER
  print('''
    Welcome Customer

    1. Daftar Mobil
    2. Rent A Car
    3. Exit
    ''')
  user_input = input('Choose Action: ')
  if user_input == '1':
    database()
    return customer()
  elif user_input == '2':
    rent()
  elif user_input == '3':
    return print('Thank You For Booking With Easy Rental')

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

main()   