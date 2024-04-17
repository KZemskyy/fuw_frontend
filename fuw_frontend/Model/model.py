from enum import Enum
from datetime import datetime
import numpy as np

class ExperimentStatus(str,Enum):
    EDIT = "Edit"
    PROCESING = "Procesing"
    CALCULATE = "Calculate"
    PARTLY_COMLETE = "partly_complete"
    COMLETE = "complete"

class MeteringStatus(str, Enum):
    EDIT = "Edit"
    PROCESING = "Procesing"
    CALCULATE = "Calculate"
    PARTLY_COMLETE = "partly_complete"
    COMLETE = "complete"


class Parameter():
    def __init__(self, **kwards) -> None:
        self.__id = kwards.get("id",None)
        self.__fullWidth = kwards.get("fullWidth",0)
        self.__fullModulation = kwards.get("fullModulation",0)
        self.__narrowWidth = kwards.get("narrowWidth",0)
        self.__narrowModulation = kwards.get("narrowModulation",0)
        self.__countMetering = kwards.get("countMetering",0)
 
    @property
    def id(self)->int:
        return self.__id
    @id.setter
    def id(self, id:int):
        self.__id=id
    
    @property
    def fullWidth(self)->float:
        return self.__fullWidth
    @fullWidth.setter
    def fullWidth(self, fullWidth:float):
        self.__fullWidth = fullWidth 

    @property
    def fullModulation(self)->float:
        return self.__fullModulation
    @fullModulation.setter
    def fullModulation(self, fullModulation:float):
        self.__fullModulation = fullModulation 
    
    @property
    def narrowWidth(self)->float:
        return self.__narrowWidth
    @narrowWidth.setter
    def narrowWidth(self, narrowWidth:float):
        self.__narrowWidth = narrowWidth 

    @property
    def narrowModulation(self)->float:
        return self.__narrowModulation
    @narrowModulation.setter
    def narrowModulation(self, narrowModulation:float):
        self.__narrowModulation = narrowModulation

    @property
    def countMetering(self)->int:
        return self.__countMetering
    @countMetering.setter
    def countMetering(self, countMetering:int):
        self.__countMetering = countMetering

    
class Metering():
    def __init__(self,**kwargs) -> None:
        self.__id = kwargs.get("id")
        self.__description = kwargs.get("description")   
        self.__status = MeteringStatus.EDIT

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
    
    @property
    def narrow(self)->np.array:
        self.__narrow
    @narrow.setter
    def narrow(self, data:np.array):
        self.__narrow = data
    
    @property
    def full(self)->np.array:
        self.__full
    @full.setter
    def full(self, data:np.array):
        self.__full = data

class Experiment():
    def __init__(self, **kwards):
        print(kwards)
        self.__id = kwards["_Experiment__id"]
        self.__description = kwards["_Experiment__description"]
        self.__dateCreate = datetime.now()
        self.__lastChange = datetime.now()
        self.__status = ExperimentStatus.EDIT
        self.__parameter = Parameter()
        self.__meterings = []

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
    def parameter(self)->Parameter:
        return self.__parameter
    @parameter.setter
    def parameter(self, parameter:Parameter):
        self.__parameter = parameter

    @property
    def meterings(self)->list:
        return self.__meterings
    
    def setMetering(self, metering:Metering)->None:
        self.__meterings.append(metering)


class Model():
    def __init__(self) -> None:
        self._experementList=set()
        self._selectedExperement = Experiment()

    def createNewExperement(self):
        self._selectedExperement = Experiment()

    def getSelectedExperement(self)->Experiment:
        return self._selectedExperement

    def getExperementList(self):
        return self._experementList
        
    def getMeteringList(self):
        return [["Metering1", "EDIT"],["Metering2", "EDIT"],["Metering2", "EDIT"]]
    
    def putExperimentToList(self, experiment:Experiment) -> None:
        self._experementList.add(experiment)

