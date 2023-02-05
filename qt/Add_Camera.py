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
        MainWindow.resize(175, 353)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 48))
        self.frame.setMaximumSize(QSize(157, 48))
        font = QFont()
        font.setFamily(u"Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.frame.setFont(font)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 181, 41))
        self.label.setMinimumSize(QSize(181, 0))
        self.label.setMaximumSize(QSize(181, 41))
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(157, 47))
        self.frame_2.setMaximumSize(QSize(157, 47))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 0, 81, 21))
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.label_2.setFont(font1)
        self.inputCamIP = QLineEdit(self.frame_2)
        self.inputCamIP.setObjectName(u"inputCamIP")
        self.inputCamIP.setGeometry(QRect(0, 20, 151, 20))
        self.inputCamIP.setMinimumSize(QSize(151, 0))

        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(157, 48))
        self.frame_3.setMaximumSize(QSize(157, 48))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 0, 71, 21))
        self.label_3.setFont(font1)
        self.inputCamUsername = QLineEdit(self.frame_3)
        self.inputCamUsername.setObjectName(u"inputCamUsername")
        self.inputCamUsername.setGeometry(QRect(0, 20, 151, 20))
        self.inputCamUsername.setMinimumSize(QSize(151, 0))

        self.verticalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(157, 47))
        self.frame_4.setMaximumSize(QSize(157, 47))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 0, 61, 16))
        self.label_4.setFont(font1)
        self.inputCamPassword = QLineEdit(self.frame_4)
        self.inputCamPassword.setObjectName(u"inputCamPassword")
        self.inputCamPassword.setGeometry(QRect(0, 20, 151, 20))
        self.inputCamPassword.setMinimumSize(QSize(151, 0))

        self.verticalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(157, 48))
        self.frame_5.setMaximumSize(QSize(157, 48))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 0, 91, 16))
        self.label_5.setFont(font1)
        self.inputCamDisplayName = QLineEdit(self.frame_5)
        self.inputCamDisplayName.setObjectName(u"inputCamDisplayName")
        self.inputCamDisplayName.setGeometry(QRect(0, 20, 151, 20))
        self.inputCamDisplayName.setMinimumSize(QSize(151, 0))

        self.verticalLayout.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.centralwidget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(157, 47))
        self.frame_6.setMaximumSize(QSize(157, 47))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.addCamBtn = QPushButton(self.frame_6)
        self.addCamBtn.setObjectName(u"addCamBtn")
        self.addCamBtn.setGeometry(QRect(0, 10, 151, 23))
        self.addCamBtn.setMinimumSize(QSize(151, 0))
        self.addCamBtn.setFont(font1)

        self.verticalLayout.addWidget(self.frame_6)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Add Camera", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Camera IP", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Display name", None))
        self.addCamBtn.setText(QCoreApplication.translate("MainWindow", u"Add Camera", None))
    # retranslateUi

