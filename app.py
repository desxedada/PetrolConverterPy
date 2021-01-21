import sys
import os

from configparser import ConfigParser

from PySide2 import QtCore
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

from PetrolConverter import Ui_ConvertWindow
from ClickableLineEdit import ClickableLineEdit


class PetrolConverterApp(QMainWindow, Ui_ConvertWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_ConvertWindow()
        self.ui.setupUi(self)
        self.ui.centralwidget.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint,False)

        self.iniFile = "petrol_config.ini"
        self.config = ConfigParser()
        self.config.read(self.iniFile)

        self.init_config()

        self.ui.ron95DisplayEdit.setReadOnly(True)
        self.ui.ron97DisplayEdit.setReadOnly(True)
        self.ui.dieselDisplayEdit.setReadOnly(True)

        self.read_config()

        self.ui.priceEdit.textChanged.connect(self.convert_to_litres)
        self.ui.saveButton.clicked.connect(self.write_config)

    def convert_to_litres(self):
        price = float(self.ui.priceEdit.text())
        try:
            if price != 0:
                ron95_price = round(price / float(self.ui.ron95PriceEdit.text()),3)
                ron97_price = round(price / float(self.ui.ron97Edit.text()),3)
                diesel_price = round(price / float(self.ui.dieselEdit.text()),3)
                self.ui.ron95DisplayEdit.setText(str(ron95_price))
                self.ui.ron97DisplayEdit.setText(str(ron97_price))
                self.ui.dieselDisplayEdit.setText(str(diesel_price))
            elif price == 0:
                self.show_message_box("", "Unable to divide by 0", QMessageBox.Critical)
        except ValueError:
            self.show_message_box("", "Please type in number format", QMessageBox.Critical)
        except Exception as e:
            self.show_message_box("", f"{e}", QMessageBox.Critical)
            raise e

    def init_config(self):
        if not os.path.exists(self.iniFile):
            self.config.add_section('Values')
            self.config.set('Values', 'ron95', "0")
            self.config.set('Values', 'ron97', "0")
            self.config.set('Values', 'diesel', "0")

            with open(self.iniFile, 'w') as f:
                self.config.write(f)
        else:
            pass


    def read_config(self):
        self.ui.ron95PriceEdit.setText(self.config.get('Values', 'ron95'))
        self.ui.ron97Edit.setText(self.config.get('Values', 'ron97'))
        self.ui.dieselEdit.setText(self.config.get('Values', 'diesel'))

    def write_config(self):
        r95_value = self.ui.ron95PriceEdit.text()
        r97_value = self.ui.ron97Edit.text()
        dies_value =self.ui.dieselEdit.text()
        if r95_value != "" and r97_value != "" and dies_value != "":
            self.config.set('Values', 'ron95', r95_value)
            self.config.set('Values', 'ron97', r97_value)
            self.config.set('Values', 'diesel', dies_value)

            with open(self.iniFile, 'w') as f:
                self.config.write(f)


    def show_message_box(self, title, text, icon):
        msgbox = QMessageBox()
        msgbox.setWindowTitle(title)
        msgbox.setText(text)
        msgbox.setIcon(icon)
        msgbox.exec_()





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
