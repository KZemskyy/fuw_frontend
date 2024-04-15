from PySide6.QtWidgets import QHBoxLayout, QLabel, QLineEdit,QWidget

class LineEdit(QHBoxLayout):
    def __init__(self, widget:QWidget, text:str):
        super().__init__()
        self.label = QLabel(widget)
        self.label.setText(text)
        self.addWidget(self.label)
        self.input = QLineEdit(widget)
        self.addWidget(self.input)
    
    def setText(self, text):
        self.input.setText(str(text))
    
    def getValue(self):
        return self.input.text()