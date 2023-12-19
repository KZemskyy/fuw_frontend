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
from PySide6.QtWidgets import (QApplication, QGraphicsView, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QTableView, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1043, 586)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 12, 258, 521))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.CreateButton = QPushButton(self.widget)
        self.CreateButton.setObjectName(u"CreateButton")

        self.verticalLayout_2.addWidget(self.CreateButton)

        self.description = QLabel(self.widget)
        self.description.setObjectName(u"description")

        self.verticalLayout_2.addWidget(self.description)

        self.descriptionEdit = QTextEdit(self.widget)
        self.descriptionEdit.setObjectName(u"descriptionEdit")
        self.descriptionEdit.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))

        self.verticalLayout_2.addWidget(self.descriptionEdit)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.parametersLabel = QLabel(self.widget)
        self.parametersLabel.setObjectName(u"parametersLabel")

        self.verticalLayout.addWidget(self.parametersLabel)

        self.fullLineLabel = QLabel(self.widget)
        self.fullLineLabel.setObjectName(u"fullLineLabel")

        self.verticalLayout.addWidget(self.fullLineLabel)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widthFullLineLabel = QLabel(self.widget)
        self.widthFullLineLabel.setObjectName(u"widthFullLineLabel")

        self.horizontalLayout_2.addWidget(self.widthFullLineLabel)

        self.widthFullLine = QLineEdit(self.widget)
        self.widthFullLine.setObjectName(u"widthFullLine")

        self.horizontalLayout_2.addWidget(self.widthFullLine)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.modulationFullLineLabel = QLabel(self.widget)
        self.modulationFullLineLabel.setObjectName(u"modulationFullLineLabel")

        self.horizontalLayout_3.addWidget(self.modulationFullLineLabel)

        self.modulationFullLine = QLineEdit(self.widget)
        self.modulationFullLine.setObjectName(u"modulationFullLine")

        self.horizontalLayout_3.addWidget(self.modulationFullLine)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.narrowLabel = QLabel(self.widget)
        self.narrowLabel.setObjectName(u"narrowLabel")

        self.verticalLayout.addWidget(self.narrowLabel)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.widthNarrowLineLabel = QLabel(self.widget)
        self.widthNarrowLineLabel.setObjectName(u"widthNarrowLineLabel")

        self.horizontalLayout_4.addWidget(self.widthNarrowLineLabel)

        self.widthNarrowLine = QLineEdit(self.widget)
        self.widthNarrowLine.setObjectName(u"widthNarrowLine")

        self.horizontalLayout_4.addWidget(self.widthNarrowLine)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.modulationNarrowLineLabel = QLabel(self.widget)
        self.modulationNarrowLineLabel.setObjectName(u"modulationNarrowLineLabel")

        self.horizontalLayout_5.addWidget(self.modulationNarrowLineLabel)

        self.modulationNarrowLine = QLineEdit(self.widget)
        self.modulationNarrowLine.setObjectName(u"modulationNarrowLine")

        self.horizontalLayout_5.addWidget(self.modulationNarrowLine)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.numberRecLabel = QLabel(self.widget)
        self.numberRecLabel.setObjectName(u"numberRecLabel")

        self.verticalLayout.addWidget(self.numberRecLabel)

        self.numberRec = QLineEdit(self.widget)
        self.numberRec.setObjectName(u"numberRec")

        self.verticalLayout.addWidget(self.numberRec)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.recordButton = QPushButton(self.widget)
        self.recordButton.setObjectName(u"recordButton")

        self.horizontalLayout_6.addWidget(self.recordButton)

        self.calculationButton = QPushButton(self.widget)
        self.calculationButton.setObjectName(u"calculationButton")

        self.horizontalLayout_6.addWidget(self.calculationButton)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.statusLabel = QLabel(self.widget)
        self.statusLabel.setObjectName(u"statusLabel")

        self.horizontalLayout_7.addWidget(self.statusLabel)

        self.statusLabel_2 = QLineEdit(self.widget)
        self.statusLabel_2.setObjectName(u"statusLabel_2")

        self.horizontalLayout_7.addWidget(self.statusLabel_2)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.saveButton = QPushButton(self.widget)
        self.saveButton.setObjectName(u"saveButton")

        self.verticalLayout.addWidget(self.saveButton)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.widget1 = QWidget(self.centralwidget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(260, 0, 771, 571))
        self.verticalLayout_4 = QVBoxLayout(self.widget1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.experementlabel = QLabel(self.widget1)
        self.experementlabel.setObjectName(u"experementlabel")

        self.verticalLayout_4.addWidget(self.experementlabel)

        self.experementTable = QTableView(self.widget1)
        self.experementTable.setObjectName(u"experementTable")

        self.verticalLayout_4.addWidget(self.experementTable)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.dataLabel = QLabel(self.widget1)
        self.dataLabel.setObjectName(u"dataLabel")

        self.horizontalLayout.addWidget(self.dataLabel)

        self.lineEdit = QLineEdit(self.widget1)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.lastLabel = QLabel(self.widget1)
        self.lastLabel.setObjectName(u"lastLabel")

        self.horizontalLayout.addWidget(self.lastLabel)

        self.lineEdit_2 = QLineEdit(self.widget1)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout.addWidget(self.lineEdit_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.recordTable = QTableView(self.widget1)
        self.recordTable.setObjectName(u"recordTable")

        self.verticalLayout_3.addWidget(self.recordTable)

        self.graphicsView = QGraphicsView(self.widget1)
        self.graphicsView.setObjectName(u"graphicsView")

        self.verticalLayout_3.addWidget(self.graphicsView)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"FUW", None))
        self.CreateButton.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.description.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.parametersLabel.setText(QCoreApplication.translate("MainWindow", u"Parameters:", None))
        self.fullLineLabel.setText(QCoreApplication.translate("MainWindow", u"Full line:", None))
        self.widthFullLineLabel.setText(QCoreApplication.translate("MainWindow", u"width", None))
        self.modulationFullLineLabel.setText(QCoreApplication.translate("MainWindow", u"modulation", None))
        self.narrowLabel.setText(QCoreApplication.translate("MainWindow", u"Narrow Line:", None))
        self.widthNarrowLineLabel.setText(QCoreApplication.translate("MainWindow", u"width", None))
        self.modulationNarrowLineLabel.setText(QCoreApplication.translate("MainWindow", u"modulation", None))
        self.numberRecLabel.setText(QCoreApplication.translate("MainWindow", u"Number of records", None))
        self.recordButton.setText(QCoreApplication.translate("MainWindow", u"record", None))
        self.calculationButton.setText(QCoreApplication.translate("MainWindow", u"Calculation", None))
        self.statusLabel.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.saveButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.experementlabel.setText(QCoreApplication.translate("MainWindow", u"Experement", None))
        self.dataLabel.setText(QCoreApplication.translate("MainWindow", u"Data", None))
        self.lastLabel.setText(QCoreApplication.translate("MainWindow", u"Last modification", None))
    # retranslateUi

