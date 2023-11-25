
import sys
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QMainWindow 
from .Model import Model
from .presenter import Presenter
from .views import Ui_MainWindow

class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.__model = Model()
        self.__presenter = Presenter(self.__model)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)    
        # layouts = QHBoxLayout()
        # layouts.addLayout(self.__presenter.getListExperemetView())
        # experement = QVBoxLayout()
        # layouts.addLayout(experement)
        # experement.addLayout(self.__presenter.getExperemetView())
        # experement.addLayout(self.__presenter.getMeasurementView())
        # self.setLayout(layouts)

def app():
    __app = QApplication([])
    win = MyApp()
    win.show()
    __app.exec()

if __name__ == "__main__":
    app()