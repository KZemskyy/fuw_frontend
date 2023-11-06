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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QDateTimeEdit, QFrame,
    QGraphicsView, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QTableView, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.setEnabled(True)
        mainWindow.resize(1179, 752)
        mainWindow.setContextMenuPolicy(Qt.DefaultContextMenu)
        mainWindow.setAcceptDrops(True)
        mainWindow.setAnimated(False)
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(5, 10, 1191, 741))
        self.mainFraim = QFrame(self.frame)
        self.mainFraim.setObjectName(u"mainFraim")
        self.mainFraim.setGeometry(QRect(1, 1, 1173, 731))
        self.horizontalLayout_5 = QHBoxLayout(self.mainFraim)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tableView = QTableView(self.mainFraim)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout_3.addWidget(self.tableView)

        self.newExperementButton = QPushButton(self.mainFraim)
        self.newExperementButton.setObjectName(u"newExperementButton")

        self.verticalLayout_3.addWidget(self.newExperementButton)


        self.horizontalLayout_5.addLayout(self.verticalLayout_3)

        self.experementFrame = QFrame(self.mainFraim)
        self.experementFrame.setObjectName(u"experementFrame")
        self.experementFrame.setFrameShape(QFrame.Panel)
        self.experementFrame.setFrameShadow(QFrame.Plain)
        self.experementFrame.setLineWidth(1)
        self.experementFrame.setMidLineWidth(0)
        self.verticalLayout_6 = QVBoxLayout(self.experementFrame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.ExperementPanel = QFrame(self.experementFrame)
        self.ExperementPanel.setObjectName(u"ExperementPanel")
        self.ExperementPanel.setFrameShape(QFrame.Panel)
        self.horizontalLayout_3 = QHBoxLayout(self.ExperementPanel)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.nameLabel = QLabel(self.ExperementPanel)
        self.nameLabel.setObjectName(u"nameLabel")

        self.horizontalLayout_3.addWidget(self.nameLabel)

        self.lineEdit = QLineEdit(self.ExperementPanel)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_3.addWidget(self.lineEdit)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.createlabel = QLabel(self.ExperementPanel)
        self.createlabel.setObjectName(u"createlabel")
        self.createlabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.createlabel)

        self.dateTimeEdit = QDateTimeEdit(self.ExperementPanel)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")

        self.verticalLayout_4.addWidget(self.dateTimeEdit)

        self.label = QLabel(self.ExperementPanel)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label)

        self.dateTimeEdit_2 = QDateTimeEdit(self.ExperementPanel)
        self.dateTimeEdit_2.setObjectName(u"dateTimeEdit_2")

        self.verticalLayout_4.addWidget(self.dateTimeEdit_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)

        self.statusLabel = QLabel(self.ExperementPanel)
        self.statusLabel.setObjectName(u"statusLabel")

        self.horizontalLayout_3.addWidget(self.statusLabel)

        self.lineEdit_2 = QLineEdit(self.ExperementPanel)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_3.addWidget(self.lineEdit_2)

        self.saveButton = QPushButton(self.ExperementPanel)
        self.saveButton.setObjectName(u"saveButton")

        self.horizontalLayout_3.addWidget(self.saveButton)

        self.actionButton = QPushButton(self.ExperementPanel)
        self.actionButton.setObjectName(u"actionButton")

        self.horizontalLayout_3.addWidget(self.actionButton)


        self.verticalLayout_6.addWidget(self.ExperementPanel)

        self.MeasurementFtame = QFrame(self.experementFrame)
        self.MeasurementFtame.setObjectName(u"MeasurementFtame")
        self.MeasurementFtame.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_4 = QHBoxLayout(self.MeasurementFtame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.metrixListFrame = QFrame(self.MeasurementFtame)
        self.metrixListFrame.setObjectName(u"metrixListFrame")
        self.verticalLayout = QVBoxLayout(self.metrixListFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableView_2 = QTableView(self.metrixListFrame)
        self.tableView_2.setObjectName(u"tableView_2")
        self.tableView_2.horizontalHeader().setVisible(True)

        self.verticalLayout.addWidget(self.tableView_2)

        self.newMeasurement = QPushButton(self.metrixListFrame)
        self.newMeasurement.setObjectName(u"newMeasurement")

        self.verticalLayout.addWidget(self.newMeasurement)


        self.horizontalLayout_4.addWidget(self.metrixListFrame)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.MeasurementTitlPanel = QFrame(self.MeasurementFtame)
        self.MeasurementTitlPanel.setObjectName(u"MeasurementTitlPanel")
        self.MeasurementTitlPanel.setFrameShape(QFrame.Panel)
        self.horizontalLayout_2 = QHBoxLayout(self.MeasurementTitlPanel)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.descLabel = QLabel(self.MeasurementTitlPanel)
        self.descLabel.setObjectName(u"descLabel")

        self.horizontalLayout_2.addWidget(self.descLabel)

        self.lineEdit_3 = QLineEdit(self.MeasurementTitlPanel)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout_2.addWidget(self.lineEdit_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.dateTimeEdit_3 = QDateTimeEdit(self.MeasurementTitlPanel)
        self.dateTimeEdit_3.setObjectName(u"dateTimeEdit_3")

        self.verticalLayout_2.addWidget(self.dateTimeEdit_3)

        self.dateTimeEdit_4 = QDateTimeEdit(self.MeasurementTitlPanel)
        self.dateTimeEdit_4.setObjectName(u"dateTimeEdit_4")

        self.verticalLayout_2.addWidget(self.dateTimeEdit_4)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.label_2 = QLabel(self.MeasurementTitlPanel)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_4 = QLineEdit(self.MeasurementTitlPanel)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.horizontalLayout_2.addWidget(self.lineEdit_4)

        self.pushButton_5 = QPushButton(self.MeasurementTitlPanel)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_2.addWidget(self.pushButton_5)


        self.verticalLayout_5.addWidget(self.MeasurementTitlPanel)

        self.ResultPanel = QFrame(self.MeasurementFtame)
        self.ResultPanel.setObjectName(u"ResultPanel")
        self.horizontalLayout = QHBoxLayout(self.ResultPanel)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tableWidget = QTableWidget(self.ResultPanel)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableWidget.setAutoScrollMargin(15)

        self.horizontalLayout.addWidget(self.tableWidget)

        self.graphicsView = QGraphicsView(self.ResultPanel)
        self.graphicsView.setObjectName(u"graphicsView")

        self.horizontalLayout.addWidget(self.graphicsView)


        self.verticalLayout_5.addWidget(self.ResultPanel)


        self.horizontalLayout_4.addLayout(self.verticalLayout_5)


        self.verticalLayout_6.addWidget(self.MeasurementFtame)


        self.horizontalLayout_5.addWidget(self.experementFrame)

        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"NMR", None))
        self.newExperementButton.setText(QCoreApplication.translate("mainWindow", u"New Experement", None))
        self.nameLabel.setText(QCoreApplication.translate("mainWindow", u"Description ", None))
        self.createlabel.setText(QCoreApplication.translate("mainWindow", u"Create Data", None))
        self.label.setText(QCoreApplication.translate("mainWindow", u"Last modify", None))
        self.statusLabel.setText(QCoreApplication.translate("mainWindow", u"Status ", None))
        self.saveButton.setText(QCoreApplication.translate("mainWindow", u"Save", None))
        self.actionButton.setText(QCoreApplication.translate("mainWindow", u"Action", None))
        self.newMeasurement.setText(QCoreApplication.translate("mainWindow", u"New Measurement", None))
        self.descLabel.setText(QCoreApplication.translate("mainWindow", u"Description ", None))
        self.label_2.setText(QCoreApplication.translate("mainWindow", u"Startus", None))
        self.pushButton_5.setText(QCoreApplication.translate("mainWindow", u"recalculation", None))
    # retranslateUi

