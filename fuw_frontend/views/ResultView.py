
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
from ..Model.calculation import SpectrCalculation
import matplotlib.pyplot as plt1
import matplotlib.pyplot as plt2


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
        
    def getMetering(self, index):
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
        self.recordTable.doubleClicked.connect(self.selectMetering)

        self.fCoefficient = QLabel(parent)
        self.fCoefficient.setText("Full coefficient: ")
        self.addWidget(self.fCoefficient)
        self.fSquare = QLabel(parent)
        self.fSquare.setText("Full Square: ")
        self.addWidget(self.fSquare)
        self.nCoefficient = QLabel(parent)
        self.nCoefficient.setText("Narrow coefficient: ")
        self.addWidget(self.nCoefficient)
        self.nSquare = QLabel(parent)
        self.nSquare.setText("Narrow Square: ")
        self.addWidget(self.nSquare)
        self.buttonsLayout = self.setupButtonsLayout()
        self.addLayout(self.buttonsLayout)

    def setupButtonsLayout(self)->QHBoxLayout:
        layout = QHBoxLayout()
        self.showFPlotButton = QPushButton()
        self.showFPlotButton.setText("Show Full Plot")
        self.showFPlotButton.setEnabled(False)
        self.showFPlotButton.clicked.connect(self.showFPlot)
        layout.addWidget(self.showFPlotButton)
        self.showNPlotButton = QPushButton()
        self.showNPlotButton.setText("Show Narrow Plot")
        self.showNPlotButton.setEnabled(False)
        self.showNPlotButton.clicked.connect(self.showNPlot)
        layout.addWidget(self.showNPlotButton)
        return layout

    def setMeteringList(self, data):
        self.__dataModel = MeteringListModel(data)
        self.recordTable.setModel(self.__dataModel)
        self.recordTable.setWordWrap(True)
    
    def selectMetering(self):
        indexs = self.recordTable.selectionModel().selectedIndexes()
        logging.info(f" index - {indexs[0].row}")
        value = self.__dataModel.getMetering(indexs[0])
        if value.status == MeteringStatus.CALCULATE:
            full = value.result.getFullValue()
            self.fCoefficient.setText(f"Full coefficient: a={full[0]:.5f}, b={full[1]:.5f}, c={full[2]:.5f} d={full[3]:.5f}, q={full[4]:.5f} k={full[5]:.5f}")
            fSquare = value.result.squarFull.toString()
            self.fSquare.setText(f"Full Square: {fSquare}")
            narrow = value.result.getNarrowValue()
            self.nCoefficient.setText(f"Narrow coefficient: a={narrow[0]:.5f}, b={narrow[1]:.5f}, d={narrow[2]:.5f} q={narrow[3]:.5f}, w={narrow[4]:.5f} v={narrow[5]:.5f} k={narrow[6]:.5f}")
            nSquare = value.result.squarNarrow.toString()
            self.nSquare.setText(f"Narrow Square: {nSquare}")
            self.showFPlotButton.setEnabled(True)
            self.showNPlotButton.setEnabled(True)
        else:
            self.fCoefficient.setText("Full coefficient: ")
            self.fSquare.setText("Full Square: ")
            self.nCoefficient.setText("Narrow coefficient: ")
            self.nSquare.setText("Narrow Square: ")
            self.showFPlotButton.setEnabled(False)
            self.showNPlotButton.setEnabled(False)

    def showFPlot(self):
        indexs = self.recordTable.selectionModel().selectedIndexes()
        logging.info(f" index - {indexs[0].row}")
        value = self.__dataModel.getMetering(indexs[0])
        x1 = value.full[:,0]
        y1 = value.full[:,1]
        result = value.result
        plt1.plot(x1, y1, 'g', label="Исходная")
        calculation =SpectrCalculation() 
        plt1.plot(x1, calculation.fullFunc(x=x1, a=result.full_a, b=result.full_b, c1=result.full_c, d=result.full_d, q=result.full_q, k=result.full_k), label="Посчитанная")
        plt1.legend(fontsize=14)
        plt1.xlabel("x")
        plt1.ylabel("y")
        plt1.show() 
        

    def showNPlot(self):
        indexs = self.recordTable.selectionModel().selectedIndexes()
        logging.info(f" index - {indexs[0].row}")
        value = self.__dataModel.getMetering(indexs[0])
        x1 = value.narrow[:,0]
        y1 = value.narrow[:,1]
        result = value.result
        plt2.plot(x1, y1, 'g', label="Исходная")
        calculation =SpectrCalculation()
        calculation.c = result.full_c
        plt2.plot(x1, calculation.narrowFunc(x=x1, a=result.narrow_a, b=result.narrow_b, d=result.narrow_d, q=result.narrow_q, w=result.narrow_w, v=result.narrow_v, k=result.narrow_k), label="Посчитанная")
        plt2.legend(fontsize=14)
        plt2.xlabel("x")
        plt2.ylabel("y")
        plt2.show() 


