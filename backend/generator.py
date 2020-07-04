import random
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QTreeWidgetItem, QMessageBox
from ui.ui_commentform import Ui_MainWindow
from logbook_connection import CommentBot
from .phrases import PHRASES

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

    def __init__(self, username, password):
        super(GeneratorFormWindow, self).__init__()
        self.setupUi(self, username, password)
        self.show()

        self.language = 'ru'

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
        self.group_list.itemSelectionChanged.connect(self.group_changed)
        self.student_list.itemSelectionChanged.connect(self.student_changed)
        self.subject_list.itemSelectionChanged.connect(self.subject_changed)
        self.gen_comment.clicked.connect(self.generate_comment)
        self.send_comment.clicked.connect(self.send)
        self.ua_lang.toggled.connect(self.changeLanguageToUa)
        self.ru_lang.toggled.connect(self.changeLanguageToRu)

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

    def generate_comment(self):
        self.text_comment.clear()
        comment = ''
        if self.responsible.isChecked():
            comment += random.choice(PHRASES[self.language]['responsible']) + ". "
        if self.active.isChecked():
            comment += random.choice(PHRASES[self.language]['active']) + ". "
        if self.good_theme.isChecked():
            comment += random.choice(PHRASES[self.language]['good_theme']) + ". "
        if self.smart.isChecked():
            comment += random.choice(PHRASES[self.language]['smart']) + ". "
        if self.curious.isChecked():
            comment += random.choice(PHRASES[self.language]['curious']) + ". "
        if self.bad_action.isChecked():
            comment += random.choice(PHRASES[self.language]['bad_action']) + ". "
        if self.bad_hw.isChecked():
            comment += random.choice(PHRASES[self.language]['bad_hw']) + ". "
        if self.good_hw.isChecked():
            comment += random.choice(PHRASES[self.language]['good_hw']) + ". "
        if self.irresponsible.isChecked():
            comment += random.choice(PHRASES[self.language]['irresponsible']) + ". "
        if self.creative.isChecked():
            comment += random.choice(PHRASES[self.language]['creative']) + ". "
        if self.good_action.isChecked():
            comment += random.choice(PHRASES[self.language]['good_action']) + ". "
        if self.hardworker.isChecked():
            comment += random.choice(PHRASES[self.language]['hardworker']) + ". "
        if self.distracted.isChecked():
            comment += random.choice(PHRASES[self.language]['distracted']) + ". "

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
        bot.login(self.username, self.password)
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
        bot.login(self.username, self.password)
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

    def set_students(self, id):
        self.student_list.clear()
        students.clear()
        bot.login(self.username, self.password)
        for i in bot.get_students_of_group(id):
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

    def set_subjects(self, id):
        self.subject_list.clear()
        subjects.clear()
        bot.login(self.username, self.password)
        for i in bot.get_subjects_for_group(id):
            subjects.append(i)
            self.subject_list.addItem(i['name'])

    def set_comments(self, id):
        self.treeWidget.clear()
        bot.login(self.username, self.password)
        for idx, i in enumerate(bot.get_student_comments(id)):
            topItem = QTreeWidgetItem(self.treeWidget)
            topItem.setText(idx, i['teacher'])
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
