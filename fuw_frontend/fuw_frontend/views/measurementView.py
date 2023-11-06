from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QPushButton, QTableView
from PySide6 import QtCore, QtGui
from PySide6.QtCore import QObject
from .utils import LineEdit




class ExperimentLayout(QHBoxLayout):
    def __init__(self) -> None:
        super().__init__()
        self.__description = LineEdit("Description")
        self.__dateCreate = LineEdit("Date Create")
        self.__lastChange = LineEdit("Last update")
        self.__status = LineEdit("Status")
        self.__saveButton = QPushButton(text="Save")
        self.addLayout(self.__description)
        self.addLayout(self.__dateCreate)
        self.addLayout(self.__lastChange)
        self.addLayout(self.__status)
        self.addWidget(self.__saveButton)
        

class MeasurementParametrsLayout(QHBoxLayout):
    def __init__(self):
        super().__init__()
        self.__lineWidth = LineEdit("line width")
        self.__modulation = LineEdit("modulation")
        self.__type = LineEdit("Type")
        self.addLayout(self.__lineWidth)
        self.addLayout(self.__modulation)
        self.addLayout(self.__type)

class MeasurementTitleLayout(QVBoxLayout):
    def __init__(self):
        super().__init__()
        title = QHBoxLayout()
        self.__name = LineEdit("Description")
        self.__status = LineEdit("Status")
        self.__action = QPushButton(text="Action")
        title.addLayout(self.__name)
        title.addLayout(self.__status)
        title.addWidget(self.__action)
        self.addLayout(title)

    
class MeasurementResultLayout(QHBoxLayout):
    def __init__(self):
        super().__init__()
        self.__table = QTableView()
        self.addWidget(self.__table)

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


class MeasurementTableLayout(QHBoxLayout):
    def __init__(self):
        super().__init__()
        self.__table = QTableView()
        self.addWidget(self.__table)

    def setData(self, data):
        model = TableModel(data)
        self.__table.setModel(model)



    
class MeasurementLayout(QVBoxLayout):
    def __init__(self):
        super().__init__()
        self.__titleLayout = MeasurementTitleLayout()
        self.__parametrsLayout = MeasurementParametrsLayout()
        self.__table_resultLayout = QHBoxLayout()
        self.__resultLayout = MeasurementResultLayout()
        self.__tableLayout = MeasurementTableLayout()
        self.__table_resultLayout.addLayout(self.__tableLayout)
        self.__table_resultLayout.addLayout(self.__resultLayout)
        self.addLayout(self.__titleLayout)
        self.addLayout(self.__parametrsLayout)
        self.addLayout(self.__table_resultLayout)
        self.setAlignment
