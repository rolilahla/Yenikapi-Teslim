# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import uiayar as ayar

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1318, 711)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/rolix/distributor-logo-archlinux.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.widget = QtWidgets.QWidget(self.tab)
        self.widget.setMaximumSize(QtCore.QSize(250, 16777215))
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(6, 6, 6, 6)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_14 = QtWidgets.QLabel(self.widget)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_2.addWidget(self.comboBox, 0, 1, 1, 2)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 1, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.widget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout_2.addWidget(self.comboBox_2, 2, 1, 1, 2)
        self.label_27 = QtWidgets.QLabel(self.widget)
        self.label_27.setObjectName("label_27")
        self.gridLayout_2.addWidget(self.label_27, 3, 0, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.widget)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_3, 3, 1, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 4, 0, 1, 1)
        self.comboBox_4 = QtWidgets.QComboBox(self.widget)
        self.comboBox_4.setObjectName("comboBox_4")
        self.gridLayout_2.addWidget(self.comboBox_4, 4, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 5, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 5, 1, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 6, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_2.addWidget(self.lineEdit_3, 6, 1, 1, 2)
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 7, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_2.addWidget(self.lineEdit_4, 7, 1, 1, 2)
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 8, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_2.addWidget(self.lineEdit_5, 8, 1, 1, 2)
        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 9, 0, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_2.addWidget(self.lineEdit_6, 9, 1, 1, 2)
        self.label_15 = QtWidgets.QLabel(self.widget)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 10, 0, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout_2.addWidget(self.lineEdit_7, 10, 1, 1, 2)
        self.label_16 = QtWidgets.QLabel(self.widget)
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 11, 0, 1, 1)
        self.comboBox_5 = QtWidgets.QComboBox(self.widget)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_5, 11, 1, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 12, 0, 1, 1)
        self.comboBox_6 = QtWidgets.QComboBox(self.widget)
        self.comboBox_6.setObjectName("comboBox_6")
        self.gridLayout_2.addWidget(self.comboBox_6, 12, 1, 1, 2)
        self.label_28 = QtWidgets.QLabel(self.widget)
        self.label_28.setObjectName("label_28")
        self.gridLayout_2.addWidget(self.label_28, 13, 0, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout_2.addWidget(self.lineEdit_8, 13, 1, 1, 2)
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 14, 0, 1, 1)
        self.comboBox_7 = QtWidgets.QComboBox(self.widget)
        self.comboBox_7.setObjectName("comboBox_7")
        self.gridLayout_2.addWidget(self.comboBox_7, 14, 1, 1, 2)
        self.label_11 = QtWidgets.QLabel(self.widget)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 15, 0, 1, 1)
        self.comboBox_8 = QtWidgets.QComboBox(self.widget)
        self.comboBox_8.setObjectName("comboBox_8")
        self.gridLayout_2.addWidget(self.comboBox_8, 15, 1, 1, 2)
        self.comboBox_9 = QtWidgets.QComboBox(self.widget)
        self.comboBox_9.setObjectName("comboBox_9")
        self.gridLayout_2.addWidget(self.comboBox_9, 16, 1, 1, 2)
        self.label_29 = QtWidgets.QLabel(self.widget)
        self.label_29.setObjectName("label_29")
        self.gridLayout_2.addWidget(self.label_29, 17, 0, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout_2.addWidget(self.lineEdit_9, 17, 1, 1, 2)
        self.label_30 = QtWidgets.QLabel(self.widget)
        self.label_30.setObjectName("label_30")
        self.gridLayout_2.addWidget(self.label_30, 18, 0, 1, 1)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout_2.addWidget(self.lineEdit_10, 18, 1, 1, 2)
        self.label_13 = QtWidgets.QLabel(self.widget)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 19, 0, 1, 1)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout_2.addWidget(self.lineEdit_11, 19, 1, 1, 2)
        self.label_17 = QtWidgets.QLabel(self.widget)
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 20, 0, 1, 1)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.gridLayout_2.addWidget(self.lineEdit_12, 20, 1, 1, 2)
        self.label_18 = QtWidgets.QLabel(self.widget)
        self.label_18.setObjectName("label_18")
        self.gridLayout_2.addWidget(self.label_18, 21, 0, 1, 1)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.gridLayout_2.addWidget(self.lineEdit_13, 21, 1, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(123, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 22, 0, 1, 2)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 22, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.widget)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 16, 0, 1, 1)
        self.gridLayout_6.addWidget(self.widget, 0, 0, 3, 1)
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setMinimumSize(QtCore.QSize(960, 192))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 200))
        self.groupBox.setToolTipDuration(1)
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_4.setContentsMargins(-1, 3, -1, -1)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setMinimumSize(QtCore.QSize(811, 188))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        self.gridLayout_4.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox, 0, 1, 1, 2)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setContentsMargins(-1, 3, -1, -1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.groupBox_2)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(7)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, item)
        self.gridLayout_3.addWidget(self.tableWidget_2, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox_2, 1, 1, 1, 2)
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_4.setObjectName("groupBox_4")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 20, 211, 186))
        self.groupBox_5.setObjectName("groupBox_5")
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_5)
        self.progressBar.setGeometry(QtCore.QRect(10, 20, 191, 121))
        self.progressBar.setProperty("value", 23)
        self.progressBar.setOrientation(QtCore.Qt.Vertical)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.label_19 = QtWidgets.QLabel(self.groupBox_5)
        self.label_19.setGeometry(QtCore.QRect(20, 150, 171, 20))
        self.label_19.setObjectName("label_19")
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_6.setGeometry(QtCore.QRect(230, 20, 231, 186))
        self.groupBox_6.setObjectName("groupBox_6")
        self.progressBar_2 = QtWidgets.QProgressBar(self.groupBox_6)
        self.progressBar_2.setGeometry(QtCore.QRect(20, 20, 191, 121))
        self.progressBar_2.setProperty("value", 90)
        self.progressBar_2.setTextVisible(True)
        self.progressBar_2.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_2.setInvertedAppearance(False)
        self.progressBar_2.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.progressBar_2.setObjectName("progressBar_2")
        self.label_21 = QtWidgets.QLabel(self.groupBox_6)
        self.label_21.setGeometry(QtCore.QRect(20, 150, 191, 20))
        self.label_21.setObjectName("label_21")
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_7.setGeometry(QtCore.QRect(470, 20, 231, 186))
        self.groupBox_7.setObjectName("groupBox_7")
        self.progressBar_3 = QtWidgets.QProgressBar(self.groupBox_7)
        self.progressBar_3.setGeometry(QtCore.QRect(10, 20, 191, 121))
        self.progressBar_3.setProperty("value", 90)
        self.progressBar_3.setTextVisible(True)
        self.progressBar_3.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_3.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.progressBar_3.setObjectName("progressBar_3")
        self.label_23 = QtWidgets.QLabel(self.groupBox_7)
        self.label_23.setGeometry(QtCore.QRect(16, 150, 191, 20))
        self.label_23.setObjectName("label_23")
        self.gridLayout_6.addWidget(self.groupBox_4, 2, 1, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_3.setMinimumSize(QtCore.QSize(306, 213))
        self.groupBox_3.setMaximumSize(QtCore.QSize(306, 213))
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.listWidget = QtWidgets.QListWidget(self.groupBox_3)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_5.addWidget(self.listWidget, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox_3, 2, 2, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1318, 21))
        self.menubar.setObjectName("menubar")
        self.menuM_teriler = QtWidgets.QMenu(self.menubar)
        self.menuM_teriler.setObjectName("menuM_teriler")
        self.menuGemiler = QtWidgets.QMenu(self.menubar)
        self.menuGemiler.setObjectName("menuGemiler")
        self.menuRaporlama = QtWidgets.QMenu(self.menubar)
        self.menuRaporlama.setObjectName("menuRaporlama")
        self.menuDolum_Bilgileri = QtWidgets.QMenu(self.menubar)
        self.menuDolum_Bilgileri.setObjectName("menuDolum_Bilgileri")
        self.menuB_lgeler = QtWidgets.QMenu(self.menubar)
        self.menuB_lgeler.setObjectName("menuB_lgeler")
        self.menuPersonel_Bilgileri = QtWidgets.QMenu(self.menubar)
        self.menuPersonel_Bilgileri.setObjectName("menuPersonel_Bilgileri")
        self.menuAyarlar = QtWidgets.QMenu(self.menubar)
        self.menuAyarlar.setObjectName("menuAyarlar")
        self.menuNotlar = QtWidgets.QMenu(self.menubar)
        self.menuNotlar.setObjectName("menuNotlar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionYeni_M_teri_Ekle = QtWidgets.QAction(MainWindow)
        self.actionYeni_M_teri_Ekle.setObjectName("actionYeni_M_teri_Ekle")
        self.actionM_teri_Bilgisi_D_zenle = QtWidgets.QAction(MainWindow)
        self.actionM_teri_Bilgisi_D_zenle.setObjectName("actionM_teri_Bilgisi_D_zenle")
        self.actionYeni_Gemi_Ekle = QtWidgets.QAction(MainWindow)
        self.actionYeni_Gemi_Ekle.setObjectName("actionYeni_Gemi_Ekle")
        self.actionGemi_Bilgisi_D_zenle = QtWidgets.QAction(MainWindow)
        self.actionGemi_Bilgisi_D_zenle.setObjectName("actionGemi_Bilgisi_D_zenle")
        self.actionGemi_Sil = QtWidgets.QAction(MainWindow)
        self.actionGemi_Sil.setObjectName("actionGemi_Sil")
        self.actionM_teri_Sil = QtWidgets.QAction(MainWindow)
        self.actionM_teri_Sil.setObjectName("actionM_teri_Sil")
        self.actionSat_Raporu_G_nl_k = QtWidgets.QAction(MainWindow)
        self.actionSat_Raporu_G_nl_k.setObjectName("actionSat_Raporu_G_nl_k")
        self.actionG_mr_k_Kapan_Listesi = QtWidgets.QAction(MainWindow)
        self.actionG_mr_k_Kapan_Listesi.setObjectName("actionG_mr_k_Kapan_Listesi")
        self.actionAyl_k_Sarfiyat = QtWidgets.QAction(MainWindow)
        self.actionAyl_k_Sarfiyat.setObjectName("actionAyl_k_Sarfiyat")
        self.actionB_lge_Ekle = QtWidgets.QAction(MainWindow)
        self.actionB_lge_Ekle.setObjectName("actionB_lge_Ekle")
        self.actionYer_Ekle = QtWidgets.QAction(MainWindow)
        self.actionYer_Ekle.setObjectName("actionYer_Ekle")
        self.actionYeni_r_n_Ekle = QtWidgets.QAction(MainWindow)
        self.actionYeni_r_n_Ekle.setObjectName("actionYeni_r_n_Ekle")
        self.action_r_n_D_zenle = QtWidgets.QAction(MainWindow)
        self.action_r_n_D_zenle.setObjectName("action_r_n_D_zenle")
        self.actionPersonel_Ekle = QtWidgets.QAction(MainWindow)
        self.actionPersonel_Ekle.setObjectName("actionPersonel_Ekle")
        self.actionPersonel_Sil = QtWidgets.QAction(MainWindow)
        self.actionPersonel_Sil.setObjectName("actionPersonel_Sil")
        self.actionPersonel_Ekle_2 = QtWidgets.QAction(MainWindow)
        self.actionPersonel_Ekle_2.setObjectName("actionPersonel_Ekle_2")
        self.actionGemi_Personel_Sil = QtWidgets.QAction(MainWindow)
        self.actionGemi_Personel_Sil.setObjectName("actionGemi_Personel_Sil")
        self.actionPersonel_Ekle_3 = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../icon/config-users.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPersonel_Ekle_3.setIcon(icon1)
        self.actionPersonel_Ekle_3.setObjectName("actionPersonel_Ekle_3")
        self.actionPersonel_Sil_2 = QtWidgets.QAction(MainWindow)
        self.actionPersonel_Sil_2.setObjectName("actionPersonel_Sil_2")
        self.actionProgram_Ayarlae = QtWidgets.QAction(MainWindow)
        self.actionProgram_Ayarlae.setObjectName("actionProgram_Ayarlae")
        self.action_statistik_Olu_tur = QtWidgets.QAction(MainWindow)
        self.action_statistik_Olu_tur.setObjectName("action_statistik_Olu_tur")
        self.actionB_lge_Yer_Bilgisi_Sil = QtWidgets.QAction(MainWindow)
        self.actionB_lge_Yer_Bilgisi_Sil.setObjectName("actionB_lge_Yer_Bilgisi_Sil")
        self.actionNot_Ekle = QtWidgets.QAction(MainWindow)
        self.actionNot_Ekle.setObjectName("actionNot_Ekle")
        self.menuM_teriler.addAction(self.actionYeni_M_teri_Ekle)
        self.menuM_teriler.addAction(self.actionM_teri_Bilgisi_D_zenle)
        self.menuM_teriler.addAction(self.actionM_teri_Sil)
        self.menuGemiler.addAction(self.actionYeni_Gemi_Ekle)
        self.menuGemiler.addAction(self.actionGemi_Bilgisi_D_zenle)
        self.menuGemiler.addAction(self.actionGemi_Sil)
        self.menuRaporlama.addAction(self.actionSat_Raporu_G_nl_k)
        self.menuRaporlama.addAction(self.actionG_mr_k_Kapan_Listesi)
        self.menuRaporlama.addAction(self.actionAyl_k_Sarfiyat)
        self.menuDolum_Bilgileri.addAction(self.actionYeni_r_n_Ekle)
        self.menuDolum_Bilgileri.addAction(self.action_r_n_D_zenle)
        self.menuB_lgeler.addAction(self.actionB_lge_Ekle)
        self.menuB_lgeler.addAction(self.actionYer_Ekle)
        self.menuB_lgeler.addAction(self.actionB_lge_Yer_Bilgisi_Sil)
        self.menuPersonel_Bilgileri.addAction(self.actionPersonel_Ekle_3)
        self.menuPersonel_Bilgileri.addAction(self.actionPersonel_Sil_2)
        self.menuAyarlar.addAction(self.actionProgram_Ayarlae)
        self.menuAyarlar.addAction(self.action_statistik_Olu_tur)
        self.menuNotlar.addAction(self.actionNot_Ekle)
        self.menubar.addAction(self.menuM_teriler.menuAction())
        self.menubar.addAction(self.menuGemiler.menuAction())
        self.menubar.addAction(self.menuRaporlama.menuAction())
        self.menubar.addAction(self.menuDolum_Bilgileri.menuAction())
        self.menubar.addAction(self.menuB_lgeler.menuAction())
        self.menubar.addAction(self.menuPersonel_Bilgileri.menuAction())
        self.menubar.addAction(self.menuAyarlar.menuAction())
        self.menubar.addAction(self.menuNotlar.menuAction())
        self.label_17.hide()
        self.label_18.hide()
        self.lineEdit_12.hide()
        self.lineEdit_13.hide()

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.setFocus)
        self.actionYeni_M_teri_Ekle.triggered.connect(ayar.Folustur)
        self.actionM_teri_Bilgisi_D_zenle.triggered.connect(ayar.Fguncelle)
        self.actionM_teri_Sil.triggered.connect(ayar.Fsil)
        self.actionYeni_Gemi_Ekle.triggered.connect(ayar.Gekle)
        self.actionGemi_Bilgisi_D_zenle.triggered.connect(ayar.Gduz)
        self.actionGemi_Sil.triggered.connect(ayar.Gsil)

        self.action_r_n_D_zenle.triggered.connect(ayar.Ygun)
        self.actionPersonel_Ekle_3.triggered.connect(ayar.Perekle)
        self.actionPersonel_Sil_2.triggered.connect(ayar.Persil)
        self.actionB_lge_Ekle.triggered.connect(ayar.bolekle)
        self.actionYer_Ekle.triggered.connect(ayar.yerek)
        self.actionB_lge_Yer_Bilgisi_Sil.triggered.connect(ayar.bysil)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.actionYeni_r_n_Ekle.triggered.connect(ayar.Uekle)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Yenikapı Teslimat"))
        self.label_14.setText(_translate("MainWindow", "Danışman"))
        self.comboBox.setItemText(0, _translate("MainWindow", "OPET"))
        self.comboBox.setItemText(1, _translate("MainWindow", "ARMARİN"))
        self.label.setText(_translate("MainWindow", "Müşteri Kodu"))
        self.label_2.setText(_translate("MainWindow", "Gemi Adı"))
        self.label_27.setText(_translate("MainWindow", "Yakıt Türü"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "YAKIT TÜRÜ SEÇ"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "MOTORİN"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "RME 180"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "RMG 380"))
        self.label_4.setText(_translate("MainWindow", "Yoğunluk"))
        self.label_3.setText(_translate("MainWindow", "Sipariş Miktarı"))
        self.label_5.setText(_translate("MainWindow", "Sıcaklık"))
        self.label_8.setText(_translate("MainWindow", "V.C.F  T54"))
        self.label_9.setText(_translate("MainWindow", "Litre"))
        self.label_10.setText(_translate("MainWindow", "Kilogram"))
        self.label_15.setText(_translate("MainWindow", "İrsali No"))
        self.label_16.setText(_translate("MainWindow", "Ödeme"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "AÇIK"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "KREDİ KARTI"))
        self.label_6.setText(_translate("MainWindow", "Teslimatçı"))

        self.label_28.setText(_translate("MainWindow", "Yakıt Alan Kişi"))
        self.label_7.setText(_translate("MainWindow", "Gemici"))

        self.label_11.setText(_translate("MainWindow", "Bölge"))
        self.label_29.setText(_translate("MainWindow", "Başlama Saati"))
        self.label_30.setText(_translate("MainWindow", "Bitiş Saati"))
        self.label_13.setText(_translate("MainWindow", "Sarfiyat"))
        self.label_17.setText(_translate("MainWindow", "Viçe Mühür"))
        self.label_18.setText(_translate("MainWindow", "Müşteri Mühür"))
        self.pushButton.setText(_translate("MainWindow", "Oluştur"))
        self.label_12.setText(_translate("MainWindow", "Yer"))
        self.groupBox.setTitle(_translate("MainWindow", "Son 5 Teslimat"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Sıra"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Tarih"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Gemi"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Cins"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "İrsaliye"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Yakıt"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Density"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Litre"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Kg"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Yakıt Veren"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Stok Durumu"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Yükleme Tarihi"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Yakıt Türü"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Yüklenen Litre"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "YüklenenKg"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Yoğunluk"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Stok Litre"))
        item = self.tableWidget_2.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Stok Kg"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Ürün Doluluk Durumu"))
        self.groupBox_5.setTitle(_translate("MainWindow", "MOTORİN"))
        self.progressBar.setFormat(_translate("MainWindow", "%p%"))
        self.label_19.setText(_translate("MainWindow", "Text"))
        self.groupBox_6.setTitle(_translate("MainWindow", "RME 180"))
        self.label_21.setText(_translate("MainWindow", "Text"))
        self.groupBox_7.setTitle(_translate("MainWindow", "RMG 380"))
        self.label_23.setText(_translate("MainWindow", "Text"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Notlar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Teslimat Oluştur"))
        self.menuM_teriler.setTitle(_translate("MainWindow", "Müşteriler"))
        self.menuGemiler.setTitle(_translate("MainWindow", "Gemiler"))
        self.menuRaporlama.setTitle(_translate("MainWindow", "Raporlama"))
        self.menuDolum_Bilgileri.setTitle(_translate("MainWindow", "Dolum Bilgileri"))
        self.menuB_lgeler.setTitle(_translate("MainWindow", "Bölgeler"))
        self.menuPersonel_Bilgileri.setTitle(_translate("MainWindow", "Personel Bilgileri"))
        self.menuAyarlar.setTitle(_translate("MainWindow", "Ayarlar"))
        self.menuNotlar.setTitle(_translate("MainWindow", "Notlar"))
        self.actionYeni_M_teri_Ekle.setText(_translate("MainWindow", "Yeni Müşteri Ekle"))
        self.actionM_teri_Bilgisi_D_zenle.setText(_translate("MainWindow", "Müşteri Bilgisi Düzenle"))
        self.actionYeni_Gemi_Ekle.setText(_translate("MainWindow", "Yeni Gemi Ekle"))
        self.actionGemi_Bilgisi_D_zenle.setText(_translate("MainWindow", "Gemi Bilgisi Düzenle"))
        self.actionGemi_Sil.setText(_translate("MainWindow", "Gemi Sil"))
        self.actionM_teri_Sil.setText(_translate("MainWindow", "Müşteri Sil"))
        self.actionSat_Raporu_G_nl_k.setText(_translate("MainWindow", "Satış Raporu (Günlük)"))
        self.actionG_mr_k_Kapan_Listesi.setText(_translate("MainWindow", "Gümrük Kapanış Listesi"))
        self.actionAyl_k_Sarfiyat.setText(_translate("MainWindow", "Aylık Sarfiyat"))
        self.actionB_lge_Ekle.setText(_translate("MainWindow", "Bölge Ekle"))
        self.actionYer_Ekle.setText(_translate("MainWindow", "Yer Ekle"))
        self.actionYeni_r_n_Ekle.setText(_translate("MainWindow", "Yeni Ürün Ekle"))
        self.action_r_n_D_zenle.setText(_translate("MainWindow", "Ürün Düzenle"))
        self.actionPersonel_Ekle.setText(_translate("MainWindow", "İntertek Personel Ekle"))
        self.actionPersonel_Sil.setText(_translate("MainWindow", "İntertek Personel Sil"))
        self.actionPersonel_Ekle_2.setText(_translate("MainWindow", "Gemi Personel Ekle"))
        self.actionGemi_Personel_Sil.setText(_translate("MainWindow", "Gemi Personel Sil"))
        self.actionPersonel_Ekle_3.setText(_translate("MainWindow", "Personel Ekle"))
        self.actionPersonel_Sil_2.setText(_translate("MainWindow", "Personel Sil"))
        self.actionProgram_Ayarlae.setText(_translate("MainWindow", "Program Ayarları"))
        self.action_statistik_Olu_tur.setText(_translate("MainWindow", "İstatistik Oluşturma "))
        self.actionB_lge_Yer_Bilgisi_Sil.setText(_translate("MainWindow", "Bölge / Yer Bilgisi Sil"))
        self.actionNot_Ekle.setText(_translate("MainWindow", "Not Ekle"))

    def tetikle_kart(self) -> object:
        ayar.Kartut()


import ic_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

