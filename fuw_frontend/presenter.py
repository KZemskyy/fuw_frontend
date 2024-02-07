
from PySide6.QtWidgets import QMainWindow 
from .Model import Model
from .views import Ui_MainWindow
from operator import attrgetter

class Presenter():
    def __init__(self, model:Model,MainWindow: QMainWindow) -> None:
        self.__model = model
        self.__ui = Ui_MainWindow()
        self.__ui.setupUi(MainWindow)    
        self.__ui.setCreateButtonListener(self.newExperemenetClieckAction)
        self.__ui.setSaveButtonListener(self.saveExperement)
        
    def getUI(self):
        return self.__ui


    def newExperemenetClieckAction(self):
        self.__model.createNewExperement()
        self.__ui.setExperement(self.__model.getSelectedExperement())
        print("Clicked!")

    def saveExperement(self):
        # need save to BD or file 
        exp = self.__model.getSelectedExperement()
        if (exp.id==None):
            print("new exp")
            exp.id = self.createId()
        l = self.__model.getExperementList()
        self.__model.putExperimentToList(self.__model.getSelectedExperement())
        self.__ui.experementListLayout.setExperementList(self.__model.getExperementList())
        l = self.__model.getExperementList()
        print(len(l))

    def createId(self):
        l = self.__model.getExperementList()
        print(len(l))
        if (len(l)==0):
            return 1
        max=0
        for exp in l:
            if (exp.id>max):
                max= exp.id
        return max+1

       