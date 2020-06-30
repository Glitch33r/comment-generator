# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginform.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from commentform import Ui_MainWindow
from parse_comment import CommentBot

bot = CommentBot()

class Ui_login_window(object):
    def setupUi(self, login_window):
        login_window.setObjectName("login_window")
        login_window.resize(380, 300)
        login_window.setMinimumSize(QtCore.QSize(380, 300))
        login_window.setMaximumSize(QtCore.QSize(380, 300))
        login_window.setAutoFillBackground(False)
        login_window.setStyleSheet("")
        self.username_label = QtWidgets.QLabel(login_window)
        self.username_label.setGeometry(QtCore.QRect(70, 130, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.username_label.setFont(font)
        self.username_label.setAlignment(QtCore.Qt.AlignCenter)
        self.username_label.setObjectName("username_label")
        self.password_label = QtWidgets.QLabel(login_window)
        self.password_label.setGeometry(QtCore.QRect(70, 160, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.password_label.setFont(font)
        self.password_label.setAlignment(QtCore.Qt.AlignCenter)
        self.password_label.setObjectName("password_label")
        self.username_lineEdit = QtWidgets.QLineEdit(login_window)
        self.username_lineEdit.setGeometry(QtCore.QRect(170, 130, 113, 20))
        self.username_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.username_lineEdit.setObjectName("username_lineEdit")
        self.password_lineEdit = QtWidgets.QLineEdit(login_window)
        self.password_lineEdit.setGeometry(QtCore.QRect(170, 160, 113, 20))
        self.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.login_btn = QtWidgets.QPushButton(login_window)
        self.login_btn.setGeometry(QtCore.QRect(150, 230, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.login_btn.setFont(font)
        self.login_btn.setObjectName("login_btn")

        self.login_btn.clicked.connect(self.login_button)

        self.title_label = QtWidgets.QLabel(login_window)
        self.title_label.setGeometry(QtCore.QRect(70, 40, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setUnderline(True)
        self.title_label.setFont(font)
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName("title_label")

        self.retranslateUi(login_window)
        QtCore.QMetaObject.connectSlotsByName(login_window)

    def retranslateUi(self, login_window):
        _translate = QtCore.QCoreApplication.translate
        login_window.setWindowTitle(_translate("login_window", "LogIn to Logbook"))
        self.username_label.setText(_translate("login_window", "Username"))
        self.password_label.setText(_translate("login_window", "Password"))
        self.login_btn.setText(_translate("login_window", "LOGIN"))
        self.title_label.setText(_translate("login_window", "LogIn to Logbook"))

    def login_button(self):
        result = bot.login(self.username_lineEdit.text(), self.password_lineEdit.text())

        if result:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.window, self.username_lineEdit.text(), self.password_lineEdit.text())
            self.window.show()
            login_window.hide()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Login")
            msg.setText("Your password and/or login are  wrong! Try again")
            msg.exec_()



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    login_window = QtWidgets.QDialog()
    ui = Ui_login_window()
    ui.setupUi(login_window)
    login_window.show()
    sys.exit(app.exec_())
