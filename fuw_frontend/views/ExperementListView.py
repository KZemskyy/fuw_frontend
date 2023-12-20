
from PySide6.QtWidgets import QLabel, QTableView,  QVBoxLayout, QWidget

class ExperementListView(QVBoxLayout):
    def __init__(self, parent: QWidget)->None:
        super().__init__(parent)
        
        self.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(parent)
        self.label.setText("Experement")
        self.addWidget(self.label)
        self.experementlist = QTableView(parent)
        self.addWidget(self.experementlist)        
