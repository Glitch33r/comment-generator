import random
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QTreeWidgetItem, QMessageBox
from ui.ui_commentform import Ui_MainWindow
from logbook_connection import CommentBot

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

        self.responsible.stateChanged.connect(
            lambda state=self.responsible.isChecked(), elem=self.responsible.objectName(): self.changeCheckBoxState(state, elem))
        self.irresponsible.stateChanged.connect(
            lambda state=self.irresponsible.isChecked(), elem=self.irresponsible.objectName(): self.changeCheckBoxState(state, elem))
        self.bad_action.stateChanged.connect(
            lambda state=self.bad_action.isChecked(), elem=self.bad_action.objectName(): self.changeCheckBoxState(state, elem))
        self.good_action.stateChanged.connect(
            lambda state=self.good_action.isChecked(), elem=self.good_action.objectName(): self.changeCheckBoxState(state, elem))
        self.bad_hw.stateChanged.connect(
            lambda state=self.bad_hw.isChecked(), elem=self.bad_hw.objectName(): self.changeCheckBoxState(state, elem))
        self.good_hw.stateChanged.connect(
            lambda state=self.good_hw.isChecked(), elem=self.good_hw.objectName(): self.changeCheckBoxState(state, elem))
        self.active.stateChanged.connect(
            lambda state=self.active.isChecked(), elem=self.active.objectName(): self.changeCheckBoxState(state, elem))
        self.distracted.stateChanged.connect(
            lambda state=self.distracted.isChecked(), elem=self.distracted.objectName(): self.changeCheckBoxState(state, elem))

    def changeCheckBoxState(self, toggle, elem):
        if toggle == QtCore.Qt.Checked:
            if elem in self.checkboxes.keys():
                self.checkboxes[elem].setEnabled(False)
        elif toggle == QtCore.Qt.Unchecked:
            if elem in self.checkboxes.keys():
                self.checkboxes[elem].setEnabled(True)

    def generate_comment(self):
        self.text_comment.clear()
        comment = ''
        if self.responsible.isChecked():
            comment += random.choice(
                ["Прекрасно проявил себя на занятиях",
                 "Отлично проявляет себя на занятиях",
                 "Замечательно проявил себя в данном блоке",
                 "Ответственно отнесся к блоку",
                 "Проявил себя как ответственный студент"]
            ) + ". "
        if self.active.isChecked():
            comment += random.choice(
                ["Проявляет себя заинтересованным и всегда вовлечен в работу",
                 "Берет участие в любой активности, отвечая на вопросы и предоставляя хорошие идеи",
                 "Быстро справляется с любыми заданиями на отлично!"]
            ) + ". "
        if self.good_theme.isChecked():
            comment += random.choice(
                ["Усвоение материала не вызвало никаких проблем",
                 "С легкостью разобрался со всем материалом блока",
                 "Студент с легкостью смог разобраться в теме и может использовать полученные знания самостоятельно"]
            ) + ". "
        if self.smart.isChecked():
            comment += random.choice(
                ["Студент самостоятельно может применять знания и использовать их в нестандартных ситуациях",
                 "Может самостоятельно работать над более сложными проектами",
                 "Является одним из лучших в группе!",
                 'В числе первых справляется с заданиями, всегда выполняя работу на "отлично"',
                 "Является примером для всей группы"]
            ) + ". "
        if self.curious.isChecked():
            comment += random.choice(
                ["У студента крайне пытливый ум, что помогает ему справляться с любыми заданиями",
                 "Всегда задает интересные вопросы",
                 "Всегда заинтересован в дополнительных знаниях по теме"]
            ) + ". "
        if self.bad_action.isChecked():
            comment += random.choice(
                ["Поведение оставляет желать лучшего",
                 "Стоит больше внимания уделить поведению"]
            ) + ". "
        if self.bad_hw.isChecked():
            comment += random.choice(
                ["К сожалению, следует больше внимания уделить домашним заданиям",
                 "Больше внимания к домашним заданиям, т.к. с ними есть проблемы",
                 "Следует больше внимания уделять домашним заданиям"]
            ) + ". "
        if self.good_hw.isChecked():
            comment += random.choice(
                ["Всегда сдает домашние задания на отлично",
                 "Домашние задания всегда верны и сданы вовремя",
                 "Работа над домашними заданиями вызывает только восторг",
                 "Домашние задания всегда выполнены на высшем уровне"]
            ) + ". "
        if self.irresponsible.isChecked():
            comment += random.choice(
                ["К изучению темы подошел спустя рукава. Работы сделаны очень поверхностно",
                 "К сожалению, работа на парах не воспринимается должным образом",
                 "Плохо работает на парах, что ведет к соответствующим оценкам"]
            ) + ". "
        if self.creative.isChecked():
            comment += random.choice(
                ["Предоставлял оригинальные работы, подходя к каждой теме максимально креативно",
                 "Оригинально подходит к заданиям", "Всегда находит оригинальные решения",
                 "Выделяется нестандартными работами на фоне группы",
                 "Часто выделяется из группы нестандартным подходом",
                 "Креативно выполняет все работы, о чем могут сказать отличные оценки"]
            ) + ". "
        if self.good_action.isChecked():
            comment += random.choice(
                ["Является примером поведения для всей группы",
                 "Поведение на парах претензий не вызывает :)",
                 "Поведение на парах всегда отличное"]
            ) + ". "
        if self.hardworker.isChecked():
            comment += random.choice(
                ["Усердно работал над каждой темой",
                 "Каждая из работ стоит отдельного внимания",
                 "Каждая из работ студента выполнена идеально",
                 "Работа на парах всегда на высоте",
                 "На каждом уроке выкладывался на полную",
                 "Провел достойную работу над каждым из своих проектов"]
            ) + ". "
        if self.distracted.isChecked():
            comment += random.choice(
                ["Часто переключает внимание на посторонние темы и не может включиться в работу",
                 "Задает интересные вопросы, однако не всегда по теме",
                 "Может отвлекаться на посторонние разговоры или другую деятельность"]
            ) + ". "

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
