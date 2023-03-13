class AkunBank():

  #constructor
  def __init__(self,no_pelanggan,nama_pelanggan,jumlah_saldo):
      self.__no_pelanggan = no_pelanggan
      self.__nama_pelanggan = nama_pelanggan
      self.__jumlah_saldo = jumlah_saldo

  def lihat_saldo(self):
      print(f"\n{self.__nama_pelanggan} memiliki saldo Rp {self.__jumlah_saldo}")

  def tarik_tunai(self):
      nominal = int(input("\nMasukkan jumlah nominal yang ingin ditarik: "))
      while  nominal > self.__jumlah_saldo:
        print("Nominal saldo yang Anda punya tidak cukup!")
        nominal = int(input("\nMasukkan jumlah nominal yang ingin ditarik: "))
      print("Saldo berhasil ditarik!")

  def transfer(self):
      list_pelanggan = {'Nana':1234, 'Ukraina':2345, 'Elon Musk': 3456}
      no_rek = int(input("\nMasukkan no rekening tujuan: "))
      if no_rek in list_pelanggan.values():
        jumlah_transfer = int(input("Masukkan nominal yang ingin ditransfer: "))
        if jumlah_transfer > self.__jumlah_saldo:
          print("Saldo yang Anda miliki tidak cukup untuk ditransfer")
        else:
          def return_key(val):
            for key, value in list_pelanggan.items():
              if value==val:
                return key
            return('Key Not Found')
          print(f"Transfer Rp {jumlah_transfer} ke {return_key(no_rek)} Sukses!")
      else:
        print("No rekening tujuan tidak dikenal! Kembali ke menu utama...")
  
  def lihat_menu(self):
      print ("Selamat datang di Bank Jago")
      print (f"Halo {self.__nama_pelanggan}, ingin melakukan apa?")
      print ("1. Lihat Saldo")
      print ("2. Tarik Tunai")
      print ("3. Transfer Saldo")
      print ("4. Keluar")
      pilihan = int(input("\nMasukkan nomor input: "))
      if pilihan == 1:
        Akun1.lihat_saldo()
      elif pilihan == 2:
        Akun1.tarik_tunai()
      elif pilihan == 3:
        Akun1.transfer()
      else:
        print("\nTransaksi Selesai!")

# Instansi Object
Akun1 = AkunBank(1234, "Hasna", 5000000000)
Akun2 = AkunBank(2345, "Ukraina", 6666666666)
Akun3 = AkunBank(3456, "Elon Musk", 9999999999)


Akun1.lihat_menu()
