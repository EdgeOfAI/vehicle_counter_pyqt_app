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
        Form.resize(1107, 645)
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
        self.label_5 = QLabel(self.mediaGBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")

        self.gridLayout_2.addLayout(self.horizontalLayout_10, 2, 2, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_9.setContentsMargins(-1, -1, 0, -1)
        self.comboBox = QComboBox(self.mediaGBox)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setEditable(True)

        self.horizontalLayout_9.addWidget(self.comboBox)


        self.gridLayout_2.addLayout(self.horizontalLayout_9, 0, 2, 1, 1)

        self.startInferenceBtn = QPushButton(self.mediaGBox)
        self.startInferenceBtn.setObjectName(u"startInferenceBtn")

        self.gridLayout_2.addWidget(self.startInferenceBtn, 3, 0, 1, 1)

        self.refreshCamerasBtn = QPushButton(self.mediaGBox)
        self.refreshCamerasBtn.setObjectName(u"refreshCamerasBtn")

        self.gridLayout_2.addWidget(self.refreshCamerasBtn, 3, 2, 1, 1)


        self.horizontalLayout_2.addWidget(self.mediaGBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.stopProcessBtn = QPushButton(Form)
        self.stopProcessBtn.setObjectName(u"stopProcessBtn")

        self.verticalLayout_2.addWidget(self.stopProcessBtn)

        self.verticalLayout_2.setStretch(2, 1)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, -1, -1, -1)
        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setEnabled(True)
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.SSmcycle = QLCDNumber(self.widget_2)
        self.SSmcycle.setObjectName(u"SSmcycle")
        self.SSmcycle.setLineWidth(0)
        self.SSmcycle.setDigitCount(3)
        self.SSmcycle.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.SSmcycle, 17, 7, 1, 1)

        self.NEmcycle = QLCDNumber(self.widget_2)
        self.NEmcycle.setObjectName(u"NEmcycle")
        self.NEmcycle.setLineWidth(0)
        self.NEmcycle.setDigitCount(3)
        self.NEmcycle.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.NEmcycle, 2, 7, 1, 1)

        self.NEbicycleCount = QLCDNumber(self.widget_2)
        self.NEbicycleCount.setObjectName(u"NEbicycleCount")
        self.NEbicycleCount.setFrameShadow(QFrame.Raised)
        self.NEbicycleCount.setLineWidth(0)
        self.NEbicycleCount.setDigitCount(3)
        self.NEbicycleCount.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.NEbicycleCount, 2, 2, 1, 1)

        self.SNmcycle = QLCDNumber(self.widget_2)
        self.SNmcycle.setObjectName(u"SNmcycle")
        self.SNmcycle.setLineWidth(0)
        self.SNmcycle.setDigitCount(3)
        self.SNmcycle.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.SNmcycle, 14, 7, 1, 1)

        self.NWmcycle = QLCDNumber(self.widget_2)
        self.NWmcycle.setObjectName(u"NWmcycle")
        self.NWmcycle.setLineWidth(0)
        self.NWmcycle.setDigitCount(3)
        self.NWmcycle.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.NWmcycle, 3, 7, 1, 1)

        self.WSmcycle = QLCDNumber(self.widget_2)
        self.WSmcycle.setObjectName(u"WSmcycle")
        self.WSmcycle.setLineWidth(0)
        self.WSmcycle.setDigitCount(3)
        self.WSmcycle.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.WSmcycle, 13, 7, 1, 1)

        self.NWbicycleCount_2 = QLCDNumber(self.widget_2)
        self.NWbicycleCount_2.setObjectName(u"NWbicycleCount_2")
        self.NWbicycleCount_2.setLineWidth(0)
        self.NWbicycleCount_2.setDigitCount(3)
        self.NWbicycleCount_2.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.NWbicycleCount_2, 3, 2, 1, 1)

        self.label_8 = QLabel(self.widget_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 1, 0, 1, 1)

        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.label_2, 0, 5, 1, 1, Qt.AlignHCenter)

        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1, Qt.AlignHCenter)

        self.label_31 = QLabel(self.widget_2)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout.addWidget(self.label_31, 14, 0, 1, 1)

        self.label_29 = QLabel(self.widget_2)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout.addWidget(self.label_29, 8, 0, 1, 1)

        self.label_28 = QLabel(self.widget_2)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout.addWidget(self.label_28, 7, 0, 1, 1)

        self.label_25 = QLabel(self.widget_2)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout.addWidget(self.label_25, 12, 0, 1, 1)

        self.label_26 = QLabel(self.widget_2)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout.addWidget(self.label_26, 13, 0, 1, 1)

        self.label_32 = QLabel(self.widget_2)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout.addWidget(self.label_32, 15, 0, 1, 1)

        self.NEbusCount = QLCDNumber(self.widget_2)
        self.NEbusCount.setObjectName(u"NEbusCount")
        self.NEbusCount.setLineWidth(0)
        self.NEbusCount.setDigitCount(3)
        self.NEbusCount.setSegmentStyle(QLCDNumber.Flat)
        self.NEbusCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.NEbusCount, 2, 6, 1, 1)

        self.NEtruckCount = QLCDNumber(self.widget_2)
        self.NEtruckCount.setObjectName(u"NEtruckCount")
        self.NEtruckCount.setLineWidth(0)
        self.NEtruckCount.setDigitCount(3)
        self.NEtruckCount.setSegmentStyle(QLCDNumber.Flat)
        self.NEtruckCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.NEtruckCount, 2, 1, 1, 1)

        self.label_30 = QLabel(self.widget_2)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout.addWidget(self.label_30, 9, 0, 1, 1)

        self.label_27 = QLabel(self.widget_2)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout.addWidget(self.label_27, 6, 0, 1, 1)

        self.label_33 = QLabel(self.widget_2)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout.addWidget(self.label_33, 16, 0, 1, 1)

        self.NWtruckCount = QLCDNumber(self.widget_2)
        self.NWtruckCount.setObjectName(u"NWtruckCount")
        self.NWtruckCount.setLineWidth(0)
        self.NWtruckCount.setDigitCount(3)
        self.NWtruckCount.setSegmentStyle(QLCDNumber.Flat)
        self.NWtruckCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.NWtruckCount, 3, 1, 1, 1)

        self.NWcarCount = QLCDNumber(self.widget_2)
        self.NWcarCount.setObjectName(u"NWcarCount")
        self.NWcarCount.setLineWidth(0)
        self.NWcarCount.setDigitCount(3)
        self.NWcarCount.setSegmentStyle(QLCDNumber.Flat)
        self.NWcarCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.NWcarCount, 3, 5, 1, 1)

        self.NWbusCount = QLCDNumber(self.widget_2)
        self.NWbusCount.setObjectName(u"NWbusCount")
        self.NWbusCount.setLineWidth(0)
        self.NWbusCount.setDigitCount(3)
        self.NWbusCount.setSegmentStyle(QLCDNumber.Flat)
        self.NWbusCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.NWbusCount, 3, 6, 1, 1)

        self.NEcarCount = QLCDNumber(self.widget_2)
        self.NEcarCount.setObjectName(u"NEcarCount")
        self.NEcarCount.setLineWidth(0)
        self.NEcarCount.setDigitCount(3)
        self.NEcarCount.setSegmentStyle(QLCDNumber.Flat)
        self.NEcarCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.NEcarCount, 2, 5, 1, 1)

        self.label_34 = QLabel(self.widget_2)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout.addWidget(self.label_34, 17, 0, 1, 1)

        self.NStruckCount = QLCDNumber(self.widget_2)
        self.NStruckCount.setObjectName(u"NStruckCount")
        self.NStruckCount.setLineWidth(0)
        self.NStruckCount.setDigitCount(3)
        self.NStruckCount.setSegmentStyle(QLCDNumber.Flat)
        self.NStruckCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.NStruckCount, 5, 1, 1, 1)

        self.NSbusCount = QLCDNumber(self.widget_2)
        self.NSbusCount.setObjectName(u"NSbusCount")
        self.NSbusCount.setLineWidth(0)
        self.NSbusCount.setDigitCount(3)
        self.NSbusCount.setSegmentStyle(QLCDNumber.Flat)
        self.NSbusCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.NSbusCount, 5, 6, 1, 1)

        self.NScarCount = QLCDNumber(self.widget_2)
        self.NScarCount.setObjectName(u"NScarCount")
        self.NScarCount.setLineWidth(0)
        self.NScarCount.setDigitCount(3)
        self.NScarCount.setSegmentStyle(QLCDNumber.Flat)
        self.NScarCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.NScarCount, 5, 5, 1, 1)

        self.EEcarCount = QLCDNumber(self.widget_2)
        self.EEcarCount.setObjectName(u"EEcarCount")
        self.EEcarCount.setLineWidth(0)
        self.EEcarCount.setDigitCount(3)
        self.EEcarCount.setSegmentStyle(QLCDNumber.Flat)
        self.EEcarCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.EEcarCount, 7, 5, 1, 1)

        self.ENcarCount = QLCDNumber(self.widget_2)
        self.ENcarCount.setObjectName(u"ENcarCount")
        self.ENcarCount.setLineWidth(0)
        self.ENcarCount.setDigitCount(3)
        self.ENcarCount.setSegmentStyle(QLCDNumber.Flat)
        self.ENcarCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.ENcarCount, 6, 5, 1, 1)

        self.ENbusCount = QLCDNumber(self.widget_2)
        self.ENbusCount.setObjectName(u"ENbusCount")
        self.ENbusCount.setLineWidth(0)
        self.ENbusCount.setDigitCount(3)
        self.ENbusCount.setSegmentStyle(QLCDNumber.Flat)
        self.ENbusCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.ENbusCount, 6, 6, 1, 1)

        self.EScarCount = QLCDNumber(self.widget_2)
        self.EScarCount.setObjectName(u"EScarCount")
        self.EScarCount.setLineWidth(0)
        self.EScarCount.setDigitCount(3)
        self.EScarCount.setSegmentStyle(QLCDNumber.Flat)
        self.EScarCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.EScarCount, 9, 5, 1, 1)

        self.ENtruckCount = QLCDNumber(self.widget_2)
        self.ENtruckCount.setObjectName(u"ENtruckCount")
        self.ENtruckCount.setLineWidth(0)
        self.ENtruckCount.setDigitCount(3)
        self.ENtruckCount.setSegmentStyle(QLCDNumber.Flat)
        self.ENtruckCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.ENtruckCount, 6, 1, 1, 1)

        self.EWtruckCount = QLCDNumber(self.widget_2)
        self.EWtruckCount.setObjectName(u"EWtruckCount")
        self.EWtruckCount.setLineWidth(0)
        self.EWtruckCount.setDigitCount(3)
        self.EWtruckCount.setSegmentStyle(QLCDNumber.Flat)
        self.EWtruckCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.EWtruckCount, 8, 1, 1, 1)

        self.EEbusCount = QLCDNumber(self.widget_2)
        self.EEbusCount.setObjectName(u"EEbusCount")
        self.EEbusCount.setLineWidth(0)
        self.EEbusCount.setDigitCount(3)
        self.EEbusCount.setSegmentStyle(QLCDNumber.Flat)
        self.EEbusCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.EEbusCount, 7, 6, 1, 1)

        self.EWcarCount = QLCDNumber(self.widget_2)
        self.EWcarCount.setObjectName(u"EWcarCount")
        self.EWcarCount.setLineWidth(0)
        self.EWcarCount.setDigitCount(3)
        self.EWcarCount.setSegmentStyle(QLCDNumber.Flat)
        self.EWcarCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.EWcarCount, 8, 5, 1, 1)

        self.EEtruckCount = QLCDNumber(self.widget_2)
        self.EEtruckCount.setObjectName(u"EEtruckCount")
        self.EEtruckCount.setLineWidth(0)
        self.EEtruckCount.setDigitCount(3)
        self.EEtruckCount.setSegmentStyle(QLCDNumber.Flat)
        self.EEtruckCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.EEtruckCount, 7, 1, 1, 1)

        self.EWbusCount = QLCDNumber(self.widget_2)
        self.EWbusCount.setObjectName(u"EWbusCount")
        self.EWbusCount.setLineWidth(0)
        self.EWbusCount.setDigitCount(3)
        self.EWbusCount.setSegmentStyle(QLCDNumber.Flat)
        self.EWbusCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.EWbusCount, 8, 6, 1, 1)

        self.WWtruckCount = QLCDNumber(self.widget_2)
        self.WWtruckCount.setObjectName(u"WWtruckCount")
        self.WWtruckCount.setLineWidth(0)
        self.WWtruckCount.setDigitCount(3)
        self.WWtruckCount.setSegmentStyle(QLCDNumber.Flat)
        self.WWtruckCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.WWtruckCount, 11, 1, 1, 1)

        self.ESbusCount = QLCDNumber(self.widget_2)
        self.ESbusCount.setObjectName(u"ESbusCount")
        self.ESbusCount.setLineWidth(0)
        self.ESbusCount.setDigitCount(3)
        self.ESbusCount.setSegmentStyle(QLCDNumber.Flat)
        self.ESbusCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.ESbusCount, 9, 6, 1, 1)

        self.WNtruckCount = QLCDNumber(self.widget_2)
        self.WNtruckCount.setObjectName(u"WNtruckCount")
        self.WNtruckCount.setLineWidth(0)
        self.WNtruckCount.setDigitCount(3)
        self.WNtruckCount.setSegmentStyle(QLCDNumber.Flat)
        self.WNtruckCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.WNtruckCount, 10, 1, 1, 1)

        self.EStruckCount = QLCDNumber(self.widget_2)
        self.EStruckCount.setObjectName(u"EStruckCount")
        self.EStruckCount.setLineWidth(0)
        self.EStruckCount.setDigitCount(3)
        self.EStruckCount.setSegmentStyle(QLCDNumber.Flat)
        self.EStruckCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.EStruckCount, 9, 1, 1, 1)

        self.WNbusCount = QLCDNumber(self.widget_2)
        self.WNbusCount.setObjectName(u"WNbusCount")
        self.WNbusCount.setLineWidth(0)
        self.WNbusCount.setDigitCount(3)
        self.WNbusCount.setSegmentStyle(QLCDNumber.Flat)
        self.WNbusCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.WNbusCount, 10, 6, 1, 1)

        self.WWcarCount = QLCDNumber(self.widget_2)
        self.WWcarCount.setObjectName(u"WWcarCount")
        self.WWcarCount.setLineWidth(0)
        self.WWcarCount.setDigitCount(3)
        self.WWcarCount.setSegmentStyle(QLCDNumber.Flat)
        self.WWcarCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.WWcarCount, 11, 5, 1, 1)

        self.WEtruckCount = QLCDNumber(self.widget_2)
        self.WEtruckCount.setObjectName(u"WEtruckCount")
        self.WEtruckCount.setLineWidth(0)
        self.WEtruckCount.setDigitCount(3)
        self.WEtruckCount.setSegmentStyle(QLCDNumber.Flat)
        self.WEtruckCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.WEtruckCount, 12, 1, 1, 1)

        self.WNcarCount = QLCDNumber(self.widget_2)
        self.WNcarCount.setObjectName(u"WNcarCount")
        self.WNcarCount.setLineWidth(0)
        self.WNcarCount.setDigitCount(3)
        self.WNcarCount.setSegmentStyle(QLCDNumber.Flat)
        self.WNcarCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.WNcarCount, 10, 5, 1, 1)

        self.NNbicycleCount = QLCDNumber(self.widget_2)
        self.NNbicycleCount.setObjectName(u"NNbicycleCount")
        self.NNbicycleCount.setFrameShadow(QFrame.Raised)
        self.NNbicycleCount.setLineWidth(0)
        self.NNbicycleCount.setDigitCount(3)
        self.NNbicycleCount.setSegmentStyle(QLCDNumber.Flat)
        self.NNbicycleCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.NNbicycleCount, 1, 2, 1, 1)

        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)

        self.NNmcycle = QLCDNumber(self.widget_2)
        self.NNmcycle.setObjectName(u"NNmcycle")
        self.NNmcycle.setLineWidth(0)
        self.NNmcycle.setDigitCount(3)
        self.NNmcycle.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.NNmcycle, 1, 7, 1, 1)

        self.ENbicycleCount = QLCDNumber(self.widget_2)
        self.ENbicycleCount.setObjectName(u"ENbicycleCount")
        self.ENbicycleCount.setLineWidth(0)
        self.ENbicycleCount.setDigitCount(3)
        self.ENbicycleCount.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.ENbicycleCount, 6, 2, 1, 1)

        self.EWbicycleCount = QLCDNumber(self.widget_2)
        self.EWbicycleCount.setObjectName(u"EWbicycleCount")
        self.EWbicycleCount.setLineWidth(0)
        self.EWbicycleCount.setDigitCount(3)
        self.EWbicycleCount.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.EWbicycleCount, 8, 2, 1, 1)

        self.WNbicycleCount = QLCDNumber(self.widget_2)
        self.WNbicycleCount.setObjectName(u"WNbicycleCount")
        self.WNbicycleCount.setLineWidth(0)
        self.WNbicycleCount.setDigitCount(3)
        self.WNbicycleCount.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.WNbicycleCount, 10, 2, 1, 1)

        self.SNbicycleCount = QLCDNumber(self.widget_2)
        self.SNbicycleCount.setObjectName(u"SNbicycleCount")
        self.SNbicycleCount.setLineWidth(0)
        self.SNbicycleCount.setDigitCount(3)
        self.SNbicycleCount.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.SNbicycleCount, 14, 2, 1, 1)

        self.WWbicycleCount = QLCDNumber(self.widget_2)
        self.WWbicycleCount.setObjectName(u"WWbicycleCount")
        self.WWbicycleCount.setLineWidth(0)
        self.WWbicycleCount.setDigitCount(3)
        self.WWbicycleCount.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.WWbicycleCount, 11, 2, 1, 1)

        self.ESbicycleCount = QLCDNumber(self.widget_2)
        self.ESbicycleCount.setObjectName(u"ESbicycleCount")
        self.ESbicycleCount.setLineWidth(0)
        self.ESbicycleCount.setDigitCount(3)
        self.ESbicycleCount.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.ESbicycleCount, 9, 2, 1, 1)

        self.WEbicycleCount = QLCDNumber(self.widget_2)
        self.WEbicycleCount.setObjectName(u"WEbicycleCount")
        self.WEbicycleCount.setLineWidth(0)
        self.WEbicycleCount.setDigitCount(3)
        self.WEbicycleCount.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.WEbicycleCount, 12, 2, 1, 1)

        self.SEbicycleCount = QLCDNumber(self.widget_2)
        self.SEbicycleCount.setObjectName(u"SEbicycleCount")
        self.SEbicycleCount.setLineWidth(0)
        self.SEbicycleCount.setDigitCount(3)
        self.SEbicycleCount.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.SEbicycleCount, 15, 2, 1, 1)

        self.WSbicycleCount = QLCDNumber(self.widget_2)
        self.WSbicycleCount.setObjectName(u"WSbicycleCount")
        self.WSbicycleCount.setLineWidth(0)
        self.WSbicycleCount.setDigitCount(3)
        self.WSbicycleCount.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.WSbicycleCount, 13, 2, 1, 1)

        self.label_23 = QLabel(self.widget_2)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout.addWidget(self.label_23, 10, 0, 1, 1)

        self.label_22 = QLabel(self.widget_2)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout.addWidget(self.label_22, 5, 0, 1, 1)

        self.label_20 = QLabel(self.widget_2)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout.addWidget(self.label_20, 3, 0, 1, 1)

        self.label_21 = QLabel(self.widget_2)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout.addWidget(self.label_21, 2, 0, 1, 1)

        self.label_15 = QLabel(self.widget_2)
        self.label_15.setObjectName(u"label_15")
        sizePolicy1.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.label_15, 0, 6, 1, 1, Qt.AlignHCenter)

        self.SEcarCount = QLCDNumber(self.widget_2)
        self.SEcarCount.setObjectName(u"SEcarCount")
        self.SEcarCount.setLineWidth(0)
        self.SEcarCount.setDigitCount(3)
        self.SEcarCount.setSegmentStyle(QLCDNumber.Flat)
        self.SEcarCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.SEcarCount, 15, 5, 1, 1)

        self.carCount = QLCDNumber(self.widget_2)
        self.carCount.setObjectName(u"carCount")
        self.carCount.setLineWidth(0)
        self.carCount.setDigitCount(3)
        self.carCount.setSegmentStyle(QLCDNumber.Flat)
        self.carCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.carCount, 1, 5, 1, 1)

        self.busCount = QLCDNumber(self.widget_2)
        self.busCount.setObjectName(u"busCount")
        self.busCount.setLineWidth(0)
        self.busCount.setDigitCount(3)
        self.busCount.setSegmentStyle(QLCDNumber.Flat)
        self.busCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.busCount, 1, 6, 1, 1)

        self.SEbusCount = QLCDNumber(self.widget_2)
        self.SEbusCount.setObjectName(u"SEbusCount")
        self.SEbusCount.setLineWidth(0)
        self.SEbusCount.setDigitCount(3)
        self.SEbusCount.setSegmentStyle(QLCDNumber.Flat)
        self.SEbusCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.SEbusCount, 15, 6, 1, 1)

        self.SWbusCount = QLCDNumber(self.widget_2)
        self.SWbusCount.setObjectName(u"SWbusCount")
        self.SWbusCount.setLineWidth(0)
        self.SWbusCount.setDigitCount(3)
        self.SWbusCount.setSegmentStyle(QLCDNumber.Flat)
        self.SWbusCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.SWbusCount, 16, 6, 1, 1)

        self.SEtruckCount = QLCDNumber(self.widget_2)
        self.SEtruckCount.setObjectName(u"SEtruckCount")
        self.SEtruckCount.setLineWidth(0)
        self.SEtruckCount.setDigitCount(3)
        self.SEtruckCount.setSegmentStyle(QLCDNumber.Flat)
        self.SEtruckCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.SEtruckCount, 15, 1, 1, 1)

        self.SWtruckCount = QLCDNumber(self.widget_2)
        self.SWtruckCount.setObjectName(u"SWtruckCount")
        self.SWtruckCount.setLineWidth(0)
        self.SWtruckCount.setDigitCount(3)
        self.SWtruckCount.setSegmentStyle(QLCDNumber.Flat)
        self.SWtruckCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.SWtruckCount, 16, 1, 1, 1)

        self.SSbusCount = QLCDNumber(self.widget_2)
        self.SSbusCount.setObjectName(u"SSbusCount")
        self.SSbusCount.setLineWidth(0)
        self.SSbusCount.setDigitCount(3)
        self.SSbusCount.setSegmentStyle(QLCDNumber.Flat)
        self.SSbusCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.SSbusCount, 17, 6, 1, 1)

        self.SStruckCount = QLCDNumber(self.widget_2)
        self.SStruckCount.setObjectName(u"SStruckCount")
        self.SStruckCount.setLineWidth(0)
        self.SStruckCount.setDigitCount(3)
        self.SStruckCount.setSegmentStyle(QLCDNumber.Flat)
        self.SStruckCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.SStruckCount, 17, 1, 1, 1)

        self.SScarCount = QLCDNumber(self.widget_2)
        self.SScarCount.setObjectName(u"SScarCount")
        self.SScarCount.setLineWidth(0)
        self.SScarCount.setDigitCount(3)
        self.SScarCount.setSegmentStyle(QLCDNumber.Flat)
        self.SScarCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.SScarCount, 17, 5, 1, 1)

        self.SWcarCount = QLCDNumber(self.widget_2)
        self.SWcarCount.setObjectName(u"SWcarCount")
        self.SWcarCount.setLineWidth(0)
        self.SWcarCount.setDigitCount(3)
        self.SWcarCount.setSegmentStyle(QLCDNumber.Flat)
        self.SWcarCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.SWcarCount, 16, 5, 1, 1)

        self.truckCount = QLCDNumber(self.widget_2)
        self.truckCount.setObjectName(u"truckCount")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.truckCount.sizePolicy().hasHeightForWidth())
        self.truckCount.setSizePolicy(sizePolicy2)
        self.truckCount.setLineWidth(0)
        self.truckCount.setDigitCount(3)
        self.truckCount.setSegmentStyle(QLCDNumber.Flat)
        self.truckCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.truckCount, 1, 1, 1, 1)

        self.label_24 = QLabel(self.widget_2)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout.addWidget(self.label_24, 11, 0, 1, 1)

        self.WStruckCount = QLCDNumber(self.widget_2)
        self.WStruckCount.setObjectName(u"WStruckCount")
        self.WStruckCount.setLineWidth(0)
        self.WStruckCount.setDigitCount(3)
        self.WStruckCount.setSegmentStyle(QLCDNumber.Flat)
        self.WStruckCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.WStruckCount, 13, 1, 1, 1)

        self.WEcarCount = QLCDNumber(self.widget_2)
        self.WEcarCount.setObjectName(u"WEcarCount")
        self.WEcarCount.setLineWidth(0)
        self.WEcarCount.setDigitCount(3)
        self.WEcarCount.setSegmentStyle(QLCDNumber.Flat)
        self.WEcarCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.WEcarCount, 12, 5, 1, 1)

        self.WSbusCount = QLCDNumber(self.widget_2)
        self.WSbusCount.setObjectName(u"WSbusCount")
        self.WSbusCount.setLineWidth(0)
        self.WSbusCount.setDigitCount(3)
        self.WSbusCount.setSegmentStyle(QLCDNumber.Flat)
        self.WSbusCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.WSbusCount, 13, 6, 1, 1)

        self.WEbusCount = QLCDNumber(self.widget_2)
        self.WEbusCount.setObjectName(u"WEbusCount")
        self.WEbusCount.setLineWidth(0)
        self.WEbusCount.setDigitCount(3)
        self.WEbusCount.setSegmentStyle(QLCDNumber.Flat)
        self.WEbusCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.WEbusCount, 12, 6, 1, 1)

        self.SNbusCount = QLCDNumber(self.widget_2)
        self.SNbusCount.setObjectName(u"SNbusCount")
        self.SNbusCount.setLineWidth(0)
        self.SNbusCount.setDigitCount(3)
        self.SNbusCount.setSegmentStyle(QLCDNumber.Flat)
        self.SNbusCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.SNbusCount, 14, 6, 1, 1)

        self.WWbusCount = QLCDNumber(self.widget_2)
        self.WWbusCount.setObjectName(u"WWbusCount")
        self.WWbusCount.setLineWidth(0)
        self.WWbusCount.setDigitCount(3)
        self.WWbusCount.setSegmentStyle(QLCDNumber.Flat)
        self.WWbusCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.WWbusCount, 11, 6, 1, 1)

        self.WScarCount = QLCDNumber(self.widget_2)
        self.WScarCount.setObjectName(u"WScarCount")
        self.WScarCount.setLineWidth(0)
        self.WScarCount.setDigitCount(3)
        self.WScarCount.setSegmentStyle(QLCDNumber.Flat)
        self.WScarCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.WScarCount, 13, 5, 1, 1)

        self.SNtruckCount = QLCDNumber(self.widget_2)
        self.SNtruckCount.setObjectName(u"SNtruckCount")
        self.SNtruckCount.setLineWidth(0)
        self.SNtruckCount.setDigitCount(3)
        self.SNtruckCount.setSegmentStyle(QLCDNumber.Flat)
        self.SNtruckCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.SNtruckCount, 14, 1, 1, 1)

        self.SNcarCount = QLCDNumber(self.widget_2)
        self.SNcarCount.setObjectName(u"SNcarCount")
        self.SNcarCount.setLineWidth(0)
        self.SNcarCount.setDigitCount(3)
        self.SNcarCount.setSegmentStyle(QLCDNumber.Flat)
        self.SNcarCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.SNcarCount, 14, 5, 1, 1)

        self.SSbicycleCount = QLCDNumber(self.widget_2)
        self.SSbicycleCount.setObjectName(u"SSbicycleCount")
        self.SSbicycleCount.setLineWidth(0)
        self.SSbicycleCount.setDigitCount(3)
        self.SSbicycleCount.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.SSbicycleCount, 17, 2, 1, 1)

        self.EEbicycleCount = QLCDNumber(self.widget_2)
        self.EEbicycleCount.setObjectName(u"EEbicycleCount")
        self.EEbicycleCount.setLineWidth(0)
        self.EEbicycleCount.setDigitCount(3)
        self.EEbicycleCount.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.EEbicycleCount, 7, 2, 1, 1)

        self.SWbicycleCount = QLCDNumber(self.widget_2)
        self.SWbicycleCount.setObjectName(u"SWbicycleCount")
        self.SWbicycleCount.setLineWidth(0)
        self.SWbicycleCount.setDigitCount(3)
        self.SWbicycleCount.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.SWbicycleCount, 16, 2, 1, 1)

        self.NSbicycleCount = QLCDNumber(self.widget_2)
        self.NSbicycleCount.setObjectName(u"NSbicycleCount")
        self.NSbicycleCount.setLineWidth(0)
        self.NSbicycleCount.setDigitCount(3)
        self.NSbicycleCount.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.NSbicycleCount, 5, 2, 1, 1)

        self.NSmcycle = QLCDNumber(self.widget_2)
        self.NSmcycle.setObjectName(u"NSmcycle")
        self.NSmcycle.setLineWidth(0)
        self.NSmcycle.setDigitCount(3)
        self.NSmcycle.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.NSmcycle, 5, 7, 1, 1)

        self.WEmcycle = QLCDNumber(self.widget_2)
        self.WEmcycle.setObjectName(u"WEmcycle")
        self.WEmcycle.setLineWidth(0)
        self.WEmcycle.setDigitCount(3)
        self.WEmcycle.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.WEmcycle, 12, 7, 1, 1)

        self.ENmcycle = QLCDNumber(self.widget_2)
        self.ENmcycle.setObjectName(u"ENmcycle")
        self.ENmcycle.setLineWidth(0)
        self.ENmcycle.setDigitCount(3)
        self.ENmcycle.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.ENmcycle, 6, 7, 1, 1)

        self.SWmcycle = QLCDNumber(self.widget_2)
        self.SWmcycle.setObjectName(u"SWmcycle")
        self.SWmcycle.setLineWidth(0)
        self.SWmcycle.setDigitCount(3)
        self.SWmcycle.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.SWmcycle, 16, 7, 1, 1)

        self.ESmcycle = QLCDNumber(self.widget_2)
        self.ESmcycle.setObjectName(u"ESmcycle")
        self.ESmcycle.setLineWidth(0)
        self.ESmcycle.setDigitCount(3)
        self.ESmcycle.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.ESmcycle, 9, 7, 1, 1)

        self.EWmcycle = QLCDNumber(self.widget_2)
        self.EWmcycle.setObjectName(u"EWmcycle")
        self.EWmcycle.setLineWidth(0)
        self.EWmcycle.setDigitCount(3)
        self.EWmcycle.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.EWmcycle, 8, 7, 1, 1)

        self.WWmcycle = QLCDNumber(self.widget_2)
        self.WWmcycle.setObjectName(u"WWmcycle")
        self.WWmcycle.setLineWidth(0)
        self.WWmcycle.setDigitCount(3)
        self.WWmcycle.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.WWmcycle, 11, 7, 1, 1)

        self.SEmcycle = QLCDNumber(self.widget_2)
        self.SEmcycle.setObjectName(u"SEmcycle")
        self.SEmcycle.setLineWidth(0)
        self.SEmcycle.setDigitCount(3)
        self.SEmcycle.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.SEmcycle, 15, 7, 1, 1)

        self.EEmcycle = QLCDNumber(self.widget_2)
        self.EEmcycle.setObjectName(u"EEmcycle")
        self.EEmcycle.setLineWidth(0)
        self.EEmcycle.setDigitCount(3)
        self.EEmcycle.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.EEmcycle, 7, 7, 1, 1)

        self.WNmcycle = QLCDNumber(self.widget_2)
        self.WNmcycle.setObjectName(u"WNmcycle")
        self.WNmcycle.setLineWidth(0)
        self.WNmcycle.setDigitCount(3)
        self.WNmcycle.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.WNmcycle, 10, 7, 1, 1)

        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 7, 1, 1)


        self.verticalLayout.addWidget(self.widget_2)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        self.comboBox.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Traffic Vehicle Counter", None))
        self.addCamBtn.setText(QCoreApplication.translate("Form", u"Add Camera", None))
        self.editCameraBtn.setText(QCoreApplication.translate("Form", u"Edit Camera", None))
        self.removeCameraBtn.setText(QCoreApplication.translate("Form", u"Remove Camera", None))
        self.showDataBtn.setText(QCoreApplication.translate("Form", u"Show Data", None))
        self.videoSwitcher.setTitle("")
        self.mediaGBox.setTitle("")
        self.label_5.setText(QCoreApplication.translate("Form", u"IP", None))
        self.comboBox.setCurrentText("")
        self.startInferenceBtn.setText(QCoreApplication.translate("Form", u"START", None))
        self.refreshCamerasBtn.setText(QCoreApplication.translate("Form", u"Refresh", None))
        self.stopProcessBtn.setText(QCoreApplication.translate("Form", u"STOP", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"NN", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Cars", None))
        self.label.setText(QCoreApplication.translate("Form", u"Trucks", None))
        self.label_31.setText(QCoreApplication.translate("Form", u"SN", None))
        self.label_29.setText(QCoreApplication.translate("Form", u"EW", None))
        self.label_28.setText(QCoreApplication.translate("Form", u"EE", None))
        self.label_25.setText(QCoreApplication.translate("Form", u"WE", None))
        self.label_26.setText(QCoreApplication.translate("Form", u"WS", None))
        self.label_32.setText(QCoreApplication.translate("Form", u"SE", None))
        self.label_30.setText(QCoreApplication.translate("Form", u"ES", None))
        self.label_27.setText(QCoreApplication.translate("Form", u"EN", None))
        self.label_33.setText(QCoreApplication.translate("Form", u"SW", None))
        self.label_34.setText(QCoreApplication.translate("Form", u"SS", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Bicycle", None))
        self.label_23.setText(QCoreApplication.translate("Form", u"WN", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"NS", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"NW", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"NE", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Bus", None))
        self.label_24.setText(QCoreApplication.translate("Form", u"WW", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Mcycle", None))
    # retranslateUi

