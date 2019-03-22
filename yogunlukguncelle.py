# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'yogunlukguncelle.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import mesajlar as mes
from vtbgln import VbagKur

class Ui_YogunlukGuncelle(object):
    def __init__(self):
        self.yaz = VbagKur()
        self.change_id_no = 0

    def setupUi(self, YogunlukGuncelle):
        YogunlukGuncelle.setObjectName("YogunlukGuncelle")
        YogunlukGuncelle.resize(671, 273)
        self.listWidget = QtWidgets.QListWidget(YogunlukGuncelle)
        self.listWidget.setGeometry(QtCore.QRect(10, 40, 411, 211))
        self.listWidget.setObjectName("listWidget")
        self.label = QtWidgets.QLabel(YogunlukGuncelle)
        self.label.setGeometry(QtCore.QRect(10, 10, 211, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(YogunlukGuncelle)
        self.label_2.setGeometry(QtCore.QRect(440, 40, 80, 20))
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(YogunlukGuncelle)
        self.comboBox.setGeometry(QtCore.QRect(540, 40, 120, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_3 = QtWidgets.QLabel(YogunlukGuncelle)
        self.label_3.setGeometry(QtCore.QRect(440, 70, 80, 20))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(YogunlukGuncelle)
        self.lineEdit.setGeometry(QtCore.QRect(540, 70, 120, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(YogunlukGuncelle)
        self.lineEdit_2.setGeometry(QtCore.QRect(540, 100, 120, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(YogunlukGuncelle)
        self.label_4.setGeometry(QtCore.QRect(440, 100, 80, 20))
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(YogunlukGuncelle)
        self.lineEdit_3.setGeometry(QtCore.QRect(540, 130, 120, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(YogunlukGuncelle)
        self.label_5.setGeometry(QtCore.QRect(440, 130, 80, 20))
        self.label_5.setObjectName("label_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(YogunlukGuncelle)
        self.lineEdit_4.setGeometry(QtCore.QRect(540, 160, 120, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_6 = QtWidgets.QLabel(YogunlukGuncelle)
        self.label_6.setGeometry(QtCore.QRect(440, 160, 80, 20))
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(YogunlukGuncelle)
        self.pushButton.setGeometry(QtCore.QRect(580, 210, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.yogunluk_listele()

        self.retranslateUi(YogunlukGuncelle)
        self.listWidget.itemDoubleClicked.connect(self.oyna)
        self.pushButton.clicked.connect(self.yguncelle)
        QtCore.QMetaObject.connectSlotsByName(YogunlukGuncelle)

    def yogunluk_listele(self):
        sonuc = self.yaz.density_duzenle(self.yaz.hepsini_oku("", "densitys"))
        sayac = 0
        for i in range(int(len(sonuc)/8)):
            a = str(sonuc[sayac]) + "   -->  " + \
                str(sonuc[sayac + 1]) + "   -->  " + \
                str(sonuc[sayac + 2]) + "   -->  " + \
                str(sonuc[sayac + 3]) + "   -->  " + \
                str(sonuc[sayac + 4]) + "   -->  " + \
                str(sonuc[sayac + 5]) + "   -->  " + \
            self.listWidget.addItem(a)
            sayac += 8

    def oyna(self):
        mersi = self.listWidget.currentItem().text()
        sayi = int((mersi[0:3]))
        sorgu = self.yaz.tek_oku("densitys", "id", sayi)
        self.comboBox.setCurrentText(sorgu[0][2])
        self.lineEdit.setText(sorgu[0][3])
        self.lineEdit_2.setText(sorgu[0][4])
        self.lineEdit_3.setText(sorgu[0][5])
        self.lineEdit_4.setText(sorgu[0][1])
        self.change_id_no = sorgu[0][0]

    def yguncelle(self):
        self.yaz.yogunluk_gun(self.lineEdit_4.text(),
                              self.comboBox.currentText(),
                              self.lineEdit.text(),
                              self.lineEdit_2.text(),
                              self.lineEdit_3.text(),
                              self.change_id_no)
        mes.uyari("Yoğunluk Bilgileri başarıyla veritabanına kaydedildi",
                  "Bilgilendirme")
        self.comboBox.clear()
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.listWidget.clear()

        self.yogunluk_listele()

    def retranslateUi(self, YogunlukGuncelle):
        _translate = QtCore.QCoreApplication.translate
        YogunlukGuncelle.setWindowTitle(_translate("YogunlukGuncelle", "Yoğunluk Güncelle"))
        self.label.setText(_translate("YogunlukGuncelle", "Stokta Bulunan Ürün Yoğunluklar"))
        self.label_2.setText(_translate("YogunlukGuncelle", "Ürün"))
        self.comboBox.setItemText(0, _translate("YogunlukGuncelle", "MOTORİN"))
        self.comboBox.setItemText(1, _translate("YogunlukGuncelle", "RME 180"))
        self.comboBox.setItemText(2, _translate("YogunlukGuncelle", "RMG 380"))
        self.label_3.setText(_translate("YogunlukGuncelle", "Litre"))
        self.label_4.setText(_translate("YogunlukGuncelle", "Kilogram"))
        self.label_5.setText(_translate("YogunlukGuncelle", "Yoğunluk"))
        self.label_6.setText(_translate("YogunlukGuncelle", "Yükleme Tarihi"))
        self.pushButton.setText(_translate("YogunlukGuncelle", "Güncelle"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    YogunlukGuncelle = QtWidgets.QDialog()
    ui = Ui_YogunlukGuncelle()
    ui.setupUi(YogunlukGuncelle)
    YogunlukGuncelle.show()
    sys.exit(app.exec_())

