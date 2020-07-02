from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from backend.generator import GeneratorFormWindow
from logbook_connection import CommentBot
from ui.ui_loginform import Ui_login_window

bot = CommentBot()


class LoginFormWindow(QtWidgets.QMainWindow, Ui_login_window):

    def __init__(self):
        super(LoginFormWindow, self).__init__()
        self.setupUi(self)
        self.show()

        # Connect login button
        self.login_btn.clicked.connect(self.login_button)

    def login_button(self):
        result = bot.login(self.username_lineEdit.text(), self.password_lineEdit.text())

        if result:
            GeneratorFormWindow(self.username_lineEdit.text(), self.password_lineEdit.text())
            self.hide()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Login")
            msg.setText("Your password and/or login are  wrong! Try again")
            msg.exec_()
