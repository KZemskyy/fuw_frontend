
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout
from .views import MainMenu,MeasurementLayout

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        layouts = QHBoxLayout()
        layouts.addLayout(MainMenu())
        layouts.addLayout(MeasurementLayout())
        self.setLayout(layouts)

def app():
    __app = QApplication([])
    win = MyApp()
    win.show()
    __app.exec()

if __name__ == "__main__":
    app()