
import logging
from typing import Optional
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6 import QtCore
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)

from PySide6.QtWidgets import (QApplication, QGraphicsView, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QTableView, QTextEdit, QVBoxLayout,
    QWidget)
from .utils import LineEdit
from ..Model import Metering, MeteringStatus, Result


class MeteringListModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(MeteringListModel, self).__init__()
        logging.info(f"MeteringListModel {data}")
        self._data=data
        logging.info(f"len data {len(self._data)}")

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            value = self.getValue(index)
            return value

    def rowCount(self, index):
        return len(self._data)
    
    def columnCount(self, index):
        return 6

    def getValue(self, index):
        metering = self._data[index.row()]
        column = index.column()
        if column == 0:
            return metering.description
        if column == 1:
            try:
                result = metering.result
                if result == None:
                    return ""
                full = metering.result.getFullValue()
                return f"(a={full[0]}, b={full[1]}, c={full[2]} d={full[3]}, q={full[4]} k={full[5]})"
            except:
                return ""            
        if column == 2:
            try:
                result = metering.result
                if result == None:
                    return ""
                return metering.result.squarFull.toString()
            except:
                return ""
        if column == 3:
            try:
                result = metering.result
                if result == None:
                    return ""
                narrow = metering.result.getNarrowValue()
                return f"(a={narrow[0]}, b={narrow[1]}, d={narrow[2]} q={narrow[3]}, w={narrow[4]} v={narrow[5]} k={narrow[6]})"
            except:
                return ""            
        if column == 4:
            try:
                result = metering.result
                if result == None:
                    return ""
                return metering.result.squarNarrow.toString()
            except:
                return ""
        if column == 5:
            return metering.status
        
    def getExperement(self, index):
        return self._data[index.row()]  

class ResultView(QVBoxLayout):
    def __init__(self,  parent: QWidget)->None:
        super().__init__(parent)
        
        self.horizontalLayout = QHBoxLayout()
        self.date = LineEdit(parent,"Date")
        self.horizontalLayout.addLayout(self.date)
        self.lastModification = LineEdit(parent,"modification")
        self.horizontalLayout.addLayout(self.lastModification)
        self.addLayout(self.horizontalLayout)

        self.recordTable = QTableView(parent)
        self.addWidget(self.recordTable)

        self.graphicsView = QGraphicsView(parent)
        self.addWidget(self.graphicsView)

    def setMeteringList(self, data):
        self.__dataModel = MeteringListModel(data)
        self.recordTable.setModel(self.__dataModel)
