# -*- coding:utf-8 -*-
# -*- coding:cp1254 -*-
# sys.path.append(r'/home/istihza/programlar') komutu ile bu modülü python yoluna ekleyebilirsin

import sqlite3
import os

class VbagKur(object):
    def __init__(self):
        dvyol = os.getcwd()+ "/lib/db/vice.sqlite"
        self.vt = sqlite3.connect(dvyol)
        self.im = self.vt.cursor()

    def teslimat_ekle(self, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15):
        self.im.execute("""INSERT INTO satis VALUES('%s', '%s', '%s', '%s', '%s',
         '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')
        """%(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15))
        self.vt.commit()
    
    def firma_ekle(self,a1,a2,a3,a4,a5,a6):
        self.im.execute("""INSERT INTO firmalar VALUES(null, '{}', '{}', '{}', '{}', '{}', '{}')
        """.format(a1,a2,a3,a4,a5,a6))
        self.vt.commit()

    def firma_guncelle(self,a1,a2,a3,a4,a5,a6,a7):
        self.im.execute("""UPDATE firmalar SET kod='{}',
            ad='{}',
            vergi_dairesi='{}',
            vergi_no='{}',
            tel='{}',
            adres='{}' WHERE id='{}'""".format(a1,a2,a3,a4,a5,a6,a7))
        self.vt.commit()

    """
    Kayıt Sil
    Parametrelere göre bir satırlık kayıt siler
    parametreler:
    
    :param  tablo (str) : Verinin silineceği tablo  
    :param  ref   (str) : Verinin silineceği tablodaki eşleştirme referansı  
    :param  deg   (str) : referans için gönderilen eşleştirme değeri
    :return None 
    """
    def kayit_sil(self, tablo, ref, deg):
        self.im.execute(""" DELETE FROM {} WHERE {} = '{}'""".format(tablo, ref, deg))
        self.vt.commit()

    def gemi_ekle(self, l):
        self.im.execute("""INSERT INTO gemiler VALUES(null, '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')
            """.format(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8],l[9]))
        self.vt.commit()

    def gemi_guncelle(self, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11):
        self.im.execute("""UPDATE gemiler SET kod='{}',
        gad='{}',
        gkod='{}',
        gcins='{}',
        defno='{}',
        belno='{}',
        sicno='{}',
        imo='{}',
        acenta='{}',
        actel='{}' WHERE id = '{}'""".format
           (a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11))
        self.vt.commit()

    #Tüm verileri çekme
    """
                Belli bir kritere göre toplam sonuç ve kritersiz gönderimde tüm sonuçları döker
                parametreler:
                - aranan : İstenilen bölümü çeker
                - tablo  : Arama yapılmak istenilen tablo 
                - Yer    : Where işleci için şart sütunu
                - İstenilen: Karşılaştırma verisi

            """
    def hepsini_oku(self, aranan=None, tablo = None, yer=None, istenilen=None):
        if istenilen == None:
            self.im.execute("SELECT * FROM {}".format(tablo))
            return self.im.fetchall()
        else:
            self.im.execute("SELECT {} FROM {} WHERE {} = '{}'".format(aranan, tablo, yer, istenilen))
            return self.im.fetchall()

    def kolon_oku(self, sutun, tablo):
        self.im.execute("SELECT {} FROM {}".format(sutun, tablo))
        return self.im.fetchall()

    """Tek Oku 
            Tek satırlık veri çeker

            :param  tablo    : Verinin aranacağı tablo
            :param  yer      : eşleştirme referansı
            :param  deger    : bulunmak istenen referans değeri
            :returns veriler : Liste içinde tek satır sonuçlarını tüp olarak döndürür
            """
    def tek_oku(self, tablo, yer, deger):
        self.im.execute("SELECT * FROM {} Where {} == '{}'".format(tablo, yer, deger))
        return self.im.fetchall()


    def veri_duzenle(self, demet: object) -> object:
        dizi = []
        for i in range(len(demet)):
            dizi.append(str(demet[i][0]))
        return dizi

    def density_duzenle(self, demet):
        dizi = []
        for i in range(len(demet)):
            a = list(demet[i])
            for im in range(len(a)):
                dizi.append(a[im])
        return dizi

    def dolum_ekle(self, tarih, tur, lt, kg, kesafet, beyan):
        self.im.execute("""INSERT INTO densitys VALUES(null,
         '{}',
          '{}',
           '{}',
            '{}',
            '{}', 0, 0,{})""".format(tarih, tur, lt, kg, kesafet, beyan))
        self.vt.commit()

    def yogunluk_gun(self, tarih, tur, lt, kg, yog, id_no):
        self.im.execute("""UPDATE densitys SET tarih = '{}',
        tur = '{}',
        litre = '{}',
        kg = '{}',
         kesafet = '{}' WHERE id = '{}'""".format(tarih, tur, lt, kg, yog, id_no))
        self.vt.commit()

    """
    Personel Ekle
    
    Gemi çalışanlarını personel tablosuna ekler
    Parametreler:
    :param      firma(int) :  Çalışanın Hangi Firmaya bağlı olduğu
    :param      ad   (text):  Çalışanın isim bilgisi
    :return     None
    """
    def personel_ekle(self, firma, ad):
        self.im.execute("INSERT INTO personel VALUES(null,'{}', '{}')".format(firma, ad))
        self.vt.commit()


    def bolge_ekle(self, kod, ad):
        self.im.execute("INSERT INTO bolge VALUES(null,'{}', '{}')".format(kod, ad))
        self.vt.commit()


    def yer_ekle(self, ad, kod):
        self.im.execute("INSERT INTO yer VALUES(null,'{}', '{}')".format(ad, kod))
        self.vt.commit()

    def coklu_tup_temizle(self, liste):
        bos_liste = []
        for i in range(len(liste)):
            bos_liste.append(liste[i][0])
        return bos_liste

    def kart_bilgisi_ekle(self, id, firma, gemi, litre, person):
        self.im.execute("INSERT INTO kart VALUES(null, firma, gemi, litre, yakitalan)".format(firma,
                                                                                              gemi, litre, person))
        self.vt.commit()

    """
    Satış Ekleme
    """
    def satis_ekle(self, tarih, kod, dan, mad, gad, gcins, irs, urn, densit, lit, kil, yer, sarf, teslmci, ode):
        self.im.execute("INSERT INTO satis VALUES(null, '{}', '{}', '{}', '{}', '{}', '{}', '{}',"
                        "'{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(tarih, kod, dan, mad, gad,
                                                                                 gcins, irs, urn, densit, lit,
                                                                                 kil, yer, sarf, teslmci, ode))
        self.vt.commit()

    def son_eleman(self, tablo):
        self.im.execute("select * from {} order by id  desc limit 1".format(tablo))
        return self.im.fetchall()

    def son_on_eleman(self):
        self.im.execute("select id,tar,gemi,cinsi,irsaliye,urun,dens,lit,kg,ver from satis order by id  desc limit 5")
        return self.im.fetchall()

    def urun_stok_tablo(self):
        self.im.execute("select tarih, tur, litre,kg,kesafet, satılan_litre, satılan_kg from densitys")
        return self.im.fetchall()


    def veritabanini_kapat(self):
        self.vt.close()
