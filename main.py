import sys
from PyQt5.QtWidgets import QApplication
from backend.login import LoginFormWindow

app = QApplication(sys.argv)
login = LoginFormWindow()
sys.exit(app.exec_())
