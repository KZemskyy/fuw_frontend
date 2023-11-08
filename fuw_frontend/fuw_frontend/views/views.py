# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'views.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateTimeEdit, QGraphicsView, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QTableView,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
from ..Model import Model, Experiment

class Ui_MainWindow(object):

    def __init__(self, model:Model) -> None:
        super().__init__()
        self.__model = model

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1114, 598)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.experimenTitleGroup = QGroupBox(self.centralwidget)
        self.experimenTitleGroup.setObjectName(u"experimenTitleGroup")
        self.experimenTitleGroup.setGeometry(QRect(130, 0, 981, 121))
        self.layoutWidget = QWidget(self.experimenTitleGroup)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 20, 971, 96))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.experimetDesrciptionLabel = QLabel(self.layoutWidget)
        self.experimetDesrciptionLabel.setObjectName(u"experimetDesrciptionLabel")

        self.verticalLayout.addWidget(self.experimetDesrciptionLabel)

        self.experimentDescription = QLineEdit(self.layoutWidget)
        self.experimentDescription.setObjectName(u"experimentDescription")
        self.experimentDescription.textEdited.connect(self.expetementDescriptionEdit)

        self.verticalLayout.addWidget(self.experimentDescription)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.createDateLabel = QLabel(self.layoutWidget)
        self.createDateLabel.setObjectName(u"createDateLabel")

        self.verticalLayout_2.addWidget(self.createDateLabel)

        self.dateTimeEdit = QDateTimeEdit(self.layoutWidget)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")

        self.verticalLayout_2.addWidget(self.dateTimeEdit)

        self.lastModyficationLabel = QLabel(self.layoutWidget)
        self.lastModyficationLabel.setObjectName(u"lastModyficationLabel")

        self.verticalLayout_2.addWidget(self.lastModyficationLabel)

        self.dateTimeEdit_2 = QDateTimeEdit(self.layoutWidget)
        self.dateTimeEdit_2.setObjectName(u"dateTimeEdit_2")

        self.verticalLayout_2.addWidget(self.dateTimeEdit_2)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.statusLabel = QLabel(self.layoutWidget)
        self.statusLabel.setObjectName(u"statusLabel")

        self.verticalLayout_3.addWidget(self.statusLabel)

        self.status = QLineEdit(self.layoutWidget)
        self.status.setObjectName(u"status")

        self.verticalLayout_3.addWidget(self.status)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.experimentSaveButton = QPushButton(self.layoutWidget)
        self.experimentSaveButton.setObjectName(u"experimentSaveButton")
        self.experimentSaveButton.clicked.connect(self.saveExperementFunction)

        self.verticalLayout_4.addWidget(self.experimentSaveButton)

        self.pushButton_2 = QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_4.addWidget(self.pushButton_2)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 5, 131, 591))
        self.verticalLayout_13 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.experementListLabel = QLabel(self.layoutWidget1)
        self.experementListLabel.setObjectName(u"experementListLabel")

        self.verticalLayout_13.addWidget(self.experementListLabel)

        self.ExperementListTable = QTableWidget(self.layoutWidget1)
        self.ExperementListTable.setObjectName(u"ExperementListTable")

        self.verticalLayout_13.addWidget(self.ExperementListTable)

        self.newExperementButton = QPushButton(self.layoutWidget1)
        self.newExperementButton.setObjectName(u"newExperementButton")
        self.newExperementButton.clicked.connect(self.newExperemenetClieck)

        self.verticalLayout_13.addWidget(self.newExperementButton)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(140, 120, 974, 471))
        self.MeteringsLayout = QHBoxLayout(self.widget)
        self.MeteringsLayout.setObjectName(u"MeteringsLayout")
        self.MeteringsLayout.setContentsMargins(0, 0, 0, 0)
        self.meteringListLayout = QVBoxLayout()
        self.meteringListLayout.setObjectName(u"meteringListLayout")
        self.meteringListLabel = QLabel(self.widget)
        self.meteringListLabel.setObjectName(u"meteringListLabel")

        self.meteringListLayout.addWidget(self.meteringListLabel)

        self.meteringListTable = QTableWidget(self.widget)
        self.meteringListTable.setObjectName(u"meteringListTable")

        self.meteringListLayout.addWidget(self.meteringListTable)

        self.newMeteringButton = QPushButton(self.widget)
        self.newMeteringButton.setObjectName(u"newMeteringButton")

        self.meteringListLayout.addWidget(self.newMeteringButton)


        self.MeteringsLayout.addLayout(self.meteringListLayout)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.meteringTitleLayout = QVBoxLayout()
        self.meteringTitleLayout.setObjectName(u"meteringTitleLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.meteringDescriptionLabel = QLabel(self.widget)
        self.meteringDescriptionLabel.setObjectName(u"meteringDescriptionLabel")

        self.verticalLayout_5.addWidget(self.meteringDescriptionLabel)

        self.meteringDescription = QLineEdit(self.widget)
        self.meteringDescription.setObjectName(u"meteringDescription")

        self.verticalLayout_5.addWidget(self.meteringDescription)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.meteringLastModificationLabel = QLabel(self.widget)
        self.meteringLastModificationLabel.setObjectName(u"meteringLastModificationLabel")

        self.verticalLayout_6.addWidget(self.meteringLastModificationLabel)

        self.dateTimeEdit_3 = QDateTimeEdit(self.widget)
        self.dateTimeEdit_3.setObjectName(u"dateTimeEdit_3")

        self.verticalLayout_6.addWidget(self.dateTimeEdit_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.meteringStatus = QLabel(self.widget)
        self.meteringStatus.setObjectName(u"meteringStatus")

        self.verticalLayout_7.addWidget(self.meteringStatus)

        self.meteringSatus = QLineEdit(self.widget)
        self.meteringSatus.setObjectName(u"meteringSatus")

        self.verticalLayout_7.addWidget(self.meteringSatus)


        self.horizontalLayout_2.addLayout(self.verticalLayout_7)

        self.recalculationButton = QPushButton(self.widget)
        self.recalculationButton.setObjectName(u"recalculationButton")

        self.horizontalLayout_2.addWidget(self.recalculationButton)


        self.meteringTitleLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.verticalLayout_14.addWidget(self.label)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.lineWidthLabel = QLabel(self.widget)
        self.lineWidthLabel.setObjectName(u"lineWidthLabel")

        self.verticalLayout_8.addWidget(self.lineWidthLabel)

        self.lineWidth = QLineEdit(self.widget)
        self.lineWidth.setObjectName(u"lineWidth")

        self.verticalLayout_8.addWidget(self.lineWidth)


        self.horizontalLayout_3.addLayout(self.verticalLayout_8)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.modulationLabel = QLabel(self.widget)
        self.modulationLabel.setObjectName(u"modulationLabel")

        self.verticalLayout_9.addWidget(self.modulationLabel)

        self.modulation = QLineEdit(self.widget)
        self.modulation.setObjectName(u"modulation")

        self.verticalLayout_9.addWidget(self.modulation)


        self.horizontalLayout_3.addLayout(self.verticalLayout_9)


        self.verticalLayout_14.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_5.addLayout(self.verticalLayout_14)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_15.addWidget(self.label_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.lineWidthLabel_2 = QLabel(self.widget)
        self.lineWidthLabel_2.setObjectName(u"lineWidthLabel_2")

        self.verticalLayout_11.addWidget(self.lineWidthLabel_2)

        self.modulation_2 = QLineEdit(self.widget)
        self.modulation_2.setObjectName(u"modulation_2")

        self.verticalLayout_11.addWidget(self.modulation_2)


        self.horizontalLayout_4.addLayout(self.verticalLayout_11)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.modulationLabel_2 = QLabel(self.widget)
        self.modulationLabel_2.setObjectName(u"modulationLabel_2")

        self.verticalLayout_10.addWidget(self.modulationLabel_2)

        self.lineWidth_2 = QLineEdit(self.widget)
        self.lineWidth_2.setObjectName(u"lineWidth_2")

        self.verticalLayout_10.addWidget(self.lineWidth_2)


        self.horizontalLayout_4.addLayout(self.verticalLayout_10)


        self.verticalLayout_15.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_5.addLayout(self.verticalLayout_15)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_16.addWidget(self.label_3)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout_16.addWidget(self.lineEdit)


        self.horizontalLayout_5.addLayout(self.verticalLayout_16)


        self.meteringTitleLayout.addLayout(self.horizontalLayout_5)


        self.verticalLayout_17.addLayout(self.meteringTitleLayout)

        self.resultLayout = QHBoxLayout()
        self.resultLayout.setObjectName(u"resultLayout")
        self.tableView = QTableView(self.widget)
        self.tableView.setObjectName(u"tableView")

        self.resultLayout.addWidget(self.tableView)

        self.graphicsView = QGraphicsView(self.widget)
        self.graphicsView.setObjectName(u"graphicsView")

        self.resultLayout.addWidget(self.graphicsView)


        self.verticalLayout_17.addLayout(self.resultLayout)


        self.MeteringsLayout.addLayout(self.verticalLayout_17)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"NMR", None))
        self.experimenTitleGroup.setTitle(QCoreApplication.translate("MainWindow", u"Experimen Title", None))
        self.experimetDesrciptionLabel.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.createDateLabel.setText(QCoreApplication.translate("MainWindow", u"Create Date", None))
        self.lastModyficationLabel.setText(QCoreApplication.translate("MainWindow", u"Last modification", None))
        self.statusLabel.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.experimentSaveButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Action", None))
        self.experementListLabel.setText(QCoreApplication.translate("MainWindow", u"Experement List", None))
        self.newExperementButton.setText(QCoreApplication.translate("MainWindow", u"New Experement", None))
        self.meteringListLabel.setText(QCoreApplication.translate("MainWindow", u"Metering List", None))
        self.newMeteringButton.setText(QCoreApplication.translate("MainWindow", u"New Metering", None))
        self.meteringDescriptionLabel.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.meteringLastModificationLabel.setText(QCoreApplication.translate("MainWindow", u"Last modification", None))
        self.meteringStatus.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.recalculationButton.setText(QCoreApplication.translate("MainWindow", u"Action", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"wide line", None))
        self.lineWidthLabel.setText(QCoreApplication.translate("MainWindow", u"Line width", None))
        self.modulationLabel.setText(QCoreApplication.translate("MainWindow", u"Modulation", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"narrow line", None))
        self.lineWidthLabel_2.setText(QCoreApplication.translate("MainWindow", u"Line width", None))
        self.modulationLabel_2.setText(QCoreApplication.translate("MainWindow", u"Modulation", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"number of Metering", None))
    # retranslateUi

    def setNewExperementFunction(self, newExperemenetClieckAction):
        self.newExperemenetClieck = newExperemenetClieckAction
    def setSaveExperementFunction(self, savefunction):
        self.saveExperementFunction = savefunction

    def setExperement(self, selectedExperement:Experiment):
        self.experimentDescription.setText(selectedExperement.description) 

    def expetementDescriptionEdit(self, text):
        self.__model.getSelectedExperement().description = text


