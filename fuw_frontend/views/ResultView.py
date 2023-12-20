
from typing import Optional
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)

from PySide6.QtWidgets import (QApplication, QGraphicsView, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QTableView, QTextEdit, QVBoxLayout,
    QWidget)
from .utils import LineEdit

class ResultView(QVBoxLayout):
    def __init__(self,  parent: QWidget)->None:
        super().__init__(parent)

        
        self.horizontalLayout = QHBoxLayout()
        self.date = LineEdit(parent,"Date")
        self.horizontalLayout.addLayout(self.date)
        self.lastModification = LineEdit(parent,"modification")
        self.horizontalLayout.addLayout(self.lastModification)
        self.addLayout(self.horizontalLayout)

        # self.verticalLayout_3 = QVBoxLayout()
        # self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.recordTable = QTableView(parent)
        self.addWidget(self.recordTable)

        self.graphicsView = QGraphicsView(parent)
        self.addWidget(self.graphicsView)
