class Mobil:
    _merk = None
    _tipe = None
    _kapasitasBBM = None
    _jenisBahanBakar = None

    def __init__(self,merk,tipe):
        self._merk = merk
        self._tipe = tipe

    def getmerk(self):
        return self._merk
    def gettipe(self):
        return self._tipe
    def getbahanBakar(self):
        return self._jenisBahanBakar
    def getkapasitasBBM(self):
        return self._kapasitasBBM

    def setkapasitasBBM(self,kapasitasBBM):
        self._kapasitasBBM = kapasitasBBM
    def setbahanbakar(self, bahanbakar):
        self._bahanbakar = bahanbakar  


    def printInfo(self):
        print("=======INFO=========")
        print("Merk:", self.getmerk())
        print("Tipe: ", self.gettipe())
        print("Bahan Bakar:", self.getbahanBakar())
        print("Kapasitas BBM:", self.getkapasitasBBM())


    def isiBBM(self,harga):
        if self._kapasitasBBM == None:
            print("ERROR! Kapasitas BBM atau Jenis Bahan Bakar belum di inputkan ")
        else:
            y = harga*self._kapasitasBBM
            print("Mengisi 20 Liter")
            print("Total Harga: ", y)

        
    

if __name__ == "__main__":
    mobil1 = Mobil("Toyota", "Avanza")
    mobil1.printInfo()

    mobil2 = Mobil("Nissan", "Grand Livina")
    mobil2.setbahanbakar("Bensin")
    mobil2.setkapasitasBBM(20)
    mobil2.printInfo()
    
    mobil1.isiBBM(14500)
    mobil2.isiBBM(14500)