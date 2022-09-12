class Insan:
    def __init__(self,isim,soyisim):
        self.isim=isim
        self.soyisim=soyisim
    def selamla(self):
        print(f"merhaba {self.isim}")
    def yemek(self):
        print("döner ver")
    def maas(self):
        print("söylenmez")

class KibarInsan(Insan):
    pass
class KabaInsan(Insan):
    def __init__(self, isim, soyisim,maas):
        self.maasi=maas
        self.isim=isim
        self.soyisim=soyisim
    def maas(self):
        print(f"{self.maasi} maaş")
        super().selamla()

insan=Insan("Kurtuluş","Öztürk")
insan.selamla()

Kibarinsan=KibarInsan("Hasan","yıldızkaydı")
Kibarinsan.maas()

Kaba=KabaInsan("Kurt","ÖZt",maas="200")
Kaba.maas()