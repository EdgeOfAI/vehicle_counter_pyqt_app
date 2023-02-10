# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Edit_Camera.ui'
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
        MainWindow.resize(259, 648)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(240, 48))
        self.frame.setMaximumSize(QSize(240, 48))
        font = QFont()
        font.setFamily(u"Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.frame.setFont(font)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(0)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 240, 41))
        self.label.setMinimumSize(QSize(240, 0))
        self.label.setMaximumSize(QSize(240, 41))
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.frame)

        self.camerasList = QComboBox(self.centralwidget)
        self.camerasList.setObjectName(u"camerasList")
        self.camerasList.setMinimumSize(QSize(235, 0))
        self.camerasList.setMaximumSize(QSize(180, 16777215))

        self.verticalLayout.addWidget(self.camerasList)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(235, 47))
        self.frame_2.setMaximumSize(QSize(157, 47))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setLineWidth(0)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 0, 81, 21))
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.label_2.setFont(font1)
        self.inputCamIP = QLineEdit(self.frame_2)
        self.inputCamIP.setObjectName(u"inputCamIP")
        self.inputCamIP.setGeometry(QRect(0, 20, 235, 20))
        self.inputCamIP.setMinimumSize(QSize(235, 0))

        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(235, 48))
        self.frame_3.setMaximumSize(QSize(157, 48))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setLineWidth(0)
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 0, 71, 21))
        self.label_3.setFont(font1)
        self.inputCamUsername = QLineEdit(self.frame_3)
        self.inputCamUsername.setObjectName(u"inputCamUsername")
        self.inputCamUsername.setGeometry(QRect(0, 20, 235, 20))
        self.inputCamUsername.setMinimumSize(QSize(235, 0))

        self.verticalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(235, 47))
        self.frame_4.setMaximumSize(QSize(157, 47))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_4.setLineWidth(0)
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 0, 100, 16))
        self.label_4.setMinimumSize(QSize(100, 0))
        self.label_4.setFont(font1)
        self.inputCamPassword = QLineEdit(self.frame_4)
        self.inputCamPassword.setObjectName(u"inputCamPassword")
        self.inputCamPassword.setGeometry(QRect(0, 20, 235, 20))
        self.inputCamPassword.setMinimumSize(QSize(235, 0))

        self.verticalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(235, 48))
        self.frame_5.setMaximumSize(QSize(157, 48))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_5.setLineWidth(0)
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 0, 91, 16))
        self.label_5.setFont(font1)
        self.inputCamDisplayName = QLineEdit(self.frame_5)
        self.inputCamDisplayName.setObjectName(u"inputCamDisplayName")
        self.inputCamDisplayName.setGeometry(QRect(0, 20, 235, 20))
        self.inputCamDisplayName.setMinimumSize(QSize(235, 0))

        self.verticalLayout.addWidget(self.frame_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetMaximumSize)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setLineWidth(0)

        self.horizontalLayout_2.addWidget(self.label_6)

        self.Nx1 = QLineEdit(self.centralwidget)
        self.Nx1.setObjectName(u"Nx1")

        self.horizontalLayout_2.addWidget(self.Nx1)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setLineWidth(0)

        self.horizontalLayout_4.addWidget(self.label_8)

        self.Ny1 = QLineEdit(self.centralwidget)
        self.Ny1.setObjectName(u"Ny1")

        self.horizontalLayout_4.addWidget(self.Ny1)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setLineWidth(0)

        self.horizontalLayout_5.addWidget(self.label_9)

        self.Nx2 = QLineEdit(self.centralwidget)
        self.Nx2.setObjectName(u"Nx2")

        self.horizontalLayout_5.addWidget(self.Nx2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setLineWidth(0)

        self.horizontalLayout_7.addWidget(self.label_11)

        self.Ny2 = QLineEdit(self.centralwidget)
        self.Ny2.setObjectName(u"Ny2")

        self.horizontalLayout_7.addWidget(self.Ny2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setLineWidth(0)

        self.horizontalLayout_6.addWidget(self.label_10)

        self.Wx1 = QLineEdit(self.centralwidget)
        self.Wx1.setObjectName(u"Wx1")

        self.horizontalLayout_6.addWidget(self.Wx1)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setLineWidth(0)

        self.horizontalLayout_9.addWidget(self.label_12)

        self.Wy1 = QLineEdit(self.centralwidget)
        self.Wy1.setObjectName(u"Wy1")

        self.horizontalLayout_9.addWidget(self.Wy1)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setLineWidth(0)

        self.horizontalLayout_8.addWidget(self.label_13)

        self.Wx2 = QLineEdit(self.centralwidget)
        self.Wx2.setObjectName(u"Wx2")

        self.horizontalLayout_8.addWidget(self.Wx2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setLineWidth(0)

        self.horizontalLayout_3.addWidget(self.label_7)

        self.Wy2 = QLineEdit(self.centralwidget)
        self.Wy2.setObjectName(u"Wy2")

        self.horizontalLayout_3.addWidget(self.Wy2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setLineWidth(0)
        self.label_14.setTextFormat(Qt.AutoText)

        self.horizontalLayout_10.addWidget(self.label_14)

        self.Ex1 = QLineEdit(self.centralwidget)
        self.Ex1.setObjectName(u"Ex1")

        self.horizontalLayout_10.addWidget(self.Ex1)


        self.verticalLayout_3.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setLineWidth(0)

        self.horizontalLayout_18.addWidget(self.label_15)

        self.Ey1 = QLineEdit(self.centralwidget)
        self.Ey1.setObjectName(u"Ey1")

        self.horizontalLayout_18.addWidget(self.Ey1)


        self.verticalLayout_3.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_16 = QLabel(self.centralwidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setLineWidth(0)

        self.horizontalLayout_17.addWidget(self.label_16)

        self.Ex2 = QLineEdit(self.centralwidget)
        self.Ex2.setObjectName(u"Ex2")

        self.horizontalLayout_17.addWidget(self.Ex2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_17 = QLabel(self.centralwidget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setLineWidth(0)

        self.horizontalLayout_16.addWidget(self.label_17)

        self.Ey2 = QLineEdit(self.centralwidget)
        self.Ey2.setObjectName(u"Ey2")

        self.horizontalLayout_16.addWidget(self.Ey2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_18 = QLabel(self.centralwidget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setLineWidth(0)

        self.horizontalLayout_15.addWidget(self.label_18)

        self.Sx1 = QLineEdit(self.centralwidget)
        self.Sx1.setObjectName(u"Sx1")

        self.horizontalLayout_15.addWidget(self.Sx1)


        self.verticalLayout_3.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_19 = QLabel(self.centralwidget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setLineWidth(0)

        self.horizontalLayout_14.addWidget(self.label_19)

        self.Sy1 = QLineEdit(self.centralwidget)
        self.Sy1.setObjectName(u"Sy1")

        self.horizontalLayout_14.addWidget(self.Sy1)


        self.verticalLayout_3.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_20 = QLabel(self.centralwidget)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setLineWidth(0)

        self.horizontalLayout_13.addWidget(self.label_20)

        self.Sx2 = QLineEdit(self.centralwidget)
        self.Sx2.setObjectName(u"Sx2")

        self.horizontalLayout_13.addWidget(self.Sx2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_21 = QLabel(self.centralwidget)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setLineWidth(0)

        self.horizontalLayout_12.addWidget(self.label_21)

        self.Sy2 = QLineEdit(self.centralwidget)
        self.Sy2.setObjectName(u"Sy2")

        self.horizontalLayout_12.addWidget(self.Sy2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_12)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.frame_6 = QFrame(self.centralwidget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(235, 47))
        self.frame_6.setMaximumSize(QSize(157, 47))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.frame_6.setLineWidth(0)
        self.editCamBtn = QPushButton(self.frame_6)
        self.editCamBtn.setObjectName(u"editCamBtn")
        self.editCamBtn.setGeometry(QRect(0, 10, 235, 23))
        self.editCamBtn.setMinimumSize(QSize(235, 0))
        self.editCamBtn.setFont(font1)

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
        self.label.setText(QCoreApplication.translate("MainWindow", u"Edit Camera", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Camera IP", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Display name", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Nx1", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Ny1", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Nx2", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Ny2", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Wx1", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Wy1", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Wx2", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Wy2", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Ex1", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Ey1", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Ex2", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Ey2", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Sx1", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Sy1", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Sx2", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Sy2", None))
        self.editCamBtn.setText(QCoreApplication.translate("MainWindow", u"Edit Info", None))
    # retranslateUi

