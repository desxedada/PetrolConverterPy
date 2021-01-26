from PySide2 import QtCore
from PySide2.QtCore import Slot, Signal
from PySide2.QtWidgets import QLineEdit, QApplication, QMessageBox


class DieselClickable(QLineEdit):
    messageSignal = Signal(str)

    def __init__(self,label,parent=None):
        QLineEdit.__init__(self,parent)
        self.label = label


    def mousePressEvent(self, event):
        super(DieselClickable, self).mousePressEvent(event)
        cb = QApplication.clipboard()
        if self.text() != "":
            self.setFocus()
            cb.clear(mode=cb.Clipboard)
            cb.setText(self.text(), mode=cb.Clipboard)
        else:
            pass





