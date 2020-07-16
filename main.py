import configparser
import sys

from PyQt5.QtWidgets import QApplication

from backend.db import DB
from backend.login import LoginFormWindow

config = configparser.ConfigParser()
config.read('.config.ini')

db = DB(
    config["database"]['dbname'],
    config["database"]['user'],
    config["database"]['password'],
    config["database"]['host']
)
db.connect()


app = QApplication(sys.argv)
app.setStyle('Fusion')
login = LoginFormWindow(db)
sys.exit(app.exec_())
