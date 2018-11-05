# -*- coding:utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from untitled import Ui_MainWindow
import ic_rc
import mico as zoro
from mesajlar import uyari, kart_kullanim_soru


class MainWindow(QMainWindow,  Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.triggerfinger()
		self.hazirlik()
		self.son_on_satis()
		self.urun_stok()

		self.grafik_bilgi("MOTORİN")

	def hazirlik(self):
		""" Bölgeleri veritabanından çek"""
		self.ui.comboBox_8.addItems(zoro.bolge_hazirla())

		"""	Teslimatçıları listele	"""
		self.ui.comboBox_6.addItems(zoro.personel_hazirla("0"))

		"""	Gemi çalışanlarını Hazırla	"""
		self.ui.comboBox_7.addItems(zoro.personel_hazirla("1"))

		""" Varsayılan Ayarları Yükle """
		self.yakit_numune_siniri = zoro.tek_sonuc_cek("deger", "settingsler", "id", 1)
		harf = "D-"
		rakam = 545000
		self.ui.lineEdit_7.setText(harf + str(rakam))

	def tgemi(self):
		self.ui.comboBox_2.clear()
		self.ui.comboBox_2.addItems(zoro.gemi_listele(self.ui.lineEdit.text()))

	def tyogun(self):
		self.ui.comboBox_4.clear()
		self.ui.comboBox_4.addItems(zoro.yogunluk_listele(self.ui.comboBox_3.currentText()))

	def vcf_hesapla(self):
		sonuc = zoro.v_c_f(self.ui.comboBox_4.currentText(),
				   self.ui.lineEdit_2.text(),
				   self.ui.lineEdit_3.text())

		self.ui.lineEdit_4.setText(sonuc[0])
		self.ui.lineEdit_5.setText(sonuc[1])
		self.ui.lineEdit_6.setText(sonuc[2])

	def muhur_sina(self):
		if self.ui.lineEdit_5.text() == "":
			pass
		else:
			if float(self.ui.lineEdit_5.text()) < float(self.yakit_numune_siniri[0][0]):
				self.ui.label_17.hide()
				self.ui.label_18.hide()
				self.ui.lineEdit_12.hide()
				self.ui.lineEdit_13.hide()
			else:
				self.ui.label_17.show()
				self.ui.label_18.show()
				self.ui.lineEdit_12.show()
				self.ui.lineEdit_13.show()

	def yer_bul(self):
		self.ui.comboBox_9.clear()
		self.ui.comboBox_9.addItems(zoro.yer_hazirla(self.ui.comboBox_8.currentText()))

	def olustur(self):
		"""	Artık Veritabanına bilgileri eklemek için değişkenleri almaya başlamamız lazım	"""
		danisman = self.ui.comboBox.currentText()
		musteri_kodu = self.ui.lineEdit.text()
		gemi = self.ui.comboBox_2.currentText()
		yakit_turu =self.ui.comboBox_3.currentText()
		yogunluk = self.ui.comboBox_4.currentText()
		brut_litre = self.ui.lineEdit_2.text()
		sicaklik = self.ui.lineEdit_3.text()
		net_litre = self.ui.lineEdit_5.text()
		volum_correction = self.ui.lineEdit_4.text()
		kilogram = self.ui.lineEdit_6.text()
		irsaliye_no = self.ui.lineEdit_7.text()
		odeme_turu = self.ui.comboBox_5.currentText()
		teslimatci = self.ui.comboBox_6.currentText()
		yakit_alan_kisi = self.ui.lineEdit_8.text()
		gemici = self.ui.comboBox_7.currentText()
		bolge = self.ui.comboBox_8.currentText()
		yer = self.ui.comboBox_9.currentText()
		baslama_saati = self.ui.lineEdit_9.text()
		bitis_saati = self.ui.lineEdit_10.text()
		sarfiyat = self.ui.lineEdit_11.text()
		barge_numune_muhur = None
		gemi_numune_muhur = None

		if float(self.ui.lineEdit_5.text()) < float(self.yakit_numune_siniri[0][0]):
			pass
		else:
			barge_numune_muhur = self.ui.lineEdit_12.text()
			gemi_numune_muhur = self.ui.lineEdit_13.text()


		mesaj = gemi + " gemisine ait " + net_litre + \
				" litrelik teslimat bilgisi veritabanına eklendi. Teslimat dosyaları oluşturuluyor"
		uyari(mesaj, "Bilgilendirme")

		zoro.teslimat_hazirliği_yap(danisman ,musteri_kodu ,gemi, yakit_turu, yogunluk,
				   brut_litre, sicaklik , volum_correction, net_litre, kilogram,
				   irsaliye_no, odeme_turu, teslimatci, yakit_alan_kisi, gemici,
				   bolge, yer,
				   baslama_saati, bitis_saati, sarfiyat, barge_numune_muhur, gemi_numune_muhur)

		if odeme_turu == "AÇIK":
			pass
		else:
			if kart_kullanim_soru() == True:
				self.ui.tetikle_kart()
			else:
				pass


		self.ui.lineEdit.clear()
		self.ui.comboBox_2.clear()
		self.ui.comboBox_3.setCurrentIndex(0)
		self.ui.comboBox_4.clear()
		self.ui.lineEdit_2.clear()
		self.ui.lineEdit_3.clear()
		self.ui.lineEdit_5.clear()
		self.ui.lineEdit_4.clear()
		self.ui.lineEdit_6.clear()
		self.ui.lineEdit_7.clear()
		self.ui.lineEdit_8.clear()
		self.ui.lineEdit_9.clear()
		self.ui.lineEdit_10.clear()
		self.ui.lineEdit_11.clear()
		self.ui.lineEdit_12.clear()
		self.ui.lineEdit_13.clear()

	def son_on_satis(self):
		sonuc = zoro.son_on()
		self.ui.tableWidget.setRowCount(len(sonuc))
		satir = 0
		sutun = 0
		for i in range(len(sonuc)):
			for im in range(10):
				self.ui.tableWidget.setItem(satir, sutun, QTableWidgetItem("{}".format(sonuc[i][im])))
				sutun += 1
			sutun = 0
			satir += 1

	def urun_stok(self):
		sonuc = zoro.stok_urun()
		self.ui.tableWidget_2.setRowCount(len(sonuc))
		satir = 0
		sutun = 0
		for i in range(len(sonuc)):
			for im in range(len(sonuc[i])):
				self.ui.tableWidget_2.setItem(satir, sutun, QTableWidgetItem("{}".format(sonuc[i][im])))
				sutun += 1
			sutun = 0
			satir +=1

	def grafik_bilgi(self, yakit):
		sonuc = zoro.urun_grafik("litre, kg", yakit)
		yakit_litre = []
		yakit_kilo = []
		for i in range(len(sonuc)):
			yakit_litre.append(int(sonuc[i][0].replace(".", "")))
			yakit_kilo.append(int(sonuc[i][1].replace(".", "")))

		toplam_litre = 0
		for i in range(len(yakit_litre)):
			toplam_litre += yakit_litre[i]

		toplam_kilo = 0
		for i in range(len(yakit_kilo)):
			toplam_kilo += yakit_kilo[i]


		print("Toplam litre ", toplam_litre)
		print("Toplam Kilogram", toplam_kilo)



	def triggerfinger(self):
		self.ui.lineEdit.returnPressed.connect(self.tgemi)
		self.ui.comboBox_3.currentIndexChanged.connect(self.tyogun)
		self.ui.lineEdit_3.returnPressed.connect(self.vcf_hesapla)
		self.ui.lineEdit_5.textChanged.connect(self.muhur_sina)
		self.ui.comboBox_8.currentIndexChanged.connect(self.yer_bul)
		self.ui.pushButton.clicked.connect(self.olustur)



app = QApplication(sys.argv)
form = MainWindow()
form.show()
sys.exit(app.exec_())

