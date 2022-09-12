alacaklar = set(['elma','armut','kiraz']) #listenin rahat kullanılışı sıra dağılabilir önemsiz olması lazım

alacaklar.add('araba')
alacaklar.add('ev')
alacaklar.add('kitap')
alacaklar.add('kitap')#ikinci kez eklenemez

alacaklar.remove('araba') #kaldırır
# alacaklar.clear() tümünü siler
print(alacaklar)
print("--------------------------")



teksayilar=set([1,3,5,7,9])
ciftsayilar=set([2,4,6,8])
asalsayilar=set([2,3,5,7])

print(ciftsayilar.union(teksayilar))        #birleşim
print(teksayilar.intersection(asalsayilar)) #kesişim





