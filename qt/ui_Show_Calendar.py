# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Show_Calendar.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(450, 600)
        MainWindow.setMinimumSize(QSize(450, 600))
        MainWindow.setMaximumSize(QSize(450, 600))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(450, 294))
        self.centralwidget.setMaximumSize(QSize(450, 600))
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(441, 301))
        self.frame.setMaximumSize(QSize(441, 600))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.comboBox = QComboBox(self.frame)
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout.addWidget(self.comboBox)

        self.calendarWidget = QCalendarWidget(self.frame)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setMaximumSize(QSize(16777215, 300))

        self.verticalLayout.addWidget(self.calendarWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.timeEdit = QTimeEdit(self.frame)
        self.timeEdit.setObjectName(u"timeEdit")

        self.horizontalLayout.addWidget(self.timeEdit)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.timeEdit_2 = QTimeEdit(self.frame)
        self.timeEdit_2.setObjectName(u"timeEdit_2")
        self.timeEdit_2.setCurrentSection(QDateTimeEdit.HourSection)
        self.timeEdit_2.setCalendarPopup(False)
        self.timeEdit_2.setTime(QTime(23, 59, 59))

        self.horizontalLayout_2.addWidget(self.timeEdit_2)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.showDataBtn = QPushButton(self.frame)
        self.showDataBtn.setObjectName(u"showDataBtn")

        self.verticalLayout.addWidget(self.showDataBtn)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_2.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.downloadExcelDataBtn = QPushButton(self.frame)
        self.downloadExcelDataBtn.setObjectName(u"downloadExcelDataBtn")

        self.verticalLayout_3.addWidget(self.downloadExcelDataBtn)


        self.verticalLayout.addLayout(self.verticalLayout_3)


        self.verticalLayout_4.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 450, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Calendar", None))
        self.timeEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"h:mm", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Start time", None))
        self.timeEdit_2.setDisplayFormat(QCoreApplication.translate("MainWindow", u"h:mm", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"End time", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.showDataBtn.setText(QCoreApplication.translate("MainWindow", u"Show Data Hourly", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Show Data Cardinalwise", None))
        self.downloadExcelDataBtn.setText(QCoreApplication.translate("MainWindow", u"Download Excel Data", None))
    # retranslateUi

