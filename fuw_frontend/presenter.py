
from PySide6.QtWidgets import QMainWindow 
from .Model import Model
from .views import Ui_MainWindow

class Presenter():
    def __init__(self, model:Model,MainWindow: QMainWindow) -> None:
        self.__model = model
        self.__ui = Ui_MainWindow()
        self.__ui.setupUi(MainWindow)    
        self.__ui.setCreateButtonListener(self.newExperemenetClieckAction)
        
    def getUI(self):
        return self.__ui


    def newExperemenetClieckAction(self):
        self.__model.createNewExperement()
        self.__ui.setExperement(self.__model.getSelectedExperement())
        print("Clicked!")

    def saveExperement(self):
        print(self.__model.getSelectedExperement().description)