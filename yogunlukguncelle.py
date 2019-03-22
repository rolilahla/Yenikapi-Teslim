# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'yogunlukguncelle.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import mesajlar
from vtbgln import VbagKur


class Ui_YogunlukGuncelle(QtWidgets.QDialog):
    clicked = QtCore.pyqtSignal(bool)

    def __init__(self):
        super(Ui_YogunlukGuncelle, self).__init__()
        self.yaz = VbagKur()
        self.change_id_no = 0
        self.setupUi()

    def setupUi(self):
        self.setObjectName("YogunlukGuncelle")
        self.resize(671, 273)
        self.listWidget = QtWidgets.QListWidget(self)
        self.listWidget.setGeometry(QtCore.QRect(10, 40, 411, 211))
        self.listWidget.setObjectName("listWidget")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(10, 10, 211, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(440, 40, 80, 20))
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setGeometry(QtCore.QRect(540, 40, 120, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(440, 70, 80, 20))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(540, 70, 120, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(540, 100, 120, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(440, 100, 80, 20))
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self)
        self.lineEdit_3.setGeometry(QtCore.QRect(540, 130, 120, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(440, 130, 80, 20))
        self.label_5.setObjectName("label_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(self)
        self.lineEdit_4.setGeometry(QtCore.QRect(540, 160, 120, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(440, 160, 80, 20))
        self.label_6.setObjectName("label_6")

        self.lineEdit_5 = QtWidgets.QLineEdit(self)
        self.lineEdit_5.setGeometry(QtCore.QRect(540, 190, 120, 20))
        self.lineEdit_5.setObjectName("lineEdit_4")
        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(440, 190, 80, 20))
        self.label_7.setObjectName("label_6")
        self.label_7.setText("Beyanname No")

        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(580, 220, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.yogunluk_listele()

        self.retranslateUi()
        self.listWidget.itemDoubleClicked.connect(self.oyna)
        self.pushButton.clicked.connect(self.yguncelle)
        QtCore.QMetaObject.connectSlotsByName(self)

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
                str(sonuc[sayac + 8]) + "   -->  "
            self.listWidget.addItem(a)
            sayac += 9

    def oyna(self):
        mersi = self.listWidget.currentItem().text()
        sayi = int((mersi[0:3]))
        sorgu = self.yaz.tek_oku("densitys", "id", sayi)
        self.comboBox.setCurrentText(sorgu[0][2])
        self.lineEdit.setText(sorgu[0][3])
        self.lineEdit_2.setText(sorgu[0][4])
        self.lineEdit_3.setText(sorgu[0][5])
        self.lineEdit_4.setText(sorgu[0][1])
        self.lineEdit_5.setText(str(sorgu[0][8]))
        self.change_id_no = sorgu[0][0]

    def yguncelle(self):
        self.yaz.yogunluk_gun(self.lineEdit_4.text(),
                              self.comboBox.currentText(),
                              self.lineEdit.text(),
                              self.lineEdit_2.text(),
                              self.lineEdit_3.text(),
                              self.change_id_no,
                              self.lineEdit_5.text())
        mesajlar.uyari("Yoğunluk Bilgileri başarıyla veritabanına kaydedildi",
                  "Bilgilendirme")
        self.comboBox.clear()
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.listWidget.clear()
        self.yogunluk_listele()
        self.on_changed_value(True)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("YogunlukGuncelle", "Yoğunluk Güncelle"))
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

    def on_changed_value(self, value):
        self.clicked.emit(value)