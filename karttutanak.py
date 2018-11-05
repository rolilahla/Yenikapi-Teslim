# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'karttutanak.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from shutil import copy2
from vtbgln import VbagKur
import os
import xlwings as xw

class Ui_KrediKari(object):
    def __init__(self):
        self.yaz = VbagKur()

    def setupUi(self, KrediKari):
        KrediKari.setObjectName("KrediKari")
        KrediKari.resize(723, 377)
        self.label = QtWidgets.QLabel(KrediKari)
        self.label.setGeometry(QtCore.QRect(9, 15, 35, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(KrediKari)
        self.lineEdit.setGeometry(QtCore.QRect(116, 15, 201, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(KrediKari)
        self.lineEdit_2.setGeometry(QtCore.QRect(116, 47, 201, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(KrediKari)
        self.label_2.setGeometry(QtCore.QRect(9, 47, 87, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(KrediKari)
        self.label_3.setGeometry(QtCore.QRect(9, 79, 89, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(KrediKari)
        self.lineEdit_3.setGeometry(QtCore.QRect(116, 79, 201, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(KrediKari)
        self.label_4.setGeometry(QtCore.QRect(9, 111, 26, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(KrediKari)
        self.lineEdit_4.setGeometry(QtCore.QRect(116, 111, 201, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_5 = QtWidgets.QLabel(KrediKari)
        self.label_5.setGeometry(QtCore.QRect(9, 143, 80, 16))
        self.label_5.setObjectName("label_5")
        self.lineEdit_5 = QtWidgets.QLineEdit(KrediKari)
        self.lineEdit_5.setGeometry(QtCore.QRect(116, 143, 201, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_6 = QtWidgets.QLabel(KrediKari)
        self.label_6.setGeometry(QtCore.QRect(9, 175, 47, 16))
        self.label_6.setObjectName("label_6")
        self.lineEdit_6 = QtWidgets.QLineEdit(KrediKari)
        self.lineEdit_6.setGeometry(QtCore.QRect(116, 175, 201, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(KrediKari)
        self.lineEdit_7.setGeometry(QtCore.QRect(116, 207, 201, 20))
        self.lineEdit_7.setText("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_7 = QtWidgets.QLabel(KrediKari)
        self.label_7.setGeometry(QtCore.QRect(9, 207, 94, 16))
        self.label_7.setObjectName("label_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(KrediKari)
        self.lineEdit_8.setGeometry(QtCore.QRect(116, 239, 201, 20))
        self.lineEdit_8.setText("")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_8 = QtWidgets.QLabel(KrediKari)
        self.label_8.setGeometry(QtCore.QRect(9, 303, 67, 16))
        self.label_8.setObjectName("label_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(KrediKari)
        self.lineEdit_9.setGeometry(QtCore.QRect(116, 304, 201, 20))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.pushButton = QtWidgets.QPushButton(KrediKari)
        self.pushButton.setGeometry(QtCore.QRect(230, 340, 82, 23))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(KrediKari)
        self.textEdit.setGeometry(QtCore.QRect(340, 15, 371, 311))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setFontPointSize(10.0)
        self.pushButton_2 = QtWidgets.QPushButton(KrediKari)
        self.pushButton_2.setGeometry(QtCore.QRect(635, 338, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_9 = QtWidgets.QLabel(KrediKari)
        self.label_9.setGeometry(QtCore.QRect(9, 239, 101, 16))
        self.label_9.setObjectName("label_9")
        self.line = QtWidgets.QFrame(KrediKari)
        self.line.setGeometry(QtCore.QRect(320, 15, 16, 346))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_10 = QtWidgets.QLabel(KrediKari)
        self.label_10.setGeometry(QtCore.QRect(9, 271, 67, 16))
        self.label_10.setObjectName("label_10")
        self.comboBox = QtWidgets.QComboBox(KrediKari)
        self.comboBox.setGeometry(QtCore.QRect(116, 271, 201, 20))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        #son eklenen kredi kartı verisini çek
        self.bilgileri_cek()


        self.retranslateUi(KrediKari)
        self.pushButton.clicked.connect(self.tutanak_tasarla)
        self.pushButton_2.clicked.connect(self.tatata)
        QtCore.QMetaObject.connectSlotsByName(KrediKari)

    def bilgileri_cek(self):
        self.bilgiler = self.yaz.son_eleman("satis")
        self.lineEdit.setText(self.bilgiler[0][4])  # Müşteri
        self.lineEdit_2.setText(self.bilgiler[0][5])  # gemi
        self.lineEdit_3.setText(self.bilgiler[0][10])  # litre

    def tutanak_tasarla(self):
        tutanak = """
                {} tarihinde {} 'a ait, {}  {} teknesine Viçe barcından {} litre {} aldım.Turarı olan {} TL'yi {} adına kayıtlı {} 'a ait {} ************ {} numaralı {} kredi kartı ile ödedim.

                Hesaba virman yapılmasını arz ederim.

                {} 
                """.format(self.bilgiler[0][1], self.lineEdit.text(), self.lineEdit_2.text(), self.bilgiler[0][6],
                           self.bilgiler[0][10], self.bilgiler[0][8],
                           self.lineEdit_4.text(), self.lineEdit_5.text(), self.lineEdit_6.text(),
                           self.lineEdit_7.text(), self.lineEdit_8.text(), self.comboBox.currentText(),
                           self.lineEdit_9.text())

        self.textEdit.setPlainText(tutanak)

    def tatata(self):
        gem = self.lineEdit_2.text() + " KART TUTANAK" + self.bilgiler[0][1]
        ana_dizin = os.getcwd()
        irsaliye_yolu = "\\lib\\usefile\\karttutanak.xlsx"
        hedef_dizin = "C:\\viçe\\evraklar\\"
        kaynak = ana_dizin + irsaliye_yolu
        hedef = hedef_dizin + gem + ".xlsx"
        copy2(kaynak, hedef)

        wb = xw.Book(hedef)
        sht = wb.sheets['Sayfa1']
        sht.range('A15').value = self.textEdit.toPlainText()



    def retranslateUi(self, KrediKari):
        _translate = QtCore.QCoreApplication.translate
        KrediKari.setWindowTitle(_translate("KrediKari", "Kredi Kartı Tutanak Bilgileri"))
        self.label.setText(_translate("KrediKari", "Müşteri"))
        self.label_2.setText(_translate("KrediKari", "Yakıt Alınan Tekne"))
        self.label_3.setText(_translate("KrediKari", "Alınan Yakıt Miktarı"))
        self.label_4.setText(_translate("KrediKari", "Tutar"))
        self.label_5.setText(_translate("KrediKari", "Kredi Kartı Sahibi"))
        self.label_6.setText(_translate("KrediKari", "Banka Adı"))
        self.label_7.setText(_translate("KrediKari", "Kart No İlk 4 Rakam"))
        self.label_8.setText(_translate("KrediKari", "Yakıtı Alan Kişi"))
        self.pushButton.setText(_translate("KrediKari", "Tutanak Hazırla"))
        self.pushButton_2.setText(_translate("KrediKari", "Dosyaya Yaz"))
        self.label_9.setText(_translate("KrediKari", "Kart No Son 4 Rakam"))
        self.label_10.setText(_translate("KrediKari", "Yakıtı Alan Kişi"))
        self.comboBox.setItemText(0, _translate("KrediKari", "Kart Türü Seç"))
        self.comboBox.setItemText(1, _translate("KrediKari", "VİSA"))
        self.comboBox.setItemText(2, _translate("KrediKari", "MASTER CARD"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    KrediKari = QtWidgets.QDialog()
    ui = Ui_KrediKari()
    ui.setupUi(KrediKari)
    KrediKari.show()
    sys.exit(app.exec_())

