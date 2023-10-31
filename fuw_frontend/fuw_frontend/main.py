
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout
from .Model import Model
from .presenter import Presenter

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.__model = Model()
        self.__presenter = Presenter(self.__model)
        layouts = QHBoxLayout()
        layouts.addLayout(self.__presenter.getListExperemetView())
        experement = QVBoxLayout()
        layouts.addLayout(experement)
        experement.addLayout(self.__presenter.getExperemetView())
        experement.addLayout(self.__presenter.getMeasurementView())
        self.setLayout(layouts)

def app():
    __app = QApplication([])
    win = MyApp()
    win.show()
    __app.exec()

if __name__ == "__main__":
    app()