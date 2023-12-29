
import sys
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QMainWindow 
from .Model import Model
from .presenter import Presenter
from .views import Ui_MainWindow

class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.__model = Model()
        self.__presenter = Presenter(self.__model, self)

        self.ui = self.__presenter.getUI()
        # self.ui.setupUi(self)    

def app():
    __app = QApplication([])
    win = MyApp()
    win.show()
    __app.exec()

if __name__ == "__main__":
    app()