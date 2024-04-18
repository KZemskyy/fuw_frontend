import logging
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
        self.__id = kwards.get("_Parameter__id",None)
        self.__fullWidth = kwards.get("_Parameter__fullWidth",0)
        self.__fullModulation = kwards.get("_Parameter__fullModulation",0)
        self.__narrowWidth = kwards.get("_Parameter__narrowWidth",0)
        self.__narrowModulation = kwards.get("_Parameter__narrowModulation",0)
        self.__countMetering = kwards.get("_Parameter__countMetering",0)
 
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
        self.__id = kwargs.get("_Metering__id", None)
        self.__description = kwargs.get("_Metering__description","")   
        self.__status = kwargs.get("_Metering__status", MeteringStatus.EDIT)
        f = kwargs.get("_Metering__full",None)
        if f !=None:
            self.__full = np.array(f)
        n = kwargs.get("_Metering__narrow",None)
        if f !=None:
            self.__narrow = np.array(n)
        logging.info(f"init full {self.__full}")
        logging.info(f"init narrow {self.__narrow}")

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
        return self.__narrow
    @narrow.setter
    def narrow(self, data:np.array):
        self.__narrow = data
    
    @property
    def full(self)->np.array:
        return self.__full
    @full.setter
    def full(self, data:np.array):
        self.__full = data

class Experiment():
    def __init__(self, **kwards):
        print(kwards)
        self.__id = kwards.get("_Experiment__id", None)
        self.__description = kwards.get("_Experiment__description","")
        create =kwards.get("_Experiment__dateCreate",None)
        self.__dateCreate = datetime.strptime(create,"%Y-%m-%dT%H:%M:%S.%f") if create!=None else datetime.now()
        last =kwards.get("_Experiment__dateCreate",None)
        self.__lastChange = datetime.strptime(last,"%Y-%m-%dT%H:%M:%S.%f") if last!=None else datetime.now()
        self.__status = kwards.get("_Experiment__status",ExperimentStatus.EDIT)
        self.__parameter = Parameter(**kwards.get("_Experiment__parameter",{}))
        self.__meterings = []
        for m in kwards.get('_Experiment__meterings',[]):
            self.__meterings.append(Metering(**m))


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

