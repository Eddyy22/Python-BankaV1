bakiye = 0
Tc = "100200"
password = "2020"

if Tc == input("Kullanici Adi :") and password == input("Şifre :"):
        print("Hos Geldiniz..")
else:
        print("Bilgiler Yanlis..!")

while True:
        print("""*****************
        ANASAYFA
    1. Mevcut Bakiye
    2. Para Yatir
    3. Para Cek
    4. Cikis
    *****************""")
        Secenek = int(input("Ne yapmak istiyorsunuz? :"))
        if Secenek == 1:
            print("Bakiyeniz :",bakiye)
        elif Secenek ==2:
            paraYatir = int(input("Yatiracaginiz Miktari Girin :"))
            if paraYatir < 0:
                 print("Negatif Islem Yapamazsin..!")
            else:
                 bakiye += paraYatir
                 print("Hasabiniza",paraYatir,"TL Yatirildi."," Hesapta :",bakiye,"TL'niz var.")
        elif Secenek == 3:
            paraCek = int(input("Cekeceginiz Miktari Girin :"))
            if paraCek < 0:
                print("Negatif Islem Yapamazsin..!")
            elif  bakiye - paraCek < 0:
                print("Yeterli Paraniz Yok.")
            else:
                bakiye -= paraCek
                print("Hesabinizdan",paraCek,"TL Cektiniz.")
        elif Secenek == 4:
            print("Cikis Yapiliyor... IYI GUNLER")
            break