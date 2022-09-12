#args için unpacking
def toplam(a,b,c,d):
    return a+b+c+d

sayilar=[1,2,3,4]
sonuc= toplam(*sayilar)
print(sonuc)


#args için unpacking
def toplam2(*args):
    i=0
    a=0
    sonuc=0
    while i<len(args):
        a=args[i]
        sonuc=a+sonuc
        i=1+i
    print(sonuc)
    return 
toplam2(0,1,2,3,4,5,6,7)

#kwargs için unpacking
def yazdır(isim,soyisim):
    print(isim,soyisim)
dic={'isim':'Kurtuluş' ,'soyisim':'Öztürk'}
yazdır(**dic)

#kwargs için packing
def yazdır2(**kwargs):
    print(kwargs)
yazdır2(isim='Kurtuluş',soyisim='öztürk')
