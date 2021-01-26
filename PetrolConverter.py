# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PetrolConverter.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from DieselClickable import DieselClickable
from RON95Clickable import RON95Clickable


class Ui_ConvertWindow(object):
    def setupUi(self, ConvertWindow):
        if not ConvertWindow.objectName():
            ConvertWindow.setObjectName(u"ConvertWindow")
        ConvertWindow.resize(224, 141)
        ConvertWindow.setMinimumSize(QSize(212, 141))
        ConvertWindow.setMaximumSize(QSize(1184, 633))
        ConvertWindow.setContextMenuPolicy(Qt.NoContextMenu)
        ConvertWindow.setStyleSheet(u"font: 75 10.5pt \"MS Shell Dlg 2\";")
        ConvertWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        ConvertWindow.setAnimated(False)
        ConvertWindow.setDocumentMode(False)
        ConvertWindow.setTabShape(QTabWidget.Rounded)
        ConvertWindow.setDockNestingEnabled(False)
        self.centralwidget = QWidget(ConvertWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(111111, 111111))
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.dieselDisplayEdit = DieselClickable(self.centralwidget)
        self.dieselDisplayEdit.setObjectName(u"dieselDisplayEdit")
        self.dieselDisplayEdit.setStyleSheet(u"background-color: transparent")
        self.dieselDisplayEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.dieselDisplayEdit, 2, 4, 1, 2)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 0, 2, 3, 1)

        self.ron95PriceEdit = QLineEdit(self.centralwidget)
        self.ron95PriceEdit.setObjectName(u"ron95PriceEdit")
        self.ron95PriceEdit.setStyleSheet(u"font: 75 12pt \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.ron95PriceEdit, 1, 1, 1, 1)

        self.ron95DisplayEdit = RON95Clickable(self.centralwidget)
        self.ron95DisplayEdit.setObjectName(u"ron95DisplayEdit")
        self.ron95DisplayEdit.setFocusPolicy(Qt.TabFocus)
        self.ron95DisplayEdit.setStyleSheet(u"background-color: transparent")
        self.ron95DisplayEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.ron95DisplayEdit, 1, 4, 1, 2)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.dieselEdit = QLineEdit(self.centralwidget)
        self.dieselEdit.setObjectName(u"dieselEdit")
        self.dieselEdit.setStyleSheet(u"font: 75 12pt \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.dieselEdit, 2, 1, 1, 1)

        self.priceEdit = QLineEdit(self.centralwidget)
        self.priceEdit.setObjectName(u"priceEdit")
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.priceEdit.setFont(font)
        self.priceEdit.setStyleSheet(u"font: 75 12pt \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.priceEdit, 0, 1, 1, 1)

        self.warningLabel = QLabel(self.centralwidget)
        self.warningLabel.setObjectName(u"warningLabel")

        self.gridLayout.addWidget(self.warningLabel, 3, 0, 1, 7)

        self.saveBtn = QPushButton(self.centralwidget)
        self.saveBtn.setObjectName(u"saveBtn")
        self.saveBtn.setStyleSheet(u"QPushButton{border: none;}\n"
"QPushButton:hover{\n"
"	color: rgb(255, 202, 96);\n"
"\n"
"}\n"
"\n"
"QPushButtonl:pressed{\n"
"	color:white\n"
"}")

        self.gridLayout.addWidget(self.saveBtn, 0, 4, 1, 1)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"QPushButton{border: none;}\n"
"QPushButton:hover{\n"
"	color: rgb(255, 202, 96);\n"
"\n"
"}\n"
"\n"
"QPushButtonl:pressed{\n"
"	color:white\n"
"}")

        self.gridLayout.addWidget(self.pushButton, 0, 5, 1, 1)

        ConvertWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(ConvertWindow)
        self.statusbar.setObjectName(u"statusbar")
        ConvertWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ConvertWindow)

        QMetaObject.connectSlotsByName(ConvertWindow)
    # setupUi

    def retranslateUi(self, ConvertWindow):
        ConvertWindow.setWindowTitle("Converter")
        self.label_2.setText(QCoreApplication.translate("ConvertWindow", u"RON95", None))
        self.label_4.setText(QCoreApplication.translate("ConvertWindow", u"Diesel", None))
        self.ron95PriceEdit.setPlaceholderText(QCoreApplication.translate("ConvertWindow", u"0.00", None))
        self.label.setText(QCoreApplication.translate("ConvertWindow", u"$$", None))
        self.dieselEdit.setPlaceholderText(QCoreApplication.translate("ConvertWindow", u"0.00", None))
        self.priceEdit.setPlaceholderText(QCoreApplication.translate("ConvertWindow", u"0.00", None))
        self.warningLabel.setText(QCoreApplication.translate("ConvertWindow", u"WarningMsg", None))
        self.saveBtn.setText(QCoreApplication.translate("ConvertWindow", u"Save", None))
        self.pushButton.setText(QCoreApplication.translate("ConvertWindow", u"Close", None))
    # retranslateUi

