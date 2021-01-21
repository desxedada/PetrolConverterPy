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

from ClickableLineEdit import ClickableLineEdit


class Ui_ConvertWindow(object):
    def setupUi(self, ConvertWindow):
        if not ConvertWindow.objectName():
            ConvertWindow.setObjectName(u"ConvertWindow")
        ConvertWindow.resize(336, 218)
        ConvertWindow.setMinimumSize(QSize(336, 218))
        ConvertWindow.setMaximumSize(QSize(336, 218))
        ConvertWindow.setContextMenuPolicy(Qt.NoContextMenu)
        ConvertWindow.setStyleSheet(u"font: 75 10.5pt \"MS Shell Dlg 2\";")
        self.centralwidget = QWidget(ConvertWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(336, 196))
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.dieselEdit = QLineEdit(self.groupBox)
        self.dieselEdit.setObjectName(u"dieselEdit")

        self.gridLayout_3.addWidget(self.dieselEdit, 4, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 2, 2, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 4, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 1)

        self.priceEdit = QLineEdit(self.groupBox)
        self.priceEdit.setObjectName(u"priceEdit")

        self.gridLayout_3.addWidget(self.priceEdit, 0, 1, 1, 3)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.ron95PriceEdit = QLineEdit(self.groupBox)
        self.ron95PriceEdit.setObjectName(u"ron95PriceEdit")

        self.gridLayout_3.addWidget(self.ron95PriceEdit, 1, 1, 1, 1)

        self.ron97Edit = QLineEdit(self.groupBox)
        self.ron97Edit.setObjectName(u"ron97Edit")

        self.gridLayout_3.addWidget(self.ron97Edit, 2, 1, 1, 1)

        self.ron95DisplayEdit = ClickableLineEdit(self.groupBox)
        self.ron95DisplayEdit.setObjectName(u"ron95DisplayEdit")
        self.ron95DisplayEdit.setFocusPolicy(Qt.TabFocus)
        self.ron95DisplayEdit.setStyleSheet(u"background-color: transparent")
        self.ron95DisplayEdit.setReadOnly(True)

        self.gridLayout_3.addWidget(self.ron95DisplayEdit, 1, 4, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 4, 2, 1, 1)

        self.ron97DisplayEdit = ClickableLineEdit(self.groupBox)
        self.ron97DisplayEdit.setObjectName(u"ron97DisplayEdit")
        self.ron97DisplayEdit.setStyleSheet(u"background-color: transparent")
        self.ron97DisplayEdit.setReadOnly(True)

        self.gridLayout_3.addWidget(self.ron97DisplayEdit, 2, 4, 1, 1)

        self.dieselDisplayEdit = QLineEdit(self.groupBox)
        self.dieselDisplayEdit.setObjectName(u"dieselDisplayEdit")
        self.dieselDisplayEdit.setStyleSheet(u"background-color: transparent")
        self.dieselDisplayEdit.setReadOnly(True)

        self.gridLayout_3.addWidget(self.dieselDisplayEdit, 4, 4, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 1, 2, 1, 1)

        self.saveButton = QPushButton(self.groupBox)
        self.saveButton.setObjectName(u"saveButton")

        self.gridLayout_3.addWidget(self.saveButton, 5, 1, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        ConvertWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(ConvertWindow)
        self.statusbar.setObjectName(u"statusbar")
        ConvertWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ConvertWindow)

        QMetaObject.connectSlotsByName(ConvertWindow)
    # setupUi

    def retranslateUi(self, ConvertWindow):
        ConvertWindow.setWindowTitle(QCoreApplication.translate("ConvertWindow", u"Price to Petrol Converter", None))
        self.groupBox.setTitle(QCoreApplication.translate("ConvertWindow", u"Converter", None))
        self.label_6.setText(QCoreApplication.translate("ConvertWindow", u"To", None))
        self.label_2.setText(QCoreApplication.translate("ConvertWindow", u"RON95", None))
        self.label_4.setText(QCoreApplication.translate("ConvertWindow", u"Diesel", None))
        self.label_3.setText(QCoreApplication.translate("ConvertWindow", u"RON97", None))
        self.label.setText(QCoreApplication.translate("ConvertWindow", u"Petrol Price", None))
        self.label_7.setText(QCoreApplication.translate("ConvertWindow", u"To", None))
        self.label_5.setText(QCoreApplication.translate("ConvertWindow", u"To", None))
        self.saveButton.setText(QCoreApplication.translate("ConvertWindow", u"Save", None))
    # retranslateUi

