
def karesini_al(x):
    return x**2

def cif_sayilari_filtrele(x):
    if x%2==0:
        return x
    else:
        return None

sayilar=[*range(1,6)]
print(sayilar)
print("------------------")


for index in range(len (sayilar)):
    sayilar[index]=karesini_al(sayilar[index])
print(sayilar)
print("------------------")


print(list(map(karesini_al,sayilar)))#soldaki fonksiyonu sağdaki listeye uygular
print("------------------")


sayilar2=[*range(1,6)]
print([*filter(cif_sayilari_filtrele,sayilar2)])#filtreleme fonksiyonlarında kullaanılır
print("------------------")


sayilar3=[*range(1,6)]
print(list(map(lambda sayi:sayi**2,sayilar3)))#tek satırda fonksiyonsuz işlem yapmamızı saglar 
print("------------------")


sayilar4=[*range(1,6)]
print([*filter(lambda x: x if x%2==0 else None, sayilar4)])