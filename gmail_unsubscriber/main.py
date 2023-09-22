import typing
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, uic
from PyQt5.QtWidgets import QWidget
import sys
import os

if getattr(sys, 'frozen', False):
    RELATIVE_PATH = os.path.dirname(sys.executable)
else:
    RELATIVE_PATH = os.path.dirname(__file__)


class MainGui(QMainWindow):

    def __init__(self) -> None:
        super(MainGui, self).__init__()
        self._ui_path = RELATIVE_PATH
        uic.loadUi(os.path.join(self._ui_path, 'login_form.ui'), self)
        self.show()
        self.setFixedSize(self.size())


def check_credentials(self):
    # For demonstration purposes, let's assume the correct credentials are:
    # Username: admin
    # Password: password123
    pass

def main():
    app = QApplication([])
    window = MainGui()
    app.exec_()

if __name__ == "__main__":
    main()

