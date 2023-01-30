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
        Form.resize(1107, 820)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(8, 8, 8, 8)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, 0, -1)
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

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(10, -1, 10, 0)
        self.stopProcessBtn = QPushButton(self.videoSwitcher)
        self.stopProcessBtn.setObjectName(u"stopProcessBtn")
        self.stopProcessBtn.setEnabled(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.stopProcessBtn.sizePolicy().hasHeightForWidth())
        self.stopProcessBtn.setSizePolicy(sizePolicy1)

        self.horizontalLayout_5.addWidget(self.stopProcessBtn)

        self.frameSlider = QSlider(self.videoSwitcher)
        self.frameSlider.setObjectName(u"frameSlider")
        self.frameSlider.setEnabled(True)
        self.frameSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_5.addWidget(self.frameSlider)

        self.frameNum = QLabel(self.videoSwitcher)
        self.frameNum.setObjectName(u"frameNum")

        self.horizontalLayout_5.addWidget(self.frameNum)

        self.label_13 = QLabel(self.videoSwitcher)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_5.addWidget(self.label_13)

        self.maxFrameNum = QLabel(self.videoSwitcher)
        self.maxFrameNum.setObjectName(u"maxFrameNum")

        self.horizontalLayout_5.addWidget(self.maxFrameNum)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)


        self.verticalLayout_2.addWidget(self.videoSwitcher)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(7)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, 0, 0, 0)
        self.mediaGBox = QGroupBox(Form)
        self.mediaGBox.setObjectName(u"mediaGBox")
        self.gridLayout_2 = QGridLayout(self.mediaGBox)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_9 = QLabel(self.mediaGBox)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)

        self.label_10 = QLabel(self.mediaGBox)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 2, 0, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_9.setContentsMargins(-1, -1, 0, -1)
        self.inputVideoFileLabel = QLineEdit(self.mediaGBox)
        self.inputVideoFileLabel.setObjectName(u"inputVideoFileLabel")

        self.horizontalLayout_9.addWidget(self.inputVideoFileLabel)

        self.loadVideoBtn = QToolButton(self.mediaGBox)
        self.loadVideoBtn.setObjectName(u"loadVideoBtn")

        self.horizontalLayout_9.addWidget(self.loadVideoBtn)


        self.gridLayout_2.addLayout(self.horizontalLayout_9, 0, 1, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.cacheDataLabel = QLineEdit(self.mediaGBox)
        self.cacheDataLabel.setObjectName(u"cacheDataLabel")

        self.horizontalLayout_10.addWidget(self.cacheDataLabel)

        self.loadCacheBtn = QToolButton(self.mediaGBox)
        self.loadCacheBtn.setObjectName(u"loadCacheBtn")

        self.horizontalLayout_10.addWidget(self.loadCacheBtn)


        self.gridLayout_2.addLayout(self.horizontalLayout_10, 2, 1, 1, 1)


        self.verticalLayout_9.addWidget(self.mediaGBox)

        self.maskingGBox = QGroupBox(Form)
        self.maskingGBox.setObjectName(u"maskingGBox")
        self.gridLayout_5 = QGridLayout(self.maskingGBox)
        self.gridLayout_5.setSpacing(5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(5, 5, 5, 5)
        self.saveMaskBtn = QPushButton(self.maskingGBox)
        self.saveMaskBtn.setObjectName(u"saveMaskBtn")

        self.gridLayout_5.addWidget(self.saveMaskBtn, 3, 2, 1, 1)

        self.resetMaskBtn = QPushButton(self.maskingGBox)
        self.resetMaskBtn.setObjectName(u"resetMaskBtn")

        self.gridLayout_5.addWidget(self.resetMaskBtn, 3, 0, 1, 1)

        self.drawMaskBtn = QPushButton(self.maskingGBox)
        self.drawMaskBtn.setObjectName(u"drawMaskBtn")

        self.gridLayout_5.addWidget(self.drawMaskBtn, 3, 1, 1, 1)

        self.label_19 = QLabel(self.maskingGBox)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_5.addWidget(self.label_19, 2, 0, 1, 1)

        self.label_17 = QLabel(self.maskingGBox)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_5.addWidget(self.label_17, 1, 0, 1, 1)

        self.maskStokeSpn = QSpinBox(self.maskingGBox)
        self.maskStokeSpn.setObjectName(u"maskStokeSpn")
        self.maskStokeSpn.setMaximum(200)
        self.maskStokeSpn.setValue(50)

        self.gridLayout_5.addWidget(self.maskStokeSpn, 1, 1, 1, 2)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(1)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.maskFileLbl = QLineEdit(self.maskingGBox)
        self.maskFileLbl.setObjectName(u"maskFileLbl")
        self.maskFileLbl.setReadOnly(True)

        self.horizontalLayout_8.addWidget(self.maskFileLbl)

        self.setMaskFileBtn = QToolButton(self.maskingGBox)
        self.setMaskFileBtn.setObjectName(u"setMaskFileBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.setMaskFileBtn.sizePolicy().hasHeightForWidth())
        self.setMaskFileBtn.setSizePolicy(sizePolicy2)

        self.horizontalLayout_8.addWidget(self.setMaskFileBtn)


        self.gridLayout_5.addLayout(self.horizontalLayout_8, 2, 1, 1, 2)


        self.verticalLayout_9.addWidget(self.maskingGBox)


        self.horizontalLayout_2.addLayout(self.verticalLayout_9)

        self.inferenceGBox = QGroupBox(Form)
        self.inferenceGBox.setObjectName(u"inferenceGBox")
        self.inferenceGBox.setEnabled(True)
        self.formLayout = QFormLayout(self.inferenceGBox)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(5)
        self.formLayout.setVerticalSpacing(5)
        self.formLayout.setContentsMargins(8, 8, 8, 8)
        self.modelLabel = QLabel(self.inferenceGBox)
        self.modelLabel.setObjectName(u"modelLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.modelLabel)

        self.modelComboBox = QComboBox(self.inferenceGBox)
        self.modelComboBox.addItem("")
        self.modelComboBox.setObjectName(u"modelComboBox")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.modelComboBox)

        self.iOUThresholdLabel_2 = QLabel(self.inferenceGBox)
        self.iOUThresholdLabel_2.setObjectName(u"iOUThresholdLabel_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.iOUThresholdLabel_2)

        self.cosineDistSpn = QDoubleSpinBox(self.inferenceGBox)
        self.cosineDistSpn.setObjectName(u"cosineDistSpn")
        self.cosineDistSpn.setDecimals(1)
        self.cosineDistSpn.setValue(0.400000000000000)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.cosineDistSpn)

        self.iOUThresholdLabel = QLabel(self.inferenceGBox)
        self.iOUThresholdLabel.setObjectName(u"iOUThresholdLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.iOUThresholdLabel)

        self.iouThreshSpn = QDoubleSpinBox(self.inferenceGBox)
        self.iouThreshSpn.setObjectName(u"iouThreshSpn")
        self.iouThreshSpn.setDecimals(2)
        self.iouThreshSpn.setValue(0.450000000000000)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.iouThreshSpn)

        self.confidenceThresholdLabel = QLabel(self.inferenceGBox)
        self.confidenceThresholdLabel.setObjectName(u"confidenceThresholdLabel")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.confidenceThresholdLabel)

        self.scoreThreshSpn = QDoubleSpinBox(self.inferenceGBox)
        self.scoreThreshSpn.setObjectName(u"scoreThreshSpn")
        self.scoreThreshSpn.setDecimals(1)
        self.scoreThreshSpn.setValue(0.700000000000000)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.scoreThreshSpn)

        self.label_7 = QLabel(self.inferenceGBox)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_7)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.outputFileLabel = QLineEdit(self.inferenceGBox)
        self.outputFileLabel.setObjectName(u"outputFileLabel")
        self.outputFileLabel.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.outputFileLabel)

        self.setOutputFileBtn = QToolButton(self.inferenceGBox)
        self.setOutputFileBtn.setObjectName(u"setOutputFileBtn")
        sizePolicy2.setHeightForWidth(self.setOutputFileBtn.sizePolicy().hasHeightForWidth())
        self.setOutputFileBtn.setSizePolicy(sizePolicy2)

        self.horizontalLayout_4.addWidget(self.setOutputFileBtn)


        self.formLayout.setLayout(5, QFormLayout.FieldRole, self.horizontalLayout_4)

        self.startInferenceBtn = QPushButton(self.inferenceGBox)
        self.startInferenceBtn.setObjectName(u"startInferenceBtn")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.startInferenceBtn)


        self.horizontalLayout_2.addWidget(self.inferenceGBox)

        self.countingGBox = QGroupBox(Form)
        self.countingGBox.setObjectName(u"countingGBox")
        self.verticalLayout_8 = QVBoxLayout(self.countingGBox)
        self.verticalLayout_8.setSpacing(2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(8, 8, 8, 8)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_16 = QLabel(self.countingGBox)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_7.addWidget(self.label_16)

        self.countMethodCmb = QComboBox(self.countingGBox)
        self.countMethodCmb.addItem("")
        self.countMethodCmb.addItem("")
        self.countMethodCmb.setObjectName(u"countMethodCmb")

        self.horizontalLayout_7.addWidget(self.countMethodCmb)


        self.verticalLayout_8.addLayout(self.horizontalLayout_7)

        self.countingMethodSwitcher = QStackedWidget(self.countingGBox)
        self.countingMethodSwitcher.setObjectName(u"countingMethodSwitcher")
        self.vectorPage = QWidget()
        self.vectorPage.setObjectName(u"vectorPage")
        self.gridLayout_3 = QGridLayout(self.vectorPage)
        self.gridLayout_3.setSpacing(5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(5, 5, 5, 5)
        self.widthFilterVectorSpn = QSpinBox(self.vectorPage)
        self.widthFilterVectorSpn.setObjectName(u"widthFilterVectorSpn")
        self.widthFilterVectorSpn.setMaximum(1000)
        self.widthFilterVectorSpn.setValue(192)

        self.gridLayout_3.addWidget(self.widthFilterVectorSpn, 2, 2, 1, 1)

        self.xFilterVectorSpn = QDoubleSpinBox(self.vectorPage)
        self.xFilterVectorSpn.setObjectName(u"xFilterVectorSpn")
        self.xFilterVectorSpn.setDecimals(0)
        self.xFilterVectorSpn.setMinimum(-1000.000000000000000)
        self.xFilterVectorSpn.setMaximum(1000.000000000000000)
        self.xFilterVectorSpn.setValue(-258.000000000000000)

        self.gridLayout_3.addWidget(self.xFilterVectorSpn, 0, 2, 1, 1)

        self.label_12 = QLabel(self.vectorPage)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_3.addWidget(self.label_12, 1, 1, 1, 1)

        self.label_5 = QLabel(self.vectorPage)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 3, 0, 1, 1)

        self.label_14 = QLabel(self.vectorPage)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_3.addWidget(self.label_14, 2, 0, 1, 1)

        self.label_11 = QLabel(self.vectorPage)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_3.addWidget(self.label_11, 0, 1, 1, 1)

        self.label_6 = QLabel(self.vectorPage)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 4, 0, 1, 1)

        self.distFilterSpn = QSpinBox(self.vectorPage)
        self.distFilterSpn.setObjectName(u"distFilterSpn")
        self.distFilterSpn.setMaximum(1000)
        self.distFilterSpn.setValue(440)

        self.gridLayout_3.addWidget(self.distFilterSpn, 3, 2, 1, 1)

        self.skipFrameFilterSpn = QSpinBox(self.vectorPage)
        self.skipFrameFilterSpn.setObjectName(u"skipFrameFilterSpn")
        self.skipFrameFilterSpn.setValue(10)

        self.gridLayout_3.addWidget(self.skipFrameFilterSpn, 4, 2, 1, 1)

        self.label_4 = QLabel(self.vectorPage)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)

        self.visualizeChk = QCheckBox(self.vectorPage)
        self.visualizeChk.setObjectName(u"visualizeChk")

        self.gridLayout_3.addWidget(self.visualizeChk, 5, 0, 1, 1)

        self.yFilterVectorSpn = QDoubleSpinBox(self.vectorPage)
        self.yFilterVectorSpn.setObjectName(u"yFilterVectorSpn")
        self.yFilterVectorSpn.setEnabled(False)
        self.yFilterVectorSpn.setDecimals(0)
        self.yFilterVectorSpn.setMinimum(-1000.000000000000000)
        self.yFilterVectorSpn.setMaximum(1000.000000000000000)
        self.yFilterVectorSpn.setValue(357.000000000000000)

        self.gridLayout_3.addWidget(self.yFilterVectorSpn, 1, 2, 1, 1)

        self.vectorDirectionLbl = QLabel(self.vectorPage)
        self.vectorDirectionLbl.setObjectName(u"vectorDirectionLbl")
        self.vectorDirectionLbl.setStyleSheet(u"color: rgb(252, 1, 7);")

        self.gridLayout_3.addWidget(self.vectorDirectionLbl, 1, 0, 1, 1, Qt.AlignHCenter)

        self.countingMethodSwitcher.addWidget(self.vectorPage)
        self.finishLinePage = QWidget()
        self.finishLinePage.setObjectName(u"finishLinePage")
        self.gridLayout_4 = QGridLayout(self.finishLinePage)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.finishLineFramesSpn = QSpinBox(self.finishLinePage)
        self.finishLineFramesSpn.setObjectName(u"finishLineFramesSpn")
        self.finishLineFramesSpn.setMaximum(200)
        self.finishLineFramesSpn.setValue(5)

        self.gridLayout_4.addWidget(self.finishLineFramesSpn, 0, 1, 1, 1)

        self.finishLineChk = QCheckBox(self.finishLinePage)
        self.finishLineChk.setObjectName(u"finishLineChk")

        self.gridLayout_4.addWidget(self.finishLineChk, 1, 0, 1, 1)

        self.label_18 = QLabel(self.finishLinePage)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_4.addWidget(self.label_18, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.countingMethodSwitcher.addWidget(self.finishLinePage)

        self.verticalLayout_8.addWidget(self.countingMethodSwitcher)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.countAnalyzeBtn = QPushButton(self.countingGBox)
        self.countAnalyzeBtn.setObjectName(u"countAnalyzeBtn")

        self.horizontalLayout_6.addWidget(self.countAnalyzeBtn)

        self.countBtn = QPushButton(self.countingGBox)
        self.countBtn.setObjectName(u"countBtn")

        self.horizontalLayout_6.addWidget(self.countBtn)


        self.verticalLayout_8.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_2.addWidget(self.countingGBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2.setStretch(0, 1)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, -1, -1, -1)
        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setEnabled(True)
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_8 = QLabel(self.widget_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 1, 0, 1, 1)

        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1, Qt.AlignHCenter)

        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy3.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1, Qt.AlignHCenter)

        self.label_15 = QLabel(self.widget_2)
        self.label_15.setObjectName(u"label_15")
        sizePolicy3.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.label_15, 0, 3, 1, 1, Qt.AlignHCenter)

        self.carCount = QLCDNumber(self.widget_2)
        self.carCount.setObjectName(u"carCount")
        self.carCount.setLineWidth(0)
        self.carCount.setDigitCount(3)
        self.carCount.setSegmentStyle(QLCDNumber.Flat)
        self.carCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.carCount, 1, 2, 1, 1)

        self.busCount = QLCDNumber(self.widget_2)
        self.busCount.setObjectName(u"busCount")
        self.busCount.setLineWidth(0)
        self.busCount.setDigitCount(3)
        self.busCount.setSegmentStyle(QLCDNumber.Flat)
        self.busCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.busCount, 1, 3, 1, 1)

        self.SWbusCount = QLCDNumber(self.widget_2)
        self.SWbusCount.setObjectName(u"SWbusCount")
        self.SWbusCount.setLineWidth(0)
        self.SWbusCount.setDigitCount(3)
        self.SWbusCount.setSegmentStyle(QLCDNumber.Flat)
        self.SWbusCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.SWbusCount, 16, 3, 1, 1)

        self.SEcarCount = QLCDNumber(self.widget_2)
        self.SEcarCount.setObjectName(u"SEcarCount")
        self.SEcarCount.setLineWidth(0)
        self.SEcarCount.setDigitCount(3)
        self.SEcarCount.setSegmentStyle(QLCDNumber.Flat)
        self.SEcarCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.SEcarCount, 15, 2, 1, 1)

        self.SEtruckCount = QLCDNumber(self.widget_2)
        self.SEtruckCount.setObjectName(u"SEtruckCount")
        self.SEtruckCount.setLineWidth(0)
        self.SEtruckCount.setDigitCount(3)
        self.SEtruckCount.setSegmentStyle(QLCDNumber.Flat)
        self.SEtruckCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.SEtruckCount, 15, 1, 1, 1)

        self.SEbusCount = QLCDNumber(self.widget_2)
        self.SEbusCount.setObjectName(u"SEbusCount")
        self.SEbusCount.setLineWidth(0)
        self.SEbusCount.setDigitCount(3)
        self.SEbusCount.setSegmentStyle(QLCDNumber.Flat)
        self.SEbusCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.SEbusCount, 15, 3, 1, 1)

        self.SWcarCount = QLCDNumber(self.widget_2)
        self.SWcarCount.setObjectName(u"SWcarCount")
        self.SWcarCount.setLineWidth(0)
        self.SWcarCount.setDigitCount(3)
        self.SWcarCount.setSegmentStyle(QLCDNumber.Flat)
        self.SWcarCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.SWcarCount, 16, 2, 1, 1)

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

        self.gridLayout.addWidget(self.SSbusCount, 17, 3, 1, 1)

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

        self.gridLayout.addWidget(self.SScarCount, 17, 2, 1, 1)

        self.truckCount = QLCDNumber(self.widget_2)
        self.truckCount.setObjectName(u"truckCount")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.truckCount.sizePolicy().hasHeightForWidth())
        self.truckCount.setSizePolicy(sizePolicy4)
        self.truckCount.setLineWidth(0)
        self.truckCount.setDigitCount(3)
        self.truckCount.setSegmentStyle(QLCDNumber.Flat)
        self.truckCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.truckCount, 1, 1, 1, 1)

        self.label_24 = QLabel(self.widget_2)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout.addWidget(self.label_24, 11, 0, 1, 1)

        self.label_22 = QLabel(self.widget_2)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout.addWidget(self.label_22, 5, 0, 1, 1)

        self.label_20 = QLabel(self.widget_2)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout.addWidget(self.label_20, 3, 0, 1, 1)

        self.label_21 = QLabel(self.widget_2)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout.addWidget(self.label_21, 2, 0, 1, 1)

        self.label_23 = QLabel(self.widget_2)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout.addWidget(self.label_23, 10, 0, 1, 1)

        self.label_25 = QLabel(self.widget_2)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout.addWidget(self.label_25, 12, 0, 1, 1)

        self.label_26 = QLabel(self.widget_2)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout.addWidget(self.label_26, 13, 0, 1, 1)

        self.label_31 = QLabel(self.widget_2)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout.addWidget(self.label_31, 14, 0, 1, 1)

        self.label_29 = QLabel(self.widget_2)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout.addWidget(self.label_29, 8, 0, 1, 1)

        self.label_28 = QLabel(self.widget_2)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout.addWidget(self.label_28, 7, 0, 1, 1)

        self.NEtruckCount = QLCDNumber(self.widget_2)
        self.NEtruckCount.setObjectName(u"NEtruckCount")
        self.NEtruckCount.setLineWidth(0)
        self.NEtruckCount.setDigitCount(3)
        self.NEtruckCount.setSegmentStyle(QLCDNumber.Flat)
        self.NEtruckCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.NEtruckCount, 2, 1, 1, 1)

        self.label_27 = QLabel(self.widget_2)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout.addWidget(self.label_27, 6, 0, 1, 1)

        self.label_30 = QLabel(self.widget_2)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout.addWidget(self.label_30, 9, 0, 1, 1)

        self.label_32 = QLabel(self.widget_2)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout.addWidget(self.label_32, 15, 0, 1, 1)

        self.NEbusCount = QLCDNumber(self.widget_2)
        self.NEbusCount.setObjectName(u"NEbusCount")
        self.NEbusCount.setLineWidth(0)
        self.NEbusCount.setDigitCount(3)
        self.NEbusCount.setSegmentStyle(QLCDNumber.Flat)
        self.NEbusCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.NEbusCount, 2, 3, 1, 1)

        self.NEcarCount = QLCDNumber(self.widget_2)
        self.NEcarCount.setObjectName(u"NEcarCount")
        self.NEcarCount.setLineWidth(0)
        self.NEcarCount.setDigitCount(3)
        self.NEcarCount.setSegmentStyle(QLCDNumber.Flat)
        self.NEcarCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.NEcarCount, 2, 2, 1, 1)

        self.label_34 = QLabel(self.widget_2)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout.addWidget(self.label_34, 17, 0, 1, 1)

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

        self.gridLayout.addWidget(self.NWcarCount, 3, 2, 1, 1)

        self.NWbusCount = QLCDNumber(self.widget_2)
        self.NWbusCount.setObjectName(u"NWbusCount")
        self.NWbusCount.setLineWidth(0)
        self.NWbusCount.setDigitCount(3)
        self.NWbusCount.setSegmentStyle(QLCDNumber.Flat)
        self.NWbusCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.NWbusCount, 3, 3, 1, 1)

        self.NStruckCount = QLCDNumber(self.widget_2)
        self.NStruckCount.setObjectName(u"NStruckCount")
        self.NStruckCount.setLineWidth(0)
        self.NStruckCount.setDigitCount(3)
        self.NStruckCount.setSegmentStyle(QLCDNumber.Flat)
        self.NStruckCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.NStruckCount, 5, 1, 1, 1)

        self.NScarCount = QLCDNumber(self.widget_2)
        self.NScarCount.setObjectName(u"NScarCount")
        self.NScarCount.setLineWidth(0)
        self.NScarCount.setDigitCount(3)
        self.NScarCount.setSegmentStyle(QLCDNumber.Flat)
        self.NScarCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.NScarCount, 5, 2, 1, 1)

        self.NSbusCount = QLCDNumber(self.widget_2)
        self.NSbusCount.setObjectName(u"NSbusCount")
        self.NSbusCount.setLineWidth(0)
        self.NSbusCount.setDigitCount(3)
        self.NSbusCount.setSegmentStyle(QLCDNumber.Flat)
        self.NSbusCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.NSbusCount, 5, 3, 1, 1)

        self.EEcarCount = QLCDNumber(self.widget_2)
        self.EEcarCount.setObjectName(u"EEcarCount")
        self.EEcarCount.setLineWidth(0)
        self.EEcarCount.setDigitCount(3)
        self.EEcarCount.setSegmentStyle(QLCDNumber.Flat)
        self.EEcarCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.EEcarCount, 7, 2, 1, 1)

        self.ENcarCount = QLCDNumber(self.widget_2)
        self.ENcarCount.setObjectName(u"ENcarCount")
        self.ENcarCount.setLineWidth(0)
        self.ENcarCount.setDigitCount(3)
        self.ENcarCount.setSegmentStyle(QLCDNumber.Flat)
        self.ENcarCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.ENcarCount, 6, 2, 1, 1)

        self.ENbusCount = QLCDNumber(self.widget_2)
        self.ENbusCount.setObjectName(u"ENbusCount")
        self.ENbusCount.setLineWidth(0)
        self.ENbusCount.setDigitCount(3)
        self.ENbusCount.setSegmentStyle(QLCDNumber.Flat)
        self.ENbusCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.ENbusCount, 6, 3, 1, 1)

        self.EEtruckCount = QLCDNumber(self.widget_2)
        self.EEtruckCount.setObjectName(u"EEtruckCount")
        self.EEtruckCount.setLineWidth(0)
        self.EEtruckCount.setDigitCount(3)
        self.EEtruckCount.setSegmentStyle(QLCDNumber.Flat)
        self.EEtruckCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.EEtruckCount, 7, 1, 1, 1)

        self.ENtruckCount = QLCDNumber(self.widget_2)
        self.ENtruckCount.setObjectName(u"ENtruckCount")
        self.ENtruckCount.setLineWidth(0)
        self.ENtruckCount.setDigitCount(3)
        self.ENtruckCount.setSegmentStyle(QLCDNumber.Flat)
        self.ENtruckCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.ENtruckCount, 6, 1, 1, 1)

        self.EEbusCount = QLCDNumber(self.widget_2)
        self.EEbusCount.setObjectName(u"EEbusCount")
        self.EEbusCount.setLineWidth(0)
        self.EEbusCount.setDigitCount(3)
        self.EEbusCount.setSegmentStyle(QLCDNumber.Flat)
        self.EEbusCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.EEbusCount, 7, 3, 1, 1)

        self.EWcarCount = QLCDNumber(self.widget_2)
        self.EWcarCount.setObjectName(u"EWcarCount")
        self.EWcarCount.setLineWidth(0)
        self.EWcarCount.setDigitCount(3)
        self.EWcarCount.setSegmentStyle(QLCDNumber.Flat)
        self.EWcarCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.EWcarCount, 8, 2, 1, 1)

        self.EWtruckCount = QLCDNumber(self.widget_2)
        self.EWtruckCount.setObjectName(u"EWtruckCount")
        self.EWtruckCount.setLineWidth(0)
        self.EWtruckCount.setDigitCount(3)
        self.EWtruckCount.setSegmentStyle(QLCDNumber.Flat)
        self.EWtruckCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.EWtruckCount, 8, 1, 1, 1)

        self.EScarCount = QLCDNumber(self.widget_2)
        self.EScarCount.setObjectName(u"EScarCount")
        self.EScarCount.setLineWidth(0)
        self.EScarCount.setDigitCount(3)
        self.EScarCount.setSegmentStyle(QLCDNumber.Flat)
        self.EScarCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.EScarCount, 9, 2, 1, 1)

        self.EWbusCount = QLCDNumber(self.widget_2)
        self.EWbusCount.setObjectName(u"EWbusCount")
        self.EWbusCount.setLineWidth(0)
        self.EWbusCount.setDigitCount(3)
        self.EWbusCount.setSegmentStyle(QLCDNumber.Flat)
        self.EWbusCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.EWbusCount, 8, 3, 1, 1)

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

        self.gridLayout.addWidget(self.WNbusCount, 10, 3, 1, 1)

        self.WWtruckCount = QLCDNumber(self.widget_2)
        self.WWtruckCount.setObjectName(u"WWtruckCount")
        self.WWtruckCount.setLineWidth(0)
        self.WWtruckCount.setDigitCount(3)
        self.WWtruckCount.setSegmentStyle(QLCDNumber.Flat)
        self.WWtruckCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.WWtruckCount, 11, 1, 1, 1)

        self.WWcarCount = QLCDNumber(self.widget_2)
        self.WWcarCount.setObjectName(u"WWcarCount")
        self.WWcarCount.setLineWidth(0)
        self.WWcarCount.setDigitCount(3)
        self.WWcarCount.setSegmentStyle(QLCDNumber.Flat)
        self.WWcarCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.WWcarCount, 11, 2, 1, 1)

        self.ESbusCount = QLCDNumber(self.widget_2)
        self.ESbusCount.setObjectName(u"ESbusCount")
        self.ESbusCount.setLineWidth(0)
        self.ESbusCount.setDigitCount(3)
        self.ESbusCount.setSegmentStyle(QLCDNumber.Flat)
        self.ESbusCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.ESbusCount, 9, 3, 1, 1)

        self.WNtruckCount = QLCDNumber(self.widget_2)
        self.WNtruckCount.setObjectName(u"WNtruckCount")
        self.WNtruckCount.setLineWidth(0)
        self.WNtruckCount.setDigitCount(3)
        self.WNtruckCount.setSegmentStyle(QLCDNumber.Flat)
        self.WNtruckCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.WNtruckCount, 10, 1, 1, 1)

        self.WNcarCount = QLCDNumber(self.widget_2)
        self.WNcarCount.setObjectName(u"WNcarCount")
        self.WNcarCount.setLineWidth(0)
        self.WNcarCount.setDigitCount(3)
        self.WNcarCount.setSegmentStyle(QLCDNumber.Flat)
        self.WNcarCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.WNcarCount, 10, 2, 1, 1)

        self.WEtruckCount = QLCDNumber(self.widget_2)
        self.WEtruckCount.setObjectName(u"WEtruckCount")
        self.WEtruckCount.setLineWidth(0)
        self.WEtruckCount.setDigitCount(3)
        self.WEtruckCount.setSegmentStyle(QLCDNumber.Flat)
        self.WEtruckCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.WEtruckCount, 12, 1, 1, 1)

        self.WWbusCount = QLCDNumber(self.widget_2)
        self.WWbusCount.setObjectName(u"WWbusCount")
        self.WWbusCount.setLineWidth(0)
        self.WWbusCount.setDigitCount(3)
        self.WWbusCount.setSegmentStyle(QLCDNumber.Flat)
        self.WWbusCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.WWbusCount, 11, 3, 1, 1)

        self.WEcarCount = QLCDNumber(self.widget_2)
        self.WEcarCount.setObjectName(u"WEcarCount")
        self.WEcarCount.setLineWidth(0)
        self.WEcarCount.setDigitCount(3)
        self.WEcarCount.setSegmentStyle(QLCDNumber.Flat)
        self.WEcarCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.WEcarCount, 12, 2, 1, 1)

        self.WStruckCount = QLCDNumber(self.widget_2)
        self.WStruckCount.setObjectName(u"WStruckCount")
        self.WStruckCount.setLineWidth(0)
        self.WStruckCount.setDigitCount(3)
        self.WStruckCount.setSegmentStyle(QLCDNumber.Flat)
        self.WStruckCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.WStruckCount, 13, 1, 1, 1)

        self.WEbusCount = QLCDNumber(self.widget_2)
        self.WEbusCount.setObjectName(u"WEbusCount")
        self.WEbusCount.setLineWidth(0)
        self.WEbusCount.setDigitCount(3)
        self.WEbusCount.setSegmentStyle(QLCDNumber.Flat)
        self.WEbusCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.WEbusCount, 12, 3, 1, 1)

        self.WScarCount = QLCDNumber(self.widget_2)
        self.WScarCount.setObjectName(u"WScarCount")
        self.WScarCount.setLineWidth(0)
        self.WScarCount.setDigitCount(3)
        self.WScarCount.setSegmentStyle(QLCDNumber.Flat)
        self.WScarCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.WScarCount, 13, 2, 1, 1)

        self.WSbusCount = QLCDNumber(self.widget_2)
        self.WSbusCount.setObjectName(u"WSbusCount")
        self.WSbusCount.setLineWidth(0)
        self.WSbusCount.setDigitCount(3)
        self.WSbusCount.setSegmentStyle(QLCDNumber.Flat)
        self.WSbusCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.WSbusCount, 13, 3, 1, 1)

        self.SNbusCount = QLCDNumber(self.widget_2)
        self.SNbusCount.setObjectName(u"SNbusCount")
        self.SNbusCount.setLineWidth(0)
        self.SNbusCount.setDigitCount(3)
        self.SNbusCount.setSegmentStyle(QLCDNumber.Flat)
        self.SNbusCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.SNbusCount, 14, 3, 1, 1)

        self.SNcarCount = QLCDNumber(self.widget_2)
        self.SNcarCount.setObjectName(u"SNcarCount")
        self.SNcarCount.setLineWidth(0)
        self.SNcarCount.setDigitCount(3)
        self.SNcarCount.setSegmentStyle(QLCDNumber.Flat)
        self.SNcarCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.SNcarCount, 14, 2, 1, 1)

        self.SNtruckCount = QLCDNumber(self.widget_2)
        self.SNtruckCount.setObjectName(u"SNtruckCount")
        self.SNtruckCount.setLineWidth(0)
        self.SNtruckCount.setDigitCount(3)
        self.SNtruckCount.setSegmentStyle(QLCDNumber.Flat)
        self.SNtruckCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.SNtruckCount, 14, 1, 1, 1)


        self.verticalLayout.addWidget(self.widget_2)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.previewTabWidget = QTabWidget(Form)
        self.previewTabWidget.setObjectName(u"previewTabWidget")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.previewTabWidget.sizePolicy().hasHeightForWidth())
        self.previewTabWidget.setSizePolicy(sizePolicy5)
        self.previewTabWidget.setMinimumSize(QSize(220, 0))
        self.truckPreviewTab = QWidget()
        self.truckPreviewTab.setObjectName(u"truckPreviewTab")
        self.verticalLayout_5 = QVBoxLayout(self.truckPreviewTab)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.truckPreviewTable = QTableWidget(self.truckPreviewTab)
        if (self.truckPreviewTable.columnCount() < 2):
            self.truckPreviewTable.setColumnCount(2)
        if (self.truckPreviewTable.rowCount() < 30):
            self.truckPreviewTable.setRowCount(30)
        self.truckPreviewTable.setObjectName(u"truckPreviewTable")
        self.truckPreviewTable.setRowCount(30)
        self.truckPreviewTable.setColumnCount(2)
        self.truckPreviewTable.horizontalHeader().setVisible(True)
        self.truckPreviewTable.horizontalHeader().setMinimumSectionSize(110)
        self.truckPreviewTable.horizontalHeader().setDefaultSectionSize(110)
        self.truckPreviewTable.verticalHeader().setMinimumSectionSize(110)
        self.truckPreviewTable.verticalHeader().setDefaultSectionSize(110)

        self.verticalLayout_5.addWidget(self.truckPreviewTable)

        self.previewTabWidget.addTab(self.truckPreviewTab, "")
        self.carPreviewTab = QWidget()
        self.carPreviewTab.setObjectName(u"carPreviewTab")
        self.verticalLayout_6 = QVBoxLayout(self.carPreviewTab)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.carPreviewTable = QTableWidget(self.carPreviewTab)
        if (self.carPreviewTable.columnCount() < 2):
            self.carPreviewTable.setColumnCount(2)
        if (self.carPreviewTable.rowCount() < 30):
            self.carPreviewTable.setRowCount(30)
        self.carPreviewTable.setObjectName(u"carPreviewTable")
        self.carPreviewTable.setShowGrid(True)
        self.carPreviewTable.setGridStyle(Qt.SolidLine)
        self.carPreviewTable.setRowCount(30)
        self.carPreviewTable.setColumnCount(2)
        self.carPreviewTable.horizontalHeader().setMinimumSectionSize(110)
        self.carPreviewTable.horizontalHeader().setDefaultSectionSize(110)
        self.carPreviewTable.verticalHeader().setMinimumSectionSize(110)
        self.carPreviewTable.verticalHeader().setDefaultSectionSize(110)

        self.verticalLayout_6.addWidget(self.carPreviewTable)

        self.previewTabWidget.addTab(self.carPreviewTab, "")
        self.busPreviewTab = QWidget()
        self.busPreviewTab.setObjectName(u"busPreviewTab")
        self.verticalLayout_7 = QVBoxLayout(self.busPreviewTab)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.busPreviewTable = QTableWidget(self.busPreviewTab)
        if (self.busPreviewTable.columnCount() < 2):
            self.busPreviewTable.setColumnCount(2)
        if (self.busPreviewTable.rowCount() < 30):
            self.busPreviewTable.setRowCount(30)
        self.busPreviewTable.setObjectName(u"busPreviewTable")
        self.busPreviewTable.setShowGrid(True)
        self.busPreviewTable.setGridStyle(Qt.SolidLine)
        self.busPreviewTable.setRowCount(30)
        self.busPreviewTable.setColumnCount(2)
        self.busPreviewTable.horizontalHeader().setMinimumSectionSize(110)
        self.busPreviewTable.horizontalHeader().setDefaultSectionSize(110)
        self.busPreviewTable.verticalHeader().setMinimumSectionSize(110)
        self.busPreviewTable.verticalHeader().setDefaultSectionSize(110)

        self.verticalLayout_7.addWidget(self.busPreviewTable)

        self.previewTabWidget.addTab(self.busPreviewTab, "")

        self.verticalLayout.addWidget(self.previewTabWidget)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(Form)
        self.visualizeChk.toggled.connect(self.xFilterVectorSpn.setEnabled)
        self.visualizeChk.toggled.connect(self.widthFilterVectorSpn.setEnabled)
        self.visualizeChk.toggled.connect(self.distFilterSpn.setEnabled)
        self.visualizeChk.toggled.connect(self.yFilterVectorSpn.setEnabled)

        self.countMethodCmb.setCurrentIndex(1)
        self.countingMethodSwitcher.setCurrentIndex(1)
        self.previewTabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Traffic Vehicle Counter", None))
        self.videoSwitcher.setTitle(QCoreApplication.translate("Form", u"Video", None))
        self.stopProcessBtn.setText(QCoreApplication.translate("Form", u"STOP", None))
        self.frameNum.setText(QCoreApplication.translate("Form", u"0", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"/", None))
        self.maxFrameNum.setText(QCoreApplication.translate("Form", u"N", None))
        self.mediaGBox.setTitle(QCoreApplication.translate("Form", u"Media", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Input Video:", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Model Path:", None))
        self.loadVideoBtn.setText(QCoreApplication.translate("Form", u"...", None))
        self.loadCacheBtn.setText(QCoreApplication.translate("Form", u"...", None))
        self.maskingGBox.setTitle(QCoreApplication.translate("Form", u"Masking", None))
        self.saveMaskBtn.setText(QCoreApplication.translate("Form", u"Save", None))
        self.resetMaskBtn.setText(QCoreApplication.translate("Form", u"Reset", None))
        self.drawMaskBtn.setText(QCoreApplication.translate("Form", u"Draw", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"Mask File:", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"Stroke Size:", None))
        self.setMaskFileBtn.setText(QCoreApplication.translate("Form", u"...", None))
        self.inferenceGBox.setTitle(QCoreApplication.translate("Form", u"Inference", None))
        self.modelLabel.setText(QCoreApplication.translate("Form", u"Model: ", None))
        self.modelComboBox.setItemText(0, QCoreApplication.translate("Form", u"YoloV4", None))

        self.iOUThresholdLabel_2.setText(QCoreApplication.translate("Form", u"Cosine Distance:", None))
        self.iOUThresholdLabel.setText(QCoreApplication.translate("Form", u"IOU Threshold:", None))
        self.confidenceThresholdLabel.setText(QCoreApplication.translate("Form", u"Score Threshold", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Output File:", None))
        self.setOutputFileBtn.setText(QCoreApplication.translate("Form", u"...", None))
        self.startInferenceBtn.setText(QCoreApplication.translate("Form", u"START", None))
        self.countingGBox.setTitle(QCoreApplication.translate("Form", u"Counting", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Method:", None))
        self.countMethodCmb.setItemText(0, QCoreApplication.translate("Form", u"Vector", None))
        self.countMethodCmb.setItemText(1, QCoreApplication.translate("Form", u"Finish Line", None))

        self.countMethodCmb.setCurrentText(QCoreApplication.translate("Form", u"Finish Line", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Y:", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Travel Distance (pixels)", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"Filter Vector Width", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"X:", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Max Skipped Frames", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Filter Vector (pixels)", None))
        self.visualizeChk.setText(QCoreApplication.translate("Form", u"Show Vector", None))
        self.vectorDirectionLbl.setText(QCoreApplication.translate("Form", u"DOWN", None))
        self.finishLineChk.setText(QCoreApplication.translate("Form", u"Show Finish Line", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"frames to count:", None))
        self.countAnalyzeBtn.setText(QCoreApplication.translate("Form", u"Count + Analyze", None))
        self.countBtn.setText(QCoreApplication.translate("Form", u"Quick Count", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"NN", None))
        self.label.setText(QCoreApplication.translate("Form", u"Trucks", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Cars", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Bus", None))
        self.label_24.setText(QCoreApplication.translate("Form", u"WW", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"NS", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"NW", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"NE", None))
        self.label_23.setText(QCoreApplication.translate("Form", u"WN", None))
        self.label_25.setText(QCoreApplication.translate("Form", u"WE", None))
        self.label_26.setText(QCoreApplication.translate("Form", u"WS", None))
        self.label_31.setText(QCoreApplication.translate("Form", u"SN", None))
        self.label_29.setText(QCoreApplication.translate("Form", u"EW", None))
        self.label_28.setText(QCoreApplication.translate("Form", u"EE", None))
        self.label_27.setText(QCoreApplication.translate("Form", u"EN", None))
        self.label_30.setText(QCoreApplication.translate("Form", u"ES", None))
        self.label_32.setText(QCoreApplication.translate("Form", u"SE", None))
        self.label_34.setText(QCoreApplication.translate("Form", u"SS", None))
        self.label_33.setText(QCoreApplication.translate("Form", u"SW", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Detections", None))
        self.previewTabWidget.setTabText(self.previewTabWidget.indexOf(self.truckPreviewTab), QCoreApplication.translate("Form", u"Trucks", None))
        self.previewTabWidget.setTabText(self.previewTabWidget.indexOf(self.carPreviewTab), QCoreApplication.translate("Form", u"Cars", None))
        self.previewTabWidget.setTabText(self.previewTabWidget.indexOf(self.busPreviewTab), QCoreApplication.translate("Form", u"Bus", None))
    # retranslateUi

