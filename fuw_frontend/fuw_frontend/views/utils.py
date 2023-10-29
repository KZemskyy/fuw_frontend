from ..Model import Presenter

class Controle():
    def __init__(self) -> None:
        pass
    
    @property
    def presenter(self):
        return self.__presenter
    
    @property.setter
    def presenter(self, presenter: Presenter):
        self.__presenter = presenter