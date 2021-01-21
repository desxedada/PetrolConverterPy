from PySide2 import QtCore
from PySide2.QtWidgets import QLineEdit, QApplication, QMessageBox


class ClickableLineEdit(QLineEdit):
    clicked = QtCore.Signal()

    def __init__(self,parent):
        QLineEdit.__init__(self,parent)

    def mousePressEvent(self, event):
        super(ClickableLineEdit, self).mousePressEvent(event)
        if self.text() != "":
            cb = QApplication.clipboard()
            cb.clear(mode=cb.Clipboard)
            cb.setText(self.text(), mode=cb.Clipboard)
            self.show_message_box("Copied", "Copied to Clipboard", QMessageBox.Information)
        else:
            pass


    def show_message_box(self, title, text, icon):
        msgbox = QMessageBox()
        msgbox.setWindowTitle(title)
        msgbox.setText(text)
        msgbox.setIcon(icon)
        msgbox.exec_()