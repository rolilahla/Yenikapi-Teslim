# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from vtbgln import VbagKur
import math, time, os
from shutil import copy2
import xlwings as xw




t = time.strftime("%d %m %Y")
tar = t.replace(" ", ".")

yaz = VbagKur()

def gemi_listele(arg):
    return yaz.veri_duzenle(yaz.hepsini_oku("gad", "gemiler", "kod", arg))

def yogunluk_listele(arg):
    return yaz.veri_duzenle(yaz.hepsini_oku("kesafet", "densitys", "tur", arg))

def v_c_f(density, brut, sicaklik):
    if len(brut) == 3:
        sonuc_liste = []
        deger = (float(density) * 2000) / 2
        if int(deger) >= 839 & int(deger) <= 1075:
            sonuc = 186.9696 / (math.pow(deger, 2)) + 0.4862 / deger
        elif int(deger) >= 788 & (deger) <= 838.5:
            sonuc = 594.5418 / (math.pow(deger, 2))
        elif int(deger) >= 770.5 & int(deger) <= 787.5:
            sonuc = 2680.3206 / (math.pow(deger, 2)) - 0.00336312
        elif int(deger) >= 653 & int(deger) <= 770:
            sonuc = ((346.4228 / (math.pow(deger, 2)) + 0.4388 / deger) * math.pow(10, 7) + 0.5) / math.pow(10, 7)
        else:
            print("Bu işte bir yanlışlık var")

        a = sonuc - (2 * sonuc)
        b = a * (float(sicaklik) - 15) * (1 + 0.8 * a * (float(sicaklik) - 15))
        t54 = math.pow(math.e, b)
        t54d = format(t54, '.4f')
        net_litre = float(brut) * float(t54d)
        kilogram = net_litre * (float(density) - 0.0011)
        sonuc_liste.append(str(t54d))
        sonuc_liste.append(str(round(net_litre)))
        sonuc_liste.append(str(round(kilogram)))
        return sonuc_liste
    else:
        sonuc_liste = []
        deger = (float(density) * 2000) / 2
        if int(deger) >= 839 & int(deger) <= 1075:
            sonuc = 186.9696 / (math.pow(deger, 2)) + 0.4862 / deger
        elif int(deger) >= 788 & (deger) <= 838.5:
            sonuc = 594.5418 / (math.pow(deger, 2))
        elif int(deger) >= 770.5 & int(deger) <= 787.5:
            sonuc = 2680.3206 / (math.pow(deger, 2)) - 0.00336312
        elif int(deger) >= 653 & int(deger) <= 770:
            sonuc = ((346.4228 / (math.pow(deger, 2)) + 0.4388 / deger) * math.pow(10, 7) + 0.5) / math.pow(10, 7)
        else:
            print("Bu işte bir yanlışlık var")

        a = sonuc - (2 * sonuc)
        b = a * (float(sicaklik) - 15) * (1 + 0.8 * a * (float(sicaklik) - 15))
        t54 = math.pow(math.e, b)
        t54d = format(t54, '.4f')
        net_litre = float(brut) * float(t54d)
        kilogram = net_litre * (float(density) - 0.0011)
        sonuc_liste.append(str(t54d))
        sonuc_liste.append(str(format(net_litre, '.3f')))
        sonuc_liste.append(str(format(kilogram, '.3f')))
        return sonuc_liste


def bolge_hazirla():
    return yaz.veri_duzenle(yaz.kolon_oku("ad", "bolge"))


def yer_hazirla(argv):
    oku = yaz.veri_duzenle(yaz.hepsini_oku("kod", "bolge", "ad", argv))
    return yaz.veri_duzenle(yaz.hepsini_oku("ad", "yer", "kod", oku[0]))

def tek_sonuc_cek(ad, firmalar, kod, deger):
    return yaz.veri_duzenle(yaz.hepsini_oku(ad, firmalar, kod, deger)[0])

def personel_hazirla(firma):
    return yaz.veri_duzenle(yaz.hepsini_oku("ad", "personel", "firma", firma))


def teslimat_hazirliği_yap(danisman ,musteri_kodu ,gemi, yakit_turu, yogunluk,
				   brut_litre, sicaklik , volum_correction, net_litre, kilogram,
				   irsaliye_no, odeme_turu, teslimatci, yakit_alan_kisi, gemici,
				   bolge, yer,
				   baslama_saati, bitis_saati, sarfiyat, barge_numune_muhur, gemi_numune_muhur):

    """ Müşteri Bilgilerini Getir
    """
    musteri_info = yaz.tek_oku("firmalar", "kod", musteri_kodu)
    musteri_ad = musteri_info[0][2]
    musteri_vergid = musteri_info[0][3]
    musteri_vergin = musteri_info[0][4]
    musteri_tel = musteri_info[0][5]
    musteri_adres = musteri_info[0][6]

    """ Gemi Bilgilerini Getir 
    """
    gemi_info = yaz.tek_oku("gemiler", "gad", gemi)
    gemi_id = gemi_info[0][0]
    gemi_kod = gemi_info[0][3]
    gemi_cins = gemi_info[0][4]
    gemi_defterno = gemi_info[0][5]
    gemi_belgeno = gemi_info[0][6]
    gemi_sicilno = gemi_info[0][7]
    gemi_imo = gemi_info[0][8]
    gemi_acenta = gemi_info[0][9]
    gemi_acentatel = gemi_info[0][10]
    """ Yakıt Bilgilerini Ve Bölge Kodlarını Getir.
    """
    urun_info = yaz.tek_oku("urun", "ad", yakit_turu)
    urun_kod = urun_info[0][0]
    urun_infor = urun_info[0][2]

    #BÖLGE KODU
    bolge_info = yaz.hepsini_oku("kod", "bolge", "ad", bolge)
    bolge_kodu = bolge_info[0][0]

    # Kredi kartı ile Ödeme Durumu varsa sınama yapılıp, Kart Tutanak Penceresi AÇmvıljfsır
    if odeme_turu == "AÇIK":
        pass


    #mühürleri birleştir
    if barge_numune_muhur == None:
        muhur = ""
    else:
        muhur = barge_numune_muhur + " / " + gemi_numune_muhur


    #satış bilgilerini veritabanına yaz
    yaz.satis_ekle(tar, musteri_kodu, danisman,musteri_ad, gemi, gemi_cins, irsaliye_no, yakit_turu, yogunluk,
                   net_litre, kilogram, yer, sarfiyat, teslimatci, odeme_turu)


    irsaliye_yaz(musteri_kodu, musteri_ad, musteri_adres, musteri_vergid, musteri_vergin, tar, urun_kod,
                 urun_infor, yakit_turu, yogunluk, net_litre, kilogram, bolge_kodu, bolge, gemi_belgeno,
                 teslimatci, yakit_alan_kisi, gemi, gemi_kod, gemi_sicilno, gemi_cins, gemi_defterno, muhur)

    ek_bir_yaz(gemi, gemi_cins, gemi_imo, musteri_ad, yakit_alan_kisi, teslimatci, musteri_adres, musteri_tel, gemi_acenta,
               gemi_acentatel, bolge, baslama_saati, bitis_saati, yakit_turu, net_litre, kilogram, gemici)

    check_list_yaz(teslimatci, gemi, gemi_defterno, gemi_belgeno)


def irsaliye_yaz(kod, must, adres, vergi_dairesi, vergi_no, tar,urun_kodu,
                 urun_infor, urun, dens, litre, kg, yer_kodu, bolge, belge_no,
                 veren, alan, gemi, gemi_kodu, sicil, cins, defter_no, muhur):
    gemlover = gemi + " " + tar
    gem = gemlover.lower()
    ana_dizin = os.getcwd()
    irsaliye_yolu = "\\lib\\usefile\\irsaliye.xlsx"
    hedef_dizin = "C:\\viçe\\evraklar\\"
    kaynak = ana_dizin + irsaliye_yolu
    hedef = hedef_dizin + gem + ".xlsx"
    copy2(kaynak, hedef)

    wb = xw.Book(hedef)
    sht = wb.sheets['Sayfa1']
    sht.range('AB1').value = kod
    sht.range('AB2').value = must
    sht.range('AB3').value = adres
    sht.range('AB4').value = vergi_dairesi
    sht.range('AB5').value = vergi_no
    sht.range('AB6').value = tar
    sht.range('AB7').value = urun_kodu
    sht.range('AB8').value = urun_infor
    sht.range('AB9').value = urun
    sht.range('AB10').value = dens
    sht.range('AB11').value = str(litre).replace(",", "", 1)
    sht.range('AB12').value = str(kg).replace(",","", 1)
    sht.range('AB13').value = yer_kodu
    sht.range('AB14').value = bolge
    sht.range('AB16').value = belge_no
    sht.range('AB17').value = veren
    sht.range('AB18').value = alan
    sht.range('AB19').value = gemi
    sht.range('AB20').value = gemi_kodu
    sht.range('AB21').value = sicil
    sht.range('AB22').value = cins
    sht.range('AB23').value = defter_no
    sht.range('AB24').value = muhur

def ek_bir_yaz(gad, gcins, imo, firma, ceng, teslimatci, adres, ftel, acente, actel, mevki, basaat, bisaat,
               yakit, litre, kg, gemici):
    gemlover = "Opet Ek-1 " + gad.lower() + " " + tar
    gem = gemlover.lower()
    ana_dizin = os.getcwd()
    irsaliye_yolu = "\\lib\\usefile\\ekbir.xlsx"
    hedef_dizin = "C:\\viçe\\evraklar\\"
    kaynak = ana_dizin + irsaliye_yolu
    hedef = hedef_dizin + gem + ".xlsx"
    copy2(kaynak, hedef)

    wb = xw.Book(hedef)
    sht = wb.sheets['Sayfa1']
    sht.range('M1').value = gad
    sht.range('M2').value = gcins
    sht.range('M3').value = imo
    sht.range('M4').value = firma
    sht.range('M5').value = ceng
    sht.range('M6').value = teslimatci
    sht.range('M7').value = adres
    sht.range('M8').value = ftel
    sht.range('M9').value = acente
    sht.range('M10').value = actel
    sht.range('M11').value = mevki
    sht.range('M12').value = basaat
    sht.range('M13').value = bisaat
    sht.range('M14').value = yakit
    sht.range('M15').value = litre.replace(",", "", 1)
    sht.range('M16').value = kg.replace(",", "", 1)
    sht.range('M17').value = gemici

def check_list_yaz(teslimatci, gemi, defter_no, belge_no):
    gemlover = "Check List " + gemi
    gem = gemlover.lower()
    ana_dizin = os.getcwd()
    irsaliye_yolu = "\\lib\\usefile\\checklist.xlsx"
    hedef_dizin = "C:\\viçe\\evraklar\\"
    kaynak = ana_dizin + irsaliye_yolu
    hedef = hedef_dizin + gem + ".xlsx"
    copy2(kaynak, hedef)

    wb = xw.Book(hedef)
    sht = wb.sheets['Sayfa 1']
    sht.range('M1').value = teslimatci
    sht.range('M2').value = gemi
    sht.range('M3').value = defter_no
    sht.range('M4').value = belge_no

def son_on():
    return yaz.son_on_eleman()

def stok_urun():
    return yaz.urun_stok_tablo()

def urun_grafik(lkg, urun):
    return yaz.hepsini_oku(lkg, "densitys", "tur", urun)

