from .Model import Model
from .views import Ui_MainWindow

class Presenter():
    def __init__(self, model:Model) -> None:
        self.__model = model
        self.__ui = Ui_MainWindow(self.__model)
        self.__ui.setNewExperementFunction(self.newExperemenetClieckAction)
        self.__ui.setSaveExperementFunction(self.saveExperement)

    def getUI(self):
        return self.__ui


    def newExperemenetClieckAction(self):
        self.__model.createNewExperement()
        self.__ui.setExperement(self.__model.getSelectedExperement())
        print("Clicked!")

    def saveExperement(self):
        print(self.__model.getSelectedExperement().description)