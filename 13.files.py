file= open("dosya.txt","r") #w dosyayı oluşturur içindekileri siler
                            #r dosya okumak için kullanılır
                            #a dosyaya oluşturur ekleme yapar
#file.write("naber pyhton\n")
veri=file.read(1)#1 konumluk oku
print(veri)
file.seek(10)#10.konuma git
file.seek(0)

for satir in file:#dosya okur
    print(satir)
file.close