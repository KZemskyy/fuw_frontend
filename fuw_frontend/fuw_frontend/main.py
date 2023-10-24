
import sys
from PyQt6.QtWidgets import QApplication, QWidget
from .views import MainMenu

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

def app():
    __app = QApplication([])
    win = MyApp()
    win.setLayout(MainMenu())
    win.show()
    __app.exec()