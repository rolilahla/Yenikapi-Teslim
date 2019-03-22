# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'personekle.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from vtbgln import VbagKur
import mesajlar as mes

class Ui_PersonelEkle(QtWidgets.QDialog):
    signal = QtCore.pyqtSignal(int)

    def __init__(self):
        super(Ui_PersonelEkle, self).__init__()
        self.yaz = VbagKur()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("PersonelEkle")
        self.resize(399, 148)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(150, 20, 90, 20))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setGeometry(QtCore.QRect(270, 20, 100, 20))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(270, 50, 100, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(150, 50, 90, 20))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(300, 90, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 121, 121))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/rolix/config-users.png"))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")

        self.retranslateUi()
        self.pushButton.clicked.connect(self.persekle)
        QtCore.QMetaObject.connectSlotsByName(self)

    def persekle(self):
        if self.lineEdit.text() == "":
            pass # Hata kaydı eklenecek
        else:
            self.yaz.personel_ekle(self.comboBox.currentIndex(),
                               self.lineEdit.text())
            mesaj = self.lineEdit.text() + " "  + self.comboBox.currentText() +" çalışanı olarak veritabanına eklendi"
            mes.uyari(mesaj, "Bilgilendirme")
            self.lineEdit.clear()
            self.on_changed_value(1)


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("PersonelEkle", "Personel Ekle"))
        self.label.setText(_translate("PersonelEkle", "Bağlı Olduğu Yer"))
        self.comboBox.setItemText(0, _translate("PersonelEkle", "İntertek"))
        self.comboBox.setItemText(1, _translate("PersonelEkle", "Gemi Adamı"))
        self.label_2.setText(_translate("PersonelEkle", "Ad Soyad"))
        self.pushButton.setText(_translate("PersonelEkle", "Ekle"))

    def on_changed_value(self, value):
        self.signal.emit(value)

import ic_rc


