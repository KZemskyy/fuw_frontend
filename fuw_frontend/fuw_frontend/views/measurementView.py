from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit

class MeasurementParametrsLayout(QHBoxLayout):
    def __init__(self):
        super().__init__()

class MeasurementTitleLayout(QVBoxLayout):
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

class MeasurementResultLayout(QHBoxLayout):
    def __init__(self):
        super().__init__()
    
class MeasurementLayout(QVBoxLayout):
    def __init__(self):
        super().__init__()
        self.__titleLayout = MeasurementTitleLayout()
        self.__parametrsLayout = MeasurementParametrsLayout()
        self.__resultLayout = MeasurementResultLayout()
        self.addLayout(self.__titleLayout)
        self.addLayout(self.__parametrsLayout)
        self.addLayout(self.__resultLayout)