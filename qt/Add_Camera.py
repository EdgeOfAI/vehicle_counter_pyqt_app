# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Add_Camera.ui'
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
        MainWindow.resize(297, 447)
        MainWindow.setMinimumSize(QSize(297, 400))
        MainWindow.setMaximumSize(QSize(450, 450))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(180, 335))
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setLineWidth(0)

        self.verticalLayout_6.addWidget(self.label_2)

        self.inputCamIP = QLineEdit(self.centralwidget)
        self.inputCamIP.setObjectName(u"inputCamIP")
        self.inputCamIP.setMinimumSize(QSize(151, 0))

        self.verticalLayout_6.addWidget(self.inputCamIP)


        self.verticalLayout.addLayout(self.verticalLayout_6)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setLineWidth(0)

        self.verticalLayout_5.addWidget(self.label_3)

        self.inputCamUsername = QLineEdit(self.centralwidget)
        self.inputCamUsername.setObjectName(u"inputCamUsername")
        self.inputCamUsername.setMinimumSize(QSize(151, 0))

        self.verticalLayout_5.addWidget(self.inputCamUsername)


        self.verticalLayout.addLayout(self.verticalLayout_5)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setLineWidth(0)

        self.verticalLayout_4.addWidget(self.label_4)

        self.inputCamPassword = QLineEdit(self.centralwidget)
        self.inputCamPassword.setObjectName(u"inputCamPassword")
        self.inputCamPassword.setMinimumSize(QSize(151, 0))

        self.verticalLayout_4.addWidget(self.inputCamPassword)


        self.verticalLayout.addLayout(self.verticalLayout_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setLineWidth(0)

        self.verticalLayout_3.addWidget(self.label_5)

        self.inputCamDisplayName = QLineEdit(self.centralwidget)
        self.inputCamDisplayName.setObjectName(u"inputCamDisplayName")
        self.inputCamDisplayName.setMinimumSize(QSize(151, 0))

        self.verticalLayout_3.addWidget(self.inputCamDisplayName)


        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.addCamBtn = QPushButton(self.centralwidget)
        self.addCamBtn.setObjectName(u"addCamBtn")
        self.addCamBtn.setMinimumSize(QSize(151, 0))
        self.addCamBtn.setFont(font)

        self.verticalLayout_2.addWidget(self.addCamBtn)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Add Camera", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Camera IP", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Display name", None))
        self.addCamBtn.setText(QCoreApplication.translate("MainWindow", u"Add Camera", None))
    # retranslateUi

