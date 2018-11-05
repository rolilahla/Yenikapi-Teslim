# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'personelsil.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from vtbgln import VbagKur
import mesajlar as mes

class Ui_PersonelSil(object):
    def __init__(self):
        self.yaz = VbagKur()

    def setupUi(self, PersonelSil):
        PersonelSil.setObjectName("PersonelSil")
        PersonelSil.resize(452, 197)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/rolix/dialog-error.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PersonelSil.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(PersonelSil)
        self.label.setGeometry(QtCore.QRect(10, 10, 121, 121))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/rolix/dialog-error.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(PersonelSil)
        self.listWidget.setGeometry(QtCore.QRect(120, 10, 311, 141))
        self.listWidget.setObjectName("listWidget")
        self.pushButton = QtWidgets.QPushButton(PersonelSil)
        self.pushButton.setGeometry(QtCore.QRect(360, 160, 73, 23))
        self.pushButton.setObjectName("pushButton")
        self.personel_bul()

        self.retranslateUi(PersonelSil)
        self.pushButton.clicked.connect(self.perisil)
        self.listWidget.itemDoubleClicked['QListWidgetItem*'].connect(self.perisil)
        QtCore.QMetaObject.connectSlotsByName(PersonelSil)

    def personel_bul(self):
        sorgu = self.yaz.kolon_oku("ad", "personel")
        for i in range(len(sorgu)):
            self.listWidget.addItem(sorgu[i][0])

    def perisil(self):
        if mes.per_sil(self.listWidget.currentItem().text()) == True:
            self.yaz.kayit_sil("personel", "ad", self.listWidget.currentItem().text())
            self.listWidget.clear()
            self.personel_bul()
        else:
            pass


    def retranslateUi(self, PersonelSil):
        _translate = QtCore.QCoreApplication.translate
        PersonelSil.setWindowTitle(_translate("PersonelSil", "Personel Sil"))
        self.pushButton.setText(_translate("PersonelSil", "Sil"))

import ic_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PersonelSil = QtWidgets.QDialog()
    ui = Ui_PersonelSil()
    ui.setupUi(PersonelSil)
    PersonelSil.show()
    sys.exit(app.exec_())

