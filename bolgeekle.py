# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bolgeekle.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import mesajlar as mes
from vtbgln import VbagKur

class Ui_BolgeEkle(object):
    def __init__(self):
        self.yaz = VbagKur()

    def setupUi(self, BolgeEkle):
        BolgeEkle.setObjectName("BolgeEkle")
        BolgeEkle.resize(366, 133)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/rolix/docky.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        BolgeEkle.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(BolgeEkle)
        self.label.setGeometry(QtCore.QRect(10, -1, 100, 100))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/rolix/docky.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(BolgeEkle)
        self.label_2.setGeometry(QtCore.QRect(140, 20, 60, 20))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(BolgeEkle)
        self.lineEdit.setGeometry(QtCore.QRect(210, 20, 130, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(BolgeEkle)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 50, 130, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(BolgeEkle)
        self.label_3.setGeometry(QtCore.QRect(140, 50, 60, 20))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(BolgeEkle)
        self.pushButton.setGeometry(QtCore.QRect(270, 90, 72, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(BolgeEkle)
        self.pushButton.clicked.connect(self.ekle)
        QtCore.QMetaObject.connectSlotsByName(BolgeEkle)

    def ekle(self):
        self.yaz.bolge_ekle(self.lineEdit.text(),self.lineEdit_2.text())
        mesaj = self.lineEdit_2.text() + " Bölgesi Veritanına eklendi"
        mes.uyari(mesaj, "Bilgilendirme")
        self.lineEdit.clear()
        self.lineEdit_2.clear()


    def retranslateUi(self, BolgeEkle):
        _translate = QtCore.QCoreApplication.translate
        BolgeEkle.setWindowTitle(_translate("BolgeEkle", "Bölge Ekle"))
        self.label_2.setText(_translate("BolgeEkle", "Bölge Kodu"))
        self.label_3.setText(_translate("BolgeEkle", "Bölge Adı"))
        self.pushButton.setText(_translate("BolgeEkle", "Ekle"))

import ic_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BolgeEkle = QtWidgets.QDialog()
    ui = Ui_BolgeEkle()
    ui.setupUi(BolgeEkle)
    BolgeEkle.show()
    sys.exit(app.exec_())

