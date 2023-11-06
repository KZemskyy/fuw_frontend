from PySide6.QtWidgets import QHBoxLayout, QLabel, QLineEdit

class LineEdit(QHBoxLayout):
    def __init__(self, text1:str, text2:str):
        super().__init__()
        self.__lable1 = QLabel(); 
        self.__lable1.setText(text1)
        self.__lable2 = QLabel(); 
        self.__lable2.setText(text2)
        self.__value = QLineEdit()
        self.addWidget(self.__lable1)
        self.addWidget(self.__value)
        self.addWidget(self.__lable2)

    def __init__(self, text1:str):
        super().__init__()
        self.__lable1 = QLabel(); 
        self.__lable1.setText(text1)
        self.__value = QLineEdit()
        self.addWidget(self.__lable1)
        self.addWidget(self.__value)
        