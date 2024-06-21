from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import  QDialog, QLayout,QVBoxLayout,QLabel
from ..Model import ExperimentStatus

class BaseDialog(QDialog):
    def __init__(self, title:str, layout:QLayout) -> None:
        super().__init__()
        self.setWindowTitle(title)
        self.setLayout(layout)

class LoadFilesDialog(BaseDialog):
    def __init__(self, files) -> None:
        layout = QVBoxLayout()
        for file in files:
            label = QLabel()
            if file["status"] == "succes":
                label.setText(f"{file['name']}  - succes")
            else:
                label.setText(f"{file['name']}  - error")
            layout.addWidget(label)
        super().__init__("Load Files report", layout)

class CalculationResultDialog(BaseDialog):
    def __init__(self, status: ExperimentStatus, exceptionMetering:list) -> None:
        layout = QVBoxLayout()
        if status == ExperimentStatus.CALCULATE:
            label = QLabel()
            label.setText("All calulations Complete!")
            layout.addWidget(label)
        else:
            label = QLabel()
            label.setText("Calulations are particle Complete!")
            layout.addWidget(label)
            label = QLabel()
            label.setText("metering where was exceptions:")
            layout.addWidget(label)
            for metering in exceptionMetering:
                label = QLabel()
                label.setText(metering)
                layout.addWidget(label)
        super().__init__("Calculations Report", layout)