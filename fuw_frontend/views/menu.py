import sys
from PySide6.QtWidgets import QVBoxLayout, QPushButton,QTableView
from PySide6 import QtCore, QtGui
from PySide6.QtCore import QObject
from .utils import LineEdit
from ..Model import Model


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])

class MainMenu(QVBoxLayout):
    def __init__(self):
        super().__init__()
        self.__listExperement = QTableView()
        self.__createExpermentBtn = QPushButton()
        self.__createExpermentBtn.setText("Create")
        self.addWidget(self.__listExperement)
        self.addWidget(self.__createExpermentBtn)
    
    def setData(self, data: []):
        model = TableModel(data)
        self.__listExperement.setModel(model)