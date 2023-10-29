from enum import Enum
from datetime import datetime
from typing import Any

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

class ModelExperiment():
    def __init__(self) -> None:
        self.description = ""
        self.dateCreate = datetime.now()
        self.lastChange = datetime.now()
        self.status = ExperimentStatus.EDIT

    @property
    def id(self)->int:
        return self.__id
    @property.setter
    def id(self,id:int):
        self.__id=id
    
    @property
    def description(self)->str:
        return self.__description
    
    @property.setter
    def name(self, description:str):
        self.__description = description
    
    @property
    def dateCreate(self)->datetime:
        return self.__dateCreate
    
    @property.setter
    def dateCreate(self, date:datetime):
        self.__dateCreate = date
    
    @property
    def lastChange(self)->datetime:
        return self.__lastChange
    
    @property.setter
    def lastChange(self, date:datetime):
        self.__lastChange = date
    
    @property
    def status(self)->ExperimentStatus:
        return self.__status
    
    @property.setter
    def status(self, experimentStatus:ExperimentStatus):
        self.__status = experimentStatus

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
    @property.setter
    def id(self,id:int):
        self.__id=id
        
    @property
    def experimentId(self)->int:
        return self.__experimentId
    @property.setter
    def experimentId(self, id:int):
        self.__experimentId = id

    @property
    def description(self)->str:
        return self.__description
    @property.setter
    def description(self, description:str):
        self.__description = description
        
    @property
    def status(self)->MeteringStatus:
        return self.__status
    @property.setter
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
    @property.setter
    def id(self,id:int):
        self.__id=id
    
    @property
    def experimentId(self)->int:
        return self.__experimentId
    @property.setter
    def experimentId(self, id:int):
        self.__experimentId = id
    
    @property
    def name(self)->str:
        return self.__name
    @property.setter
    def name(self, name:str):
        self.__name = name 
    
    @property
    def value(self)->float:
        return self.__value
    @property.setter
    def value(self,value:float):
        self.__value = value 

class Model():
    def __init__(self) -> None:
        pass
    