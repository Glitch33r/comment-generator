from PyQt5 import QtCore, QtWidgets


class Ui_addPhrase:
    def setupUi(self, MainWindow, username):
        self.user__name = username.split('_')[0]

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.data = QtWidgets.QTreeWidget(self.centralwidget)
        self.data.setGeometry(QtCore.QRect(10, 10, 781, 401))
        self.data.setObjectName("data")
        self.c_buttons = QtWidgets.QComboBox(self.centralwidget)
        self.c_buttons.setGeometry(QtCore.QRect(20, 430, 161, 22))
        self.c_buttons.setObjectName("c_buttons")
        self.c_lang = QtWidgets.QComboBox(self.centralwidget)
        self.c_lang.setGeometry(QtCore.QRect(20, 470, 81, 22))
        self.c_lang.setObjectName("c_lang")
        self.c_lang.addItem('ru')
        self.c_lang.addItem('ua')
        self.phrase = QtWidgets.QTextEdit(self.centralwidget)
        self.phrase.setGeometry(QtCore.QRect(260, 430, 481, 91))
        self.phrase.setObjectName("phrase")
        self.user_name = QtWidgets.QLabel(self.centralwidget)
        self.user_name.setGeometry(QtCore.QRect(90, 510, 111, 21))
        self.user_name.setObjectName("user_name")
        self.user_name.setText(self.user__name)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 510, 61, 21))
        self.label_2.setObjectName("label_2")
        self.insert_phrase = QtWidgets.QPushButton(self.centralwidget)
        self.insert_phrase.setGeometry(QtCore.QRect(40, 552, 91, 31))
        self.insert_phrase.setObjectName("insert_phrase")
        MainWindow.setCentralWidget(self.centralwidget)
        self.data.headerItem().setHidden(True)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("Add custom comment")
        self.label_2.setText("Username:")
        self.insert_phrase.setText("Добавить")


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_addPhrase()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
