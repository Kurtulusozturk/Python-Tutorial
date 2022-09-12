def selamla(isim):
    print("Merhaba", isim)
    print("Nasılsın?")
    return 0

def toplama(a,b,c):
    print("Toplam",a+b+c)
    return a+b+c

def isim_soyisim_birlestir(*args):
    print( " ".join(args))
    return " ".join(args)

isim=input("İsminizi giriniz:")
selamla(isim)
print("------------------------------")
toplama(1,2,5)
#" ".join("Kurtuluş","Öztürk") #iki değeri birleştirir
#"Kurtuluş Öztürk".split() #iki değeri index olarak ayırma 
print("------------------------------")
isim_soyisim_birlestir("Kurtuluş","Ruşen","Öztürk")



#def aaa (**kwargs) sözlü yapısı ile kullanılan arg