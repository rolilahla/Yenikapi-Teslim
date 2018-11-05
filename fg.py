# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fg.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QStringListModel
import mesajlar as mes
from vtbgln import VbagKur


class Ui_Fg(object):
    def __init__(self):
        self.yaz = VbagKur()
        self.change_id = 0

    def setupUi(self, Fg):
        Fg.setObjectName("Fg")
        Fg.resize(518, 406)
        self.label = QtWidgets.QLabel(Fg)
        self.label.setGeometry(QtCore.QRect(10, 10, 100, 20))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Fg)
        self.lineEdit.setGeometry(QtCore.QRect(90, 10, 200, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Fg)
        self.pushButton.setGeometry(QtCore.QRect(320, 10, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(Fg)
        self.label_3.setGeometry(QtCore.QRect(210, 50, 68, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Fg)
        self.label_4.setGeometry(QtCore.QRect(210, 80, 68, 20))
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(Fg)
        self.label_7.setGeometry(QtCore.QRect(210, 170, 68, 20))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Fg)
        self.label_8.setGeometry(QtCore.QRect(210, 200, 91, 20))
        self.label_8.setObjectName("label_8")
        self.label_5 = QtWidgets.QLabel(Fg)
        self.label_5.setGeometry(QtCore.QRect(210, 110, 68, 20))
        self.label_5.setObjectName("label_5")
        self.label_10 = QtWidgets.QLabel(Fg)
        self.label_10.setGeometry(QtCore.QRect(210, 260, 68, 20))
        self.label_10.setObjectName("label_10")
        self.label_6 = QtWidgets.QLabel(Fg)
        self.label_6.setGeometry(QtCore.QRect(210, 140, 68, 20))
        self.label_6.setObjectName("label_6")
        self.label_9 = QtWidgets.QLabel(Fg)
        self.label_9.setGeometry(QtCore.QRect(210, 230, 68, 20))
        self.label_9.setObjectName("label_9")
        self.lineEdit_2 = QtWidgets.QLineEdit(Fg)
        self.lineEdit_2.setGeometry(QtCore.QRect(310, 50, 181, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Fg)
        self.lineEdit_3.setGeometry(QtCore.QRect(310, 80, 181, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Fg)
        self.lineEdit_4.setGeometry(QtCore.QRect(310, 110, 181, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Fg)
        self.lineEdit_5.setGeometry(QtCore.QRect(310, 140, 181, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(Fg)
        self.lineEdit_6.setGeometry(QtCore.QRect(310, 170, 181, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(Fg)
        self.lineEdit_7.setGeometry(QtCore.QRect(310, 200, 181, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(Fg)
        self.lineEdit_8.setGeometry(QtCore.QRect(310, 230, 181, 20))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(Fg)
        self.lineEdit_9.setGeometry(QtCore.QRect(310, 260, 181, 20))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.pushButton_2 = QtWidgets.QPushButton(Fg)
        self.pushButton_2.setGeometry(QtCore.QRect(420, 350, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Fg)
        self.pushButton_3.setGeometry(QtCore.QRect(150, 160, 41, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.listWidget = QtWidgets.QListWidget(Fg)
        self.listWidget.setGeometry(QtCore.QRect(10, 40, 131, 351))
        self.listWidget.setObjectName("listWidget")
        self.label_12 = QtWidgets.QLabel(Fg)
        self.label_12.setGeometry(QtCore.QRect(210, 290, 68, 20))
        self.label_12.setObjectName("label_12")
        self.lineEdit_10 = QtWidgets.QLineEdit(Fg)
        self.lineEdit_10.setGeometry(QtCore.QRect(310, 290, 181, 20))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_13 = QtWidgets.QLabel(Fg)
        self.label_13.setGeometry(QtCore.QRect(210, 320, 68, 20))
        self.label_13.setObjectName("label_13")
        self.lineEdit_11 = QtWidgets.QLineEdit(Fg)
        self.lineEdit_11.setGeometry(QtCore.QRect(310, 320, 181, 20))
        self.lineEdit_11.setObjectName("lineEdit_11")

        self.retranslateUi(Fg)
        self.pushButton.clicked.connect(self.gemi_bul)
        self.pushButton_3.clicked.connect(self.gemi_sec)
        self.pushButton_2.clicked.connect(self.guncelle)
        self.listWidget.itemDoubleClicked.connect(self.gemi_sec)
        QtCore.QMetaObject.connectSlotsByName(Fg)

    def gemi_bul(self):
        sor = self.yaz.hepsini_oku("gad", "gemiler", "kod", self.lineEdit.text())
        liste = []
        self.listWidget.clear()
        for i in range(len(sor)):
            self.listWidget.addItem(sor[i][0])

    def gemi_sec(self):
        soru = self.yaz.tek_oku("gemiler", "gad", self.listWidget.currentItem().text())
        self.lineEdit_2.setText(str(soru[0][1]))
        self.lineEdit_3.setText(soru[0][2])
        self.lineEdit_4.setText(soru[0][3])
        self.lineEdit_5.setText(soru[0][4])
        self.lineEdit_6.setText(soru[0][5])
        self.lineEdit_7.setText(soru[0][6])
        self.lineEdit_8.setText(soru[0][7])
        self.lineEdit_9.setText(soru[0][8])
        self.lineEdit_10.setText(soru[0][9])
        self.lineEdit_11.setText(soru[0][10])
        self.change_id = soru[0][0]

    def guncelle(self):
        self.yaz.gemi_guncelle(self.lineEdit_2.text(),
                               self.lineEdit_3.text(),
                               self.lineEdit_4.text(),
                               self.lineEdit_5.text(),
                               self.lineEdit_6.text(),
                               self.lineEdit_7.text(),
                               self.lineEdit_8.text(),
                               self.lineEdit_9.text(),
                               self.lineEdit_10.text(),
                               self.lineEdit_11.text(),
                               self.change_id
                               )
        mesaj = self.lineEdit_3.text() + " Gemisinin Kaydı Başarıyla Değiştirildi"
        mes.uyari(mesaj, "Bilgilendirme")
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()
        self.lineEdit_7.clear()
        self.lineEdit_8.clear()
        self.lineEdit_9.clear()
        self.lineEdit_10.clear()
        self.lineEdit_11.clear()
        self.listWidget.clear()
        self.gemi_bul()



    def retranslateUi(self, Fg):
        _translate = QtCore.QCoreApplication.translate
        Fg.setWindowTitle(_translate("Fg", "Gemi Bilgisi Düzenle"))
        self.label.setText(_translate("Fg", "Firma Kodu"))
        self.pushButton.setText(_translate("Fg", "Listele"))
        self.label_3.setText(_translate("Fg", "Müşteri"))
        self.label_4.setText(_translate("Fg", "Gemi Adı"))
        self.label_7.setText(_translate("Fg", "Defter No"))
        self.label_8.setText(_translate("Fg", "Belge No"))
        self.label_5.setText(_translate("Fg", "Gemi No"))
        self.label_10.setText(_translate("Fg", "İmo / Çağrı"))
        self.label_6.setText(_translate("Fg", "Gemi Cinsi"))
        self.label_9.setText(_translate("Fg", "Sicil No"))
        self.pushButton_2.setText(_translate("Fg", "Güncelle"))
        self.pushButton_3.setText(_translate("Fg", "Seç"))
        self.label_12.setText(_translate("Fg", "Acenta "))
        self.label_13.setText(_translate("Fg", "Acenta Tel"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Fg = QtWidgets.QDialog()
    ui = Ui_Fg()
    ui.setupUi(Fg)
    Fg.show()
    sys.exit(app.exec_())

