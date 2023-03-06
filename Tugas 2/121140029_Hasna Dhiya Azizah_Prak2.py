class Data_diri:
    def __init__(self, nama, tanggal_lahir, alamat):
        self.nama = nama
        self.tanggal_lahir = tanggal_lahir
        self.alamat = alamat

    def Nama(self):
        print("Nama             : ", self.nama)
    def Tanggal_lahir(self):
        print("Tanggal_lahir    : ", self.tanggal_lahir)
    def Alamat(self):
        print("Alamat           : ", self.alamat)

Data = Data_diri("Hasna Dhiya Azizah", 20, "Bandar Lampung")
Data.Nama()
Data.Tanggal_lahir()
Data.Alamat()