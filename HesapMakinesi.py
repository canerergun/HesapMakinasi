import time

while True:
    print("""
    Toplama İçin: 1
    Çıkarma için: 2
    Çarpma İçin : 3
    Bölme İçin  : 4
    """)
    try:
        sec = int(input("Yapmak istediğiniz işlemi seçiniz: "))
        sayi1 = int(input("Sayı Giriniz: "))
        sayi2 = int(input("Sayı Giriniz: "))

        if sec == 1:
            sonuc = sayi1 + sayi2
        elif sec == 2:
            sonuc = sayi1 - sayi2
        elif sec == 3:
            sonuc = sayi1 * sayi2
        elif sec == 4:
            sonuc = sayi1 / sayi2
        else:
            print("Hatalı Giriş!")

        print(f"{sayi1} ve {sayi2}'nin sonucu {sonuc}")


    except NameError:
        print("Sadece 1 İla 4 arası rakam girebilirsiniz, 3 Saniye Sonra Tekrar Deneyiniz!")
        time.sleep(3)

    except ValueError:
        print("Neyin Kafası Lan Bu Sadece Sayı Yaz, 6 Saniye de Bekle Azcık Düşünerek Hesapla!")
        time.sleep(6)


print("DevSeu Yapımıdır!")