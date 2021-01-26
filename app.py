import sys
import os

from configparser import ConfigParser

from PySide2 import QtCore, QtGui
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

from PetrolConverter import Ui_ConvertWindow
from RON95Clickable import RON95Clickable
from DieselClickable import DieselClickable



class PetrolConverterApp(QMainWindow, Ui_ConvertWindow):
    def __init__(self):
        QMainWindow.__init__(self,None,Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint | Qt.WindowTitleHint)

        self.ui = Ui_ConvertWindow()
        self.ui.setupUi(self)
        self.iniFile = "petrol_config.ini"
        self.config = ConfigParser()
        self.config.read(self.iniFile)

        self.init_config()
        self.ui.centralwidget.setWindowTitle("")

        self.ui.warningLabel.setText("")
        self.ui.priceEdit.setStyleSheet("color: blue;")
        self.ui.ron95PriceEdit.setStyleSheet("color: green;")
        self.ui.dieselEdit.setStyleSheet("color: green;")
        self.ui.ron95DisplayEdit.setReadOnly(True)
        self.ui.dieselDisplayEdit.setReadOnly(True)
        self.read_config()

        # self.saveLbl = SaveLabel(self)
        self.clickREdit = RON95Clickable(self.ui.warningLabel)
        self.clickDEdit = DieselClickable(self.ui.warningLabel)
        self.ui.priceEdit.textChanged.connect(self.convert_to_litres)
        self.ui.saveBtn.clicked.connect(self.write_config)
        self.ui.pushButton.clicked.connect(lambda x: sys.exit(0))


    def convert_to_litres(self):

        try:
            price = float(self.ui.priceEdit.text())
            self.ui.warningLabel.setVisible(True)
            if price != 0:
                self.ui.warningLabel.setText("")
                ron95_price = round(price / float(self.ui.ron95PriceEdit.text()),3)
                # ron97_price = round(price / float(self.ui.ron97Edit.text()),3)
                diesel_price = round(price / float(self.ui.dieselEdit.text()),3)
                self.ui.ron95DisplayEdit.setText(str(ron95_price))
                # self.ui.ron97DisplayEdit.setText(str(ron97_price))
                self.ui.dieselDisplayEdit.setText(str(diesel_price))
            elif price == 0:
                self.ui.warningLabel.setVisible(True)
                self.ui.warningLabel.setText("Unable to divide by 0")
                self.ui.warningLabel.setStyleSheet("color: rgb(255, 0, 0);")
        except ValueError:
            self.ui.warningLabel.setVisible(True)
            self.ui.warningLabel.setText("Please type in number format")
            self.ui.warningLabel.setStyleSheet("color: rgb(255, 0, 0);")

    def init_config(self):
        if not os.path.exists(self.iniFile):
            self.config.add_section('Values')
            self.config.set('Values', 'ron95', "0")
            self.config.set('Values', 'diesel', "0")

            with open(self.iniFile, 'w') as f:
                self.config.write(f)
        else:
            pass


    def read_config(self):
        self.ui.ron95PriceEdit.setText(self.config.get('Values', 'ron95'))
        self.ui.dieselEdit.setText(self.config.get('Values', 'diesel'))

    def write_config(self):
        self.ui.warningLabel.setText("")
        r95_value = self.ui.ron95PriceEdit.text()
        dies_value = self.ui.dieselEdit.text()
        if r95_value != "" and dies_value != "":
            self.config.set('Values', 'ron95', r95_value)
            self.config.set('Values', 'diesel', dies_value)
            with open(self.iniFile, 'w') as f:
                self.config.write(f)
        self.ui.warningLabel.setText("Settings saved")


    def show_message_box(self, title, text, icon):
        msgbox = QMessageBox()
        msgbox.setWindowTitle(title)
        msgbox.setText(text)
        msgbox.setIcon(icon)
        msgbox.exec_()



def run_app():
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = PetrolConverterApp()
    ui.setupUi(window)
    ui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    run_app()
