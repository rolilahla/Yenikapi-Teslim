# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'personekle.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from vtbgln import VbagKur
import mesajlar as mes

class Ui_PersonelEkle(object):
    def __init__(self):
        self.yaz = VbagKur()

    def setupUi(self, PersonelEkle):
        PersonelEkle.setObjectName("PersonelEkle")
        PersonelEkle.resize(399, 148)
        self.label = QtWidgets.QLabel(PersonelEkle)
        self.label.setGeometry(QtCore.QRect(150, 20, 90, 20))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(PersonelEkle)
        self.comboBox.setGeometry(QtCore.QRect(270, 20, 100, 20))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.lineEdit = QtWidgets.QLineEdit(PersonelEkle)
        self.lineEdit.setGeometry(QtCore.QRect(270, 50, 100, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(PersonelEkle)
        self.label_2.setGeometry(QtCore.QRect(150, 50, 90, 20))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(PersonelEkle)
        self.pushButton.setGeometry(QtCore.QRect(300, 90, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(PersonelEkle)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 121, 121))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/rolix/config-users.png"))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(PersonelEkle)
        self.pushButton.clicked.connect(self.persekle)
        QtCore.QMetaObject.connectSlotsByName(PersonelEkle)

    def persekle(self):
        self.yaz.personel_ekle(self.comboBox.currentIndex(),
                               self.lineEdit.text())
        mesaj = self.lineEdit.text() + " "  + self.comboBox.currentText() +" çalışanı olarak veritabanına eklendi"
        mes.uyari(mesaj, "Bilgilendirme")
        self.lineEdit.clear()


    def retranslateUi(self, PersonelEkle):
        _translate = QtCore.QCoreApplication.translate
        PersonelEkle.setWindowTitle(_translate("PersonelEkle", "Personel Ekle"))
        self.label.setText(_translate("PersonelEkle", "Bağlı Olduğu Yer"))
        self.comboBox.setItemText(0, _translate("PersonelEkle", "İntertek"))
        self.comboBox.setItemText(1, _translate("PersonelEkle", "Gemi Adamı"))
        self.label_2.setText(_translate("PersonelEkle", "Ad Soyad"))
        self.pushButton.setText(_translate("PersonelEkle", "Ekle"))

import ic_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PersonelEkle = QtWidgets.QDialog()
    ui = Ui_PersonelEkle()
    ui.setupUi(PersonelEkle)
    PersonelEkle.show()
    sys.exit(app.exec_())

