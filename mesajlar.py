# -*- coding:utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

def uyari(mesaj, baslik):
    inf = QMessageBox()
    inf.setIcon(QMessageBox.Information)
    inf.setWindowTitle(baslik)
    inf.setText(mesaj)
    inf.setStandardButtons(QMessageBox.Ok)
    inf.exec_()

def soru(gemi):
    dens_box = QMessageBox()
    dens_box.setIcon(QMessageBox.Question)
    dens_box.setWindowTitle('Kayıt Silme Uyarısı !!!')
    yazi = gemi + 'Bilgilerini veritabanından silmek istediğinize emin misiniz ?'
    dens_box.setText(yazi)
    dens_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    buttonY = dens_box.button(QMessageBox.Yes)
    buttonY.setText('EVET')
    buttonN = dens_box.button(QMessageBox.No)
    buttonN.setText('HAYIR')
    dens_box.exec_()
    if dens_box.clickedButton() == buttonY:
        mesaj = gemi + "Kaydı Başarı ile silindi"
        uyari(mesaj, "Bilgilendirme")
        return True
    else:
        mesaj = gemi + "Kaydını silme işlemi iptal edildi"
        uyari(mesaj, "Bilgilendirme")
        return False

def per_sil(ad):
    dens_box = QMessageBox()
    dens_box.setIcon(QMessageBox.Question)
    dens_box.setWindowTitle('Personel Silinsin mi ?')
    yazi = ad + ' adlı personelin kaydını veritabanından silmek istediğinize emin misiniz ?'
    dens_box.setText(yazi)
    dens_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    buttonY = dens_box.button(QMessageBox.Yes)
    buttonY.setText('Sil')
    buttonN = dens_box.button(QMessageBox.No)
    buttonN.setText('İptal')
    dens_box.exec_()
    if dens_box.clickedButton() == buttonY:
        mesaj = ad + ' adlı personelin kaydı veritabanından başarıyla silinmiştir'
        uyari(mesaj, "Bilgilendirme")
        return True
    else:
        mesaj = ad + ' adlı personelin kayıt silme işlemi iptal edilmiştir'
        uyari(mesaj, "Bilgilendirme")
        return False

def yerbolsil(gemi):
    dens_box = QMessageBox()
    dens_box.setIcon(QMessageBox.Question)
    dens_box.setWindowTitle('Kayıt Silme Uyarısı !!!')
    yazi = gemi + ' kaydını veritabanından silmek istediğinize emin misiniz ?'
    dens_box.setText(yazi)
    dens_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    buttonY = dens_box.button(QMessageBox.Yes)
    buttonY.setText('EVET')
    buttonN = dens_box.button(QMessageBox.No)
    buttonN.setText('HAYIR')
    dens_box.exec_()
    if dens_box.clickedButton() == buttonY:
        mesaj = gemi + " Kaydı Başarı ile silindi"
        uyari(mesaj, "Bilgilendirme")
        return True
    else:
        mesaj = gemi + " Kaydını silme işlemi iptal edildi"
        uyari(mesaj, "Bilgilendirme")
        return False

def kart_kullanim_soru():
    dens_box = QMessageBox()
    dens_box.setIcon(QMessageBox.Question)
    dens_box.setWindowTitle('Kredi Kartı Ödeme Seçeneği !!!')
    yazi = 'Kredi Kartı ile ödeme seçeneği seçildi.Eğer yakıt alan firma , ' \
           ' Kart sahibi ve yakıt alan kişi aynı değilse Tutanak hazırlanmalı.' \
           'Ödeme durumu için Kredi Kartı Tutanağı hazırlansın mı ?'
    dens_box.setText(yazi)
    dens_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    buttonY = dens_box.button(QMessageBox.Yes)
    buttonY.setText('EVET')
    buttonN = dens_box.button(QMessageBox.No)
    buttonN.setText('HAYIR')
    dens_box.exec_()
    if dens_box.clickedButton() == buttonY:
        return True
    else:
        return False