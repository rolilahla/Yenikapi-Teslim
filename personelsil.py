# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'personelsil.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from vtbgln import VbagKur
import mesajlar as mes

class Ui_PersonelSil(QtWidgets.QDialog):
    signal = QtCore.pyqtSignal(int)
    def __init__(self):
        super(Ui_PersonelSil, self).__init__()
        self.yaz = VbagKur()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("PersonelSil")
        self.resize(452, 197)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/rolix/dialog-error.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(10, 10, 121, 121))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/rolix/dialog-error.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(self)
        self.listWidget.setGeometry(QtCore.QRect(120, 10, 311, 141))
        self.listWidget.setObjectName("listWidget")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(360, 160, 73, 23))
        self.pushButton.setObjectName("pushButton")
        self.personel_bul()

        self.retranslateUi()
        self.pushButton.clicked.connect(self.perisil)
        self.listWidget.itemDoubleClicked['QListWidgetItem*'].connect(self.perisil)
        QtCore.QMetaObject.connectSlotsByName(self)

    def personel_bul(self):
        sorgu = self.yaz.kolon_oku("ad", "personel")
        for i in range(len(sorgu)):
            self.listWidget.addItem(sorgu[i][0])

    def perisil(self):
        if mes.per_sil(self.listWidget.currentItem().text()) == True:
            self.yaz.kayit_sil("personel", "ad", self.listWidget.currentItem().text())
            self.listWidget.clear()
            self.personel_bul()
            self.on_changed_value(1)
        else:
            pass


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("PersonelSil", "Personel Sil"))
        self.pushButton.setText(_translate("PersonelSil", "Sil"))

    def on_changed_value(self, value):
        self.signal.emit(value)

import ic_rc


