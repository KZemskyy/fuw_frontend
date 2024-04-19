# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'views.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

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
from .CreateExperementView import CreateBar
from .ExperementListView import ExperementListView
from .ResultView import ResultView
from ..Model import Experiment

class Ui_MainWindow(object):
        
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1043, 586)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.__createWidget = CreateBar(self.centralwidget)
        
        self.widget1 = QWidget(self.centralwidget)
        self.widget1.setGeometry(QRect(260, 0, 771, 571))
        self.experementListLayout = ExperementListView(self.widget1)
        
        self.result =ResultView(self.widget1)
        self.experementListLayout.addLayout(self.result)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"FUW", None))

    def setCreateButtonListener(self, listener)->None:
        self.__createWidget.setCreateButtonListener(listener)

    def setSaveButtonListener(self, listener)->None:
        self.__createWidget.setSaveButtonListener(listener)       

    def setExperement(self,experement:Experiment)->None:
        self.__createWidget.bind(experement)
    
    def setRecordButtonListener(self, listener)->None:
        self.__createWidget.setRecordButtonListener(listener)
    
    def setSelectExperementInList(self, listener)->None:
        self.experementListLayout.setSelectExperement(listener)



