class Kampus(object): # parent class
	# construktor
	def __init__(self, nama, status, jurusan): # private fungsi
		self.nama = nama  #public atribut
		self.__status = status #private atribut
		self.__jurusan = jurusan #private atribut
	def Salam(self): # public fungsi
		print("Selamat Belajar") # isi informasi pada fungsi Salam
	def _Info(self): # protected fungsi
		print("INFO")
		print("Nama     : " + self.nama) 
		print("Jurusan  : " + self._Kampus__jurusan) # Kampus merupakan class Protected karena bisa diakses oleh class lain

class Mahasiswa(Kampus):  # class mahasiswa merupakan turunan dari class Kampus
	# construktor
	def __init__(self, nama, status, jurusan, nim): # private fungsi
		super().__init__(nama, status, jurusan) # class Mahasiswa mewarisi atribut dari class parent (nama, status, jurusan)
		self.__nim = nim # class mahasiswa memiliki atribut private nim
	def SalamMhs(self):
		print('Hai Teman-teman, kami {} {} mengucapkan ' .format(
			self._Kampus__status, self._Kampus__jurusan))
		self.Salam()

#Input Data
namaMhs =str(input("Masukkan Nama Mahasiswa    : "))
jurusan = str(input('Masukkan Jurusan Mahasiswa : '))
nim = str(input('Masukkan Nim: '))
# memanggil konstruktor
x = Mahasiswa(namaMhs, "Mahasiswa" , jurusan , nim)
x.SalamMhs() # public fungsi
x._Info() # protected fungsi

