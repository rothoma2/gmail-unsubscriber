import typing
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, uic
from PyQt5.QtWidgets import QWidget
from functools import partial
import sys
import os

if getattr(sys, 'frozen', False):
    RELATIVE_PATH = os.path.dirname(sys.executable)
else:
    RELATIVE_PATH = os.path.dirname(__file__)

def attempt_login(MainForm) -> None:
    email = MainForm.txt_email.text()
    password = MainForm.txt_password.text()
    if email == "user" and password == "pass":
        print("Login Success")
    MainForm.unsubscribe_form.show()
    MainForm.hide()


class MainForm(QMainWindow):

    def __init__(self) -> None:
        super(MainForm, self).__init__()
        self._ui_path = RELATIVE_PATH
        uic.loadUi(os.path.join(self._ui_path, 'login_form.ui'), self)
        self.unsubscribe_form = UnsubscribeForm(self)
        self.unsubscribe_form.hide()
        #self.btn_login.clicked.connect(self.btn_login_clicked)
        login_func = partial(attempt_login, self)
        self.btn_login.clicked.connect(login_func)
        self.show()
        self.setFixedSize(self.size())

    def btn_login_clicked(self):
        email = self.txt_email.text()
        password = self.txt_password.text()

class UnsubscribeForm(QDialog):

    def __init__(self, parent) -> None:
        super(UnsubscribeForm, self).__init__()
        self._ui_path = RELATIVE_PATH
        uic.loadUi(os.path.join(self._ui_path, 'unsubscribe_form.ui'), self)
        self.hide()

    def btn_login_clicked(self):
        email = self.txt_email.text()
        password = self.txt_password.text()
        attempt_login(email, password)




def main():
    app = QApplication([])
    window = MainForm()
    app.exec_()

if __name__ == "__main__":
    main()

