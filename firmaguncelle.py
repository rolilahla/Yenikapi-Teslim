# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firmaguncelle.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from vtbgln import VbagKur
import mesajlar as mes

class Ui_Firmaguncelle(VbagKur):
    def __init__(self):
        self.yaz = VbagKur()
        self.change_no = 0

    def setupUi(self, Firmaguncelle):
        Firmaguncelle.setObjectName("Firmaguncelle")
        Firmaguncelle.resize(398, 300)
        self.label_2 = QtWidgets.QLabel(Firmaguncelle)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 68, 20))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(Firmaguncelle)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 68, 20))
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(Firmaguncelle)
        self.label.setGeometry(QtCore.QRect(10, 10, 68, 20))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Firmaguncelle)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 68, 20))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(Firmaguncelle)
        self.label_5.setGeometry(QtCore.QRect(10, 160, 68, 20))
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(Firmaguncelle)
        self.lineEdit.setGeometry(QtCore.QRect(90, 10, 291, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Firmaguncelle)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 40, 291, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Firmaguncelle)
        self.lineEdit_3.setGeometry(QtCore.QRect(90, 70, 291, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Firmaguncelle)
        self.lineEdit_4.setGeometry(QtCore.QRect(90, 100, 291, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Firmaguncelle)
        self.lineEdit_5.setGeometry(QtCore.QRect(90, 130, 291, 21))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_6 = QtWidgets.QLabel(Firmaguncelle)
        self.label_6.setGeometry(QtCore.QRect(10, 130, 68, 20))
        self.label_6.setObjectName("label_6")
        self.textEdit = QtWidgets.QTextEdit(Firmaguncelle)
        self.textEdit.setGeometry(QtCore.QRect(90, 160, 291, 101))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(Firmaguncelle)
        self.pushButton.setGeometry(QtCore.QRect(310, 270, 75, 23))
        self.pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Firmaguncelle)
        self.lineEdit.returnPressed.connect(self.bilgibul)
        self.pushButton.clicked.connect(self.guncelle)
        QtCore.QMetaObject.connectSlotsByName(Firmaguncelle)

    def guncelle(self):
        kod = self.lineEdit.text()
        ad = self.lineEdit_2.text()
        vergidairesi = self.lineEdit_3.text()
        vergino = self.lineEdit_4.text()
        telefon = self.lineEdit_5.text()
        adres = self.textEdit.toPlainText()
        self.yaz.firma_guncelle(kod, ad, vergidairesi, vergino, telefon, adres, self.change_no)
        mesaj = ad + " Firmasının veritabanı kaydı başarıyla güncellendi"
        mes.uyari(mesaj, "Bilgilendirme")

        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.textEdit.clear()

        self.yaz.veritabanini_kapat()

    def bilgibul(self):
        if self.lineEdit.text() == "":
            pass
        else:
            veri = self.yaz.tek_oku("firmalar", "kod", self.lineEdit.text())
            self.lineEdit_2.setText(veri[0][2])
            self.lineEdit_3.setText(veri[0][3])
            self.lineEdit_4.setText(veri[0][4])
            self.lineEdit_5.setText(veri[0][5])
            self.textEdit.setPlainText(veri[0][6])
            self.change_no = veri[0][0]



    def retranslateUi(self, Firmaguncelle):
        _translate = QtCore.QCoreApplication.translate
        Firmaguncelle.setWindowTitle(_translate("Firmaguncelle", "Müşteri Bilgisi Güncelle"))
        self.label_2.setText(_translate("Firmaguncelle", "Müşteri Adı"))
        self.label_4.setText(_translate("Firmaguncelle", "Vergi No"))
        self.label.setText(_translate("Firmaguncelle", "Müşteri Kodu"))
        self.label_3.setText(_translate("Firmaguncelle", "Vergi Dairesi"))
        self.label_5.setText(_translate("Firmaguncelle", "Adres"))
        self.label_6.setText(_translate("Firmaguncelle", "Telefon"))
        self.pushButton.setText(_translate("Firmaguncelle", "GÜNCELLE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Firmaguncelle = QtWidgets.QDialog()
    ui = Ui_Firmaguncelle()
    ui.setupUi(Firmaguncelle)
    Firmaguncelle.show()
    sys.exit(app.exec_())

