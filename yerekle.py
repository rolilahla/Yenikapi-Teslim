# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'yerekle.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import mesajlar as mes
from vtbgln import VbagKur

class Ui_YerEkle(object):
    def __init__(self):
        self.yaz = VbagKur()

    def setupUi(self, YerEkle):
        YerEkle.setObjectName("YerEkle")
        YerEkle.resize(367, 140)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/rolix/docky.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        YerEkle.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(YerEkle)
        self.label.setGeometry(QtCore.QRect(10, 10, 100, 100))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/rolix/docky.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(YerEkle)
        self.label_2.setGeometry(QtCore.QRect(140, 20, 60, 20))
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(YerEkle)
        self.comboBox.setGeometry(QtCore.QRect(220, 20, 130, 22))
        self.comboBox.setObjectName("comboBox")
        self.label_3 = QtWidgets.QLabel(YerEkle)
        self.label_3.setGeometry(QtCore.QRect(140, 60, 60, 20))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(YerEkle)
        self.lineEdit.setGeometry(QtCore.QRect(220, 60, 130, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(YerEkle)
        self.pushButton.setGeometry(QtCore.QRect(278, 95, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.bolge_listele()

        self.retranslateUi(YerEkle)
        self.pushButton.clicked.connect(self.yekle)
        QtCore.QMetaObject.connectSlotsByName(YerEkle)

    def bolge_listele(self):
        soru = self.yaz.kolon_oku("ad", "bolge")
        sonuc = self.yaz.veri_duzenle(soru)
        for i in range(len(sonuc)):
            self.comboBox.addItem(sonuc[i])

    def yekle(self):
        b = self.comboBox.currentText()
        vtbolge = self.yaz.tek_oku("bolge", "ad", b)
        self.yaz.yer_ekle(self.lineEdit.text(), vtbolge[0][1])
        mesaj = self.lineEdit.text() + " veritabanına eklendi."
        mes.uyari(mesaj, "Bilgilendirme")
        self.lineEdit.clear()


    def retranslateUi(self, YerEkle):
        _translate = QtCore.QCoreApplication.translate
        YerEkle.setWindowTitle(_translate("YerEkle", "Yer ekle"))
        self.label_2.setText(_translate("YerEkle", "Bölgesi"))
        self.label_3.setText(_translate("YerEkle", "Yer Adı"))
        self.pushButton.setText(_translate("YerEkle", "Ekle"))

import ic_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    YerEkle = QtWidgets.QDialog()
    ui = Ui_YerEkle()
    ui.setupUi(YerEkle)
    YerEkle.show()
    sys.exit(app.exec_())

