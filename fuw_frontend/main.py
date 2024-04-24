
import logging, os
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QMainWindow 
from .Model import Model
from .presenter import Presenter
from .views import Ui_MainWindow

def init_logger():
    logging.basicConfig()
    levels = {'DEBUG': logging.DEBUG, 'INFO': logging.INFO, 'WARN': logging.WARN, 'ERROR': logging.ERROR}
    level = os.getenv('LOGLEVEL', 'INFO').upper()
    logging.getLogger().setLevel(levels[level] if level in levels else logging.INFO)


class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.__model = Model()
        self.__presenter = Presenter(self.__model, self)
        logging.debug("main load")
        self.__presenter.load()

        self.ui = self.__presenter.getUI()
        # self.ui.setupUi(self)    

def app():
    init_logger()
    logging.info("start APP")
    __app = QApplication([])
    win = MyApp()
    win.show()
    __app.exec()

if __name__ == "__main__":
    app()