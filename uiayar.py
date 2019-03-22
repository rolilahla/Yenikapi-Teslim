# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from firmaolustur import Ui_Firmaolustur
from firmaguncelle import Ui_Firmaguncelle
from firmasil import Ui_Firmasil
from gemiekle import Ui_GemiEkle
from fg import Ui_Fg
from gemisil import Ui_GemiSil



from karttutanak import Ui_KrediKari


"""
    Teslimat ui dosyasını signal slot bağlantıları
    ----------------------------------------------
    
    self.retranslateUi(MainWindow)
    self.tabWidget.setCurrentIndex(0)
    self.pushButton.clicked.connect(MainWindow.setFocus)
    self.actionYeni_M_teri_Ekle.triggered.connect(ayar.Folustur)
    self.actionM_teri_Bilgisi_D_zenle.triggered.connect(ayar.Fguncelle)
    self.actionM_teri_Sil.triggered.connect(ayar.Fsil)
    self.actionYeni_Gemi_Ekle.triggered.connect(ayar.Gekle)
    self.actionGemi_Bilgisi_D_zenle.triggered.connect(ayar.Gduz)
    self.actionGemi_Sil.triggered.connect(ayar.Gsil)
    self.actionYeni_r_n_Ekle.triggered.connect(ayar.Uekle)
    self.action_r_n_D_zenle.triggered.connect(ayar.Ygun)
    self.actionPersonel_Ekle_3.triggered.connect(ayar.Perekle)
    self.actionPersonel_Sil_2.triggered.connect(ayar.Persil)
    QtCore.QMetaObject.connectSlotsByName(MainWindow)

"""

def Fguncelle(self):
    Firmaguncelle = QtWidgets.QDialog()
    ui = Ui_Firmaguncelle()
    ui.setupUi(Firmaguncelle)
    Firmaguncelle.show()
    Firmaguncelle.exec_()

def Folustur(self):
    Firmaolustur = QtWidgets.QDialog()
    ui = Ui_Firmaolustur()
    ui.setupUi(Firmaolustur)
    Firmaolustur.show()
    Firmaolustur.exec_()

def Fsil(self):
    Firmasil = QtWidgets.QDialog()
    ui = Ui_Firmasil()
    ui.setupUi(Firmasil)
    Firmasil.show()
    Firmasil.exec_()

def Gekle(self):
    GemiEkle = QtWidgets.QDialog()
    ui = Ui_GemiEkle()
    ui.setupUi(GemiEkle)
    GemiEkle.show()
    GemiEkle.exec()

def Gduz(self):
    Fg = QtWidgets.QDialog()
    ui = Ui_Fg()
    ui.setupUi(Fg)
    Fg.show()
    Fg.exec_()

def Gsil(self):
    GemiSil = QtWidgets.QDialog()
    ui = Ui_GemiSil()
    ui.setupUi(GemiSil)
    GemiSil.show()
    GemiSil.exec_()






def Kartut():
    KrediKari = QtWidgets.QDialog()
    ui = Ui_KrediKari()
    ui.setupUi(KrediKari)
    KrediKari.show()
    KrediKari.exec()
