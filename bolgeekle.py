# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bolgeekle.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import mesajlar as mes
from vtbgln import VbagKur

class Ui_BolgeEkle(QtWidgets.QDialog):
    signal = QtCore.pyqtSignal(int)

    def __init__(self):
        super(Ui_BolgeEkle, self).__init__()
        self.yaz = VbagKur()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("BolgeEkle")
        self.resize(366, 133)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/rolix/docky.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(10, -1, 100, 100))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/rolix/docky.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(140, 20, 60, 20))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(210, 20, 130, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 50, 130, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(140, 50, 60, 20))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(270, 90, 72, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi()
        self.pushButton.clicked.connect(self.ekle)
        QtCore.QMetaObject.connectSlotsByName(self)

    def ekle(self):
        self.yaz.bolge_ekle(self.lineEdit.text(),self.lineEdit_2.text())
        mesaj = self.lineEdit_2.text() + " Bölgesi Veritanına eklendi"
        mes.uyari(mesaj, "Bilgilendirme")
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.on_change_value(1)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("BolgeEkle", "Bölge Ekle"))
        self.label_2.setText(_translate("BolgeEkle", "Bölge Kodu"))
        self.label_3.setText(_translate("BolgeEkle", "Bölge Adı"))
        self.pushButton.setText(_translate("BolgeEkle", "Ekle"))

    def on_change_value(self, value):
        self.signal.emit(value)
import ic_rc

