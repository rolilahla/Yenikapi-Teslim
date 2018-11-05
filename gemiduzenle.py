# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gemiduzenle.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from vtbgln import VbagKur
import mesajlar as mes

class Ui_GemiBilgisiDuzenle(object):
    def __init__(self):
        self.yaz = VbagKur()

    def setupUi(self, GemiBilgisiDuzenle):
        GemiBilgisiDuzenle.setObjectName("GemiBilgisiDuzenle")
        GemiBilgisiDuzenle.resize(357, 362)
        self.label_2 = QtWidgets.QLabel(GemiBilgisiDuzenle)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 68, 20))
        self.label_2.setObjectName("label_2")
        self.label_7 = QtWidgets.QLabel(GemiBilgisiDuzenle)
        self.label_7.setGeometry(QtCore.QRect(10, 190, 68, 20))
        self.label_7.setObjectName("label_7")
        self.label_5 = QtWidgets.QLabel(GemiBilgisiDuzenle)
        self.label_5.setGeometry(QtCore.QRect(10, 130, 68, 20))
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(GemiBilgisiDuzenle)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 68, 20))
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(GemiBilgisiDuzenle)
        self.label.setGeometry(QtCore.QRect(10, 10, 68, 20))
        self.label.setObjectName("label")
        self.label_10 = QtWidgets.QLabel(GemiBilgisiDuzenle)
        self.label_10.setGeometry(QtCore.QRect(10, 280, 68, 20))
        self.label_10.setObjectName("label_10")
        self.label_3 = QtWidgets.QLabel(GemiBilgisiDuzenle)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 68, 20))
        self.label_3.setObjectName("label_3")
        self.label_8 = QtWidgets.QLabel(GemiBilgisiDuzenle)
        self.label_8.setGeometry(QtCore.QRect(10, 220, 91, 20))
        self.label_8.setObjectName("label_8")
        self.label_6 = QtWidgets.QLabel(GemiBilgisiDuzenle)
        self.label_6.setGeometry(QtCore.QRect(10, 160, 68, 20))
        self.label_6.setObjectName("label_6")
        self.label_9 = QtWidgets.QLabel(GemiBilgisiDuzenle)
        self.label_9.setGeometry(QtCore.QRect(10, 250, 68, 20))
        self.label_9.setObjectName("label_9")
        self.lineEdit = QtWidgets.QLineEdit(GemiBilgisiDuzenle)
        self.lineEdit.setGeometry(QtCore.QRect(140, 10, 200, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox = QtWidgets.QComboBox(GemiBilgisiDuzenle)
        self.comboBox.setGeometry(QtCore.QRect(140, 40, 200, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.lineEdit_2 = QtWidgets.QLineEdit(GemiBilgisiDuzenle)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 70, 200, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(GemiBilgisiDuzenle)
        self.lineEdit_3.setGeometry(QtCore.QRect(140, 100, 200, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(GemiBilgisiDuzenle)
        self.lineEdit_4.setGeometry(QtCore.QRect(140, 130, 200, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(GemiBilgisiDuzenle)
        self.lineEdit_5.setGeometry(QtCore.QRect(140, 160, 200, 21))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(GemiBilgisiDuzenle)
        self.lineEdit_6.setGeometry(QtCore.QRect(140, 190, 200, 21))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(GemiBilgisiDuzenle)
        self.lineEdit_7.setGeometry(QtCore.QRect(140, 220, 200, 21))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(GemiBilgisiDuzenle)
        self.lineEdit_8.setGeometry(QtCore.QRect(140, 250, 200, 21))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(GemiBilgisiDuzenle)
        self.lineEdit_9.setGeometry(QtCore.QRect(140, 280, 200, 21))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.pushButton = QtWidgets.QPushButton(GemiBilgisiDuzenle)
        self.pushButton.setGeometry(QtCore.QRect(270, 320, 75, 23))
        self.pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton.setObjectName("pushButton")

        if self.comboBox.currentIndex() == 0:
            pass
        else:
            self.bilgi_bul()

        self.retranslateUi(GemiBilgisiDuzenle)
        self.lineEdit.returnPressed.connect(self.gemi_bul)
        #self.comboBox.currentIndexChanged['int'].connect(self.bilgi_bul)
        self.pushButton.clicked.connect(self.bilgi_guncelle)
        QtCore.QMetaObject.connectSlotsByName(GemiBilgisiDuzenle)

    def gemi_bul(self):
        sor = self.yaz.hepsini_oku("gad", "gemiler", "kod", self.lineEdit.text())
        for i in range(len(sor)):
            self.comboBox.addItem(sor[i][0])

    def bilgi_bul(self):
        sor = self.yaz.tek_oku("gemiler", "gad", self.comboBox.currentText())
        self.lineEdit_2.setText(sor[0][3])
        self.lineEdit_3.setText(sor[0][4])
        self.lineEdit_4.setText(sor[0][5])
        self.lineEdit_5.setText(sor[0][6])
        self.lineEdit_6.setText(sor[0][7])
        self.lineEdit_7.setText(sor[0][8])
        self.lineEdit_8.setText(sor[0][9])
        self.lineEdit_9.setText(sor[0][10])
        self.change_no = sor[0][0]

    def bilgi_guncelle(self):
        kod = self.lineEdit.text()
        ad = self.comboBox.currentText()
        gkod = self.lineEdit_2.text()
        cins = self.lineEdit_3.text()
        dno = self.lineEdit_4.text()
        bno = self.lineEdit_5.text()
        sno = self.lineEdit_6.text()
        imo = self.lineEdit_7.text()
        ac = self.lineEdit_8.text()
        actel = self.lineEdit_9.text()
        self.yaz.gemi_guncelle(kod, ad, gkod,
                               cins, dno, bno,
                               sno, imo, ac,
                               actel, self.change_no)
        mesaj = ad + "Gemisi'nin Bilgileri başarıyla değiştirildi"
        mes.uyari(mesaj, "Bilgilendirme")
        self.comboBox.setCurrentIndex(0)


    def retranslateUi(self, GemiBilgisiDuzenle):
        _translate = QtCore.QCoreApplication.translate
        GemiBilgisiDuzenle.setWindowTitle(_translate("GemiBilgisiDuzenle", "Gemi Bilgisi Düzenle"))
        self.label_2.setText(_translate("GemiBilgisiDuzenle", "Gemi Adı"))
        self.label_7.setText(_translate("GemiBilgisiDuzenle", "Sicil No"))
        self.label_5.setText(_translate("GemiBilgisiDuzenle", "Defter No"))
        self.label_4.setText(_translate("GemiBilgisiDuzenle", "Gemi Cinsi"))
        self.label.setText(_translate("GemiBilgisiDuzenle", "Müşteri Kodu"))
        self.label_10.setText(_translate("GemiBilgisiDuzenle", "Acenta Tel"))
        self.label_3.setText(_translate("GemiBilgisiDuzenle", "Gemi Kodu"))
        self.label_8.setText(_translate("GemiBilgisiDuzenle", "İmo / Çağrı İşareti"))
        self.label_6.setText(_translate("GemiBilgisiDuzenle", "Belge No"))
        self.label_9.setText(_translate("GemiBilgisiDuzenle", "Acenta"))
        self.comboBox.setItemText(0, _translate("GemiBilgisiDuzenle", "Gemi Seç"))
        self.pushButton.setText(_translate("GemiBilgisiDuzenle", "Güncelle"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GemiBilgisiDuzenle = QtWidgets.QDialog()
    ui = Ui_GemiBilgisiDuzenle()
    ui.setupUi(GemiBilgisiDuzenle)
    GemiBilgisiDuzenle.show()
    sys.exit(app.exec_())

