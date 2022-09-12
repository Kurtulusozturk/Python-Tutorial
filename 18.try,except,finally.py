def tam_sayiya_cevir():
    girdi=(input("bir ondalık sayı girin:"))
    status=" "
    try:
        girdi=float(girdi)
        print("yuvarlama işleminin sonucu: {}".format((round(girdi)))) 
        #try istenen formattaysak çalışır

    except:
        print("{} girdisi onadalık tipe çevrilemiyor".format(girdi)) 
        #except istenen formatta değilsek çalışır

    finally:
        #en nihayetinde şunu yap her iki durumda da tetiklenir
        status="İşlem sonlandı"
        print(status)

        
tam_sayiya_cevir()