import logging
from PySide6.QtWidgets import QMainWindow, QFileDialog
from .Model import Model, Experiment, Metering, ExperimentStatus, MeteringStatus
from .views import Ui_MainWindow
from .Model.calculation import SpectrCalculation
from operator import attrgetter
import numpy as np
import re
import os
import json
from json import JSONEncoder
from datetime import date, datetime
from .saveExls import saveExls

FULL = r'^ao_.*dat$'
NARROW = r'^au_.*dat$'
SAVE = "./save/"

class ExperimentEncoder(JSONEncoder):
        def default(self, o):
            if isinstance(o, (datetime, date)):
                return o.isoformat()
            if isinstance(o, float):
                return format(o, ".2f")
            if isinstance(o, np.ndarray):
                return o.tolist()
            return o.__dict__

class Presenter():
    def __init__(self, model:Model,MainWindow: QMainWindow) -> None:
        self.__model = model
        self.__spectrCalculation = SpectrCalculation()
        self.__ui = Ui_MainWindow()
        self.__ui.setupUi(MainWindow)    
        self.__ui.setCreateButtonListener(self.newExperemenetClieckAction)
        self.__ui.setSaveButtonListener(self.saveExperement)
        self.__ui.setRecordButtonListener(self.downLoad)
        self.__ui.setCalculationButtonListener(self.calculation)
        self.__ui.setSaveExelButtonListener(self.saveExel)
        self.__ui.setSelectExperementInList(self.selectExperement)
        
        
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
        self.saveToJson(exp)
        l = self.__model.getExperementList()
        self.__model.putExperimentToList(self.__model.getSelectedExperement())
        self.__ui.experementListLayout.setExperementList(self.__model.getExperementList())
        l = self.__model.getExperementList()
        print(len(l))
    
    def saveToJson(self,experiment:Experiment):
        id = experiment.id
        desc= experiment.description
        filename = f"./save/{id}_{desc}.json"
        with open(filename, "w") as file:
            json.dump(experiment,file,indent=4, cls=ExperimentEncoder)


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
    
    def downLoad(self):
        logging.info("downLoad")
        dialog = QFileDialog(self.__ui.centralwidget)
        # dialog.setLabelText("Load Data")
        files=dialog.getOpenFileNames(filter="Data (*.dat)")
        logging.info(f"files = {files}")
        fileList = self.__parserFileNames(files[0])
        logging.info(f"fileList - {fileList}")
        experent = self.__model._selectedExperement
        logging.info(experent.meterings)
        for files in fileList:
            metering = Metering(_Metering__description=f"{os.path.basename(files['full'])} {os.path.basename(files['narrow'])}")
            metering.full = self.__downLoadData(files["full"])
            metering.narrow = self.__downLoadData(files["narrow"])
            logging.info(f"m {metering}")
            experent.meterings.append(metering)
        self.__ui.setExperement(self.__model.getSelectedExperement())

    
    def __downLoadData(self, filename):
        print(filename)
        with open(filename) as file:
            data = np.loadtxt(file,usecols=(0, 1))
        return data

    def __parserFileNames(self, fileNames):
        logging.info(f"__parserFileNames")
        full = list(filter(lambda f: True if int(os.path.splitext(os.path.basename(f))[0])%2 == 1 else False, fileNames))
        narrow = list(filter(lambda f: True if int(os.path.splitext(os.path.basename(f))[0])%2 == 0 else False, fileNames))
        logging.info(f"fulll =P {full}")
        logging.info(f"narrow =P {narrow}")
        result = []
        for i in range(min(len(full), len(narrow))):
            result.append({"full":full[i], "narrow":narrow[i]})
        return result

    def load(self):
        logging.info("load data from ./save") 
        for fileName in os.listdir(SAVE):
            logging.info(f" load filename -{fileName}")
            if os.path.isfile(SAVE+fileName):
                with open(SAVE+fileName) as file:
                    j = json.load(file)
                    experement = Experiment(**j)
                    self.__model.putExperimentToList(experement)
                    # logging.info(f"id {experement.id} desc {experement.description} create {experement.dateCreate} last {experement.lastChange} status {experement.status}")
                    # logging.info(f"parameter: id {experement.parameter.id} count {experement.parameter.countMetering} fullM {experement.parameter.fullModulation} fullW {experement.parameter.fullWidth} narrowM {experement.parameter.narrowModulation} narrowW {experement.parameter.narrowWidth}")
                    # for m in experement.meterings:
                    #     logging.info(f"metering id {m.id} description {m.description} status {m.status} full {m.full} narrow {m.narrow}")
        self.__ui.experementListLayout.setExperementList(self.__model.getExperementList())

    def selectExperement(self, experement:Experiment):
        logging.info("selected Experement")
        self.__model.selectExperement(experement)
        self.__ui.setExperement(self.__model.getSelectedExperement())
        logging.info("selected Experement")
    
    def calculation(self):
        experement = self.__model.getSelectedExperement()
        logging.info(f"experement - {experement.meterings}")
        logging.info(f"__spectrCalculation {self.__spectrCalculation.fullModulation}")
        for metering in experement.meterings:
            logging.info(f"metering type {type(metering)}")
            self.__spectrCalculation.culculate(experement.parameter, metering)
            metering.status = MeteringStatus.CALCULATE
        experement.status = ExperimentStatus.CALCULATE
    
    def saveExel(self):
        saveExls(self.__model.getSelectedExperement())