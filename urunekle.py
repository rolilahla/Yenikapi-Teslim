# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'urunekle.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from vtbgln import VbagKur
import mesajlar as mes

class Ui_UrunEkle(object):
    def __init__(self):
        self.yaz = VbagKur()

    def setupUi(self, UrunEkle):
        UrunEkle.setObjectName("UrunEkle")
        UrunEkle.resize(232, 212)
        self.label = QtWidgets.QLabel(UrunEkle)
        self.label.setGeometry(QtCore.QRect(10, 10, 71, 20))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(UrunEkle)
        self.comboBox.setGeometry(QtCore.QRect(90, 10, 120, 20))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(UrunEkle)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 71, 20))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(UrunEkle)
        self.lineEdit.setGeometry(QtCore.QRect(90, 40, 120, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(UrunEkle)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 70, 120, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(UrunEkle)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 71, 20))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(UrunEkle)
        self.lineEdit_3.setGeometry(QtCore.QRect(90, 100, 120, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(UrunEkle)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 71, 20))
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(UrunEkle)
        self.lineEdit_4.setGeometry(QtCore.QRect(90, 130, 120, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_5 = QtWidgets.QLabel(UrunEkle)
        self.label_5.setGeometry(QtCore.QRect(10, 130, 71, 20))
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(UrunEkle)
        self.pushButton.setGeometry(QtCore.QRect(140, 170, 72, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(UrunEkle)
        self.pushButton.clicked.connect(self.urekle)
        QtCore.QMetaObject.connectSlotsByName(UrunEkle)

    def urekle(self):
        self.yaz.dolum_ekle(self.lineEdit_4.text(),
                            self.comboBox.currentText(),
                            self.lineEdit.text(),
                            self.lineEdit_2.text(),
                            self.lineEdit_3.text()
                            )
        mesaj = self.lineEdit_4.text() + " tarihinde yüklenen " + self.lineEdit.text() + " litre " + \
                self.comboBox.currentText() + " veritabanı stoğuna kaydedilmiştir "
        mes.uyari(mesaj, "Bilgilendirme")

        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()

    def retranslateUi(self, UrunEkle):
        _translate = QtCore.QCoreApplication.translate
        UrunEkle.setWindowTitle(_translate("UrunEkle", "Ürün Ekle"))
        self.label.setText(_translate("UrunEkle", "Ürün Adı"))
        self.comboBox.setItemText(0, _translate("UrunEkle", "MOTORİN"))
        self.comboBox.setItemText(1, _translate("UrunEkle", "RME 180"))
        self.comboBox.setItemText(2, _translate("UrunEkle", "RMG 380"))
        self.label_2.setText(_translate("UrunEkle", "Litre"))
        self.label_3.setText(_translate("UrunEkle", "Kilogram"))
        self.label_4.setText(_translate("UrunEkle", "Yoğunluk"))
        self.label_5.setText(_translate("UrunEkle", "Yükleme Tarihi"))
        self.pushButton.setText(_translate("UrunEkle", "Ekle"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UrunEkle = QtWidgets.QDialog()
    ui = Ui_UrunEkle()
    ui.setupUi(UrunEkle)
    UrunEkle.show()
    sys.exit(app.exec_())

