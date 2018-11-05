# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bolgesil.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import mesajlar as mes
from vtbgln import VbagKur

class Ui_BolgeYerSil(object):
    def __init__(self):
        self.yaz = VbagKur()

    def setupUi(self, BolgeYerSil):
        BolgeYerSil.setObjectName("BolgeYerSil")
        BolgeYerSil.resize(632, 316)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/rolix/docky.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        BolgeYerSil.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(BolgeYerSil)
        self.label.setGeometry(QtCore.QRect(10, 10, 91, 61))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/rolix/scalable/package-remove.svg"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(BolgeYerSil)
        self.groupBox.setGeometry(QtCore.QRect(10, 80, 300, 225))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.listWidget = QtWidgets.QListWidget(self.groupBox)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_2.addWidget(self.listWidget, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(BolgeYerSil)
        self.groupBox_2.setGeometry(QtCore.QRect(320, 80, 300, 225))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.listWidget_2 = QtWidgets.QListWidget(self.groupBox_2)
        self.listWidget_2.setObjectName("listWidget_2")
        self.gridLayout.addWidget(self.listWidget_2, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(BolgeYerSil)
        self.label_2.setGeometry(QtCore.QRect(100, 10, 511, 51))
        self.label_2.setObjectName("label_2")
        self.bilgi_listele()

        self.retranslateUi(BolgeYerSil)
        self.listWidget.itemDoubleClicked.connect(self.silb)
        self.listWidget_2.itemDoubleClicked.connect(self.sily)
        QtCore.QMetaObject.connectSlotsByName(BolgeYerSil)

    def bilgi_listele(self):
        self.listWidget.addItems(self.yaz.coklu_tup_temizle(self.yaz.kolon_oku("ad", "bolge")))
        self.listWidget_2.addItems(self.yaz.coklu_tup_temizle(self.yaz.kolon_oku("ad", "yer")))


    def silb(self):
        if mes.yerbolsil(self.listWidget.currentItem().text()) == True:
            self.yaz.kayit_sil("bolge", "ad", self.listWidget.currentItem().text())
            self.listWidget.clear()
            self.listWidget_2.clear()
            self.bilgi_listele()
        else:
            pass


    def sily(self):
        if mes.yerbolsil(self.listWidget_2.currentItem().text()) == True:
            self.yaz.kayit_sil("yer", "ad", self.listWidget_2.currentItem().text())
            self.listWidget.clear()
            self.listWidget_2.clear()
            self.bilgi_listele()
        else:
            pass


    def retranslateUi(self, BolgeYerSil):
        _translate = QtCore.QCoreApplication.translate
        BolgeYerSil.setWindowTitle(_translate("BolgeYerSil", "Bölge Ve Yer Sil"))
        self.groupBox.setTitle(_translate("BolgeYerSil", "Bölge Listesi"))
        self.groupBox_2.setTitle(_translate("BolgeYerSil", "Yer Listesi"))
        self.label_2.setText(_translate("BolgeYerSil", "Veritabanından silmek istediğiniz Bölge veya Yer bilgisinin üzerine çift tıklayınız."))

import ic_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BolgeYerSil = QtWidgets.QDialog()
    ui = Ui_BolgeYerSil()
    ui.setupUi(BolgeYerSil)
    BolgeYerSil.show()
    sys.exit(app.exec_())

