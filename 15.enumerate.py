harfler=['a','b','c','d','e']
for harf in enumerate (harfler):#enumerate index sayısını başa ekler
    print((harf))
print("-------------------------------------")
for index,harf in enumerate(harfler):
    print("{}.harf: {}".format(index+1,harf))