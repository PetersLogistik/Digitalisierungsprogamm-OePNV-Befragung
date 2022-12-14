# -*- coding: utf-8 -*-

# Erstellungszeit: 03.12.2022 18.30-00.30
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import os
import csv
import sys
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(487, 851)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 461, 791))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.top = QtWidgets.QHBoxLayout()
        self.top.setObjectName("top")
        self.linie = QtWidgets.QComboBox(self.widget)
        self.linie.setObjectName("linie")
        self.top.addWidget(self.linie)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.top.addItem(spacerItem)
        self.label_Iv_nummer = QtWidgets.QLabel(self.widget)
        self.label_Iv_nummer.setObjectName("label_Iv_nummer")
        self.top.addWidget(self.label_Iv_nummer)
        self.iv_nummer = QtWidgets.QLineEdit(self.widget)
        self.iv_nummer.setObjectName("iv_nummer")
        self.top.addWidget(self.iv_nummer)
        self.verticalLayout_2.addLayout(self.top)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.seriennummer = QtWidgets.QLineEdit(self.widget)
        self.seriennummer.setObjectName("seriennummer")
        self.horizontalLayout.addWidget(self.seriennummer)
        self.label_laufnr = QtWidgets.QLabel(self.widget)
        self.label_laufnr.setObjectName("label_laufnr")
        self.horizontalLayout.addWidget(self.label_laufnr)
        self.laufnummer = QtWidgets.QSpinBox(self.widget)
        self.laufnummer.setObjectName("laufnummer")
        self.horizontalLayout.addWidget(self.laufnummer)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.comboBox_Erhebunsabschnitt = QtWidgets.QComboBox(self.widget)
        self.comboBox_Erhebunsabschnitt.setObjectName("comboBox_Erhebunsabschnitt")
        self.horizontalLayout_2.addWidget(self.comboBox_Erhebunsabschnitt)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        # spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        # self.horizontalLayout_3.addItem(spacerItem2)
        self.fahrausweiskat = QtWidgets.QComboBox(self.widget)
        self.fahrausweiskat.setObjectName("fahrausweiskat")
        self.horizontalLayout_3.addWidget(self.fahrausweiskat)
        self.fahrausweisart = QtWidgets.QComboBox(self.widget)
        self.fahrausweisart.setObjectName("fahrausweisart")
        self.horizontalLayout_3.addWidget(self.fahrausweisart)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verkaufendesvu = QtWidgets.QComboBox(self.widget)
        self.verkaufendesvu.setObjectName("verkaufendesvu")
        self.horizontalLayout_4.addWidget(self.verkaufendesvu)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.preis = QtWidgets.QDoubleSpinBox(self.widget)
        self.preis.setObjectName("preis")
        self.horizontalLayout_5.addWidget(self.preis)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.preisstufe = QtWidgets.QComboBox(self.widget)
        self.preisstufe.setObjectName("preisstufe")
        self.preisstufe.addItem("")
        self.preisstufe.addItem("A")
        self.preisstufe.addItem("B")
        self.preisstufe.addItem("C")
        self.preisstufe.addItem("D")
        self.horizontalLayout_6.addWidget(self.preisstufe)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.line_2 = QtWidgets.QFrame(self.widget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 0, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 0, 3, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.widget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 0, 4, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.widget)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 1, 0, 1, 1)
        self.spinBox_bis5 = QtWidgets.QSpinBox(self.widget)
        self.spinBox_bis5.setObjectName("spinBox_bis5")
        self.gridLayout.addWidget(self.spinBox_bis5, 1, 1, 1, 1)
        self.spinBox_bis14 = QtWidgets.QSpinBox(self.widget)
        self.spinBox_bis14.setObjectName("spinBox_bis14")
        self.gridLayout.addWidget(self.spinBox_bis14, 1, 2, 1, 1)
        self.spinBox_bis59 = QtWidgets.QSpinBox(self.widget)
        self.spinBox_bis59.setObjectName("spinBox_bis59")
        self.gridLayout.addWidget(self.spinBox_bis59, 1, 3, 1, 1)
        self.spinBox_ab60 = QtWidgets.QSpinBox(self.widget)
        self.spinBox_ab60.setObjectName("spinBox_ab60")
        self.gridLayout.addWidget(self.spinBox_ab60, 1, 4, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.line_3 = QtWidgets.QFrame(self.widget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_2.addWidget(self.line_3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_13 = QtWidgets.QLabel(self.widget)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_7.addWidget(self.label_13)
        self.einstieg = QtWidgets.QComboBox(self.widget)
        self.einstieg.setObjectName("einstieg")
        self.horizontalLayout_7.addWidget(self.einstieg)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_14 = QtWidgets.QLabel(self.widget)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_8.addWidget(self.label_14)
        self.ausstieg = QtWidgets.QComboBox(self.widget)
        self.ausstieg.setObjectName("ausstieg")
        self.horizontalLayout_8.addWidget(self.ausstieg)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.line_4 = QtWidgets.QFrame(self.widget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_2.addWidget(self.line_4)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_15 = QtWidgets.QLabel(self.widget)
        self.label_15.setObjectName("label_15")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_15)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(0, QtWidgets.QFormLayout.FieldRole, spacerItem5)
        self.label_16 = QtWidgets.QLabel(self.widget)
        self.label_16.setObjectName("label_16")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.v_vmittel1 = QtWidgets.QComboBox(self.widget)
        self.v_vmittel1.setObjectName("v_vmittel1")
        self.v_vmittel1.addItem("Fu??weg/Fahrrad", 31)
        self.v_vmittel1.addItem("Pkw/Motorrad", 32)
        self.v_vmittel1.addItem("Nahverkehrszug (RE, RB, S-Bahn)", 33)
        self.v_vmittel1.addItem("Fernverkehrszug (IC, EC, ICE)", 34)
        self.v_vmittel1.addItem("Zug mit anderem Ticket", 35)
        self.v_vmittel1.addItem("Bus/Stra??enbahn/U-Bahn", 36)
        self.v_vmittel1.addItem("Taxi", 37)
        self.v_vmittel1.addItem("Fernbus", 38)
        self.v_vmittel1.addItem("Sonstiges", 88)
        self.v_vmittel1.addItem("Keine Angabe", 89)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.v_vmittel1)
        self.label_18 = QtWidgets.QLabel(self.widget)
        self.label_18.setObjectName("label_18")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.v_haltestelle1 = QtWidgets.QComboBox(self.widget)
        self.v_haltestelle1.setObjectName("v_haltestelle1")
        self.v_haltestelle1.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.v_haltestelle1)
        self.label_17 = QtWidgets.QLabel(self.widget)
        self.label_17.setObjectName("label_17")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.v_vmittel2 = QtWidgets.QComboBox(self.widget)
        self.v_vmittel2.setObjectName("v_vmittel2")
        self.v_vmittel2.addItem("")
        self.v_vmittel2.addItem("Fu??weg/Fahrrad", 31)
        self.v_vmittel2.addItem("Pkw/Motorrad", 32)
        self.v_vmittel2.addItem("Nahverkehrszug (RE, RB, S-Bahn)", 33)
        self.v_vmittel2.addItem("Fernverkehrszug (IC, EC, ICE)", 34)
        self.v_vmittel2.addItem("Zug mit anderem Ticket", 35)
        self.v_vmittel2.addItem("Bus/Stra??enbahn/U-Bahn", 36)
        self.v_vmittel2.addItem("Taxi", 37)
        self.v_vmittel2.addItem("Fernbus", 38)
        self.v_vmittel2.addItem("Sonstiges", 88)
        self.v_vmittel2.addItem("Keine Angabe", 89)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.v_vmittel2)
        self.label_19 = QtWidgets.QLabel(self.widget)
        self.label_19.setObjectName("label_19")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_19)
        self.v_haltestelle2 = QtWidgets.QComboBox(self.widget)
        self.v_haltestelle2.setObjectName("v_haltestelle2")
        self.v_haltestelle2.addItem("")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.v_haltestelle2)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.line_8 = QtWidgets.QFrame(self.widget)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.verticalLayout_2.addWidget(self.line_8)
        self.label_20 = QtWidgets.QLabel(self.widget)
        self.label_20.setObjectName("label_20")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_20)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout_2.setItem(0, QtWidgets.QFormLayout.FieldRole, spacerItem6)
        self.label_21 = QtWidgets.QLabel(self.widget)
        self.label_21.setObjectName("label_21")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_21)
        self.n_vmittel1 = QtWidgets.QComboBox(self.widget)
        self.n_vmittel1.setObjectName("n_vmittel1")
        self.n_vmittel1.addItem("Fu??weg/Fahrrad", 31)
        self.n_vmittel1.addItem("Pkw/Motorrad", 32)
        self.n_vmittel1.addItem("Nahverkehrszug (RE, RB, S-Bahn)", 33)
        self.n_vmittel1.addItem("Fernverkehrszug (IC, EC, ICE)", 34)
        self.n_vmittel1.addItem("Zug mit anderem Ticket", 35)
        self.n_vmittel1.addItem("Bus/Stra??enbahn/U-Bahn", 36)
        self.n_vmittel1.addItem("Taxi", 37)
        self.n_vmittel1.addItem("Fernbus", 38)
        self.n_vmittel1.addItem("Sonstiges", 88)
        self.n_vmittel1.addItem("Keine Angabe", 89)
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.n_vmittel1)
        self.label_22 = QtWidgets.QLabel(self.widget)
        self.label_22.setObjectName("label_22")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_22)
        self.n_haltestelle1 = QtWidgets.QComboBox(self.widget)
        self.n_haltestelle1.setObjectName("n_haltestelle1")
        self.n_haltestelle1.addItem("")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.n_haltestelle1)
        self.label_23 = QtWidgets.QLabel(self.widget)
        self.label_23.setObjectName("label_23")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_23)
        self.n_vmittel2 = QtWidgets.QComboBox(self.widget)
        self.n_vmittel2.setObjectName("n_vmittel2")
        self.n_vmittel2.addItem("")
        self.n_vmittel2.addItem("Fu??weg/Fahrrad", 31)
        self.n_vmittel2.addItem("Pkw/Motorrad", 32)
        self.n_vmittel2.addItem("Nahverkehrszug (RE, RB, S-Bahn)", 33)
        self.n_vmittel2.addItem("Fernverkehrszug (IC, EC, ICE)", 34)
        self.n_vmittel2.addItem("Zug mit anderem Ticket", 35)
        self.n_vmittel2.addItem("Bus/Stra??enbahn/U-Bahn", 36)
        self.n_vmittel2.addItem("Taxi", 37)
        self.n_vmittel2.addItem("Fernbus", 38)
        self.n_vmittel2.addItem("Sonstiges", 88)
        self.n_vmittel2.addItem("Keine Angabe", 89)
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.n_vmittel2)
        self.label_24 = QtWidgets.QLabel(self.widget)
        self.label_24.setObjectName("label_24")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_24)
        self.n_haltestelle2 = QtWidgets.QComboBox(self.widget)
        self.n_haltestelle2.setObjectName("n_haltestelle2")
        self.n_haltestelle2.addItem("")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.n_haltestelle2)
        self.verticalLayout_2.addLayout(self.formLayout_2)
        self.line_5 = QtWidgets.QFrame(self.widget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_2.addWidget(self.line_5)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_25 = QtWidgets.QLabel(self.widget)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_9.addWidget(self.label_25)
        self.fahrtzweck = QtWidgets.QComboBox(self.widget)
        self.fahrtzweck.setObjectName("fahrtzweck")
        self.fahrtzweck.addItem("Keine Angabe", 99)
        self.fahrtzweck.addItem("Wohnung", 1)
        self.fahrtzweck.addItem("Arbeit", 2)
        self.fahrtzweck.addItem("Schule/Ausbildung", 3)
        self.fahrtzweck.addItem("Einkaufen", 4)
        self.fahrtzweck.addItem("Freizeit", 5)
        self.fahrtzweck.addItem("Dienstreise", 6)
        self.fahrtzweck.addItem("Sonstiges", 98)
        self.horizontalLayout_9.addWidget(self.fahrtzweck)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.line_6 = QtWidgets.QFrame(self.widget)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalLayout_2.addWidget(self.line_6)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_26 = QtWidgets.QLabel(self.widget)
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_10.addWidget(self.label_26)
        self.status = QtWidgets.QComboBox(self.widget)
        self.status.setObjectName("status")
        self.status.addItem("Vollst??ndig", 26)
        self.status.addItem("Erhebungsabbruch", 21)
        self.status.addItem("Verweigerung", 22)
        self.status.addItem("Wurde bereits befragt", 23)
        self.status.addItem("Muss aussteigen", 24)
        self.status.addItem("Verst??ndigungsprobleme", 25)
        self.horizontalLayout_10.addWidget(self.status)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.line_7 = QtWidgets.QFrame(self.widget)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.verticalLayout_2.addWidget(self.line_7)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.widget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.horizontalLayout_11.addWidget(self.plainTextEdit)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.buttonPruef = QtWidgets.QPushButton(self.widget, clicked = lambda: self.pruef())
        self.buttonPruef.setObjectName("buttonPruef")
        self.verticalLayout.addWidget(self.buttonPruef)
        self.buttonWeiter = QtWidgets.QPushButton(self.widget, clicked = lambda: self.get_new())
        self.buttonWeiter.setObjectName("buttonWeiter")
        self.buttonWeiter.setEnabled(False)
        self.verticalLayout.addWidget(self.buttonWeiter)
        self.buttonBeenden = QtWidgets.QPushButton(self.widget, clicked = lambda: self.get_save())
        self.buttonBeenden.setObjectName("buttonBeenden")
        self.verticalLayout.addWidget(self.buttonBeenden)
        self.horizontalLayout_11.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        MainWindow.setCentralWidget(self.centralwidget)
        # self.menubar = QtWidgets.QMenuBar(MainWindow)
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 487, 21))
        # self.menubar.setObjectName("menubar")
        # MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
#_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_
        print(self.path_to())
        #Setzen
        self.setze_linie()
        self.laden()
        
        #Combobox auslesen
        self.linie.activated.connect(self.lade_stationen)
        self.fahrausweiskat.activated.connect(self.lade_tickets)

        self.minBeschriftung(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
#_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_
# Beschriftungen #
    def laden(self):
        self.setze_tickt()
        self.setze_Vk_VU()
        self.lade_entf_station()
        
    def setze_linie(self):
        path = self.path_to() + r"/linienplan"
        for file in os.listdir(path):
            self.linie.addItem(file.strip(".csv"))
            
    def lade_stationen(self, index):
        self.comboBox_Erhebunsabschnitt.clear()
        self.einstieg.clear()
        self.ausstieg.clear()
        
        path = self.path_to() + r"/linienplan/"+self.linie.itemText(index)+".csv"
        with open(path, 'r', encoding='UTF-8') as haltestellen:
            csv_halt = csv.reader(haltestellen, delimiter=';')
            for row in csv_halt:
                self.comboBox_Erhebunsabschnitt.addItem(row[0], row[1])
                self.einstieg.addItem(row[0], row[1])
                self.ausstieg.addItem(row[0], row[1])
            self.einstieg.addItem("<null>")
            self.ausstieg.addItem("<null>")
    
    def lade_entf_station(self):
        with open(self.path_to() + r"/rahmen/hst.csv", 'r', encoding='UTF-8') as ent_sta:
                csv_ent = csv.reader(ent_sta, delimiter=';')
                for row in csv_ent:
                    self.v_haltestelle1.addItem(row[0], row[1])
                    self.v_haltestelle2.addItem(row[0], row[1])
                    self.n_haltestelle1.addItem(row[0], row[1])
                    self.n_haltestelle2.addItem(row[0], row[1])
    
    def setze_tickt(self):
        with open(self.path_to() + r"./rahmen/faw_kat.csv", 'r', encoding='UTF-8') as kat:
                csv_kat = csv.reader(kat, delimiter=';')
                for row in csv_kat:
                    self.fahrausweiskat.addItem(row[0])
    
    def lade_tickets(self, index):
        self.fahrausweisart.clear()
        with open(self.path_to() + r"/rahmen/faw.csv", 'r', encoding='UTF-8') as ticket:
            csv_ticket = csv.reader(ticket, delimiter=';')
            for row in csv_ticket:
                if row[0] == self.fahrausweiskat.itemText(index):
                    self.fahrausweisart.addItem(row[1] , row[2])
                    
    def setze_Vk_VU(self):
        with open(self.path_to() + r"/rahmen/vu.csv", 'r', encoding='UTF-8') as vk:
                csv_vu = csv.reader(vk, delimiter=';')
                for row in csv_vu:
                    self.verkaufendesvu.addItem("("+row[0]+") "+row[1], row[2])
                    
    def minBeschriftung(self, MainWindow):
        MainWindow.setWindowTitle("Befragungsbogen")
        self.label_Iv_nummer.setText("IV-Nummer:")
        self.label.setText("Seriennummer")
        self.label_laufnr.setText("Laufendenummer")
        self.label_2.setText("1. Erhebunsgabschnitt")
        self.label_3.setText("2. Fahrausweis-Art")
        self.label_4.setText("3. Verkaufendes VU")
        self.label_5.setText("4. Ticketpreis")
        self.label_6.setText("5. Preissufe")
        self.label_7.setText("6. Alter")
        self.label_8.setText("0-5 J.")
        self.label_9.setText("6-14 J.")
        self.label_10.setText("15-59 J.")
        self.label_11.setText(">60 J.")
        self.label_12.setText("Anz.")
        self.label_13.setText("7. Einstig")
        self.label_14.setText("8. Ausstieg")
        self.label_15.setText("9. Vorlauf")
        self.label_16.setText("Verkehrsmittel 1 zum Einstieg")
        self.label_18.setText("Einstiegshaltestelle 1")
        self.label_17.setText("Verkehrsmittel 2 zum Einstieg")
        self.label_19.setText("Einstiegshaltestelle 2")
        self.label_20.setText("10. Nachlauf")
        self.label_21.setText("Verkehrsmittel 1 nach Ausstieg")
        self.label_22.setText("Ausstiegshaltestelle 1")
        self.label_23.setText("Verkehrsmittel 2 nach Ausstieg")
        self.label_24.setText("Ausstiegshaltestelle 2")
        self.label_25.setText("11. Fahrtzweck")
        self.label_26.setText("12. Interviewstatus")
        self.buttonPruef.setText("Pr??fen")
        self.buttonWeiter.setText("weitere Bogen")
        self.buttonBeenden.setText("Beenden & Speichern")

#_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_
# Ausf??hrung #
    def path_to(self):
        return os.path.dirname(os.path.abspath(__file__))
    
    def get_new(self):
        url = self.path_to() + r"/ergebnisse/"+self.seriennummer.text()+".csv"
        try:
            erg_all = []
            with open(url) as csvdatei:
                csv_reader_object = csv.reader(csvdatei, delimiter=',')
                for row in csv_reader_object:
                    erg_all.append(row)
        except:
            pd.DataFrame([self.get_data()]).to_csv(url, header=False, index=False)
        else:
            erg_all.append(self.get_data())
            pd.DataFrame(erg_all).to_csv(url, header=False, index=False)
        #Elementblock
        self.linie.setEnabled(False)
        self.iv_nummer.setEnabled(False)
        self.seriennummer.setEnabled(False)
        self.laufnummer.setEnabled(False)
        self.buttonWeiter.setEnabled(False)
        #Inhalt
        self.laufnummer.setValue(self.laufnummer.value()+1)
        self.comboBox_Erhebunsabschnitt.setCurrentIndex(0)
        self.fahrausweisart.setCurrentIndex(0)
        self.verkaufendesvu.setCurrentIndex(1)
        self.preis.setValue(0.00)
        self.preisstufe.setCurrentIndex(0)
        self.spinBox_bis5.setValue(0)
        self.spinBox_bis14.setValue(0)
        self.spinBox_bis59.setValue(0)
        self.spinBox_ab60.setValue(0)
        self.einstieg.setCurrentIndex(0)
        self.ausstieg.setCurrentIndex(0)
        self.v_vmittel1.setCurrentIndex(0)
        self.v_haltestelle1.setCurrentIndex(0)
        self.v_vmittel2.setCurrentIndex(0)
        self.v_haltestelle2.setCurrentIndex(0)
        self.n_vmittel1.setCurrentIndex(0)
        self.n_haltestelle1.setCurrentIndex(0)
        self.n_vmittel2.setCurrentIndex(0)
        self.n_haltestelle2.setCurrentIndex(0)
        self.fahrtzweck.setCurrentIndex(0)
        self.status.setCurrentIndex(0)
        self.plainTextEdit.clear()
        self.statusbar.showMessage("Warten auf Eingabe")
    
    def get_save(self):
        head = ["Seriennummer", "lf_Nr", "IV_Nr", "Erhebungsabschnitt", "FAW_Kategorie", "FAW_Art", "VU	Preis", "Preisstufe", 
                "Pers_0-5", "Pers_6-14", "Pers_15-59", "Pers_>60", "Einstieg", "Ausstieg", "VL1_VM", "VL1_HST", "VL2_VM", "VL2_HST", 
                "NL1_VM", "NL1_HST", "NL2_VM", "NL2_HST", "Zweck", "Status", "Bemerkungen"]
        
        url = self.path_to() + r"/ergebnisse/"+self.seriennummer.text()
        erg_all = []
        with open(url+".csv") as csvdatei:
            csv_reader_object = csv.reader(csvdatei, delimiter=',')
            for row in csv_reader_object:
                erg_all.append(row)
        
        erg_all.append(self.get_data())

        try:
            pd.DataFrame(erg_all).to_excel(url+"_befragung.xlsx", header=head, index=False)
        except:
            self.statusbar.showMessage("Es kann nicht Gespeichert werden. Bitte noch einmal versuchen.")
        else:
            self.statusbar.showMessage("Gespeichert!")
            self.enable_all()
        
    def enable_all(self):
        self.buttonPruef.setEnabled(False)
        self.buttonWeiter.setEnabled(False)
        self.buttonBeenden.setEnabled(False)
        self.statusbar.showMessage("Gespeichert! Fenster kann nun geschlossen werden.")
        
    def get_data(self):
        erg = (self.seriennummer.text(),                    #0 # = wie alte alter # fixiert
            self.laufnummer.value(),                        #1 # alte + 1
            self.iv_nummer.text(),                          #2 # = wie alter # fixiert
            self.comboBox_Erhebunsabschnitt.currentData(),  #3
            self.fahrausweisart.currentData(),              #4
            self.verkaufendesvu.currentData(),              #5
            self.preis.value(),                             #6 # > 0 bei papiertickets
            self.preisstufe.currentText(),                  #7 # != Null bei Preis > 0 #yes
            self.spinBox_bis5.value(),                      #8
            self.spinBox_bis14.value(),                     #9
            self.spinBox_bis59.value(),                     #10
            self.spinBox_ab60.value(),                      #11 # B??ren Ticket ? && Summe >= 1
            self.einstieg.currentData(),                    #12 # nach Erhebunsabschnitt?
            self.ausstieg.currentData(),                    #13 # nach Einsteiger Haltestelle?
            self.v_vmittel1.currentData(),                  #14 
            self.v_haltestelle1.currentData(),              #15 # Text bei vm1 != null #yes
            self.v_vmittel2.currentData(),                  #16 
            self.v_haltestelle2.currentData(),              #17 # Text bei vm1 != null #yes
            self.n_vmittel1.currentData(),                  #18
            self.n_haltestelle1.currentData(),              #19 # Text bei nm1 != null #yes
            self.n_vmittel2.currentData(),                  #20
            self.n_haltestelle2.currentData(),              #21 # Text bei nm2 != null #yes
            self.fahrtzweck.currentData(),                  #22
            self.status.currentData(),                      #23
            self.plainTextEdit.toPlainText())               #24
        return erg

    def pruef(self):
        self.statusbar.showMessage("Pr??fung")
        erg = self.get_data()
        lauf = [33, 34, 35, 36, 38]
        if erg[3] == "":
            self.statusbar.showMessage("Fehler: Der Erhebungsabschnitt fehlt!")
        elif erg[12] == "":
            self.statusbar.showMessage("Fehler: Der Einstieg fehlt!")
        elif erg[13] == "":
            self.statusbar.showMessage("Fehler: Der Ausstieg fehlt!")
        elif self.ausstieg.currentIndex() <= self.einstieg.currentIndex():
            self.statusbar.showMessage("Fehler: Ein- und Ausstiegshaltestelle passen nicht!") 
        elif self.einstieg.currentIndex() > self.comboBox_Erhebunsabschnitt.currentIndex():
            self.statusbar.showMessage("Fahler: Einstieg liegt nach dem Erhebungsabschnitt!") 
        elif self.comboBox_Erhebunsabschnitt.currentIndex() > self.ausstieg.currentIndex():
            self.statusbar.showMessage("Fehler: Ausstieg und Erhebungsabschnitt passen nicht zusammen fehlerhaft!")  
        elif self.ausstieg.currentIndex() < self.einstieg.currentIndex():
            self.statusbar.showMessage("Fehler: Ein- und Ausstieg sind fehlerhaft!")
        elif self.fahrausweiskat.currentIndex() == 1 and erg[6] == 0:
            self.statusbar.showMessage("Fehler: Der Ticketpreis ist zu niedrig!")
        elif erg[6] != 0 and erg[7] == "":
            self.statusbar.showMessage("Fehler: Die Preisstufe fehlt!")
        elif erg[14] in lauf and erg[15] == "":
            self.statusbar.showMessage("Fehler: Die Einstiegshaltestelle bei Vorlauf 1 fehlt!")
        elif erg[16] in lauf and erg[17] == "":
            self.statusbar.showMessage("Fehler: Die Einstiegshaltestelle bei Vorlauf 2 fehlt!")
        elif erg[18] in lauf and erg[19] == "":
            self.statusbar.showMessage("Fehler: Die Ausstiegshaltestelle bei Nachlauf 1 fehlt!")
        elif erg[20] in lauf and erg[21] == "":
            self.statusbar.showMessage("Fehler: Die Ausstiegshaltestelle bei Nachlauf 2 fehlt!")
        elif erg[8] + erg[9] + erg[10] + erg[11] == 0 :
            self.statusbar.showMessage("Fehler: Anzahl der Reisenden ist zu niedrig.")
        else:
            self.statusbar.showMessage("Pr??fung: Kein Fehler gefunden")
        # Soll auch mit Fehlern weiter gehen.
        self.buttonWeiter.setEnabled(True)

def abfahrt():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
