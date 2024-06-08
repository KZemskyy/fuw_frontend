
import logging
from PySide6.QtWidgets import QLabel, QTableView,  QVBoxLayout, QWidget
from PySide6 import QtCore
from PyQt6.QtCore import Qt
from datetime import datetime

class ExperementListModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(ExperementListModel, self).__init__()
        self._data=list(data)
        logging.info(f"len data {len(self._data)}")

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            value = self.getValue(index)
            return value

    def rowCount(self, index):
        return len(self._data)
    
    def columnCount(self, index):
        return 5

    def getValue(self, index):
        experement = self._data[index.row()]
        column = index.column()
        if column == 0:
            return experement.id
        if column == 1:
            return experement.description 
        if column == 2:
            return experement.dateCreate.strftime("%m/%d/%Y, %H:%M:%S") 
        if column == 3:
            return experement.lastChange.strftime("%m/%d/%Y, %H:%M:%S")  
        if column == 4:
            return experement.status
        
    def getExperement(self, index):
        return self._data[index.row()]  

class ExperementListView(QVBoxLayout):
    def __init__(self, parent: QWidget)->None:
        super().__init__(parent)
        
        self.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(parent)
        self.label.setText("Experements")
        self.addWidget(self.label)
        self.experementlist = QTableView(parent)
        self.addWidget(self.experementlist)        
        self.experementlist.doubleClicked.connect(self.__selectExperement)

    def setExperementList(self, data):
        self.__dataModel = ExperementListModel(data)
        self.experementlist.setModel(self.__dataModel)
    
    def __selectExperement(self):
        indexs = self.experementlist.selectionModel().selectedIndexes()
        logging.info(f" index - {indexs[0].row}")
        value = self.__dataModel.getExperement(indexs[0])
        logging.info(f"experement id = {value.id} desc = {value.description}")
        logging.info(self.setSelectExperement)
        self.__setSelectedExperiment(value)

    def setSelectExperement(self, listener)->None:
        self.__setSelectedExperiment = listener
        
