import logging
from PySide6.QtWidgets import QMainWindow, QFileDialog
from .Model import Model, Experiment, Metering
from .views import Ui_MainWindow
from operator import attrgetter
import numpy as np
import re
import os
import json
from json import JSONEncoder
from datetime import date, datetime

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
        self.__ui = Ui_MainWindow()
        self.__ui.setupUi(MainWindow)    
        self.__ui.setCreateButtonListener(self.newExperemenetClieckAction)
        self.__ui.setSaveButtonListener(self.saveExperement)
        self.__ui.setRecordButtonListener(self.downLoad)
        
        
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
        print("downLoad")
        dialog = QFileDialog(self.__ui.centralwidget)
        # dialog.setLabelText("Load Data")
        files=dialog.getOpenFileNames(filter="Data (ao_*.dat au_*.dat)")
        print(f"files = {files}")
        fileList = self.__parserFileNames(files[0])
        print(fileList)
        experent = self.__model._selectedExperement
        print(experent.meterings)
        for files in fileList:
            metering = Metering()
            metering.description = os.path.basename(files["full"])
            metering.full = self.__downLoadData(files["full"])
            metering.narrow = self.__downLoadData(files["narrow"])
            print(f"m {metering}")
            experent.meterings.append(metering)

    
    def __downLoadData(self, filename):
        print(filename)
        with open(filename) as file:
            data = np.loadtxt(file,usecols=(0, 1))
        return data

    def __parserFileNames(self, fileNames):
        print(fileNames)
        full = list(filter(lambda f: True if re.search(FULL, os.path.basename(f)) else False, fileNames))
        narrow = list(filter(lambda f: True if re.search(NARROW, os.path.basename(f)) else False, fileNames))
        result = []
        for fname in full:
            result.append({"full":fname, "narrow":(list(filter(lambda f: True if (os.path.basename(f))[2:] == (os.path.basename(fname))[2:] else False, narrow)))[0]})
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
