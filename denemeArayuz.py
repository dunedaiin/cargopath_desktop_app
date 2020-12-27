# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'denemeArayuz.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from denemeUI import *
from PyQt5 import QtCore, QtGui, QtWidgets
import firebase_admin
import qrcode
import string
from random import *
from firebase_admin import credentials,firestore

cred = credentials.Certificate("kargoyonetimsistemi-a38eb-firebase-adminsdk-bgnas-42afab064f.json")
firebase_admin.initialize_app(cred)

firestore_db=firestore.client()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(732, 640)
        MainWindow.setStyleSheet("/*-----QWidget-----*/\n"
"QWidget\n"
"{\n"
"    background-color: #fff;\n"
"    color: red;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLabel-----*/\n"
"QLabel\n"
"{\n"
"    background-color: transparent;\n"
"    color: #454544;\n"
"    font-weight: bold;\n"
"    font-size: 13px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QPushButton-----*/\n"
"QPushButton\n"
"{\n"
"    background-color: #5c55e9;\n"
"    color: #fff;\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"    border-top-right-radius: 15px;\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"    border-bottom-left-radius: 15px;\n"
"    padding: 10px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::disabled\n"
"{\n"
"    background-color: #5c5c5c;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::hover\n"
"{\n"
"    background-color: #5564f2;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"    background-color: #3d4ef2;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QCheckBox-----*/\n"
"QCheckBox\n"
"{\n"
"    background-color: transparent;\n"
"    color: #5c55e9;\n"
"    font-size: 10px;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QCheckBox-----*/\n"
"QCheckBox::indicator\n"
"{\n"
"    background-color: #323232;\n"
"    border: 1px solid darkgray;\n"
"    width: 12px;\n"
"    height: 12px;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image:url(\"./ressources/check.png\");\n"
"    background-color: #5c55e9;\n"
"    border: 1px solid #5c55e9;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:unchecked:hover\n"
"{\n"
"    border: 1px solid #5c55e9;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::disabled\n"
"{\n"
"    color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:disabled\n"
"{\n"
"    background-color: #656565;\n"
"    color: #656565;\n"
"    border: 1px solid #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLineEdit-----*/\n"
"QLineEdit\n"
"{\n"
"    background-color: #c2c7d5;\n"
"    color: #2a547f;\n"
"    border: none;\n"
"    padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QListView-----*/\n"
"QListView\n"
"{\n"
"    background-color: #5c55e9;\n"
"    color: #fff;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    show-decoration-selected: 0;\n"
"    border-radius: 4px;\n"
"    padding-left: -15px;\n"
"    padding-right: -15px;\n"
"    padding-top: 5px;\n"
"\n"
"} \n"
"\n"
"\n"
"QListView:disabled \n"
"{\n"
"    background-color: #5c5c5c;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item\n"
"{\n"
"    background-color: #454e5e;\n"
"    border: none;\n"
"    padding: 10px;\n"
"    border-radius: 0px;\n"
"    padding-left : 10px;\n"
"    height: 32px;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:selected\n"
"{\n"
"    color: #000;\n"
"    background-color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:!selected\n"
"{\n"
"    color:white;\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    padding-left : 10px;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:!selected:hover\n"
"{\n"
"    color: #fff;\n"
"    background-color: #5564f2;\n"
"    border: none;\n"
"    padding-left : 10px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QTreeView-----*/\n"
"QTreeView \n"
"{\n"
"    background-color: #fff;\n"
"    show-decoration-selected: 0;\n"
"    color: #454544;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView:disabled\n"
"{\n"
"    background-color: #242526;\n"
"    show-decoration-selected: 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::item \n"
"{\n"
"    border-top-color: transparent;\n"
"    border-bottom-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::item:hover \n"
"{\n"
"    background-color: #bcbdbb;\n"
"    color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::item:selected \n"
"{\n"
"    background-color: #5c55e9;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::item:selected:active\n"
"{\n"
"    background-color: #5c55e9;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::item:selected:disabled\n"
"{\n"
"    background-color: #525251;\n"
"    color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed,\n"
"QTreeView::branch:closed:has-children:has-siblings \n"
"{\n"
"    image: url(://tree-closed.png);\n"
"\n"
"}\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings,\n"
"QTreeView::branch:open:has-children:has-siblings  \n"
"{\n"
"    image: url(://tree-open.png);\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QTableView & QTableWidget-----*/\n"
"QTableView\n"
"{\n"
"    background-color: #fff;\n"
"    border: 1px solid gray;\n"
"    color: #454544;\n"
"    gridline-color: gray;\n"
"    outline : 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::disabled\n"
"{\n"
"    background-color: #242526;\n"
"    border: 1px solid #32414B;\n"
"    color: #656565;\n"
"    gridline-color: #656565;\n"
"    outline : 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::item:hover \n"
"{\n"
"    background-color: #bcbdbb;\n"
"    color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::item:selected \n"
"{\n"
"    background-color: #5c55e9;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::item:selected:disabled\n"
"{\n"
"    background-color: #1a1b1c;\n"
"    border: 2px solid #525251;\n"
"    color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableCornerButton::section\n"
"{\n"
"    background-color: #ced5e3;\n"
"    border: none;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    color: #2a547f;\n"
"    border: 0px;\n"
"    background-color: #ced5e3;\n"
"    padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:disabled\n"
"{\n"
"    background-color: #525251;\n"
"    color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:checked\n"
"{\n"
"    color: #fff;\n"
"    background-color: #5c55e9;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:checked:disabled\n"
"{\n"
"    color: #656565;\n"
"    background-color: #525251;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::vertical::first,\n"
"QHeaderView::section::vertical::only-one\n"
"{\n"
"    border-top: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::vertical\n"
"{\n"
"    border-top: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::horizontal::first,\n"
"QHeaderView::section::horizontal::only-one\n"
"{\n"
"    border-left: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::horizontal\n"
"{\n"
"    border-left: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QScrollBar-----*/\n"
"QScrollBar:horizontal \n"
"{\n"
"    background-color: transparent;\n"
"    height: 8px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:horizontal \n"
"{\n"
"    border: none;\n"
"    min-width: 100px;\n"
"    background-color: #7e92b7;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal, \n"
"QScrollBar::sub-line:horizontal,\n"
"QScrollBar::add-page:horizontal, \n"
"QScrollBar::sub-page:horizontal \n"
"{\n"
"    width: 0px;\n"
"    background-color: #d8dce6;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar:vertical \n"
"{\n"
"    background-color: transparent;\n"
"    width: 8px;\n"
"    margin: 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical \n"
"{\n"
"    border: none;\n"
"    min-height: 100px;\n"
"    background-color: #7e92b7;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical, \n"
"QScrollBar::sub-line:vertical,\n"
"QScrollBar::add-page:vertical, \n"
"QScrollBar::sub-page:vertical \n"
"{\n"
"    height: 0px;\n"
"    background-color: #d8dce6;\n"
"\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gndr_grup = QtWidgets.QGroupBox(self.centralwidget)
        self.gndr_grup.setGeometry(QtCore.QRect(10, 10, 371, 321))
        self.gndr_grup.setFlat(False)
        self.gndr_grup.setObjectName("gndr_grup")
        self.adres1 = QtWidgets.QLabel(self.gndr_grup)
        self.adres1.setGeometry(QtCore.QRect(30, 220, 51, 21))
        self.adres1.setObjectName("adres1")
        self.gndr_adres_2 = QtWidgets.QTextEdit(self.gndr_grup)
        self.gndr_adres_2.setGeometry(QtCore.QRect(200, 220, 121, 71))
        self.gndr_adres_2.setObjectName("gndr_adres_2")
        self.layoutWidget = QtWidgets.QWidget(self.gndr_grup)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 20, 291, 194))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tckimlik = QtWidgets.QLabel(self.layoutWidget)
        self.tckimlik.setObjectName("tckimlik")
        self.horizontalLayout.addWidget(self.tckimlik)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gndr_tc = QtWidgets.QLineEdit(self.layoutWidget)
        self.gndr_tc.setMaxLength(11)
        self.gndr_tc.setObjectName("gndr_tc")
        self.horizontalLayout.addWidget(self.gndr_tc)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.isim1 = QtWidgets.QLabel(self.layoutWidget)
        self.isim1.setObjectName("isim1")
        self.horizontalLayout_2.addWidget(self.isim1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.gndr_isim = QtWidgets.QLineEdit(self.layoutWidget)
        self.gndr_isim.setObjectName("gndr_isim")
        self.horizontalLayout_2.addWidget(self.gndr_isim)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.soyisim1 = QtWidgets.QLabel(self.layoutWidget)
        self.soyisim1.setObjectName("soyisim1")
        self.horizontalLayout_3.addWidget(self.soyisim1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.gndr_soyisim = QtWidgets.QLineEdit(self.layoutWidget)
        self.gndr_soyisim.setObjectName("gndr_soyisim")
        self.horizontalLayout_3.addWidget(self.gndr_soyisim)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.telefon1 = QtWidgets.QLabel(self.layoutWidget)
        self.telefon1.setObjectName("telefon1")
        self.horizontalLayout_4.addWidget(self.telefon1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.gndr_telefon = QtWidgets.QLineEdit(self.layoutWidget)
        self.gndr_telefon.setClearButtonEnabled(True)
        self.gndr_telefon.setObjectName("gndr_telefon")
        self.horizontalLayout_4.addWidget(self.gndr_telefon)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Gtarih = QtWidgets.QLabel(self.layoutWidget)
        self.Gtarih.setObjectName("Gtarih")
        self.horizontalLayout_5.addWidget(self.Gtarih)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.gndr_tarih = QtWidgets.QLineEdit(self.layoutWidget)
        self.gndr_tarih.setText("")
        self.gndr_tarih.setObjectName("gndr_tarih")
        self.horizontalLayout_5.addWidget(self.gndr_tarih)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.kargoAdedi = QtWidgets.QLabel(self.layoutWidget)
        self.kargoAdedi.setObjectName("kargoAdedi")
        self.horizontalLayout_6.addWidget(self.kargoAdedi)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.KargoAdet = QtWidgets.QSpinBox(self.layoutWidget)
        self.KargoAdet.setSingleStep(1)
        self.KargoAdet.setObjectName("KargoAdet")
        self.horizontalLayout_6.addWidget(self.KargoAdet)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.Alc_grup = QtWidgets.QGroupBox(self.centralwidget)
        self.Alc_grup.setGeometry(QtCore.QRect(20, 340, 361, 251))
        self.Alc_grup.setFlat(False)
        self.Alc_grup.setObjectName("Alc_grup")
        self.layoutWidget1 = QtWidgets.QWidget(self.Alc_grup)
        self.layoutWidget1.setGeometry(QtCore.QRect(30, 30, 291, 132))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.tcKimlik1 = QtWidgets.QLabel(self.layoutWidget1)
        self.tcKimlik1.setObjectName("tcKimlik1")
        self.horizontalLayout_8.addWidget(self.tcKimlik1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem6)
        self.alc_tc = QtWidgets.QLineEdit(self.layoutWidget1)
        self.alc_tc.setMaxLength(11)
        self.alc_tc.setObjectName("alc_tc")
        self.horizontalLayout_8.addWidget(self.alc_tc)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.isim2 = QtWidgets.QLabel(self.layoutWidget1)
        self.isim2.setObjectName("isim2")
        self.horizontalLayout_9.addWidget(self.isim2)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem7)
        self.alc_isim = QtWidgets.QLineEdit(self.layoutWidget1)
        self.alc_isim.setObjectName("alc_isim")
        self.horizontalLayout_9.addWidget(self.alc_isim)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.soyisim2 = QtWidgets.QLabel(self.layoutWidget1)
        self.soyisim2.setObjectName("soyisim2")
        self.horizontalLayout_10.addWidget(self.soyisim2)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem8)
        self.alc_soyisim = QtWidgets.QLineEdit(self.layoutWidget1)
        self.alc_soyisim.setObjectName("alc_soyisim")
        self.horizontalLayout_10.addWidget(self.alc_soyisim)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.telefon2 = QtWidgets.QLabel(self.layoutWidget1)
        self.telefon2.setObjectName("telefon2")
        self.horizontalLayout_11.addWidget(self.telefon2)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem9)
        self.alc_telefon = QtWidgets.QLineEdit(self.layoutWidget1)
        self.alc_telefon.setClearButtonEnabled(True)
        self.alc_telefon.setObjectName("alc_telefon")
        self.horizontalLayout_11.addWidget(self.alc_telefon)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.adres2 = QtWidgets.QLabel(self.Alc_grup)
        self.adres2.setGeometry(QtCore.QRect(30, 170, 51, 31))
        self.adres2.setObjectName("adres2")
        self.alc_adres = QtWidgets.QTextEdit(self.Alc_grup)
        self.alc_adres.setGeometry(QtCore.QRect(200, 170, 121, 71))
        self.alc_adres.setObjectName("alc_adres")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(390, 10, 331, 321))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(30, 130, 71, 16))
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(30, 70, 91, 16))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(30, 100, 111, 16))
        self.label_4.setObjectName("label_4")
        self.kargo_tur = QtWidgets.QLineEdit(self.groupBox_3)
        self.kargo_tur.setGeometry(QtCore.QRect(190, 40, 113, 20))
        self.kargo_tur.setObjectName("kargo_tur")
        self.gndr_il = QtWidgets.QLineEdit(self.groupBox_3)
        self.gndr_il.setGeometry(QtCore.QRect(190, 70, 113, 20))
        self.gndr_il.setObjectName("gndr_il")
        self.gndr_ilce = QtWidgets.QLineEdit(self.groupBox_3)
        self.gndr_ilce.setGeometry(QtCore.QRect(190, 100, 113, 20))
        self.gndr_ilce.setObjectName("gndr_ilce")
        self.alc_il = QtWidgets.QLineEdit(self.groupBox_3)
        self.alc_il.setGeometry(QtCore.QRect(190, 130, 113, 20))
        self.alc_il.setObjectName("alc_il")
        self.label_13 = QtWidgets.QLabel(self.groupBox_3)
        self.label_13.setGeometry(QtCore.QRect(30, 160, 81, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.groupBox_3)
        self.label_14.setGeometry(QtCore.QRect(30, 190, 151, 21))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.groupBox_3)
        self.label_15.setGeometry(QtCore.QRect(30, 230, 101, 16))
        self.label_15.setObjectName("label_15")
        self.alc_ilce = QtWidgets.QLineEdit(self.groupBox_3)
        self.alc_ilce.setGeometry(QtCore.QRect(190, 160, 113, 20))
        self.alc_ilce.setObjectName("alc_ilce")
        self.tah_teslimat = QtWidgets.QLineEdit(self.groupBox_3)
        self.tah_teslimat.setGeometry(QtCore.QRect(190, 190, 113, 20))
        self.tah_teslimat.setObjectName("tah_teslimat")
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(50, 260, 51, 16))
        self.label_10.setObjectName("label_10")
        self.agirlik = QtWidgets.QLineEdit(self.groupBox_3)
        self.agirlik.setGeometry(QtCore.QRect(190, 260, 113, 20))
        self.agirlik.setObjectName("agirlik")
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setGeometry(QtCore.QRect(50, 290, 51, 16))
        self.label_11.setObjectName("label_11")
        self.blnd_yer = QtWidgets.QLineEdit(self.groupBox_3)
        self.blnd_yer.setGeometry(QtCore.QRect(190, 230, 113, 20))
        self.blnd_yer.setObjectName("blnd_yer")
        self.fiyat = QtWidgets.QLineEdit(self.groupBox_3)
        self.fiyat.setGeometry(QtCore.QRect(190, 290, 113, 20))
        self.fiyat.setObjectName("fiyat")
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(440, 460, 221, 131))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btnKaydet = QtWidgets.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.btnKaydet.setFont(font)
        self.btnKaydet.setCheckable(False)
        self.btnKaydet.setAutoDefault(False)
        self.btnKaydet.setObjectName("btnKaydet")
        self.verticalLayout_3.addWidget(self.btnKaydet)
        self.btnSifirla = QtWidgets.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.btnSifirla.setFont(font)
        self.btnSifirla.setCheckable(False)
        self.btnSifirla.setAutoDefault(False)
        self.btnSifirla.setObjectName("btnSifirla")
        self.verticalLayout_3.addWidget(self.btnSifirla)
        self.btnIptal = QtWidgets.QPushButton(self.layoutWidget2)
        self.btnIptal.setObjectName("btnIptal")
        self.verticalLayout_3.addWidget(self.btnIptal)
        self.layoutWidget.raise_()
        self.groupBox_3.raise_()
        self.Alc_grup.raise_()
        self.gndr_grup.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 732, 21))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        MainWindow.setToolTip(_translate("MainWindow", "Eklemek için tıklayınız."))
        self.gndr_grup.setTitle(_translate("MainWindow", "Gönderici:"))
        self.adres1.setText(_translate("MainWindow", "Adres: "))
        self.gndr_adres_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.tckimlik.setText(_translate("MainWindow", "TC Kimlik No:"))
        self.isim1.setText(_translate("MainWindow", "İsim:"))
        self.soyisim1.setText(_translate("MainWindow", "Soyisim:"))
        self.telefon1.setText(_translate("MainWindow", "Telefon:"))
        self.gndr_telefon.setInputMask(_translate("MainWindow", "(999)999 99 99"))
        self.Gtarih.setText(_translate("MainWindow", "Gönderilen Tarih:"))
        self.kargoAdedi.setText(_translate("MainWindow", "Kargo Adet:"))
        self.Alc_grup.setTitle(_translate("MainWindow", "Alıcı:"))
        self.tcKimlik1.setText(_translate("MainWindow", "TC Kimlik No:"))
        self.isim2.setText(_translate("MainWindow", "İsim:"))
        self.soyisim2.setText(_translate("MainWindow", "Soyisim:"))
        self.telefon2.setText(_translate("MainWindow", "Telefon:"))
        self.alc_telefon.setInputMask(_translate("MainWindow", "(999)999 99 99"))
        self.adres2.setText(_translate("MainWindow", "Adres: "))
        self.alc_adres.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Kargo Bilgileri"))
        self.label_5.setText(_translate("MainWindow", "Alınan İl:"))
        self.label_3.setText(_translate("MainWindow", "Gönderilen İl:"))
        self.label_2.setText(_translate("MainWindow", "Kargo Türü:"))
        self.label_4.setText(_translate("MainWindow", "Gönderilen İlçe:"))
        self.label_13.setText(_translate("MainWindow", "Alinan İlçe"))
        self.label_14.setText(_translate("MainWindow", "Tahmini Teslimat:"))
        self.label_15.setText(_translate("MainWindow", "Bulunduğu Yer:"))
        self.label_10.setText(_translate("MainWindow", "Agırlık:"))
        self.label_11.setText(_translate("MainWindow", "Fiyat:"))
        self.btnKaydet.setText(_translate("MainWindow", "Ekle"))
        self.btnSifirla.setText(_translate("MainWindow", "Sıfırla"))
        self.btnIptal.setText(_translate("MainWindow", "İptal Et"))

        self.KargoAdet.valueChanged.connect(self.updateLabel)
        self.btnKaydet.clicked.connect(self.onClickEkle)

    def random(self):
        ch = string.ascii_letters + string.digits
        password =  "".join(choice(ch) for x in range(randint(6, 6)))
        print(password)
        return password

    def qrUret(self,idcode):
        qr = qrcode.QRCode(version = 1,error_correction = qrcode.constants.ERROR_CORRECT_H,box_size = 10,border = 4)
        # karekod içinde saklamak istediğiniz verileriniz
        data = idcode
        # Veriyi ekleme
        qr.add_data(data)
        qr.make(fit=True)
        # Görüntü dosyasının oluşturulması
        img = qr.make_image()
        # Oluşturulan görüntü dosyasının kayıt biçimleri. İstediğiniz formatı seçebilirsiniz.:
        # img.save("image.png")
        # img.save("image.bmp")
        # img.save("image.jpeg")
        img.save(data+".jpg")

    def onClickEkle(self):
        print("Veriler Geldi")

        gndr_adres=self.gndr_adres_2.toPlainText()
        print(gndr_adres)
        gndr_isim=self.gndr_isim.text()
        print(gndr_isim)
        gndr_soyisim=self.gndr_soyisim.text()
        print(gndr_soyisim)
        gndr_tc=self.gndr_tc.text()
        print(gndr_tc)
        gndr_telefon=self.gndr_telefon.text()
        print(gndr_telefon)
        gndr_il=self.gndr_il.text()
        print(gndr_il)
        gndr_ilce=self.gndr_ilce.text()
        print(gndr_ilce)
        gndr_tarih=self.gndr_tarih.text()
        print(gndr_tarih)
        alc_adres=self.alc_adres.toPlainText()
        print(alc_adres)
        alc_isim=self.alc_isim.text()
        print(alc_isim)
        alc_soyisim=self.alc_soyisim.text()
        print(alc_soyisim)
        alc_telefon=self.alc_telefon.text()
        print(alc_telefon)
        alc_il=self.alc_il.text()
        print(alc_il)
        alc_tc=self.alc_tc.text()
        alc_ilce=self.alc_ilce.text()
        print(alc_ilce)
        agirlik=self.agirlik.text()
        print(agirlik)
        fiyat=self.fiyat.text()
        print(fiyat)
        kargo_tur=self.kargo_tur.text()
        print(kargo_tur)
        tah_teslimat=self.tah_teslimat.text()
        print(tah_teslimat)
        blnd_yer=self.blnd_yer.text()
        print(blnd_yer)

        idcode=self.random()
        self.qrUret(idcode)
        print("Veriler Gidiyor CcC")

        

        doc_ref = firestore_db.collection(u'kargolar').document(idcode)
        doc_ref.set({
            u'gndr_adres': gndr_adres,
            u'agirlik': agirlik,
            u'alc_adres': alc_adres,
            u'alc_isim': alc_isim,
            u'alc_soyisim': alc_soyisim,
            u'alc_tc': alc_tc,
            u'alc_telefon': alc_telefon,
            u'aln_il': alc_il,
            u'aln_ilce': alc_ilce,
            u'bln_yer': blnd_yer,
            u'fiyat': fiyat,
            u'gndr_il': gndr_il,
            u'gndr_ilce': gndr_ilce,
            u'gndr_isim': gndr_isim,
            u'gndr_soyisim': gndr_soyisim,
            u'gndr_tarih': gndr_tarih,
            u'gndr_tc': gndr_tc,
            u'gndr_telefon': gndr_telefon,
            u'kargoAdet': self.kargoAdet,
            u'kargo_tur': kargo_tur,
            u'tah_teslimat': tah_teslimat,
            
        })
        
    def updateLabel(self, value):
        self.kargoAdet=str(value)
        print(self.kargoAdet)
        
        

  


Uygulama=QApplication(sys.argv)
penAna=QMainWindow()
ui=Ui_MainWindow()
ui.setupUi(penAna)
penAna.show()

sys.exit(Uygulama.exec_())
