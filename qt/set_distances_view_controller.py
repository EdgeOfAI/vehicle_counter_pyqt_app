import sys
from PySide2.QtGui import QIcon
from qt.Set_Distances import Ui_MainWindow
from PySide2.QtCore import Signal, QCoreApplication
from PySide2.QtWidgets import QMessageBox, QAction, QMainWindow


class SetDistanceWindow(QMainWindow, Ui_MainWindow):
    process_done_signal = Signal(list)
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
    
    def onOkButtonClick(self):
        aa = self.label.text()
        ab = self.label2.text()
        ac = self.label_3.text()
        ad = self.label_5.text()
        ba = self.label_11.text()
        bb = self.label_4.text()
        bc = self.label_9.text()
        bd = self.label_6.text()
        ca = self.label_10.text()
        cb = self.label_8.text()
        cc = self.label_16.text()
        cd = self.label_14.text()
        da = self.label_12.text()
        db = self.label_7.text()
        dc = self.label_15.text()
        dd = self.label_13.text()
        self.distances = [aa, ab, ac, ad, ba, bb, bc, bd, ca, cb, cc, cd, da, db, dc, dd]
        self.process_done_signal.emit(self.cam_id, )
    
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", self.text_translator.remove_camera_window_title, None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", self.text_translator.remove_camera_window_camera_names, None))
        self.addCamBtn.setText(QCoreApplication.translate("MainWindow", self.text_translator.remove_camera_window_remove_camera, None))
