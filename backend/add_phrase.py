import datetime
import time

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTreeWidgetItem, QMessageBox

from ui.ui_addPhrase import Ui_addPhrase


class InsertFormWindow(QtWidgets.QMainWindow, Ui_addPhrase):

    def __init__(self, username, db):
        super(InsertFormWindow, self).__init__()
        self.setupUi(self, username)

        self.db = db

        time.sleep(3)
        self.set_data()
        self.set_combo_btn()
        self.insert_phrase.clicked.connect(self.insert_into_db)

    def set_data(self):
        self.data.clear()
        records = self.db.get_all_phrases()

        for key, value in records.items():
            who = QTreeWidgetItem(self.data)
            who.setText(0, key)
            for key, value in value.items():
                lang = QTreeWidgetItem(who)
                lang.setText(0, key)
                for key, value in value.items():
                    button = QTreeWidgetItem(lang)
                    button.setText(0, self.db.get_name_by_slug(key))
                    for idx, v in enumerate(value):
                        text = QTreeWidgetItem(button)
                        text.setText(0, v)

    def set_combo_btn(self):
        items = self.db.get_buttons_name()
        self.c_buttons.addItems(items)

    def insert_into_db(self):
        bnt = self.c_buttons.currentText()
        lang = self.c_lang.currentText()
        text = self.phrase.toPlainText()

        if text == '':
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Insertion Error")
            msg.setText("Вы не написали свою фразу..")
            msg.exec_()
        else:
            result = self.db.insert_data_to_phrases(
                (self.db.get_id_by_name('buttons', bnt), self.user__name, text, datetime.date.today(), lang)
            )
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Insertion Message")
            msg.setText(str(result))
            msg.exec_()

        self.phrase.clear()
        self.set_data()
