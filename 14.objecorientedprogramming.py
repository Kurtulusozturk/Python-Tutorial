class Account:
    def __init__(self,isim,numara,bakiye):#self parametre bulunması lazım 
                                          #obje oluştururken özellik tanımladığımız kısım
        self.isim=isim
        self.numara=numara
        self.bakiye=bakiye

    def hesapbilgileri(self):
        print("İsim:",self.isim)
        print("Numara:",self.numara)
        print("Bakiye:",self.bakiye)

    def paraCek(self,miktar):
        if(self.bakiye-miktar<0):
            print("Bakiyeniz yeterli değil")
        else:
            self.bakiye-=miktar
            print("Yeni bakiye:",self.bakiye)
    
    def parayatir(self,miktar):
        self.bakiye+=miktar
        print("Yeni bakiye:",self.bakiye)

account= Account("Kurtuluş",15554,1000)
account.hesapbilgileri()
account.parayatir(800)
account.paraCek(1200)
account.hesapbilgileri()