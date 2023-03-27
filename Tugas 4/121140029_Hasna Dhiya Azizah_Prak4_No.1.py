#Hasna Dhiya Azizah 121140029 RB
#Tugas 4 No.1

class Komputer:
    def __init__(self,nama,jenis,harga,merk) -> None:
        self.nama=nama
        self.jenis=jenis
        self.harga=harga
        self.merk=merk

class Processor(Komputer):
    def __init__(self,merk, jenis, harga,jumlah_core,kecepatan_processor) -> None:
        super().__init__("Processor", jenis, harga, merk)
        self.jumlah_core=jumlah_core
        self.kecepatan_processor=kecepatan_processor
    
    def __str__(self) -> str:
        return f"{self.nama} {self.jenis} produksi {self.merk}"

class RAM(Komputer):
    def __init__(self,merk, jenis, harga,ram_capacity) -> None:
        super().__init__("RAM", jenis, harga, merk)
        self.ram_capacity=ram_capacity

    def __str__(self) -> str:
        return f"{self.nama} {self.jenis} produksi {self.merk}"

class HDD(Komputer):
    def __init__(self,merk, jenis, harga,hdd_capacity,rpm) -> None:
        super().__init__("SATA", jenis, harga, merk)
        self.hdd_capacity=hdd_capacity
        self.rpm=rpm

    def __str__(self) -> str:
        return f"{self.nama} {self.jenis} produksi {self.merk}"

class VGA(Komputer):
    def __init__(self,merk, jenis, harga, vga_capacity) -> None:
        super().__init__("VGA", jenis, harga, merk)
        self.vga_capacity=vga_capacity

    def __str__(self) -> str:
        return f"{self.nama} {self.jenis} produksi {self.merk}"

class PSU (Komputer):
    def __init__(self,merk, jenis, harga, daya) -> None:
        super().__init__("PSU", jenis, harga, merk)
        self.daya=daya

    def __str__(self) -> str:
        return f"{self.nama} {self.jenis} produksi {self.merk}"

p1 = Processor('Intel','Core i7 7740X',4350000,4,'4.3GHz')
p2 = Processor('AMD','Ryzen 5 3600',250000,4,'4.3GHz')
ram1 = RAM('V-Gen','DDR4 SODimm PC19200/2400MHz',328000,'4GB')
ram2 = RAM('G.SKILL','DDR4 2400MHz',328000,'4GB')
hdd1 = HDD('Seagate','HDD 2.5 inch',295000,'500GB',7200)
hdd2 = HDD('Seagate','HDD 2.5 inch',295000,'1000GB',7200)
vga1 = VGA('Asus','VGA GTX 1050',250000,'2GB')
vga2 = VGA('Asus','1060Ti',250000,'8GB')
psu1 = PSU('Corsair','Corsair V550',250000,'500W')
psu2 = PSU('Corsair','Corsair V550',250000,'500W')

rakit = [[p1,ram1,hdd1,vga1,psu1],[p2,ram2,hdd2,vga2,psu2]]

case=1
for a in rakit:
    print(f"\nKomputer {case}")
    case+=1
    for b in a:
        print(b)
