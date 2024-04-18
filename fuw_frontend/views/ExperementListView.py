
from PySide6.QtWidgets import QLabel, QTableView,  QVBoxLayout, QWidget
from PySide6 import QtCore
from PyQt6.QtCore import Qt
from datetime import datetime

class ExperementListModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(ExperementListModel, self).__init__()
        self._data=list(data)
        print(f"len data {len(self._data)}")

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

class ExperementListView(QVBoxLayout):
    def __init__(self, parent: QWidget)->None:
        super().__init__(parent)
        
        self.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(parent)
        self.label.setText("Experement")
        self.addWidget(self.label)
        self.experementlist = QTableView(parent)
        self.addWidget(self.experementlist)        
        self.experementlist.doubleClicked.connect(self.selectExperement)

    def setExperementList(self, data):
        dataModel = ExperementListModel(data)
        print(type(dataModel))
        print(issubclass (ExperementListModel, QtCore.QAbstractTableModel))
        self.experementlist.setModel(dataModel)
    
    def selectExperement(self):
        indexs = self.experementlist.selectionModel().selectedIndexes()
        print(indexs)
