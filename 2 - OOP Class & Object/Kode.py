class Mobil:
    def __init__(self, warna, tahun, merek):
        self.warna = warna
        self.tahun = tahun
        self.merek = merek
    
    def nyalakan(self):
        print("Mobil dinyalakan")

    def berjalan(self):
        print(f"Mobil dengan merek", self.merek, "yang berwarna", self.warna, "sedang berjalan")

ferrari = Mobil("merah", 2020, "Ferrari")
toyota = Mobil("putih", 2019, "Toyota")
tesla = Mobil("hitam", 2023, "Tesla")

ferrari.berjalan()
toyota.berjalan()
tesla.nyalakan()

ferrari.warna = "emas"

print("Warna dari mobil Ferrari adalah:", ferrari.warna)
print("Tahun dari mobil Tesla adalah:", tesla.tahun)

del tesla.tahun

print("Tahun dari mobil Tesla adalah:", tesla.tahun)

