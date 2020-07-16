import random

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QTreeWidgetItem, QMessageBox

from logbook_connection import CommentBot
from ui.ui_commentform import Ui_MainWindow
from .add_phrase import InsertFormWindow

# from .phrases import PHRASES

bot = CommentBot()
groups = []
students = []
subjects = []
for_send = {
    "group": 0,
    "stud": 0,
    "spec": 0
}


class GeneratorFormWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, username, password, db):
        super(GeneratorFormWindow, self).__init__()
        self.setupUi(self, username, password)
        self.show()

        bot.login(self.username, self.password)
        self.language = 'ru'
        self.use = 1
        self.db = db

        self.checkboxes = {
            'responsible': self.irresponsible,
            'irresponsible': self.responsible,
            'bad_action': self.good_action,
            'good_action': self.bad_action,
            'bad_hw': self.good_hw,
            'good_hw': self.bad_hw,
            'active': self.distracted,
            'distracted': self.active,
        }

        self.set_groups()
        self.special = InsertFormWindow(self.username, db)
        self.group_list.itemSelectionChanged.connect(self.group_changed)
        self.student_list.itemSelectionChanged.connect(self.student_changed)
        self.subject_list.itemSelectionChanged.connect(self.subject_changed)
        self.gen_comment.clicked.connect(self.generate_comment)
        self.send_comment.clicked.connect(self.send)
        self.add_phrase.clicked.connect(self.add_phrase_window)
        self.ua_lang.toggled.connect(self.changeLanguageToUa)
        self.ru_lang.toggled.connect(self.changeLanguageToRu)
        self.all_phrases.toggled.connect(self.changeUseToAll)
        self.own_phrases.toggled.connect(self.changeUseToOwn)

        self.responsible.stateChanged.connect(
            lambda state=self.responsible.isChecked(), elem=self.responsible.objectName(): self.changeCheckBoxState(
                state, elem))
        self.irresponsible.stateChanged.connect(
            lambda state=self.irresponsible.isChecked(), elem=self.irresponsible.objectName(): self.changeCheckBoxState(
                state, elem))
        self.bad_action.stateChanged.connect(
            lambda state=self.bad_action.isChecked(), elem=self.bad_action.objectName(): self.changeCheckBoxState(state,
                                                                                                                  elem))
        self.good_action.stateChanged.connect(
            lambda state=self.good_action.isChecked(), elem=self.good_action.objectName(): self.changeCheckBoxState(
                state, elem))
        self.bad_hw.stateChanged.connect(
            lambda state=self.bad_hw.isChecked(), elem=self.bad_hw.objectName(): self.changeCheckBoxState(state, elem))
        self.good_hw.stateChanged.connect(
            lambda state=self.good_hw.isChecked(), elem=self.good_hw.objectName(): self.changeCheckBoxState(state,
                                                                                                            elem))
        self.active.stateChanged.connect(
            lambda state=self.active.isChecked(), elem=self.active.objectName(): self.changeCheckBoxState(state, elem))
        self.distracted.stateChanged.connect(
            lambda state=self.distracted.isChecked(), elem=self.distracted.objectName(): self.changeCheckBoxState(state,
                                                                                                                  elem))

    def changeCheckBoxState(self, toggle, elem):
        if toggle == QtCore.Qt.Checked:
            if elem in self.checkboxes.keys():
                self.checkboxes[elem].setEnabled(False)
        elif toggle == QtCore.Qt.Unchecked:
            if elem in self.checkboxes.keys():
                self.checkboxes[elem].setEnabled(True)

    def changeLanguageToRu(self, selected):
        if selected:
            self.language = 'ru'

    def changeLanguageToUa(self, selected):
        if selected:
            self.language = 'ua'

    def changeUseToAll(self, selected):
        if selected:
            self.use = 1

    def changeUseToOwn(self, selected):
        if selected:
            self.use = 0

    def generate_comment(self):
        self.text_comment.clear()
        comment = ''
        if self.use:
            PHRASES = self.db.get_phrases_by_lang(self.language)
            print('ALL\n', PHRASES)
        else:
            PHRASES = self.db.get_phrases_by_user_and_lang(self.username.split('_')[0], self.language)
            print('By User\n', PHRASES)

        if self.responsible.isChecked():
            comment += random.choice(PHRASES.get('responsible', [''])) + ". "
        if self.active.isChecked():
            comment += random.choice(PHRASES.get('active', [''])) + ". "
        if self.good_theme.isChecked():
            comment += random.choice(PHRASES.get('good_theme', [''])) + ". "
        if self.smart.isChecked():
            comment += random.choice(PHRASES.get('smart', [''])) + ". "
        if self.curious.isChecked():
            comment += random.choice(PHRASES.get('curious', [''])) + ". "
        if self.bad_action.isChecked():
            comment += random.choice(PHRASES.get('bad_action', [''])) + ". "
        if self.bad_hw.isChecked():
            comment += random.choice(PHRASES.get('bad_hw', [''])) + ". "
        if self.good_hw.isChecked():
            comment += random.choice(PHRASES.get('good_hw', [''])) + ". "
        if self.irresponsible.isChecked():
            comment += random.choice(PHRASES.get('irresponsible', [''])) + ". "
        if self.creative.isChecked():
            comment += random.choice(PHRASES.get('creative', [''])) + ". "
        if self.good_action.isChecked():
            comment += random.choice(PHRASES.get('good_action', [''])) + ". "
        if self.hardworker.isChecked():
            comment += random.choice(PHRASES.get('hardworker', [''])) + ". "
        if self.distracted.isChecked():
            comment += random.choice(PHRASES.get('distracted', [''])) + ". "

        if comment == '':
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Comment generation")
            msg.setText("Вы не выбрали ни одного критерия. Генерация невозможна :(")
            msg.exec_()
        else:
            self.text_comment.setReadOnly(False)

        self.text_comment.setText(comment)

    def send(self):
        if all(v != 0 for v in for_send.values()) and self.text_comment.toPlainText() != '':
            result = bot.send_comment(
                str(for_send['group']),
                str(for_send['stud']),
                for_send['spec'],
                self.text_comment.toPlainText()
            )
            if result:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Comment sending")
                msg.setText(
                    "Комментарий успешно добавлен!\nПри желании можете сделать проверку в Logbook!\n"
                    "\nСпасибо за использовние нашей разработки!"
                )
                msg.exec_()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Comment sending")
                msg.setText(
                    "Упс.. Что-то пошло не так :(\nПроверьте все данные и попробуйте еще раз, или попробуйте позже."
                )
                msg.exec_()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Comment sending")
            msg.setText(
                "Вы не выбрали один из елементов: группа, студент, предмет или комментарий.\nОтправка невозможна :("
            )
            msg.exec_()

    def set_groups(self):
        for i in bot.get_groups():
            groups.append(i)
            self.group_list.addItem(i['name'])

    def group_changed(self):
        current_item = self.group_list.currentItem().text()
        self.group_label_info.setText(current_item)
        for item in groups:
            if item['name'] == current_item:
                idx = item['id']

        for_send['group'] = str(idx)
        self.set_students(idx)

    def set_students(self, _id):
        self.student_list.clear()
        students.clear()
        for i in bot.get_students_of_group(_id):
            students.append(i)
            self.student_list.addItem(i['name'])

    def student_changed(self):
        current_item = self.student_list.currentItem().text()
        self.student_name_field.setText(current_item.split(' ')[1])
        for item in students:
            if item['name'] == current_item:
                idx = item['id']

        for_send['stud'] = str(idx)
        self.set_subjects(idx)
        self.set_comments(idx)

    def set_subjects(self, _id):
        self.subject_list.clear()
        subjects.clear()
        for i in bot.get_subjects_for_group(_id):
            subjects.append(i)
            self.subject_list.addItem(i['name'])

    def set_comments(self, _id):
        self.treeWidget.clear()
        for idx, i in enumerate(bot.get_student_comments(_id)):
            topItem = QTreeWidgetItem(self.treeWidget)
            topItem.setText(0, i['teacher'])
            subject = QTreeWidgetItem(topItem)
            subject.setText(0, f"Предмет: {i['subject']}")
            comment = QTreeWidgetItem(topItem)
            comment.setText(0, "\n".join(i["comment"].split(".")))

    def subject_changed(self):
        current_item = self.subject_list.currentItem().text()
        self.subject_label_info.setText("\n".join(current_item.split(" ")))
        for item in subjects:
            if item['name'] == current_item:
                idx = item['id']

        for_send['spec'] = int(idx)

    def add_phrase_window(self):
        self.special.show()


