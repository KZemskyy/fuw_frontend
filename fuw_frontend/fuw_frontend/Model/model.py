from enum import Enum
from datetime import datetime
import typing
from PyQt6 import QtCore, QtGui
from PyQt6.QtCore import QObject

class ExperimentStatus(Enum):
    EDIT = "Edit"
    PROCESING = "Procesing"
    CALCULATE = "Calculate"
    PARTLY_COMLETE = "partly_complete"
    COMLETE = "complete"

class MeteringStatus(Enum):
    EDIT = "Edit"
    PROCESING = "Procesing"
    CALCULATE = "Calculate"
    PARTLY_COMLETE = "partly_complete"
    COMLETE = "complete"

class Experiment():
    def __init__(self) -> None:
        self.description = ""
        self.dateCreate = datetime.now()
        self.lastChange = datetime.now()
        self.status = ExperimentStatus.EDIT

    def __init__(self,description:str, dateCreate: datetime, lastChange: datetime, status:ExperimentStatus) -> None:
        self.description = description
        self.dateCreate = dateCreate
        self.lastChange = lastChange
        self.status = status

    @property
    def id(self)->int:
        return self.__id
    
    @id.setter
    def id(self,id:int):
        self.__id=id
    
    @property
    def description(self)->str:
        return self.__description
    
    @description.setter
    def description(self, description:str):
        self.__description = description
    
    @property
    def dateCreate(self)->datetime:
        return self.__dateCreate
    
    @dateCreate.setter
    def dateCreate(self, date:datetime):
        self.__dateCreate = date
    
    @property
    def lastChange(self)->datetime:
        return self.__lastChange
    
    @lastChange.setter
    def lastChange(self, date:datetime):
        self.__lastChange = date
    
    @property
    def status(self)->ExperimentStatus:
        return self.__status
    
    @status.setter
    def status(self, experimentStatus:ExperimentStatus):
        self.__status = experimentStatus

    @property
    def meterings(self)->[]:
        return self.__meterings
    @meterings.setter
    def meterings(self,meterins:[]):
        self.__meterings = meterins

class Metering():
    def __init__(self) -> None:
        pass

    def __init__(self,id:int) -> None:
        self.__init__()
        self.id = id

    def __init__(self, description:str) -> None:
        self.__init__()
        self.description = description

    def __init__(self, id:int, description:str) -> None:
        self.__init__()
        self.description = description
        self.id = id

    @property
    def id(self)->int:
        return self.__id
    @id.setter
    def id(self,id:int):
        self.__id=id
        
    @property
    def experimentId(self)->int:
        return self.__experimentId
    @experimentId.setter
    def experimentId(self, id:int):
        self.__experimentId = id

    @property
    def description(self)->str:
        return self.__description
    @description.setter
    def description(self, description:str):
        self.__description = description
        
    @property
    def status(self)->MeteringStatus:
        return self.__status
    @status.setter
    def status(self, status:MeteringStatus):
        self.__status = status

class Parameter():
    def __init__(self, name:str) -> None:
        self.name = name

    def __init__(self,id:int, name:str) -> None:
        self.id = id
        self.name = name
 
    @property
    def id(self)->int:
        return self.__id
    @id.setter
    def id(self,id:int):
        self.__id=id
    
    @property
    def experimentId(self)->int:
        return self.__experimentId
    @experimentId.setter
    def experimentId(self, id:int):
        self.__experimentId = id
    
    @property
    def name(self)->str:
        return self.__name
    @name.setter
    def name(self, name:str):
        self.__name = name 
    
    @property
    def value(self)->float:
        return self.__value
    @value.setter
    def value(self,value:float):
        self.__value = value 
           

class Model():
    def __init__(self) -> None:
        self._experementList=[["Experiment1","EDIT"],["Experiment2","EDIT"]]
       
    def getExperementList(self):
        return self._experementList
        
    def getMeteringList(self):
        return [["Metering1", "EDIT"],["Metering2", "EDIT"],["Metering2", "EDIT"]]


