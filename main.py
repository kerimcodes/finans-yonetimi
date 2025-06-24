from datetime import datetime
import os
dil_sözlugu = []

proje_dizini = os.path.dirname(os.path.abspath(__file__))
veri_klasoru = os.path.join(proje_dizini,"veriler")
if not os.path.exists(veri_klasoru):
    os.makedirs(veri_klasoru)

TR = {
    "ana_sayfa": "--- Ana Sayfa ---",
    "kullanici_islemleri": "--- Kullanıcı İşlemleri Sayfası ---",
    "kayit_ol": "Lütfen bir kullanıcı adı seçiniz: ",
    "giris_yap": "2. Giriş Yap",
    "kayit_yap": "1. Kayıt Ol",
    "cikis_yap":"3. Çıkış",
    "sifre_olustur": "Lütfen kendinize bir şifre seçiniz: ",
    "kullanici_adi_alinmis": "Bu kullanıcı adı önceden alınmış. Lütfen başka bir kullanıcı adı seçiniz.",
    "kayit_basarili": "Kayıt başarılı!\n",
    "ilk_kayit": "Kayıt başarılı! \n",
    "giris_ad": "Lütfen kullanıcı adınızı giriniz: ",
    "giris_sifre": "Lütfen kullanıcı şifrenizi giriniz: ",
    "hosgeldiniz": "Hoş geldiniz {kullanici_adi}!\n",
    "hatali_giris": "Hatalı giriş. Tekrar deneyiniz.\n",
    "veri_bulunamadi": "Kullanıcı verisi bulunamadı. Lütfen önce kayıt olun.\n",
    "kullanici_degisim":"1. Kullanıcı Adını Değiştir",
    "sifre_degisim": "2. Şifre Değiştir",
    "hesap_sil":"3. Hesap Silme",
    "ayarlar_secim": "Seçiminiz: ",
    "ayar_ad_degistir": "Yeni kullanıcı adınızı giriniz: ",
    "ayar_ad_alinmis": "Bu kullanıcı adı zaten alınmış.",
    "ayar_ad_degisti": "Kullanıcı adı başarıyla değiştirildi.",
    "ayar_sifre_degistir": "Yeni şifrenizi giriniz: ",
    "ayar_sifre_degisti": "Şifre başarıyla değiştirildi.",
    "ayar_hesap_sil_onay": "Hesabınızı gerçekten silmek istiyor musunuz? (e/h)",
    "ayar_hesap_sil_ok": "Hesap başarıyla silindi",
    "ayar_hesap_sil_iptal": "Silme işleminiz iptal edilmiştir.",
    "hatali_secim": "Hatalı seçim yapıldı.",
    "gelir_ekle": "Gelirinizi ekleyiniz: ",
    "sayi_girin": "Lütfen sayıyla giriniz!",
    "negatif_sayi": "Negatif sayı girmeyiniz!",
    "kategori_sor": "Bu gelirin kategorisi nedir? (örn: maaş vb.): ",
    "kategori_bos": "Bu alan boş bırakılamaz!",
    "gelir_kaydedildi": "Gelir kaydedildi.",
    "gider_ekle": "Giderinizi ekleyiniz: ",
    "kategori_gider_sor": "Bu giderin kategorisi nedir? (örn: kira, fatura vb.): ",
    "gider_kaydedildi": "Gider kaydedildi.",
    "toplam_gelir": "Toplam gelir: {toplam_gelir}",
    "toplam_gider": "Toplam gider: {toplam_gider}",
    "bakiye": "Bakiyeniz: {bakiye}",
    "secim_yap": "Seçiminizi yapınız: ",
    "goruntuleme_sec": "Nasıl görüntülemek istersiniz?",
    "ay_gir": "Görmek istediğiniz ayı sayı ile giriniz:(örn ocak için 01)",
    "ay_gecersiz": "Lütfen geçerli bir sayı girin",
    "gelir_yok": "Henüz kayıtlı bir gelir kaydınız yok.",
    "gider_yok": "Henüz kayıtlı bir gider kaydınız yok.",
    "kayit_bulunamadi": "{ay}. aya ait kayıt bulunamadı.",
    "gelir_sil_sec": "Silmek istediğiniz satırın numarasını girin: ",
    "gider_sil_sec": "Silmek istediğiniz satırın numarasını girin: ",
    "gecersiz_sayi": "Lütfen geçerli bir sayı girin.",
    "satir_silindi": "{silinen} satırı silindi.",
    "ana_don": "Ana sayfaya dönülüyor...",
    "cikis": "Çıkış yapılıyor...",
    "ay_baz_goruntuleme":"1. Ay Bazında Görüntüleme",
    "genel_goruntuleme":"2. Genel Görüntüleme",
    "secim_sayi":"Lütfen sayı ile seçim yapınız",
    "ay_gelir": "{ay}. aya ait gelirleriniz:",
    "ay_hersey_gelirgider":"Tutar: {tutar} TL | Kategori: {kategori} | Tarih: {tarih}",
    "ay_toplam_gelir":"{ay}. aya ait toplam geliriniz: {toplam}",
    "gelir_kayit":"\n---Gelir Kayıtları---",
    "genel_gelir_goruntule":"{gelir_sayi}-Tutar: {tutar} TL | Kategori: {kategori} | Tarih: {tarih}",
    "ay_gider":"{ay}. aya ait giderleriniz:",
    "ay_toplam_gider":"{ay}. aya ait toplam gideriniz: {toplam}",
    "gider_kayit":"\n---Gider Kayıtları---",
    "genel_gider_goruntule":"{gider_sayi}-Tutar: {tutar} TL | Kategori: {kategori} | Tarih: {tarih}",
    "silinecek_gelir_yok":"Silinecek gelir kaydı bulunamadı.",
    "secim_hata":"Hatalı seçim yapıldı!",
    "silinecek_gider_yok":"Silinecek gider kaydı bulunamadı.",
    "gelir_ekleme":"1 Gelir Ekle",
    "gider_ekleme":"2. Gider Ekle",
    "bakiye_goruntule":"3. Toplam Bakiye Görüntüle",
    "gelir_gor":"4. Gelirleri Görüntüle",
    "gider_gor":"5. Giderleri Görüntüle",
    "gelir_sil":"6. Gelirleri Sil",
    "gider_sil":"7. Giderleri Sil",
    "ayar":"8. Ayarlar",
    "geri":"9. Geri",
    "sifre_sartlar":"Şifreniz en az 8 haneden oluşmalı ve içerisinde en az 1 küçük harf 1 büyük harf  ve 1 rakam olmalıdır.",
    "sifrelen_hata":"Şifreniz en az 8 haneden oluşmalıdır.",
    "sifre_onay":"Şifre onaylandı",
    "sifre_sart_hata":"Gerekli şifre şartları sağlanmadı!",
    "hatali_satir": "Hatalı satır atlandı. {satir}"
}

ENG ={
    "ana_sayfa": "--- Home Page ---",
    "kullanici_islemleri": "--- User Operations Page ---",
    "kayit_ol": "Please choose a username: ",
    "giris_yap": "2. Log In",
    "kayit_yap": "1. Sign Up",
    "cikis_yap": "3. Exit",
    "sifre_olustur": "Please choose a password: ",
    "kullanici_adi_alinmis": "This username is already taken. Please choose another.",
    "kayit_basarili": "Registration successful!\n",
    "ilk_kayit": "Registration successful! \n",
    "giris_ad": "Please enter your username: ",
    "giris_sifre": "Please enter your password: ",
    "hosgeldiniz": "Welcome {kullanici_adi}!\n",
    "hatali_giris": "Incorrect login. Please try again.\n",
    "veri_bulunamadi": "User data not found. Please sign up first.\n",
    "kullanici_degisim": "1. Change Username",
    "sifre_degisim": "2. Change Password",
    "hesap_sil": "3. Delete Account",
    "ayarlar_secim": "Your choice: ",
    "ayar_ad_degistir": "Enter your new username: ",
    "ayar_ad_alinmis": "This username is already taken.",
    "ayar_ad_degisti": "Username changed successfully.",
    "ayar_sifre_degistir": "Enter your new password: ",
    "ayar_sifre_degisti": "Password changed successfully.",
    "ayar_hesap_sil_onay": "Are you sure you want to delete your account? (y/n)",
    "ayar_hesap_sil_ok": "Account successfully deleted.",
    "ayar_hesap_sil_iptal": "Account deletion canceled.",
    "hatali_secim": "Invalid selection.",
    "gelir_ekle": "Enter your income: ",
    "sayi_girin": "Please enter a number!",
    "negatif_sayi": "Please do not enter a negative number!",
    "kategori_sor": "What is the category of this income? (e.g., salary, etc.): ",
    "kategori_bos": "This field cannot be empty!",
    "gelir_kaydedildi": "Income recorded.",
    "gider_ekle": "Enter your expense: ",
    "kategori_gider_sor": "What is the category of this expense? (e.g., rent, bills, etc.): ",
    "gider_kaydedildi": "Expense recorded.",
    "toplam_gelir": "Total income: {toplam_gelir}",
    "toplam_gider": "Total expenses: {toplam_gider}",
    "bakiye": "Your balance: {bakiye}",
    "secim_yap": "Make your selection: ",
    "goruntuleme_sec": "How would you like to view?",
    "ay_gir": "Enter the month you want to view (e.g., 01 for January):",
    "ay_gecersiz": "Please enter a valid number.",
    "gelir_yok": "You don't have any recorded income yet.",
    "gider_yok": "You don't have any recorded expenses yet.",
    "kayit_bulunamadi": "No records found for month {ay}.",
    "gelir_sil_sec": "Enter the number of the income row to delete: ",
    "gider_sil_sec": "Enter the number of the expense row to delete: ",
    "gecersiz_sayi": "Please enter a valid number.",
    "satir_silindi": "{silinen} line deleted.",
    "ana_don": "Returning to main menu...",
    "cikis": "Logging out...",
    "ay_baz_goruntuleme": "1. View by Month",
    "genel_goruntuleme": "2. General View",
    "secim_sayi": "Please make your choice using a number",
    "ay_gelir": "Your income for month {ay}:",
    "ay_hersey_gelirgider": "Amount: {tutar} TL | Category: {kategori} | Date: {tarih}",
    "ay_toplam_gelir": "Total income for month {ay}: {toplam}",
    "gelir_kayit": "\n--- Income Records ---",
    "genel_gelir_goruntule": "{gelir_sayi}-Amount: {tutar} TL | Category: {kategori} | Date: {tarih}",
    "ay_gider": "Your expenses for month {ay}:",
    "ay_toplam_gider": "Total expense for month {ay}: {toplam}",
    "gider_kayit": "\n--- Expense Records ---",
    "genel_gider_goruntule": "{gider_sayi}-Amount: {tutar} TL | Category: {kategori} | Date: {tarih}",
    "silinecek_gelir_yok": "No income record to delete.",
    "silinecek_gider_yok": "No expense record to delete.",
    "secim_hata": "Invalid selection!",
    "gelir_ekleme": "1. Add Income",
    "gider_ekleme": "2. Add Expense",
    "bakiye_goruntule": "3. View Total Balance",
    "gelir_gor": "4. View Incomes",
    "gider_gor": "5. View Expenses",
    "gelir_sil": "6. Delete Income",
    "gider_sil": "7. Delete Expense",
    "ayar": "8. Settings",
    "geri": "9. Back",
    "sifre_sartlar":"Your password must consist of at least 8 digits and must contain at least 1 lower case letter upper case letter  and 1 number.",
    "sifrelen_hata":"your password must consist of at least 8 digits",
    "sifre_onay":"Password confirmed",
    "sifre_sart_hata":"The necessary password conditions are not met",
    "hatali_satir":"Skipped faulty line {satir}"
}

while True:
        dil= input("Lütfen dilinizi seçiniz/Please select your language: (tr/eng)")
        if dil.lower() =="tr":
            dil_sözlugu = TR
            break
        elif dil.lower() == "eng":
            dil_sözlugu = ENG
            break
        else:
            print("Hatalı seçim yaptınız/You made a wrong choice.")

def dosya_yolu(dosya_adi):
    return f"{veri_klasoru}/{dosya_adi}"
    
def sifre_guclu_mu(sifre):
    if len(sifre)<8:
        print(dil_sözlugu["sifrelen_hata"])
        return False
    harf = False
    rakam = False
    buyuk_harf = False
    for karakter in sifre:
        if karakter.isalpha():
            harf = True
        if karakter.isupper():
            buyuk_harf= True
        if karakter.isdigit():
            rakam = True
    if rakam and harf and buyuk_harf:
        print(dil_sözlugu["sifre_onay"])
        return True
    else:
        print(dil_sözlugu["sifre_sart_hata"])
        return False
    
def kayit_ol():
    while True:
        kullanici_adi = input(dil_sözlugu["kayit_ol"])
        while True:
            print(dil_sözlugu["sifre_sartlar"])
            kullanici_sifresi = input(dil_sözlugu["sifre_olustur"])
            if sifre_guclu_mu(kullanici_sifresi):
                break
        try:
            with open(dosya_yolu("users.txt"), "r", encoding="utf-8") as dosya:
                satirlar = dosya.readlines()
                for satir in satirlar:
                    mevcut_kullanici = satir.strip().split(",")[0]
                    if mevcut_kullanici == kullanici_adi:
                        print(dil_sözlugu["kullanici_adi_alinmis"])
                        break
                else:
                    with open(dosya_yolu("users.txt"), "a", encoding="utf-8") as dosya_yaz:
                        dosya_yaz.write(f"{kullanici_adi},{kullanici_sifresi}\n")
                    print(dil_sözlugu["kayit_basarili"])
                    break
        except FileNotFoundError:
            with open(dosya_yolu("users.txt"), "a", encoding="utf-8") as dosya:
                dosya.write(f"{kullanici_adi},{kullanici_sifresi}\n")
            print(dil_sözlugu["ilk_kayit"])
            break

def giris_yap():
    while True:
        giris_ad = input(dil_sözlugu["giris_ad"])
        giris_sifre = input(dil_sözlugu["giris_sifre"])

        try:
            with open(dosya_yolu("users.txt"), "r", encoding="utf-8") as dosya:
                satirlar = dosya.readlines()
                for satir in satirlar:
                    kullanici_adi, kullanici_sifresi = satir.strip().split(",")
                    if giris_ad == kullanici_adi and giris_sifre == kullanici_sifresi:
                        print(dil_sözlugu["hosgeldiniz"].format(kullanici_adi=kullanici_adi))
                        return kullanici_adi
                else:
                    print(dil_sözlugu["hatali_giris"])
        except FileNotFoundError:
            print(dil_sözlugu["veri_bulunamadi"])
            return None
 
def ayarlar(kullanici_adi):
    with open(dosya_yolu("users.txt"), "r", encoding="utf-8") as dosya:
        satirlar = dosya.readlines()
    for i, satir in enumerate(satirlar):
        mevcut_kullanici, mevcut_sifre = satir.strip().split(",")
        if mevcut_kullanici == kullanici_adi:
            print(dil_sözlugu["kullanici_degisim"])
            print(dil_sözlugu["sifre_degisim"])
            print(dil_sözlugu["hesap_sil"])
            secim = input(dil_sözlugu["ayarlar_secim"])

            if secim == "1":
                yeni_ad = input(dil_sözlugu["ayar_ad_degistir"])
                for s in satirlar:
                    if s.strip().split(",")[0] == yeni_ad:
                        print(dil_sözlugu["ayar_ad_alinmis"])
                        return
                satirlar[i] = f"{yeni_ad},{mevcut_sifre}\n"
                try:
                    os.rename(dosya_yolu(f"{kullanici_adi}_gelir.txt"), dosya_yolu(f"{yeni_ad}_gelir.txt"))
                except FileNotFoundError:
                    pass
                try:
                    os.rename(dosya_yolu(f"{kullanici_adi}_gider.txt"), dosya_yolu(f"{yeni_ad}_gider.txt"))
                except FileNotFoundError:
                    pass

                print(dil_sözlugu["ayar_ad_degisti"])
                kullanici_adi = yeni_ad  

            elif secim == "2":
                while True:
                    print(dil_sözlugu["sifre_sartlar"])
                    yeni_sifre = input(dil_sözlugu["ayar_sifre_degistir"])
                    if sifre_guclu_mu(yeni_sifre):
                        break
                satirlar[i] = f"{mevcut_kullanici},{yeni_sifre}\n"
                print(dil_sözlugu["ayar_sifre_degisti"])
            elif secim == "3":
                onay = input(dil_sözlugu["ayar_hesap_sil_onay"])
                if dil_sözlugu ==TR:
                    if onay.lower() =="e":
                        satirlar.pop(i)
                        try:
                            os.remove(dosya_yolu(f"{kullanici_adi}_gelir.txt"))
                            os.remove(dosya_yolu(f"{kullanici_adi}_gider.txt"))
                        except FileNotFoundError:
                            pass
                        print(dil_sözlugu["ayar_hesap_sil_ok"])
                        with open(dosya_yolu("users.txt"), "w", encoding="utf-8") as dosya:
                            dosya.writelines(satirlar)
                        return True
                        
                    elif onay.lower() == "h":
                        print(dil_sözlugu["ayar_hesap_sil_iptal"])    
                    else:
                        print(dil_sözlugu["hatali_secim"])
                else:
                    if onay.lower() =="y":
                        satirlar.pop(i)
                        try:
                            os.remove(dosya_yolu(f"{kullanici_adi}_gelir.txt"))
                            os.remove(dosya_yolu(f"{kullanici_adi}_gider.txt"))
                        except FileNotFoundError:
                            pass
                        print(dil_sözlugu["ayar_hesap_sil_ok"])
                        with open(dosya_yolu("users.txt"), "w", encoding="utf-8") as dosya:
                            dosya.writelines(satirlar)
                        return True
                        
                    elif onay.lower() == "n":
                        print(dil_sözlugu["ayar_hesap_sil_iptal"])    
                    else:
                        print(dil_sözlugu["hatali_secim"])

            else:
                print(dil_sözlugu["hatali_secim"])

            with open(dosya_yolu("users.txt"), "w", encoding="utf-8") as dosya:
                dosya.writelines(satirlar)
            return False   
                
def gelir_ekle(kullanici_adi):
    while True:
        try:
            gelir_tutari = int(input(dil_sözlugu["gelir_ekle"]))
        except ValueError:
            print(dil_sözlugu["sayi_girin"])
            continue
        if gelir_tutari < 0:
            print(dil_sözlugu["negatif_sayi"])
            continue
        kategori = input(dil_sözlugu["kategori_sor"])
        if kategori == "":
            print(dil_sözlugu["kategori_bos"])
            continue
        tarih = datetime.now().strftime("%Y-%m-%d %H:%M")
        break
    dosya_adi = dosya_yolu(f"{kullanici_adi}_gelir.txt")
    satir = f"{gelir_tutari},{kategori},{tarih}\n"
    with open(dosya_adi, "a", encoding="utf-8") as dosya:
        dosya.write(satir)
    print(dil_sözlugu["gelir_kaydedildi"])

def gider_ekle(kullanici_adi):
    while True:
        try:
            gider_tutari = int(input(dil_sözlugu["gider_ekle"]))
        except ValueError:
            print(dil_sözlugu["sayi_girin"])
            continue
        if gider_tutari < 0:
            print(dil_sözlugu["negatif_sayi"])
            continue
        kategori = input(dil_sözlugu["kategori_gider_sor"])
        if kategori == "":
            print(dil_sözlugu["kategori_bos"])
            continue
        tarih = datetime.now().strftime("%Y-%m-%d %H:%M")
        break
    dosya_adi = dosya_yolu(f"{kullanici_adi}_gider.txt")
    satir = f"{gider_tutari},{kategori},{tarih}\n"
    with open(dosya_adi, "a", encoding="utf-8") as dosya:
        dosya.write(satir)
    print(dil_sözlugu["gider_kaydedildi"])

def toplam_bakiye(kullanici_adi):
    toplam_gelir = 0
    toplam_gider = 0
    try:
        with open(dosya_yolu(f"{kullanici_adi}_gelir.txt"), "r", encoding="utf-8") as gelir_dosyasi:
            for satir in gelir_dosyasi:
                gelir = satir.strip().split(",")[0]
                toplam_gelir += int(gelir)
    except FileNotFoundError:
        pass
    try:
        with open(dosya_yolu(f"{kullanici_adi}_gider.txt"), "r", encoding="utf-8") as gider_dosyasi:
            for satir in gider_dosyasi:
                gider = satir.strip().split(",")[0]
                toplam_gider += int(gider)
    except FileNotFoundError:
        pass
    bakiye = toplam_gelir - toplam_gider
    print(dil_sözlugu[f"toplam_gelir"].format(toplam_gelir=toplam_gelir))
    print(dil_sözlugu["toplam_gider"].format(toplam_gider=toplam_gider))
    print(dil_sözlugu[f"bakiye"].format(bakiye=bakiye))

def gelirleri_görüntüle(kullanici_adi):
    gelir_sayi = 1
    try:
        print(dil_sözlugu["ay_baz_goruntuleme"])
        print(dil_sözlugu["genel_goruntuleme"])
        secim = input(dil_sözlugu["goruntuleme_sec"])
    except ValueError:
        print(dil_sözlugu["secim_sayi"])
    if secim =="1":
        while True:
            ay =int(input(dil_sözlugu["ay_gir"]))
            if ay>12:
                print(dil_sözlugu["ay_gecersiz"])
                continue
            else:
                break
        try:
            eslesen_kayit_sayisi = 0 
            toplam = 0
            with open(dosya_yolu(f"{kullanici_adi}_gelir.txt"), "r", encoding="utf-8") as dosya:
                satirlar = dosya.readlines()
                for satir in satirlar:
                    parcalar = satir.strip().split(",")
                    if len(parcalar) != 3:
                            print(dil_sözlugu["hatali_satir"].format(satir=satir.split()))
                            continue  # bu satır geçilir
                    tutar, kategori, tarih = parcalar
                    tarih_ay = int(tarih.split("-")[1])
                    if ay == tarih_ay:
                        if eslesen_kayit_sayisi==0:
                            print(dil_sözlugu[f"ay_gelir"].format(ay=ay))
                        print(gelir_sayi,dil_sözlugu[f"ay_hersey_gelirgider"].format(tutar=tutar,kategori=kategori,tarih=tarih))
                        gelir_sayi += 1
                        toplam += int(tutar) 
                        eslesen_kayit_sayisi+=1
                if toplam !=0:    
                    print(dil_sözlugu[f"ay_toplam_gelir"].format(ay=ay,toplam=toplam))
            if eslesen_kayit_sayisi == 0:
                print(dil_sözlugu[f"kayit_bulunamadi"].format(ay=ay))
        except FileNotFoundError:
            print(dil_sözlugu["gelir_yok"])

    elif secim == "2":
        try:
            with open(dosya_yolu(f"{kullanici_adi}_gelir.txt"),"r",encoding="utf-8") as dosya:      
                satirlar = dosya.readlines()
                print(dil_sözlugu["gelir_kayit"])
                for satir in satirlar:
                    parcalar = satir.strip().split(",")
                    if len(parcalar) != 3:
                        print(f"Hatalı satır atlandı: {satir.strip()}")
                        continue  
                    tutar, kategori, tarih = parcalar
                    
                    print(dil_sözlugu["genel_gelir_goruntule"].format(gelir_sayi=gelir_sayi,tutar=tutar,tarih=tarih,kategori=kategori))
                    gelir_sayi+=1
        except FileNotFoundError:
            print(dil_sözlugu["gelir_yok"])  
    else:
        print(dil_sözlugu["secim_hata"])  

def giderleri_görüntüle(kullanici_adi):
    gider_sayi = 1
    
    print(dil_sözlugu["ay_baz_goruntuleme"])
    print(dil_sözlugu["genel_goruntuleme"])
    secim = input(dil_sözlugu["goruntuleme_sec"])
    
    if secim =="1":
        while True:
            ay =int(input(dil_sözlugu["ay_gir"]))
            if ay>12:
                print(dil_sözlugu["ay_gecersiz"])
                continue
            else:
                break
        try:
            eslesen_kayit_sayisi = 0 
            toplam = 0
            with open(dosya_yolu(f"{kullanici_adi}_gider.txt"), "r", encoding="utf-8") as dosya:
                satirlar = dosya.readlines()
                for satir in satirlar:
                    parçalar = satir.strip().split(",")
                    if len(parçalar) != 3:
                        print(dil_sözlugu["hatali_satir"].format(satir=satir.split()))
                        continue
                    tutar,kategori,tarih = parçalar
                    tarih_ay = int(tarih.split("-")[1])
                    if ay == tarih_ay:
                        if eslesen_kayit_sayisi==0:
                            print(dil_sözlugu["ay_gider"].format(ay=ay))
                        print(gider_sayi,dil_sözlugu[f"ay_hersey_gelirgider"].format(tutar=tutar,tarih=tarih,kategori=kategori))
                        gider_sayi += 1
                        toplam += int(tutar) 
                        eslesen_kayit_sayisi+=1
                if toplam !=0:
                    print(dil_sözlugu[f"ay_toplam_gider"].format(ay=ay,toplam=toplam))
            if eslesen_kayit_sayisi == 0:
                print(dil_sözlugu[f"kayit_bulunamadi"].format(ay=ay))
        except FileNotFoundError:
            print(dil_sözlugu["gider_yok"])

    elif secim == "2":
        try:
            with open(dosya_yolu(f"{kullanici_adi}_gider.txt"),"r",encoding="utf-8") as dosya:      
                satirlar = dosya.readlines()
                print(dil_sözlugu["gider_kayit"])
                for satir in satirlar:
                    satir = satir.strip()
                    tutar, kategori, tarih = satir.split(",")
                    print(dil_sözlugu["genel_gider_goruntule"].format(gider_sayi=gider_sayi,tarih=tarih,tutar=tutar,kategori=kategori))
                    gider_sayi+=1
        except FileNotFoundError:
            print(dil_sözlugu["gider_yok"])    
    else:
        print(dil_sözlugu["secim_hata"])
         
def gelir_sil(kullanici_adi):
    try:
        with open(dosya_yolu(f"{kullanici_adi}_gelir.txt"), "r", encoding="utf-8") as dosya:
            satirlar = dosya.readlines()

        if not satirlar:
            print(dil_sözlugu["silinecek_gelir_yok"])
            return

        gelirleri_görüntüle(kullanici_adi)  

        secim = input(dil_sözlugu["gelir_sil_sec"])
        if not secim.isdigit():
            print(dil_sözlugu["gecersiz_sayi"])
            return

        secim = int(secim)
        if 1 <= secim <= len(satirlar):
            silinen = satirlar.pop(secim - 1)
            with open(dosya_yolu(f"{kullanici_adi}_gelir.txt"), "w", encoding="utf-8") as dosya:
                dosya.writelines(satirlar)
            print(dil_sözlugu["satir_silindi"].format(silinen=silinen.strip()))
        else:
            print(dil_sözlugu["secim_hata"])

    except FileNotFoundError:
        print(dil_sözlugu["gelir_yok"])

def gider_sil(kullanici_adi): 
    try:
        with open(dosya_yolu(f"{kullanici_adi}_gider.txt"), "r", encoding="utf-8") as dosya:
            satirlar = dosya.readlines()

        if not satirlar:
            print(dil_sözlugu["silinecek_gider_yok"])
            return

        giderleri_görüntüle(kullanici_adi)

        secim = input(dil_sözlugu["gider_sil_sec"])
        if not secim.isdigit():
            print(dil_sözlugu["gecersiz_sayi"])
            return

        secim = int(secim)
        if 1 <= secim <= len(satirlar):
            silinen = satirlar.pop(secim - 1)
            with open(dosya_yolu(f"{kullanici_adi}_gider.txt"), "w", encoding="utf-8") as dosya:
                dosya.writelines(satirlar)
            print(dil_sözlugu["satir_silindi"].format(silinen=silinen.strip()))
        else:
            print(dil_sözlugu["secim_hata"])

    except FileNotFoundError:
        print(dil_sözlugu["gider_yok"])

def kullanici_islemleri_sayfası(kullanici_adi):
    while True:
        print(dil_sözlugu["kullanici_islemleri"])
        print(dil_sözlugu["gelir_ekleme"])
        print(dil_sözlugu["gider_ekleme"])
        print(dil_sözlugu["bakiye_goruntule"])
        print(dil_sözlugu["gelir_gor"])
        print(dil_sözlugu["gider_gor"])
        print(dil_sözlugu["gelir_sil"])
        print(dil_sözlugu["gider_sil"])
        print(dil_sözlugu["ayar"])
        print(dil_sözlugu["geri"])
        secim = input(dil_sözlugu["secim_yap"])
        
        if secim == "1":
            gelir_ekle(kullanici_adi)
        elif secim == "2":
            gider_ekle(kullanici_adi)
        elif secim == "3":
            toplam_bakiye(kullanici_adi)
        elif secim == "4":
            gelirleri_görüntüle(kullanici_adi)
        elif secim == "5":
            giderleri_görüntüle(kullanici_adi)
        elif secim=="6":
            gelir_sil(kullanici_adi)
        elif secim =="7":
            gider_sil(kullanici_adi)
        elif secim == "8":            
            hesap_silindi_mi = ayarlar(kullanici_adi)
            if hesap_silindi_mi:
                break
        elif secim == "9":
            print(dil_sözlugu["ana_don"])
            break
        else:
            print(dil_sözlugu["secim_hata"])

def ana_sayfa():
    
    while True:
        print(dil_sözlugu["ana_sayfa"])
        print(dil_sözlugu["kayit_yap"])
        print(dil_sözlugu["giris_yap"])
        print(dil_sözlugu["cikis_yap"])
        try:
            secim = int(input(dil_sözlugu["secim_yap"]))
        except ValueError:
            print(dil_sözlugu["sayi_girin"])
            continue
        if secim == 1:
            kayit_ol()
        elif secim == 2:
            kullanici_adi = giris_yap()
            if kullanici_adi:
                kullanici_islemleri_sayfası(kullanici_adi)  
        elif secim == 3:
            print(dil_sözlugu["cikis"])
            break
        else:
            print(dil_sözlugu["secim_hata"])

ana_sayfa()