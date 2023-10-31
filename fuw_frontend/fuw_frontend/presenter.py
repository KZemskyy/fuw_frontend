from .Model import Model
from .views import MainMenu, ExperimentLayout, MeasurementLayout

class Presenter():
    def __init__(self, model:Model) -> None:
        self.__model = model
        self.__listExperementView = MainMenu()
        self.__experementView = ExperimentLayout()
        self.__measurementView = MeasurementLayout()
        listExperement = self.__model.getExperementList()
        self.__listExperementView.setData(listExperement)

    def getListExperemetView(self):
        return self.__listExperementView

    def getExperemetView(self):
        return self.__experementView

    def getMeasurementView(self):
        return self.__measurementView

    