
from PySide6.QtWidgets import QMainWindow, QFileDialog
from .Model import Model
from .views import Ui_MainWindow
from operator import attrgetter
import numpy as np
import re
import os

FULL = r'^ao_.*dat$'
NARROW = r'^au_.*dat$'

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
    
    def downLoad(self):
        print("downLoad")
        dialog = QFileDialog(self.__ui.centralwidget)
        # dialog.setLabelText("Load Data")
        files=dialog.getOpenFileNames(filter="Data (ao_*.dat au_*.dat)")
        print(f"files = {files}")
        self.parserFileNames(files[0])
        self.downLoadData(files[0][0])
        pass
    
    def downLoadData(self, filename):
        print(filename)
        with open(filename) as file:
            data = np.loadtxt(file,usecols=(0, 1))
        print(data)

    def parserFileNames(self, fileNames):
        print(fileNames)
        full = list(filter(lambda f: True if re.search(FULL, os.path.basename(f)) else False, fileNames))
        map()
        print(f"full files - {full}")
    
    def  findNarrow(self,fileName, files):
        pass