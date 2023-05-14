import sys
from PySide2.QtGui import QIcon
from qt.Set_Distances import Ui_MainWindow
from PySide2.QtCore import Signal, QCoreApplication
from PySide2.QtWidgets import QMessageBox, QAction, QMainWindow


class SetDistanceWindow(QMainWindow, Ui_MainWindow):
    process_done_signal = Signal(int, list)
    def __init__(self, icon_path, text_translator, cam_id):
        super(SetDistanceWindow, self).__init__()
        self.distances = None 

        self.cam_id = cam_id
        self.icon_path = icon_path
        self.text_translator = text_translator
        self.setupUi(self)
        # self.show()
        self.setupSignalSlots()

    def setupSignalSlots(self):
        self.pushButton.clicked.connect(self.onOkButtonClick)
    
    def setDistances(self):
        aa = self.spinBox.value()
        ab = self.spinBox_2.value()
        ac = self.spinBox_3.value()
        ad = self.spinBox_4.value()
        ba = self.spinBox_5.value()
        bb = self.spinBox_6.value()
        bc = self.spinBox_7.value()
        bd = self.spinBox_8.value()
        ca = self.spinBox_9.value()
        cb = self.spinBox_10.value()
        cc = self.spinBox_11.value()
        cd = self.spinBox_12.value()
        da = self.spinBox_13.value()
        db = self.spinBox_14.value()
        dc = self.spinBox_15.value()
        dd = self.spinBox_16.value()
        self.distances = [aa, ab, ac, ad, ba, bb, bc, bd, ca, cb, cc, cd, da, db, dc, dd]
    
    def closeEvent(self, event):
        self.setDistances()
        self.process_done_signal.emit(int(self.cam_id), self.distances)
        event.accept()
    
    def onOkButtonClick(self):
        self.setDistances()
        self.process_done_signal.emit(self.cam_id, self.distances)
        self.hide()
    
    # def retranslateUi(self, MainWindow):
    #     MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", self.text_translator.remove_camera_window_title, None))
    #     self.label_2.setText(QCoreApplication.translate("MainWindow", self.text_translator.remove_camera_window_camera_names, None))
    #     self.addCamBtn.setText(QCoreApplication.translate("MainWindow", self.text_translator.remove_camera_window_remove_camera, None))
