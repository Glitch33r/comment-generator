from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_login_window:
    def setupUi(self, login_window):
        login_window.setObjectName("login_window")
        login_window.resize(380, 300)
        login_window.setMinimumSize(QtCore.QSize(380, 300))
        login_window.setMaximumSize(QtCore.QSize(380, 300))

        font = QtGui.QFont()
        font.setPointSize(12)

        self.username_label = QtWidgets.QLabel(login_window)
        self.username_label.setGeometry(QtCore.QRect(70, 130, 91, 21))
        self.username_label.setFont(font)
        self.username_label.setAlignment(QtCore.Qt.AlignCenter)
        self.username_label.setObjectName("username_label")
        self.password_label = QtWidgets.QLabel(login_window)
        self.password_label.setGeometry(QtCore.QRect(70, 160, 91, 21))
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
        self.login_btn.setFont(font)
        self.login_btn.setObjectName("login_btn")
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
        login_window.setWindowTitle("LogIn to Logbook")
        self.username_label.setText("Username")
        self.password_label.setText("Password")
        self.login_btn.setText("LOGIN")
        self.title_label.setText("LogIn to Logbook")
