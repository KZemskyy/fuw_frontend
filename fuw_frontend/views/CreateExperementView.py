
from PySide6.QtCore import  QRect

from PySide6.QtWidgets import  QHBoxLayout, QLabel,  QPushButton, QTextEdit, QVBoxLayout, QWidget
from .utils import LineEdit
from ..Model import Experiment, ExperimentStatus

class CreateBar(QWidget):
    def __init__(self, parent: QWidget ) -> None:
        super().__init__(parent)
        self.setGeometry(QRect(0, 12, 258, 521))
        self.__setupUi()
    
    def __setupUi(self):
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.createButton = QPushButton(self)
        self.createButton.setText("Create")
        self.createButton.clicked.connect(self.createExperement)
        self.layout.addWidget(self.createButton)

        self.description = QLabel(self)
        self.description.setText("Description")
        self.layout.addWidget(self.description)

        self.descriptionEdit = QTextEdit(self)
        self.descriptionEdit.setEnabled(False)
        self.layout.addWidget(self.descriptionEdit)

        self.parametrLayout = self.__setupParameterLayout()
        self.layout.addLayout(self.parametrLayout)

        self.buttonsLayout = self.__setupButtonsLayout()
        self.layout.addLayout(self.buttonsLayout)

        self.status = LineEdit(self, "Status")
        self.status.setEnabled(False)
        self.layout.addLayout(self.status)

        self.saveButton = QPushButton(self)
        self.saveButton.setText("Save")
        self.saveButton.setEnabled(True)
        self.saveButton.clicked.connect(self.__save)
        self.layout.addWidget(self.saveButton)
        


    def __setupParameterLayout(self)->QVBoxLayout:
        layout = QVBoxLayout()
        self.parametersLabel = QLabel(self)
        self.parametersLabel.setText("Parameters")
        layout.addWidget(self.parametersLabel)

        self.fullLineLabel = QLabel(self)
        self.fullLineLabel.setText("Full line:")
        layout.addWidget(self.fullLineLabel)

        self.fullModulation=LineEdit(self,"modulation")
        self.fullModulation.setEnabled(False)
        layout.addLayout(self.fullModulation)

        self.narrowLabel = QLabel(self)
        self.narrowLabel.setText("Narrow Line:")
        layout.addWidget(self.narrowLabel)

        self.narrowModulation=LineEdit(self, "modulation")
        self.narrowModulation.setEnabled(False)
        layout.addLayout(self.narrowModulation)

        self.numberRec = LineEdit(self,"Number of records")
        self.numberRec.setEnabled(False)
        layout.addLayout(self.numberRec)
        return layout
    
    def __setupButtonsLayout(self)->QHBoxLayout:
        layout = QHBoxLayout()
        self.recordButton = QPushButton(self)
        self.recordButton.setText("record")
        self.recordButton.setEnabled(False)
        self.recordButton.clicked.connect(self.__loadDataFromFiles)
        layout.addWidget(self.recordButton)
        self.calculationButton = QPushButton(self)
        self.calculationButton.setText("Calculation")
        self.calculationButton.setEnabled(False)
        layout.addWidget(self.calculationButton)
        self.saveExlButton = QPushButton(self)
        self.saveExlButton.setText("Save exel")
        self.saveExlButton.setEnabled(False)
        layout.addWidget(self.saveExlButton)
        return layout
    
    def bind(self, item:Experiment):
        self.model = item
        print(item)
        self.descriptionEdit.setText(item.description)
        self.fullModulation.setText(item.parameter.fullModulation)
        self.narrowModulation.setText(item.parameter.narrowModulation)
        self.numberRec.setText(item.parameter.countMetering)
        self.status.setText(item.status.value)
        self.setActiveComponent(item)
    
    def setCreateButtonListener(self, listener)->None:
        self._createExperementFunc = listener
    
    def createExperement(self)->None:
         self._createExperementFunc()
         self.enabled(True)


    def setSaveButtonListener(self, listener)->None:
        self.saveFunction = listener
    
    def setRecordButtonListener(self, listener)->None:
        self.recordButtonListener = listener
        
    
    def __loadDataFromFiles(self):
        self.recordButtonListener()
        self.numberRec.setText(len(self.model.meterings))
        self.calculationButton.setEnabled(True)


    def setCalculationButtonListener(self, listener)->None:
        self.calculationButton.clicked.connect(listener)

    def setSaveExelButtonListener(self, listener)->None:
        self.saveExlButton.clicked.connect(listener)

    def __save(self):
        self.model.description=self.descriptionEdit.toPlainText()
        self.model.parameter.fullModulation = float(self.fullModulation.getValue())
        self.model.parameter.narrowModulation = float(self.narrowModulation.getValue())
        self.model.parameter.countMetering = int(self.numberRec.getValue())
        self.saveFunction()
    
    def enabled(self, enable:bool):
        self.descriptionEdit.setEnabled(enable)
        self.fullModulation.setEnabled(enable)
        self.fullModulation.setEnabled(enable)
        self.narrowLabel.setEnabled(enable)
        self.narrowModulation.setEnabled(enable)
        self.recordButton.setEnabled(enable)
        # self.saveButton.setEnabled(enable)

    def setActiveComponent(self, item:Experiment):
        if item.status == ExperimentStatus.EDIT:
            self.enabled(True)
        else:
            self.enabled(False)
            self.saveExlButton.setEnabled(True)
        if len(item.meterings)>0:
            self.calculationButton.setEnabled(True)
        else:
            self.calculationButton.setEnabled(False)
