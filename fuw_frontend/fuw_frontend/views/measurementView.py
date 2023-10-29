from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit

from ..Model import Presenter
from .utils import Controle

class MeasurementParametrsLayout(QHBoxLayout,Controle):
    def __init__(self):
        super().__init__()
    

class MeasurementTitleLayout(QVBoxLayout, Controle):
    def __init__(self):
        super().__init__()
        title = QHBoxLayout()
        self.__name = QLineEdit()
        self.__status = QLineEdit()
        self.__action = QPushButton(text="Action")
        title.addWidget(self.__name)
        title.addWidget(self.__status)
        title.addWidget(self.__action)
        self.addLayout(title)

    
class MeasurementResultLayout(QHBoxLayout, Controle):
    def __init__(self):
        super().__init__()

    
class MeasurementLayout(QVBoxLayout, Controle):
    def __init__(self):
        super().__init__()
        self.__titleLayout = MeasurementTitleLayout()
        self.__parametrsLayout = MeasurementParametrsLayout()
        self.__resultLayout = MeasurementResultLayout()
        self.addLayout(self.__titleLayout)
        self.addLayout(self.__parametrsLayout)
        self.addLayout(self.__resultLayout)

    def setPresenter(self, presenter: Presenter) -> None:
        self.presenter = presenter
        self.__titleLayout.presenter = presenter
        self.__parametrsLayout.presenter = presenter
        self.__resultLayout.presenter = presenter