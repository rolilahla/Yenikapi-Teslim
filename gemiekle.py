# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gemiekle.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from vtbgln import VbagKur
import mesajlar as mes

class Ui_GemiEkle(VbagKur):
    def __init__(self):
        self.yaz = VbagKur()

    def setupUi(self, GemiEkle):
        GemiEkle.setObjectName("GemiEkle")
        GemiEkle.resize(358, 363)
        self.label = QtWidgets.QLabel(GemiEkle)
        self.label.setGeometry(QtCore.QRect(10, 10, 68, 20))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(GemiEkle)
        self.lineEdit.setGeometry(QtCore.QRect(140, 10, 200, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(GemiEkle)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 68, 20))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(GemiEkle)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 40, 200, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(GemiEkle)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 68, 20))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(GemiEkle)
        self.lineEdit_3.setGeometry(QtCore.QRect(140, 70, 200, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(GemiEkle)
        self.lineEdit_4.setGeometry(QtCore.QRect(140, 100, 200, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_4 = QtWidgets.QLabel(GemiEkle)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 68, 20))
        self.label_4.setObjectName("label_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(GemiEkle)
        self.lineEdit_5.setGeometry(QtCore.QRect(140, 130, 200, 21))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_5 = QtWidgets.QLabel(GemiEkle)
        self.label_5.setGeometry(QtCore.QRect(10, 130, 68, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(GemiEkle)
        self.label_6.setGeometry(QtCore.QRect(10, 160, 68, 20))
        self.label_6.setObjectName("label_6")
        self.lineEdit_6 = QtWidgets.QLineEdit(GemiEkle)
        self.lineEdit_6.setGeometry(QtCore.QRect(140, 160, 200, 21))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(GemiEkle)
        self.lineEdit_7.setGeometry(QtCore.QRect(140, 190, 200, 21))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_7 = QtWidgets.QLabel(GemiEkle)
        self.label_7.setGeometry(QtCore.QRect(10, 190, 68, 20))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(GemiEkle)
        self.label_8.setGeometry(QtCore.QRect(10, 220, 91, 20))
        self.label_8.setObjectName("label_8")
        self.lineEdit_8 = QtWidgets.QLineEdit(GemiEkle)
        self.lineEdit_8.setGeometry(QtCore.QRect(140, 220, 200, 21))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_9 = QtWidgets.QLabel(GemiEkle)
        self.label_9.setGeometry(QtCore.QRect(10, 250, 68, 20))
        self.label_9.setObjectName("label_9")
        self.lineEdit_9 = QtWidgets.QLineEdit(GemiEkle)
        self.lineEdit_9.setGeometry(QtCore.QRect(140, 250, 200, 21))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(GemiEkle)
        self.lineEdit_10.setGeometry(QtCore.QRect(140, 280, 200, 21))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_10 = QtWidgets.QLabel(GemiEkle)
        self.label_10.setGeometry(QtCore.QRect(10, 280, 68, 20))
        self.label_10.setObjectName("label_10")
        self.pushButton = QtWidgets.QPushButton(GemiEkle)
        self.pushButton.setGeometry(QtCore.QRect(270, 320, 75, 23))
        self.pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(GemiEkle)
        self.pushButton.clicked.connect(self.gekle)
        QtCore.QMetaObject.connectSlotsByName(GemiEkle)

    def gekle(self):
        if self.lineEdit.text() == "" and self.lineEdit_2.text() == "":
            pass
        else:
            liste = []
            liste.append(self.lineEdit.text())
            liste.append(self.lineEdit_2.text())
            liste.append(self.lineEdit_3.text())
            liste.append(self.lineEdit_4.text())
            liste.append(self.lineEdit_5.text())
            liste.append(self.lineEdit_6.text())
            liste.append(self.lineEdit_7.text())
            liste.append(self.lineEdit_8.text())
            liste.append(self.lineEdit_9.text())
            liste.append(self.lineEdit_10.text())

            self.yaz.gemi_ekle(liste)

            mesaj = self.lineEdit_2.text() + " gemisinin veritabanı kaydı başarıyla yapıldı"
            mes.uyari(mesaj, "Bilgilendirme")

            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.lineEdit_3.clear()
            self.lineEdit_4.clear()
            self.lineEdit_5.clear()
            self.lineEdit_6.clear()
            self.lineEdit_7.clear()
            self.lineEdit_8.clear()
            self.lineEdit_9.clear()
            self.lineEdit_10.clear()

            self.yaz.veritabanini_kapat()




    def retranslateUi(self, GemiEkle):
        _translate = QtCore.QCoreApplication.translate
        GemiEkle.setWindowTitle(_translate("GemiEkle", "Gemi Ekle"))
        self.label.setText(_translate("GemiEkle", "Müşteri Kodu"))
        self.label_2.setText(_translate("GemiEkle", "Gemi Adı"))
        self.label_3.setText(_translate("GemiEkle", "Gemi Kodu"))
        self.label_4.setText(_translate("GemiEkle", "Gemi Cinsi"))
        self.label_5.setText(_translate("GemiEkle", "Defter No"))
        self.label_6.setText(_translate("GemiEkle", "Belge No"))
        self.label_7.setText(_translate("GemiEkle", "Sicil No"))
        self.label_8.setText(_translate("GemiEkle", "İmo / Çağrı İşareti"))
        self.label_9.setText(_translate("GemiEkle", "Acenta"))
        self.label_10.setText(_translate("GemiEkle", "Acenta Tel"))
        self.pushButton.setText(_translate("GemiEkle", "Gemi Ekle"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GemiEkle = QtWidgets.QDialog()
    ui = Ui_GemiEkle()
    ui.setupUi(GemiEkle)
    GemiEkle.show()
    sys.exit(app.exec_())

