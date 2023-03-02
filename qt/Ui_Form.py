# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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

from pyqtgraph import ImageView


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1112, 480)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(8, 8, 8, 8)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, 0, -1)
        self.cameraEditBox = QHBoxLayout()
        self.cameraEditBox.setObjectName(u"cameraEditBox")
        self.languageChooser = QComboBox(Form)
        self.languageChooser.addItem("")
        self.languageChooser.addItem("")
        self.languageChooser.setObjectName(u"languageChooser")

        self.cameraEditBox.addWidget(self.languageChooser)

        self.addCamBtn = QPushButton(Form)
        self.addCamBtn.setObjectName(u"addCamBtn")

        self.cameraEditBox.addWidget(self.addCamBtn)

        self.editCameraBtn = QPushButton(Form)
        self.editCameraBtn.setObjectName(u"editCameraBtn")

        self.cameraEditBox.addWidget(self.editCameraBtn)

        self.removeCameraBtn = QPushButton(Form)
        self.removeCameraBtn.setObjectName(u"removeCameraBtn")

        self.cameraEditBox.addWidget(self.removeCameraBtn)

        self.showDataBtn = QPushButton(Form)
        self.showDataBtn.setObjectName(u"showDataBtn")

        self.cameraEditBox.addWidget(self.showDataBtn)


        self.verticalLayout_2.addLayout(self.cameraEditBox)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")

        self.verticalLayout_2.addLayout(self.verticalLayout_3)

        self.videoSwitcher = QGroupBox(Form)
        self.videoSwitcher.setObjectName(u"videoSwitcher")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.videoSwitcher.sizePolicy().hasHeightForWidth())
        self.videoSwitcher.setSizePolicy(sizePolicy)
        self.verticalLayout_4 = QVBoxLayout(self.videoSwitcher)
        self.verticalLayout_4.setSpacing(4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 5)
        self.frameView = ImageView(self.videoSwitcher)
        self.frameView.setObjectName(u"frameView")
        sizePolicy.setHeightForWidth(self.frameView.sizePolicy().hasHeightForWidth())
        self.frameView.setSizePolicy(sizePolicy)

        self.verticalLayout_4.addWidget(self.frameView)


        self.verticalLayout_2.addWidget(self.videoSwitcher)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(7)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.mediaGBox = QGroupBox(Form)
        self.mediaGBox.setObjectName(u"mediaGBox")
        self.gridLayout_2 = QGridLayout(self.mediaGBox)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_9.setContentsMargins(-1, -1, 0, -1)
        self.comboBox = QComboBox(self.mediaGBox)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setEditable(True)

        self.horizontalLayout_9.addWidget(self.comboBox)


        self.gridLayout_2.addLayout(self.horizontalLayout_9, 0, 1, 1, 1)

        self.stopProcessBtn = QPushButton(self.mediaGBox)
        self.stopProcessBtn.setObjectName(u"stopProcessBtn")

        self.gridLayout_2.addWidget(self.stopProcessBtn, 0, 5, 1, 1)

        self.startInferenceBtn = QPushButton(self.mediaGBox)
        self.startInferenceBtn.setObjectName(u"startInferenceBtn")

        self.gridLayout_2.addWidget(self.startInferenceBtn, 0, 4, 1, 1)

        self.checkBox = QCheckBox(self.mediaGBox)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_2.addWidget(self.checkBox, 0, 3, 1, 1)


        self.horizontalLayout_2.addWidget(self.mediaGBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2.setStretch(2, 1)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(5, -1, -1, -1)
        self.sidewiseCountMatrixDisplay = QTabWidget(Form)
        self.sidewiseCountMatrixDisplay.setObjectName(u"sidewiseCountMatrixDisplay")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.sidewiseCountMatrixDisplay.sizePolicy().hasHeightForWidth())
        self.sidewiseCountMatrixDisplay.setSizePolicy(sizePolicy1)
        self.carTab = QWidget()
        self.carTab.setObjectName(u"carTab")
        self.horizontalLayout_8 = QHBoxLayout(self.carTab)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.widget_4 = QWidget(self.carTab)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setEnabled(True)
        self.gridLayout_4 = QGridLayout(self.widget_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.EEcarCount = QLCDNumber(self.widget_4)
        self.EEcarCount.setObjectName(u"EEcarCount")
        self.EEcarCount.setLineWidth(0)
        self.EEcarCount.setDigitCount(10)
        self.EEcarCount.setSegmentStyle(QLCDNumber.Flat)
        self.EEcarCount.setProperty("intValue", 0)

        self.gridLayout_4.addWidget(self.EEcarCount, 7, 4, 1, 1)

        self.SEcarCount = QLCDNumber(self.widget_4)
        self.SEcarCount.setObjectName(u"SEcarCount")
        self.SEcarCount.setLineWidth(0)
        self.SEcarCount.setDigitCount(10)
        self.SEcarCount.setSegmentStyle(QLCDNumber.Flat)
        self.SEcarCount.setProperty("intValue", 0)

        self.gridLayout_4.addWidget(self.SEcarCount, 9, 4, 1, 1)

        self.EScarCount = QLCDNumber(self.widget_4)
        self.EScarCount.setObjectName(u"EScarCount")
        self.EScarCount.setLineWidth(0)
        self.EScarCount.setDigitCount(10)
        self.EScarCount.setSegmentStyle(QLCDNumber.Flat)
        self.EScarCount.setProperty("intValue", 0)

        self.gridLayout_4.addWidget(self.EScarCount, 7, 7, 1, 1)

        self.SWcarCount = QLCDNumber(self.widget_4)
        self.SWcarCount.setObjectName(u"SWcarCount")
        self.SWcarCount.setLineWidth(0)
        self.SWcarCount.setDigitCount(10)
        self.SWcarCount.setSegmentStyle(QLCDNumber.Flat)
        self.SWcarCount.setProperty("intValue", 0)

        self.gridLayout_4.addWidget(self.SWcarCount, 9, 6, 1, 1)

        self.SScarCount = QLCDNumber(self.widget_4)
        self.SScarCount.setObjectName(u"SScarCount")
        self.SScarCount.setLineWidth(0)
        self.SScarCount.setDigitCount(10)
        self.SScarCount.setSegmentStyle(QLCDNumber.Flat)
        self.SScarCount.setProperty("intValue", 0)

        self.gridLayout_4.addWidget(self.SScarCount, 9, 7, 1, 1)

        self.NWcarCount = QLCDNumber(self.widget_4)
        self.NWcarCount.setObjectName(u"NWcarCount")
        self.NWcarCount.setLineWidth(0)
        self.NWcarCount.setDigitCount(10)
        self.NWcarCount.setSegmentStyle(QLCDNumber.Flat)
        self.NWcarCount.setProperty("intValue", 0)

        self.gridLayout_4.addWidget(self.NWcarCount, 2, 6, 1, 1)

        self.EWcarCount = QLCDNumber(self.widget_4)
        self.EWcarCount.setObjectName(u"EWcarCount")
        self.EWcarCount.setLineWidth(0)
        self.EWcarCount.setDigitCount(10)
        self.EWcarCount.setSegmentStyle(QLCDNumber.Flat)
        self.EWcarCount.setProperty("intValue", 0)

        self.gridLayout_4.addWidget(self.EWcarCount, 7, 6, 1, 1)

        self.WNcarCount = QLCDNumber(self.widget_4)
        self.WNcarCount.setObjectName(u"WNcarCount")
        self.WNcarCount.setLineWidth(0)
        self.WNcarCount.setDigitCount(10)
        self.WNcarCount.setSegmentStyle(QLCDNumber.Flat)
        self.WNcarCount.setProperty("intValue", 0)

        self.gridLayout_4.addWidget(self.WNcarCount, 8, 3, 1, 1)

        self.NEcarCount = QLCDNumber(self.widget_4)
        self.NEcarCount.setObjectName(u"NEcarCount")
        self.NEcarCount.setLineWidth(0)
        self.NEcarCount.setDigitCount(10)
        self.NEcarCount.setSegmentStyle(QLCDNumber.Flat)
        self.NEcarCount.setProperty("intValue", 0)

        self.gridLayout_4.addWidget(self.NEcarCount, 2, 4, 1, 1)

        self.SNcarCount = QLCDNumber(self.widget_4)
        self.SNcarCount.setObjectName(u"SNcarCount")
        self.SNcarCount.setLineWidth(0)
        self.SNcarCount.setDigitCount(10)
        self.SNcarCount.setSegmentStyle(QLCDNumber.Flat)
        self.SNcarCount.setProperty("intValue", 0)

        self.gridLayout_4.addWidget(self.SNcarCount, 9, 3, 1, 1)

        self.label_39 = QLabel(self.widget_4)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout_4.addWidget(self.label_39, 9, 0, 1, 1)

        self.label_42 = QLabel(self.widget_4)
        self.label_42.setObjectName(u"label_42")

        self.gridLayout_4.addWidget(self.label_42, 8, 0, 1, 1)

        self.label_53 = QLabel(self.widget_4)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_53, 1, 4, 1, 1)

        self.WScarCount = QLCDNumber(self.widget_4)
        self.WScarCount.setObjectName(u"WScarCount")
        self.WScarCount.setLineWidth(0)
        self.WScarCount.setDigitCount(10)
        self.WScarCount.setSegmentStyle(QLCDNumber.Flat)
        self.WScarCount.setProperty("intValue", 0)

        self.gridLayout_4.addWidget(self.WScarCount, 8, 7, 1, 1)

        self.label_52 = QLabel(self.widget_4)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_52, 1, 6, 1, 1)

        self.ENcarCount = QLCDNumber(self.widget_4)
        self.ENcarCount.setObjectName(u"ENcarCount")
        self.ENcarCount.setLineWidth(0)
        self.ENcarCount.setDigitCount(10)
        self.ENcarCount.setSegmentStyle(QLCDNumber.Flat)
        self.ENcarCount.setProperty("intValue", 0)

        self.gridLayout_4.addWidget(self.ENcarCount, 7, 3, 1, 1)

        self.label_48 = QLabel(self.widget_4)
        self.label_48.setObjectName(u"label_48")

        self.gridLayout_4.addWidget(self.label_48, 7, 0, 1, 1)

        self.carCount = QLCDNumber(self.widget_4)
        self.carCount.setObjectName(u"carCount")
        self.carCount.setLineWidth(0)
        self.carCount.setDigitCount(10)
        self.carCount.setSegmentStyle(QLCDNumber.Flat)
        self.carCount.setProperty("intValue", 0)

        self.gridLayout_4.addWidget(self.carCount, 2, 3, 1, 1)

        self.label_55 = QLabel(self.widget_4)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_55, 1, 7, 1, 1)

        self.NScarCount = QLCDNumber(self.widget_4)
        self.NScarCount.setObjectName(u"NScarCount")
        self.NScarCount.setLineWidth(0)
        self.NScarCount.setDigitCount(10)
        self.NScarCount.setSegmentStyle(QLCDNumber.Flat)
        self.NScarCount.setProperty("intValue", 0)

        self.gridLayout_4.addWidget(self.NScarCount, 2, 7, 1, 1)

        self.label_9 = QLabel(self.widget_4)
        self.label_9.setObjectName(u"label_9")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy2)

        self.gridLayout_4.addWidget(self.label_9, 2, 0, 1, 1)

        self.label_2 = QLabel(self.widget_4)
        self.label_2.setObjectName(u"label_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy3)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_2, 1, 3, 1, 1)

        self.WWcarCount = QLCDNumber(self.widget_4)
        self.WWcarCount.setObjectName(u"WWcarCount")
        self.WWcarCount.setLineWidth(0)
        self.WWcarCount.setDigitCount(10)
        self.WWcarCount.setSegmentStyle(QLCDNumber.Flat)
        self.WWcarCount.setProperty("intValue", 0)

        self.gridLayout_4.addWidget(self.WWcarCount, 8, 6, 1, 1)

        self.WEcarCount = QLCDNumber(self.widget_4)
        self.WEcarCount.setObjectName(u"WEcarCount")
        self.WEcarCount.setLineWidth(0)
        self.WEcarCount.setDigitCount(10)
        self.WEcarCount.setSegmentStyle(QLCDNumber.Flat)
        self.WEcarCount.setProperty("intValue", 0)

        self.gridLayout_4.addWidget(self.WEcarCount, 8, 4, 1, 1)


        self.horizontalLayout_8.addWidget(self.widget_4)

        self.sidewiseCountMatrixDisplay.addTab(self.carTab, "")
        self.busTab = QWidget()
        self.busTab.setObjectName(u"busTab")
        self.gridLayout_7 = QGridLayout(self.busTab)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.widget_5 = QWidget(self.busTab)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setEnabled(True)
        self.gridLayout_5 = QGridLayout(self.widget_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_30 = QLabel(self.widget_5)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_5.addWidget(self.label_30, 8, 0, 1, 1)

        self.WNbusCount = QLCDNumber(self.widget_5)
        self.WNbusCount.setObjectName(u"WNbusCount")
        self.WNbusCount.setLineWidth(0)
        self.WNbusCount.setDigitCount(10)
        self.WNbusCount.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_5.addWidget(self.WNbusCount, 8, 1, 1, 1)

        self.WWbusCount = QLCDNumber(self.widget_5)
        self.WWbusCount.setObjectName(u"WWbusCount")
        self.WWbusCount.setLineWidth(0)
        self.WWbusCount.setDigitCount(10)
        self.WWbusCount.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_5.addWidget(self.WWbusCount, 8, 4, 1, 1)

        self.WSbusCount = QLCDNumber(self.widget_5)
        self.WSbusCount.setObjectName(u"WSbusCount")
        self.WSbusCount.setLineWidth(0)
        self.WSbusCount.setDigitCount(10)
        self.WSbusCount.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_5.addWidget(self.WSbusCount, 8, 5, 1, 1)

        self.label_31 = QLabel(self.widget_5)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_5.addWidget(self.label_31, 9, 0, 1, 1)

        self.SEbusCount = QLCDNumber(self.widget_5)
        self.SEbusCount.setObjectName(u"SEbusCount")
        self.SEbusCount.setLineWidth(0)
        self.SEbusCount.setDigitCount(10)
        self.SEbusCount.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_5.addWidget(self.SEbusCount, 9, 3, 1, 1)

        self.WEbusCount = QLCDNumber(self.widget_5)
        self.WEbusCount.setObjectName(u"WEbusCount")
        self.WEbusCount.setLineWidth(0)
        self.WEbusCount.setDigitCount(10)
        self.WEbusCount.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_5.addWidget(self.WEbusCount, 8, 3, 1, 1)

        self.ESbusCount = QLCDNumber(self.widget_5)
        self.ESbusCount.setObjectName(u"ESbusCount")
        self.ESbusCount.setLineWidth(0)
        self.ESbusCount.setDigitCount(10)
        self.ESbusCount.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_5.addWidget(self.ESbusCount, 7, 5, 1, 1)

        self.SNbusCount = QLCDNumber(self.widget_5)
        self.SNbusCount.setObjectName(u"SNbusCount")
        self.SNbusCount.setLineWidth(0)
        self.SNbusCount.setDigitCount(10)
        self.SNbusCount.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_5.addWidget(self.SNbusCount, 9, 1, 1, 1)

        self.SWbusCount = QLCDNumber(self.widget_5)
        self.SWbusCount.setObjectName(u"SWbusCount")
        self.SWbusCount.setLineWidth(0)
        self.SWbusCount.setDigitCount(10)
        self.SWbusCount.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_5.addWidget(self.SWbusCount, 9, 4, 1, 1)

        self.SSbusCount = QLCDNumber(self.widget_5)
        self.SSbusCount.setObjectName(u"SSbusCount")
        self.SSbusCount.setLineWidth(0)
        self.SSbusCount.setDigitCount(10)
        self.SSbusCount.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_5.addWidget(self.SSbusCount, 9, 5, 1, 1)

        self.NSbusCount = QLCDNumber(self.widget_5)
        self.NSbusCount.setObjectName(u"NSbusCount")
        self.NSbusCount.setLineWidth(0)
        self.NSbusCount.setDigitCount(10)
        self.NSbusCount.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_5.addWidget(self.NSbusCount, 2, 5, 1, 1)

        self.label_23 = QLabel(self.widget_5)
        self.label_23.setObjectName(u"label_23")
        sizePolicy3.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy3)
        self.label_23.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_23, 1, 1, 1, 1)

        self.NNbusCount = QLCDNumber(self.widget_5)
        self.NNbusCount.setObjectName(u"NNbusCount")
        self.NNbusCount.setFrameShadow(QFrame.Raised)
        self.NNbusCount.setLineWidth(0)
        self.NNbusCount.setDigitCount(10)
        self.NNbusCount.setSegmentStyle(QLCDNumber.Flat)
        self.NNbusCount.setProperty("intValue", 0)

        self.gridLayout_5.addWidget(self.NNbusCount, 2, 1, 1, 1)

        self.NEbusCount = QLCDNumber(self.widget_5)
        self.NEbusCount.setObjectName(u"NEbusCount")
        self.NEbusCount.setFrameShadow(QFrame.Raised)
        self.NEbusCount.setLineWidth(0)
        self.NEbusCount.setDigitCount(10)
        self.NEbusCount.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_5.addWidget(self.NEbusCount, 2, 3, 1, 1)

        self.label_32 = QLabel(self.widget_5)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_5.addWidget(self.label_32, 7, 0, 1, 1)

        self.ENbusCount = QLCDNumber(self.widget_5)
        self.ENbusCount.setObjectName(u"ENbusCount")
        self.ENbusCount.setLineWidth(0)
        self.ENbusCount.setDigitCount(10)
        self.ENbusCount.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_5.addWidget(self.ENbusCount, 7, 1, 1, 1)

        self.EEbusCount = QLCDNumber(self.widget_5)
        self.EEbusCount.setObjectName(u"EEbusCount")
        self.EEbusCount.setLineWidth(0)
        self.EEbusCount.setDigitCount(10)
        self.EEbusCount.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_5.addWidget(self.EEbusCount, 7, 3, 1, 1)

        self.label_4 = QLabel(self.widget_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_4, 1, 5, 1, 1)

        self.EWbusCount = QLCDNumber(self.widget_5)
        self.EWbusCount.setObjectName(u"EWbusCount")
        self.EWbusCount.setLineWidth(0)
        self.EWbusCount.setDigitCount(10)
        self.EWbusCount.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_5.addWidget(self.EWbusCount, 7, 4, 1, 1)

        self.label_24 = QLabel(self.widget_5)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_24, 1, 3, 1, 1)

        self.label_25 = QLabel(self.widget_5)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_25, 1, 4, 1, 1)

        self.label_11 = QLabel(self.widget_5)
        self.label_11.setObjectName(u"label_11")
        sizePolicy2.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.label_11, 2, 0, 1, 1)

        self.NWbusCount = QLCDNumber(self.widget_5)
        self.NWbusCount.setObjectName(u"NWbusCount")
        self.NWbusCount.setLineWidth(0)
        self.NWbusCount.setDigitCount(10)
        self.NWbusCount.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_5.addWidget(self.NWbusCount, 2, 4, 1, 1)


        self.gridLayout_7.addWidget(self.widget_5, 0, 0, 1, 1)

        self.sidewiseCountMatrixDisplay.addTab(self.busTab, "")
        self.bicycleTab = QWidget()
        self.bicycleTab.setObjectName(u"bicycleTab")
        self.horizontalLayout_3 = QHBoxLayout(self.bicycleTab)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.widget_2 = QWidget(self.bicycleTab)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setEnabled(True)
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_28 = QLabel(self.widget_2)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout.addWidget(self.label_28, 8, 0, 1, 1)

        self.WNbicycleCount = QLCDNumber(self.widget_2)
        self.WNbicycleCount.setObjectName(u"WNbicycleCount")
        self.WNbicycleCount.setLineWidth(0)
        self.WNbicycleCount.setDigitCount(10)
        self.WNbicycleCount.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.WNbicycleCount, 8, 1, 1, 1)

        self.WWbicycleCount = QLCDNumber(self.widget_2)
        self.WWbicycleCount.setObjectName(u"WWbicycleCount")
        self.WWbicycleCount.setLineWidth(0)
        self.WWbicycleCount.setDigitCount(10)
        self.WWbicycleCount.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.WWbicycleCount, 8, 4, 1, 1)

        self.WSbicycleCount = QLCDNumber(self.widget_2)
        self.WSbicycleCount.setObjectName(u"WSbicycleCount")
        self.WSbicycleCount.setLineWidth(0)
        self.WSbicycleCount.setDigitCount(10)
        self.WSbicycleCount.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.WSbicycleCount, 8, 5, 1, 1)

        self.label_29 = QLabel(self.widget_2)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout.addWidget(self.label_29, 9, 0, 1, 1)

        self.SEbicycleCount = QLCDNumber(self.widget_2)
        self.SEbicycleCount.setObjectName(u"SEbicycleCount")
        self.SEbicycleCount.setLineWidth(0)
        self.SEbicycleCount.setDigitCount(10)
        self.SEbicycleCount.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.SEbicycleCount, 9, 3, 1, 1)

        self.WEbicycleCount = QLCDNumber(self.widget_2)
        self.WEbicycleCount.setObjectName(u"WEbicycleCount")
        self.WEbicycleCount.setLineWidth(0)
        self.WEbicycleCount.setDigitCount(10)
        self.WEbicycleCount.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.WEbicycleCount, 8, 3, 1, 1)

        self.ESbicycleCount = QLCDNumber(self.widget_2)
        self.ESbicycleCount.setObjectName(u"ESbicycleCount")
        self.ESbicycleCount.setLineWidth(0)
        self.ESbicycleCount.setDigitCount(10)
        self.ESbicycleCount.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.ESbicycleCount, 7, 5, 1, 1)

        self.SNbicycleCount = QLCDNumber(self.widget_2)
        self.SNbicycleCount.setObjectName(u"SNbicycleCount")
        self.SNbicycleCount.setLineWidth(0)
        self.SNbicycleCount.setDigitCount(10)
        self.SNbicycleCount.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.SNbicycleCount, 9, 1, 1, 1)

        self.SWbicycleCount = QLCDNumber(self.widget_2)
        self.SWbicycleCount.setObjectName(u"SWbicycleCount")
        self.SWbicycleCount.setLineWidth(0)
        self.SWbicycleCount.setDigitCount(10)
        self.SWbicycleCount.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.SWbicycleCount, 9, 4, 1, 1)

        self.SSbicycleCount = QLCDNumber(self.widget_2)
        self.SSbicycleCount.setObjectName(u"SSbicycleCount")
        self.SSbicycleCount.setLineWidth(0)
        self.SSbicycleCount.setDigitCount(10)
        self.SSbicycleCount.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.SSbicycleCount, 9, 5, 1, 1)

        self.NSbicycleCount = QLCDNumber(self.widget_2)
        self.NSbicycleCount.setObjectName(u"NSbicycleCount")
        self.NSbicycleCount.setLineWidth(0)
        self.NSbicycleCount.setDigitCount(10)
        self.NSbicycleCount.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.NSbicycleCount, 2, 5, 1, 1)

        self.NNbicycleCount = QLCDNumber(self.widget_2)
        self.NNbicycleCount.setObjectName(u"NNbicycleCount")
        self.NNbicycleCount.setFrameShadow(QFrame.Raised)
        self.NNbicycleCount.setLineWidth(0)
        self.NNbicycleCount.setDigitCount(10)
        self.NNbicycleCount.setSegmentStyle(QLCDNumber.Flat)
        self.NNbicycleCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.NNbicycleCount, 2, 1, 1, 1)

        self.NEbicycleCount = QLCDNumber(self.widget_2)
        self.NEbicycleCount.setObjectName(u"NEbicycleCount")
        self.NEbicycleCount.setFrameShadow(QFrame.Raised)
        self.NEbicycleCount.setLineWidth(0)
        self.NEbicycleCount.setDigitCount(10)
        self.NEbicycleCount.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.NEbicycleCount, 2, 3, 1, 1)

        self.label_27 = QLabel(self.widget_2)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout.addWidget(self.label_27, 7, 0, 1, 1)

        self.ENbicycleCount = QLCDNumber(self.widget_2)
        self.ENbicycleCount.setObjectName(u"ENbicycleCount")
        self.ENbicycleCount.setLineWidth(0)
        self.ENbicycleCount.setDigitCount(10)
        self.ENbicycleCount.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.ENbicycleCount, 7, 1, 1, 1)

        self.EEbicycleCount = QLCDNumber(self.widget_2)
        self.EEbicycleCount.setObjectName(u"EEbicycleCount")
        self.EEbicycleCount.setLineWidth(0)
        self.EEbicycleCount.setDigitCount(10)
        self.EEbicycleCount.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.EEbicycleCount, 7, 3, 1, 1)

        self.EWbicycleCount = QLCDNumber(self.widget_2)
        self.EWbicycleCount.setObjectName(u"EWbicycleCount")
        self.EWbicycleCount.setLineWidth(0)
        self.EWbicycleCount.setDigitCount(10)
        self.EWbicycleCount.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.EWbicycleCount, 7, 4, 1, 1)

        self.label_8 = QLabel(self.widget_2)
        self.label_8.setObjectName(u"label_8")
        sizePolicy2.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.label_8, 2, 0, 1, 1)

        self.NWbicycleCount = QLCDNumber(self.widget_2)
        self.NWbicycleCount.setObjectName(u"NWbicycleCount")
        self.NWbicycleCount.setLineWidth(0)
        self.NWbicycleCount.setDigitCount(10)
        self.NWbicycleCount.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.NWbicycleCount, 2, 4, 1, 1)

        self.label_21 = QLabel(self.widget_2)
        self.label_21.setObjectName(u"label_21")
        sizePolicy3.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy3)
        self.label_21.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_21, 0, 1, 1, 1)

        self.label_22 = QLabel(self.widget_2)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_22, 0, 3, 1, 1)

        self.label_20 = QLabel(self.widget_2)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_20, 0, 4, 1, 1)

        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 0, 5, 1, 1)


        self.horizontalLayout_3.addWidget(self.widget_2)

        self.sidewiseCountMatrixDisplay.addTab(self.bicycleTab, "")
        self.mcycleTab = QWidget()
        self.mcycleTab.setObjectName(u"mcycleTab")
        self.gridLayout_8 = QGridLayout(self.mcycleTab)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.widget_6 = QWidget(self.mcycleTab)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setEnabled(True)
        self.gridLayout_6 = QGridLayout(self.widget_6)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_33 = QLabel(self.widget_6)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout_6.addWidget(self.label_33, 8, 0, 1, 1)

        self.WNmcycleCount = QLCDNumber(self.widget_6)
        self.WNmcycleCount.setObjectName(u"WNmcycleCount")
        self.WNmcycleCount.setLineWidth(0)
        self.WNmcycleCount.setDigitCount(10)
        self.WNmcycleCount.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_6.addWidget(self.WNmcycleCount, 8, 1, 1, 1)

        self.WWmcycleCount = QLCDNumber(self.widget_6)
        self.WWmcycleCount.setObjectName(u"WWmcycleCount")
        self.WWmcycleCount.setLineWidth(0)
        self.WWmcycleCount.setDigitCount(10)
        self.WWmcycleCount.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_6.addWidget(self.WWmcycleCount, 8, 4, 1, 1)

        self.WSmcycleCount = QLCDNumber(self.widget_6)
        self.WSmcycleCount.setObjectName(u"WSmcycleCount")
        self.WSmcycleCount.setLineWidth(0)
        self.WSmcycleCount.setDigitCount(10)
        self.WSmcycleCount.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_6.addWidget(self.WSmcycleCount, 8, 5, 1, 1)

        self.label_34 = QLabel(self.widget_6)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout_6.addWidget(self.label_34, 9, 0, 1, 1)

        self.SEmcycleCount = QLCDNumber(self.widget_6)
        self.SEmcycleCount.setObjectName(u"SEmcycleCount")
        self.SEmcycleCount.setLineWidth(0)
        self.SEmcycleCount.setDigitCount(10)
        self.SEmcycleCount.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_6.addWidget(self.SEmcycleCount, 9, 3, 1, 1)

        self.WEmcycleCount = QLCDNumber(self.widget_6)
        self.WEmcycleCount.setObjectName(u"WEmcycleCount")
        self.WEmcycleCount.setLineWidth(0)
        self.WEmcycleCount.setDigitCount(10)
        self.WEmcycleCount.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_6.addWidget(self.WEmcycleCount, 8, 3, 1, 1)

        self.ESmcycleCount = QLCDNumber(self.widget_6)
        self.ESmcycleCount.setObjectName(u"ESmcycleCount")
        self.ESmcycleCount.setLineWidth(0)
        self.ESmcycleCount.setDigitCount(10)
        self.ESmcycleCount.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_6.addWidget(self.ESmcycleCount, 7, 5, 1, 1)

        self.SNmcycleCount = QLCDNumber(self.widget_6)
        self.SNmcycleCount.setObjectName(u"SNmcycleCount")
        self.SNmcycleCount.setLineWidth(0)
        self.SNmcycleCount.setDigitCount(10)
        self.SNmcycleCount.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_6.addWidget(self.SNmcycleCount, 9, 1, 1, 1)

        self.SWmcycleCount = QLCDNumber(self.widget_6)
        self.SWmcycleCount.setObjectName(u"SWmcycleCount")
        self.SWmcycleCount.setLineWidth(0)
        self.SWmcycleCount.setDigitCount(10)
        self.SWmcycleCount.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_6.addWidget(self.SWmcycleCount, 9, 4, 1, 1)

        self.SSmcycleCount = QLCDNumber(self.widget_6)
        self.SSmcycleCount.setObjectName(u"SSmcycleCount")
        self.SSmcycleCount.setLineWidth(0)
        self.SSmcycleCount.setDigitCount(10)
        self.SSmcycleCount.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_6.addWidget(self.SSmcycleCount, 9, 5, 1, 1)

        self.NSmcycleCount = QLCDNumber(self.widget_6)
        self.NSmcycleCount.setObjectName(u"NSmcycleCount")
        self.NSmcycleCount.setLineWidth(0)
        self.NSmcycleCount.setDigitCount(10)
        self.NSmcycleCount.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_6.addWidget(self.NSmcycleCount, 2, 5, 1, 1)

        self.NNmcycleCount = QLCDNumber(self.widget_6)
        self.NNmcycleCount.setObjectName(u"NNmcycleCount")
        self.NNmcycleCount.setFrameShadow(QFrame.Raised)
        self.NNmcycleCount.setLineWidth(0)
        self.NNmcycleCount.setDigitCount(10)
        self.NNmcycleCount.setSegmentStyle(QLCDNumber.Flat)
        self.NNmcycleCount.setProperty("intValue", 0)

        self.gridLayout_6.addWidget(self.NNmcycleCount, 2, 1, 1, 1)

        self.NEmcycleCount = QLCDNumber(self.widget_6)
        self.NEmcycleCount.setObjectName(u"NEmcycleCount")
        self.NEmcycleCount.setFrameShadow(QFrame.Raised)
        self.NEmcycleCount.setLineWidth(0)
        self.NEmcycleCount.setDigitCount(10)
        self.NEmcycleCount.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_6.addWidget(self.NEmcycleCount, 2, 3, 1, 1)

        self.label_35 = QLabel(self.widget_6)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_6.addWidget(self.label_35, 7, 0, 1, 1)

        self.ENmcycleCount = QLCDNumber(self.widget_6)
        self.ENmcycleCount.setObjectName(u"ENmcycleCount")
        self.ENmcycleCount.setLineWidth(0)
        self.ENmcycleCount.setDigitCount(10)
        self.ENmcycleCount.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_6.addWidget(self.ENmcycleCount, 7, 1, 1, 1)

        self.EEmcycleCount = QLCDNumber(self.widget_6)
        self.EEmcycleCount.setObjectName(u"EEmcycleCount")
        self.EEmcycleCount.setLineWidth(0)
        self.EEmcycleCount.setDigitCount(10)
        self.EEmcycleCount.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_6.addWidget(self.EEmcycleCount, 7, 3, 1, 1)

        self.EWmcycleCount = QLCDNumber(self.widget_6)
        self.EWmcycleCount.setObjectName(u"EWmcycleCount")
        self.EWmcycleCount.setLineWidth(0)
        self.EWmcycleCount.setDigitCount(10)
        self.EWmcycleCount.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_6.addWidget(self.EWmcycleCount, 7, 4, 1, 1)

        self.label_12 = QLabel(self.widget_6)
        self.label_12.setObjectName(u"label_12")
        sizePolicy2.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy2)

        self.gridLayout_6.addWidget(self.label_12, 2, 0, 1, 1)

        self.NWmcycleCount = QLCDNumber(self.widget_6)
        self.NWmcycleCount.setObjectName(u"NWmcycleCount")
        self.NWmcycleCount.setLineWidth(0)
        self.NWmcycleCount.setDigitCount(10)
        self.NWmcycleCount.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_6.addWidget(self.NWmcycleCount, 2, 4, 1, 1)

        self.label_26 = QLabel(self.widget_6)
        self.label_26.setObjectName(u"label_26")
        sizePolicy3.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy3)
        self.label_26.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.label_26, 0, 1, 1, 1)

        self.label_36 = QLabel(self.widget_6)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.label_36, 0, 3, 1, 1)

        self.label_37 = QLabel(self.widget_6)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.label_37, 0, 4, 1, 1)

        self.label_6 = QLabel(self.widget_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.label_6, 0, 5, 1, 1)


        self.gridLayout_8.addWidget(self.widget_6, 0, 0, 1, 1)

        self.sidewiseCountMatrixDisplay.addTab(self.mcycleTab, "")
        self.truckTab = QWidget()
        self.truckTab.setObjectName(u"truckTab")
        self.verticalLayout_5 = QVBoxLayout(self.truckTab)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget_3 = QWidget(self.truckTab)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setEnabled(True)
        self.gridLayout_3 = QGridLayout(self.widget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.truckCount = QLCDNumber(self.widget_3)
        self.truckCount.setObjectName(u"truckCount")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.truckCount.sizePolicy().hasHeightForWidth())
        self.truckCount.setSizePolicy(sizePolicy4)
        self.truckCount.setLineWidth(0)
        self.truckCount.setDigitCount(10)
        self.truckCount.setSegmentStyle(QLCDNumber.Flat)
        self.truckCount.setProperty("intValue", 0)

        self.gridLayout_3.addWidget(self.truckCount, 2, 2, 1, 1)

        self.EWtruckCount = QLCDNumber(self.widget_3)
        self.EWtruckCount.setObjectName(u"EWtruckCount")
        self.EWtruckCount.setLineWidth(0)
        self.EWtruckCount.setDigitCount(10)
        self.EWtruckCount.setSegmentStyle(QLCDNumber.Flat)
        self.EWtruckCount.setProperty("intValue", 0)

        self.gridLayout_3.addWidget(self.EWtruckCount, 3, 5, 1, 1)

        self.SNtruckCount = QLCDNumber(self.widget_3)
        self.SNtruckCount.setObjectName(u"SNtruckCount")
        self.SNtruckCount.setLineWidth(0)
        self.SNtruckCount.setDigitCount(10)
        self.SNtruckCount.setSegmentStyle(QLCDNumber.Flat)
        self.SNtruckCount.setProperty("intValue", 0)

        self.gridLayout_3.addWidget(self.SNtruckCount, 6, 2, 1, 1)

        self.WNtruckCount = QLCDNumber(self.widget_3)
        self.WNtruckCount.setObjectName(u"WNtruckCount")
        self.WNtruckCount.setLineWidth(0)
        self.WNtruckCount.setDigitCount(10)
        self.WNtruckCount.setSegmentStyle(QLCDNumber.Flat)
        self.WNtruckCount.setProperty("intValue", 0)

        self.gridLayout_3.addWidget(self.WNtruckCount, 4, 2, 1, 1)

        self.NStruckCount = QLCDNumber(self.widget_3)
        self.NStruckCount.setObjectName(u"NStruckCount")
        self.NStruckCount.setLineWidth(0)
        self.NStruckCount.setDigitCount(10)
        self.NStruckCount.setSegmentStyle(QLCDNumber.Flat)
        self.NStruckCount.setProperty("intValue", 0)

        self.gridLayout_3.addWidget(self.NStruckCount, 2, 7, 1, 1)

        self.NWtruckCount = QLCDNumber(self.widget_3)
        self.NWtruckCount.setObjectName(u"NWtruckCount")
        self.NWtruckCount.setLineWidth(0)
        self.NWtruckCount.setDigitCount(10)
        self.NWtruckCount.setSegmentStyle(QLCDNumber.Flat)
        self.NWtruckCount.setProperty("intValue", 0)

        self.gridLayout_3.addWidget(self.NWtruckCount, 2, 5, 1, 1)

        self.NEtruckCount = QLCDNumber(self.widget_3)
        self.NEtruckCount.setObjectName(u"NEtruckCount")
        self.NEtruckCount.setLineWidth(0)
        self.NEtruckCount.setDigitCount(10)
        self.NEtruckCount.setSegmentStyle(QLCDNumber.Flat)
        self.NEtruckCount.setProperty("intValue", 0)

        self.gridLayout_3.addWidget(self.NEtruckCount, 2, 3, 1, 1)

        self.ENtruckCount = QLCDNumber(self.widget_3)
        self.ENtruckCount.setObjectName(u"ENtruckCount")
        self.ENtruckCount.setLineWidth(0)
        self.ENtruckCount.setDigitCount(10)
        self.ENtruckCount.setSegmentStyle(QLCDNumber.Flat)
        self.ENtruckCount.setProperty("intValue", 0)

        self.gridLayout_3.addWidget(self.ENtruckCount, 3, 2, 1, 1)

        self.label_49 = QLabel(self.widget_3)
        self.label_49.setObjectName(u"label_49")

        self.gridLayout_3.addWidget(self.label_49, 3, 0, 1, 1)

        self.label_38 = QLabel(self.widget_3)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_38, 1, 5, 1, 1)

        self.label_43 = QLabel(self.widget_3)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_43, 1, 7, 1, 1)

        self.label_10 = QLabel(self.widget_3)
        self.label_10.setObjectName(u"label_10")
        sizePolicy2.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.label_10, 2, 0, 1, 1)

        self.SStruckCount = QLCDNumber(self.widget_3)
        self.SStruckCount.setObjectName(u"SStruckCount")
        self.SStruckCount.setLineWidth(0)
        self.SStruckCount.setDigitCount(10)
        self.SStruckCount.setSegmentStyle(QLCDNumber.Flat)
        self.SStruckCount.setProperty("intValue", 0)

        self.gridLayout_3.addWidget(self.SStruckCount, 6, 7, 1, 1)

        self.label_40 = QLabel(self.widget_3)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_40, 1, 3, 1, 1)

        self.label_46 = QLabel(self.widget_3)
        self.label_46.setObjectName(u"label_46")

        self.gridLayout_3.addWidget(self.label_46, 4, 0, 1, 1)

        self.label_47 = QLabel(self.widget_3)
        self.label_47.setObjectName(u"label_47")

        self.gridLayout_3.addWidget(self.label_47, 6, 0, 1, 1)

        self.EEtruckCount = QLCDNumber(self.widget_3)
        self.EEtruckCount.setObjectName(u"EEtruckCount")
        self.EEtruckCount.setLineWidth(0)
        self.EEtruckCount.setDigitCount(10)
        self.EEtruckCount.setSegmentStyle(QLCDNumber.Flat)
        self.EEtruckCount.setProperty("intValue", 0)

        self.gridLayout_3.addWidget(self.EEtruckCount, 3, 3, 1, 1)

        self.WWtruckCount = QLCDNumber(self.widget_3)
        self.WWtruckCount.setObjectName(u"WWtruckCount")
        self.WWtruckCount.setLineWidth(0)
        self.WWtruckCount.setDigitCount(10)
        self.WWtruckCount.setSegmentStyle(QLCDNumber.Flat)
        self.WWtruckCount.setProperty("intValue", 0)

        self.gridLayout_3.addWidget(self.WWtruckCount, 4, 5, 1, 1)

        self.WEtruckCount = QLCDNumber(self.widget_3)
        self.WEtruckCount.setObjectName(u"WEtruckCount")
        self.WEtruckCount.setLineWidth(0)
        self.WEtruckCount.setDigitCount(10)
        self.WEtruckCount.setSegmentStyle(QLCDNumber.Flat)
        self.WEtruckCount.setProperty("intValue", 0)

        self.gridLayout_3.addWidget(self.WEtruckCount, 4, 3, 1, 1)

        self.SEtruckCount = QLCDNumber(self.widget_3)
        self.SEtruckCount.setObjectName(u"SEtruckCount")
        self.SEtruckCount.setLineWidth(0)
        self.SEtruckCount.setDigitCount(10)
        self.SEtruckCount.setSegmentStyle(QLCDNumber.Flat)
        self.SEtruckCount.setProperty("intValue", 0)

        self.gridLayout_3.addWidget(self.SEtruckCount, 6, 3, 1, 1)

        self.EStruckCount = QLCDNumber(self.widget_3)
        self.EStruckCount.setObjectName(u"EStruckCount")
        self.EStruckCount.setLineWidth(0)
        self.EStruckCount.setDigitCount(10)
        self.EStruckCount.setSegmentStyle(QLCDNumber.Flat)
        self.EStruckCount.setProperty("intValue", 0)

        self.gridLayout_3.addWidget(self.EStruckCount, 3, 7, 1, 1)

        self.label_5 = QLabel(self.widget_3)
        self.label_5.setObjectName(u"label_5")
        sizePolicy3.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy3)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_5, 1, 2, 1, 1)

        self.SWtruckCount = QLCDNumber(self.widget_3)
        self.SWtruckCount.setObjectName(u"SWtruckCount")
        self.SWtruckCount.setLineWidth(0)
        self.SWtruckCount.setDigitCount(10)
        self.SWtruckCount.setSegmentStyle(QLCDNumber.Flat)
        self.SWtruckCount.setProperty("intValue", 0)

        self.gridLayout_3.addWidget(self.SWtruckCount, 6, 5, 1, 1)

        self.WStruckCount = QLCDNumber(self.widget_3)
        self.WStruckCount.setObjectName(u"WStruckCount")
        self.WStruckCount.setLineWidth(0)
        self.WStruckCount.setDigitCount(10)
        self.WStruckCount.setSegmentStyle(QLCDNumber.Flat)
        self.WStruckCount.setProperty("intValue", 0)

        self.gridLayout_3.addWidget(self.WStruckCount, 4, 7, 1, 1)


        self.verticalLayout_5.addWidget(self.widget_3)

        self.sidewiseCountMatrixDisplay.addTab(self.truckTab, "")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.sidewiseCountMatrixDisplay)


        self.horizontalLayout.addLayout(self.formLayout)


        self.retranslateUi(Form)

        self.languageChooser.setCurrentIndex(0)
        self.comboBox.setCurrentIndex(-1)
        self.sidewiseCountMatrixDisplay.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Traffic Vehicle Counter", None))
        self.languageChooser.setItemText(0, QCoreApplication.translate("Form", u"English", None))
        self.languageChooser.setItemText(1, QCoreApplication.translate("Form", u"O'zbek", None))

        self.addCamBtn.setText(QCoreApplication.translate("Form", self.text_translator.add_camera_btn, None))
        self.editCameraBtn.setText(QCoreApplication.translate("Form", self.text_translator.edit_camera_btn, None))
        self.removeCameraBtn.setText(QCoreApplication.translate("Form", self.text_translator.remove_camera_btn, None))
        self.showDataBtn.setText(QCoreApplication.translate("Form", self.text_translator.show_data_btn, None))
        self.videoSwitcher.setTitle("")
        self.mediaGBox.setTitle("")
        self.comboBox.setCurrentText("")
        self.stopProcessBtn.setText(QCoreApplication.translate("Form", self.text_translator.stop_process_btn, None))
        self.startInferenceBtn.setText(QCoreApplication.translate("Form", self.text_translator.start_inference_btn, None))
        self.checkBox.setText(QCoreApplication.translate("Form", self.text_translator.use_video_checkbox, None))
        self.label_39.setText(QCoreApplication.translate("Form", self.text_translator.d_in, None))
        self.label_42.setText(QCoreApplication.translate("Form", self.text_translator.c_in, None))
        self.label_53.setText(QCoreApplication.translate("Form", self.text_translator.b_out, None))
        self.label_52.setText(QCoreApplication.translate("Form", self.text_translator.c_out, None))
        self.label_48.setText(QCoreApplication.translate("Form", self.text_translator.b_in, None))
        self.label_55.setText(QCoreApplication.translate("Form", self.text_translator.d_out, None))
        self.label_9.setText(QCoreApplication.translate("Form", self.text_translator.a_in, None))
        self.label_2.setText(QCoreApplication.translate("Form", self.text_translator.a_out, None))
        self.sidewiseCountMatrixDisplay.setTabText(self.sidewiseCountMatrixDisplay.indexOf(self.carTab), QCoreApplication.translate("Form", self.text_translator.cars, None))
        self.label_30.setText(QCoreApplication.translate("Form", self.text_translator.c_in, None))
        self.label_31.setText(QCoreApplication.translate("Form", self.text_translator.d_in, None))
        self.label_23.setText(QCoreApplication.translate("Form", self.text_translator.a_out, None))
        self.label_32.setText(QCoreApplication.translate("Form", self.text_translator.b_in, None))
        self.label_4.setText(QCoreApplication.translate("Form", self.text_translator.d_out, None))
        self.label_24.setText(QCoreApplication.translate("Form", self.text_translator.b_out, None))
        self.label_25.setText(QCoreApplication.translate("Form", self.text_translator.c_out, None))
        self.label_11.setText(QCoreApplication.translate("Form", self.text_translator.a_in, None))
        self.sidewiseCountMatrixDisplay.setTabText(self.sidewiseCountMatrixDisplay.indexOf(self.busTab), QCoreApplication.translate("Form", self.text_translator.buses, None))
        self.label_28.setText(QCoreApplication.translate("Form", self.text_translator.c_in, None))
        self.label_29.setText(QCoreApplication.translate("Form", self.text_translator.d_in, None))
        self.label_27.setText(QCoreApplication.translate("Form", self.text_translator.b_in, None))
        self.label_8.setText(QCoreApplication.translate("Form", self.text_translator.a_in, None))
        self.label_21.setText(QCoreApplication.translate("Form", self.text_translator.a_out, None))
        self.label_22.setText(QCoreApplication.translate("Form", self.text_translator.b_out, None))
        self.label_20.setText(QCoreApplication.translate("Form", self.text_translator.c_out, None))
        self.label_3.setText(QCoreApplication.translate("Form", self.text_translator.d_out, None))
        self.sidewiseCountMatrixDisplay.setTabText(self.sidewiseCountMatrixDisplay.indexOf(self.bicycleTab), QCoreApplication.translate("Form", self.text_translator.bicycles, None))
        self.label_33.setText(QCoreApplication.translate("Form", self.text_translator.c_in, None))
        self.label_34.setText(QCoreApplication.translate("Form", self.text_translator.d_in, None))
        self.label_35.setText(QCoreApplication.translate("Form", self.text_translator.b_in, None))
        self.label_12.setText(QCoreApplication.translate("Form", self.text_translator.a_in, None))
        self.label_26.setText(QCoreApplication.translate("Form", self.text_translator.a_out, None))
        self.label_36.setText(QCoreApplication.translate("Form", self.text_translator.b_out, None))
        self.label_37.setText(QCoreApplication.translate("Form", self.text_translator.c_out, None))
        self.label_6.setText(QCoreApplication.translate("Form", self.text_translator.d_out, None))
        self.sidewiseCountMatrixDisplay.setTabText(self.sidewiseCountMatrixDisplay.indexOf(self.mcycleTab), QCoreApplication.translate("Form", self.text_translator.motorcycles, None))
        self.label_49.setText(QCoreApplication.translate("Form", self.text_translator.b_in, None))
        self.label_38.setText(QCoreApplication.translate("Form", self.text_translator.c_out, None))
        self.label_43.setText(QCoreApplication.translate("Form", self.text_translator.d_out, None))
        self.label_10.setText(QCoreApplication.translate("Form", self.text_translator.a_in, None))
        self.label_40.setText(QCoreApplication.translate("Form", self.text_translator.b_out, None))
        self.label_46.setText(QCoreApplication.translate("Form", self.text_translator.c_in, None))
        self.label_47.setText(QCoreApplication.translate("Form", self.text_translator.d_in, None))
        self.label_5.setText(QCoreApplication.translate("Form", self.text_translator.a_out, None))
        self.sidewiseCountMatrixDisplay.setTabText(self.sidewiseCountMatrixDisplay.indexOf(self.truckTab), QCoreApplication.translate("Form", self.text_translator.trucks, None))
    # retranslateUi

