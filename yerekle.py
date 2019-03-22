# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'yerekle.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import mesajlar as mes
from vtbgln import VbagKur

class Ui_YerEkle(QtWidgets.QDialog):
    signal = QtCore.pyqtSignal(int)
    def __init__(self):
        super(Ui_YerEkle, self).__init__()
        self.yaz = VbagKur()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("YerEkle")
        self.resize(367, 140)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/rolix/docky.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(10, 10, 100, 100))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/rolix/docky.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(140, 20, 60, 20))
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setGeometry(QtCore.QRect(220, 20, 130, 22))
        self.comboBox.setObjectName("comboBox")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(140, 60, 60, 20))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(220, 60, 130, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(278, 95, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.bolge_listele()

        self.retranslateUi()
        self.pushButton.clicked.connect(self.yekle)
        QtCore.QMetaObject.connectSlotsByName(self)

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
        self.on_changed_value(2)


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("YerEkle", "Yer ekle"))
        self.label_2.setText(_translate("YerEkle", "Bölgesi"))
        self.label_3.setText(_translate("YerEkle", "Yer Adı"))
        self.pushButton.setText(_translate("YerEkle", "Ekle"))

    def on_changed_value(self, value):
        self.signal.emit(value)

import ic_rc


