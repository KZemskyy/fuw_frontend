# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'views.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################


from PySide6.QtCore import (QCoreApplication, QMetaObject,  QRect)

from PySide6.QtWidgets import QWidget
from .CreateExperementView import CreateBar
from .ExperementListView import ExperementListView
from .ResultView import ResultView
from ..Model import Experiment, Model

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
        
        self.resultView =ResultView(self.widget1)
        self.experementListLayout.addLayout(self.resultView)

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
        self.resultView.setMeteringList(experement.meterings)
    
    def setRecordButtonListener(self, listener)->None:
        self.__createWidget.setRecordButtonListener(listener)
    
    def setCalculationButtonListener(self, listener)->None:
        self.__createWidget.setCalculationButtonListener(listener)
    

    def setSelectExperementInList(self, listener)->None:
        self.experementListLayout.setSelectExperement(listener)

    def setSaveExelButtonListener(self, listener)->None:
        self.__createWidget.setSaveExelButtonListener(listener)
    
    def refresh(self, model:Model)->None:
        self.__createWidget.bind(model.getSelectedExperement())
        self.experementListLayout.setExperementList(model.getExperementList())
        self.resultView.setMeteringList(model.getSelectedExperement().meterings)
        



