# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firmasil.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from vtbgln import VbagKur
import mesajlar as mes

class Ui_Firmasil(VbagKur):
    def __init__(self):
        self.yaz = VbagKur()

    def setupUi(self, Firmasil):
        Firmasil.setObjectName("Firmasil")
        Firmasil.resize(400, 300)
        self.label = QtWidgets.QLabel(Firmasil)
        self.label.setGeometry(QtCore.QRect(10, 10, 68, 20))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Firmasil)
        self.lineEdit.setGeometry(QtCore.QRect(90, 10, 291, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Firmasil)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 40, 291, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(Firmasil)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 68, 20))
        self.label_2.setObjectName("label_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Firmasil)
        self.lineEdit_3.setGeometry(QtCore.QRect(90, 70, 291, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(Firmasil)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 68, 20))
        self.label_3.setObjectName("label_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Firmasil)
        self.lineEdit_4.setGeometry(QtCore.QRect(90, 100, 291, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_4 = QtWidgets.QLabel(Firmasil)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 68, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Firmasil)
        self.label_5.setGeometry(QtCore.QRect(10, 130, 68, 20))
        self.label_5.setObjectName("label_5")
        self.lineEdit_5 = QtWidgets.QLineEdit(Firmasil)
        self.lineEdit_5.setGeometry(QtCore.QRect(90, 130, 291, 21))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_6 = QtWidgets.QLabel(Firmasil)
        self.label_6.setGeometry(QtCore.QRect(10, 160, 68, 20))
        self.label_6.setObjectName("label_6")
        self.textEdit = QtWidgets.QTextEdit(Firmasil)
        self.textEdit.setGeometry(QtCore.QRect(90, 170, 291, 81))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(Firmasil)
        self.pushButton.setGeometry(QtCore.QRect(310, 270, 75, 23))
        self.pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Firmasil)
        self.pushButton.clicked.connect(self.sil)
        self.lineEdit.returnPressed.connect(self.bilgibul)
        QtCore.QMetaObject.connectSlotsByName(Firmasil)

    def sil(self):
        kod = self.lineEdit.text()
        ad = self.lineEdit_2.text()

        self.yaz.kayit_sil("firmalar", "kod", kod)
        mesaj = ad + " Firmasının veritabanı kaydı başarıyla silindi"
        mes.uyari(mesaj, "Bilgilendirme")

        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.textEdit.clear()


    def bilgibul(self):
        if self.lineEdit.text() == "":
            pass
        else:
            veri = self.yaz.tek_oku("firmalar", "kod", self.lineEdit.text())
            self.lineEdit_2.setText(veri[0][2])
            self.lineEdit_3.setText(veri[0][3])
            self.lineEdit_4.setText(veri[0][4])
            self.lineEdit_5.setText(veri[0][5])
            self.textEdit.setPlainText(veri[0][6])



    def retranslateUi(self, Firmasil):
        _translate = QtCore.QCoreApplication.translate
        Firmasil.setWindowTitle(_translate("Firmasil", "Müşteri Sil"))
        self.label.setText(_translate("Firmasil", "Müşteri Kodu"))
        self.label_2.setText(_translate("Firmasil", "Müşteri Adı"))
        self.label_3.setText(_translate("Firmasil", "Vergi Dairesi"))
        self.label_4.setText(_translate("Firmasil", "Vergi No"))
        self.label_5.setText(_translate("Firmasil", "Telefon"))
        self.label_6.setText(_translate("Firmasil", "Adres"))
        self.pushButton.setText(_translate("Firmasil", "Sil"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Firmasil = QtWidgets.QDialog()
    ui = Ui_Firmasil()
    ui.setupUi(Firmasil)
    Firmasil.show()
    sys.exit(app.exec_())

