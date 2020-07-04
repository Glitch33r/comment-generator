from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, username, password):
        self.username = username
        self.password = password

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 700)
        MainWindow.setMinimumSize(QtCore.QSize(900, 700))
        MainWindow.setMaximumSize(QtCore.QSize(900, 700))

        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.group_list = QtWidgets.QListWidget(self.centralwidget)
        self.group_list.setGeometry(QtCore.QRect(10, 60, 91, 291))
        self.group_list.setObjectName("group_list")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setGeometry(QtCore.QRect(10, 0, 91, 51))
        self.label.setObjectName("label")
        self.student_list = QtWidgets.QListWidget(self.centralwidget)
        self.student_list.setGeometry(QtCore.QRect(160, 60, 301, 291))
        self.student_list.setObjectName("student_list")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 0, 301, 51))
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(520, 10, 361, 41))
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.subject_list = QtWidgets.QListWidget(self.centralwidget)
        self.subject_list.setGeometry(QtCore.QRect(500, 60, 371, 111))
        self.subject_list.setObjectName("subject_list")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(520, 170, 361, 51))
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 370, 141, 41))
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 430, 31, 21))
        self.label_6.setObjectName("label_6")
        self.student_name_field = QtWidgets.QLineEdit(self.centralwidget)
        self.student_name_field.setGeometry(QtCore.QRect(40, 430, 91, 20))
        self.student_name_field.setObjectName("student_name_field")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 360, 891, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(140, 370, 20, 331))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 470, 41, 21))
        self.label_7.setObjectName("label_7")
        self.group_label_info = QtWidgets.QLabel(self.centralwidget)
        self.group_label_info.setGeometry(QtCore.QRect(60, 470, 81, 21))
        self.group_label_info.setText("")
        self.group_label_info.setAlignment(QtCore.Qt.AlignCenter)
        self.group_label_info.setObjectName("group_label_info")
        self.subject_label_info = QtWidgets.QLabel(self.centralwidget)
        self.subject_label_info.setGeometry(QtCore.QRect(10, 530, 131, 31))
        self.subject_label_info.setText("")
        self.subject_label_info.setAlignment(QtCore.Qt.AlignCenter)
        self.subject_label_info.setObjectName("subject_label_info")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 500, 51, 21))
        self.label_10.setObjectName("label_10")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(0, 570, 151, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gen_comment = QtWidgets.QPushButton(self.centralwidget)
        self.gen_comment.setGeometry(QtCore.QRect(10, 590, 121, 41))
        self.gen_comment.setStyleSheet("background-color:rgb(200, 200, 200);")
        self.gen_comment.setObjectName("gen_comment")
        self.send_comment = QtWidgets.QPushButton(self.centralwidget)
        self.send_comment.setGeometry(QtCore.QRect(10, 640, 121, 41))
        self.send_comment.setStyleSheet("background-color:rgb(255, 69, 72);")
        self.send_comment.setObjectName("send_comment")
        self.text_comment = QtWidgets.QTextEdit(self.centralwidget)
        self.text_comment.setGeometry(QtCore.QRect(170, 420, 371, 241))
        self.text_comment.setObjectName("text_comment")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(440, 380, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(650, 670, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        font.setItalic(True)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(840, 10, 41, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(570, 470, 291, 170))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.irresponsible = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.irresponsible.setObjectName("irresponsible")
        self.gridLayout.addWidget(self.irresponsible, 5, 0, 1, 1)
        self.curious = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.curious.setObjectName("curious")
        self.gridLayout.addWidget(self.curious, 3, 0, 1, 1)
        self.good_theme = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.good_theme.setObjectName("good_theme")
        self.gridLayout.addWidget(self.good_theme, 2, 0, 1, 1)
        self.responsible = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.responsible.setObjectName("responsible")
        self.gridLayout.addWidget(self.responsible, 1, 0, 1, 1)
        self.bad_hw = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.bad_hw.setObjectName("bad_hw")
        self.gridLayout.addWidget(self.bad_hw, 4, 0, 1, 1)
        self.smart = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.smart.setObjectName("smart")
        self.gridLayout.addWidget(self.smart, 2, 2, 1, 1)
        self.active = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.active.setObjectName("active")
        self.gridLayout.addWidget(self.active, 1, 2, 1, 1)
        self.bad_action = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.bad_action.setObjectName("bad_action")
        self.gridLayout.addWidget(self.bad_action, 3, 2, 1, 1)
        self.creative = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.creative.setObjectName("creative")
        self.gridLayout.addWidget(self.creative, 5, 2, 1, 1)
        self.good_hw = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.good_hw.setObjectName("good_hw")
        self.gridLayout.addWidget(self.good_hw, 4, 2, 1, 1)
        self.good_action = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.good_action.setObjectName("good_action")
        self.gridLayout.addWidget(self.good_action, 6, 0, 1, 1)
        self.hardworker = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.hardworker.setObjectName("hardworker")
        self.gridLayout.addWidget(self.hardworker, 6, 2, 1, 1)
        self.distracted = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.distracted.setObjectName("distracted")
        self.gridLayout.addWidget(self.distracted, 7, 0, 1, 1)
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(500, 220, 371, 131))
        self.treeWidget.setObjectName("treeWidget")
        self.ua_lang = QtWidgets.QRadioButton(self.centralwidget)
        self.ua_lang.setGeometry(QtCore.QRect(765, 390, 105, 17))
        self.ua_lang.setObjectName("ua_lang")
        # icon = QtGui.QIcon('ua.png')
        # self.ua_lang.setIcon(icon)
        self.ru_lang = QtWidgets.QRadioButton(self.centralwidget)
        self.ru_lang.setGeometry(QtCore.QRect(765, 420, 105, 17))
        self.ru_lang.setObjectName("ru_lang")
        # icon = QtGui.QIcon('ru.png')
        # self.ru_lang.setIcon(icon)
        self.ru_lang.setChecked(True)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.treeWidget.headerItem().setHidden(True)
        self.text_comment.setReadOnly(True)


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("Logbook comments")
        self.label.setText("Доступные\nГруппы")
        self.label_2.setText("Выберите студента")
        self.label_3.setText("Выберите предмет")
        self.label_4.setText("Существующие отзывы")
        self.label_5.setText("Блок информации")
        self.label_6.setText("Имя:")
        self.label_7.setText( "Группа:")
        self.label_10.setText("Предмет:")
        self.gen_comment.setText("Сгенерировать отзыв")
        self.send_comment.setText("Отправить отзыв")
        self.label_11.setText("Создать отзыв")
        self.label_12.setText("Developed by GendalfBlack, Glitch33r")
        self.label_13.setText("v1.2.0")
        self.irresponsible.setText("Безответственный")
        self.curious.setText("Любознательный")
        self.good_theme.setText("Отлично\nразобрался в теме")
        self.responsible.setText("Отвественный")
        self.bad_hw.setText("Не выполняет дз")
        self.smart.setText("Умный")
        self.active.setText("Активный")
        self.bad_action.setText("Полохое поведение")
        self.creative.setText("Креативный")
        self.good_hw.setText("Положительное дз")
        self.good_action.setText("Положительное поведение")
        self.hardworker.setText("Трудолюбивость")
        self.distracted.setText("Отвлекается")
        self.treeWidget.headerItem().setText(0, "Комментарии")
        self.ua_lang.setText("Украинский")
        self.ru_lang.setText("Русский")
