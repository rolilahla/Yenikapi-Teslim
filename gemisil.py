# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gemisil.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from vtbgln import VbagKur
import mesajlar as mes

class Ui_GemiSil(object):
    def __init__(self):
        self.yaz = VbagKur()

    def setupUi(self, GemiSil):
        GemiSil.setObjectName("GemiSil")
        GemiSil.resize(306, 349)
        self.label = QtWidgets.QLabel(GemiSil)
        self.label.setGeometry(QtCore.QRect(10, 10, 100, 20))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(GemiSil)
        self.lineEdit.setGeometry(QtCore.QRect(90, 10, 111, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(GemiSil)
        self.pushButton.setGeometry(QtCore.QRect(210, 10, 72, 23))
        self.pushButton.setObjectName("pushButton")
        self.listWidget = QtWidgets.QListWidget(GemiSil)
        self.listWidget.setGeometry(QtCore.QRect(10, 40, 271, 291))
        self.listWidget.setObjectName("listWidget")

        self.retranslateUi(GemiSil)
        self.pushButton.clicked.connect(self.gemi_bul)
        self.listWidget.itemDoubleClicked.connect(self.sil)
        QtCore.QMetaObject.connectSlotsByName(GemiSil)

    def gemi_bul(self):
        self.listWidget.clear()
        sor = self.yaz.hepsini_oku("gad", "gemiler", "kod", self.lineEdit.text())
        for i in range(len(sor)):
            self.listWidget.addItem(sor[i][0])

    def sil(self):
        if mes.soru(self.listWidget.currentItem().text()) == True:
            self.yaz.kayit_sil("gemiler", "gad", self.listWidget.currentItem().text())
            self.listWidget.clear()
            self.gemi_bul()
        else:
            pass


    def retranslateUi(self, GemiSil):
        _translate = QtCore.QCoreApplication.translate
        GemiSil.setWindowTitle(_translate("GemiSil", "Gemi Kaydı Sil"))
        self.label.setText(_translate("GemiSil", "Müşteri Kodu"))
        self.pushButton.setText(_translate("GemiSil", "Listele"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GemiSil = QtWidgets.QDialog()
    ui = Ui_GemiSil()
    ui.setupUi(GemiSil)
    GemiSil.show()
    sys.exit(app.exec_())

