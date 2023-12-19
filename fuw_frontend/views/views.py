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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1043, 586)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = CreateBar(self.centralwidget)
        
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
        self.experementlabel.setText(QCoreApplication.translate("MainWindow", u"Experement", None))
        self.dataLabel.setText(QCoreApplication.translate("MainWindow", u"Data", None))
        self.lastLabel.setText(QCoreApplication.translate("MainWindow", u"Last modification", None))
    # retranslateUi

