# Shakh)
import sys
from PySide2 import QtWidgets
from PySide2.QtCore import Signal
from qt.RemoveCameraUI import Ui_MainWindow
from DrawLineWidget import DrawLineWidget
from PySide2.QtWidgets import QMessageBox
from yolov5.utils.dataloaders import LoadHikvisionCamera


class RemoveCameraWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    process_done_signal = Signal()
    def __init__(self, db_conn, db_cur):
        super(RemoveCameraWindow, self).__init__()
        self.db_conn = db_conn
        self.db_cur = db_cur
        self.remove_cam_id = -1
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
        msg.setWindowTitle('Ogohlantirish!')
        msg.setText(f'{self.remove_cam_id} id ga ega bo\'lgan kamera bazadan o\'chirildi')
        msg.setIcon(QMessageBox.Information)

        x = msg.exec_()

        self.process_done_signal.emit()
        self.hide()