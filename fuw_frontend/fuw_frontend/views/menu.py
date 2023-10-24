import sys
import typing
from PyQt6.QtWidgets import QVBoxLayout, QPushButton 

class MainMenu(QVBoxLayout):
    def __init__(self):
        super().__init__()
        self.__createExpermentBtn = QPushButton()
        self.__openExpermentBtn = QPushButton()
        self.__createExpermentBtn.setText("Create")
        
        self.__openExpermentBtn.setText("Open")
        self.addWidget(self.__createExpermentBtn)
        self.addWidget(self.__openExpermentBtn)