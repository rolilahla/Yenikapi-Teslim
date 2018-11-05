# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firmaolustur.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from vtbgln import VbagKur
import mesajlar as mes

class Ui_Firmaolustur(VbagKur):
    def __init__(self):
        self.yaz = VbagKur()

    def setupUi(self, Firmaolustur):
        Firmaolustur.setObjectName("Firmaolustur")
        Firmaolustur.resize(400, 318)
        self.label = QtWidgets.QLabel(Firmaolustur)
        self.label.setGeometry(QtCore.QRect(16, 10, 68, 20))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Firmaolustur)
        self.lineEdit.setGeometry(QtCore.QRect(90, 10, 281, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Firmaolustur)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 40, 281, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(Firmaolustur)
        self.label_2.setGeometry(QtCore.QRect(16, 40, 68, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Firmaolustur)
        self.label_3.setGeometry(QtCore.QRect(16, 70, 68, 20))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(Firmaolustur)
        self.lineEdit_3.setGeometry(QtCore.QRect(90, 70, 281, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Firmaolustur)
        self.lineEdit_4.setGeometry(QtCore.QRect(90, 100, 281, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_4 = QtWidgets.QLabel(Firmaolustur)
        self.label_4.setGeometry(QtCore.QRect(16, 100, 68, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Firmaolustur)
        self.label_5.setGeometry(QtCore.QRect(16, 160, 68, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Firmaolustur)
        self.label_6.setGeometry(QtCore.QRect(16, 130, 68, 20))
        self.label_6.setObjectName("label_6")
        self.lineEdit_5 = QtWidgets.QLineEdit(Firmaolustur)
        self.lineEdit_5.setGeometry(QtCore.QRect(90, 130, 281, 20))
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.textEdit = QtWidgets.QTextEdit(Firmaolustur)
        self.textEdit.setGeometry(QtCore.QRect(90, 160, 281, 111))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(Firmaolustur)
        self.pushButton.setGeometry(QtCore.QRect(300, 280, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Firmaolustur)
        self.pushButton.clicked.connect(self.firmabilgisiyaz)
        QtCore.QMetaObject.connectSlotsByName(Firmaolustur)

    def firmabilgisiyaz(self):
        kod = self.lineEdit.text()
        ad = self.lineEdit_2.text()
        vergidairesi = self.lineEdit_3.text()
        vergino = self.lineEdit_4.text()
        telefon = self.lineEdit_5.text()
        adres = self.textEdit.toPlainText()
        self.yaz.firma_ekle(kod, ad, vergidairesi, vergino, telefon, adres)
        mesaj = ad + " Firmasının veritabanı kaydı başarıyla yapıldı"

        mes.uyari(mesaj, "Bilgilendirme")

        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.textEdit.clear()
        self.yaz.veritabanini_kapat()



    def retranslateUi(self, Firmaolustur):
        _translate = QtCore.QCoreApplication.translate
        Firmaolustur.setWindowTitle(_translate("Firmaolustur", "Firma Oluştur"))
        self.label.setText(_translate("Firmaolustur", "Müşteri Kodu"))
        self.label_2.setText(_translate("Firmaolustur", "Müşteri Adı"))
        self.label_3.setText(_translate("Firmaolustur", "Vergi Dairesi"))
        self.label_4.setText(_translate("Firmaolustur", "Vergi No"))
        self.label_5.setText(_translate("Firmaolustur", "Adres"))
        self.label_6.setText(_translate("Firmaolustur", "Telefon"))
        self.pushButton.setText(_translate("Firmaolustur", "OLUŞTUR"))



