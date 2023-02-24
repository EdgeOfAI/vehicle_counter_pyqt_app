# Shakh)
import sys
from PySide2 import QtWidgets
from PySide2.QtGui import QIcon
from PySide2.QtCore import Signal
from qt.RemoveCameraUI import Ui_MainWindow
from DrawLineWidget import DrawLineWidget
from PySide2.QtWidgets import QMessageBox, QAction
from yolov5.utils.dataloaders import LoadHikvisionCamera


class RemoveCameraWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    process_done_signal = Signal()
    def __init__(self, db_conn, db_cur, icon_path):
        super(RemoveCameraWindow, self).__init__()
        self.db_conn = db_conn
        self.db_cur = db_cur
        self.icon_path = icon_path
        self.remove_cam_id = -1
        self.aboutToQuit = QAction("Quit", self)
        self.setupUi(self)
        # self.show()
        self.db_cur.execute(f"SELECT * FROM cameras")
        cameras = self.db_cur.fetchall()
        camera_names = [row[4] for row in cameras]
        self.comboBox.clear()
        self.comboBox.addItems(camera_names)
        self.db_conn.commit()
        self.setupSignalSlots()
    
    def setCamId(self, cam_id):
        self.remove_cam_id = cam_id
    
    def closeEvent(self, event):
        self.process_done_signal.emit()
        event.accept()

    def set_db_conn_cur(self, db_conn, db_cur):
        self.db_conn = db_conn
        self.db_cur = db_cur
        self.db_cur.execute(f"SELECT * FROM cameras")
        cameras = self.db_cur.fetchall()
        camera_names = [row[4] for row in cameras]
        self.comboBox.clear()
        self.comboBox.addItems(camera_names)
        self.db_conn.commit()

    def setupSignalSlots(self):
        self.addCamBtn.clicked.connect(self.remove_cam)
        self.comboBox.activated[str].connect(self.onActivated)
        self.aboutToQuit.triggered.connect(self.closeEvent)
    
    def onActivated(self, text):
        cam_id = text.split('.')[0]
        self.remove_cam_id = cam_id

    def remove_cam(self):
        # self.inputCamIP.text()
        # self.inputCamUsername.text()
        # self.inputCamPassword.text()
        # self.inputCamDisplayName.text()
        self.db_cur.execute(f"DELETE FROM cameras where id = {self.remove_cam_id}")

        msg = QMessageBox()
        msg.setWindowTitle('Warning!')
        msg.setWindowIcon(QIcon(self.icon_path))
        msg.setText(f'Camera with {self.remove_cam_id} id removed from database')
        msg.setIcon(QMessageBox.Information)

        x = msg.exec_()

        self.process_done_signal.emit()
        self.hide()
