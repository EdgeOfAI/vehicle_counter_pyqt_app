# Shakh)
import sys
from PySide2 import QtWidgets
from PySide2.QtCore import Signal
from qt.EditCameraUI import Ui_MainWindow
from DrawLineWidget import DrawLineWidget
from PySide2.QtWidgets import QMessageBox
from yolov5.utils.dataloaders import LoadHikvisionCamera


class EditCameraWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    process_done_signal = Signal()
    def __init__(self, db_conn, db_cur):
        super(EditCameraWindow, self).__init__()
        self.db_conn = db_conn
        self.db_cur = db_cur
        self.setupUi(self)
        # self.show()
        self.db_cur.execute(f"SELECT * FROM cameras")
        cameras = self.db_cur.fetchall()
        camera_names = [row[4] for row in cameras]
        self.camerasList.clear()
        self.camerasList.addItems(camera_names)
        self.db_conn.commit()
        # if cameras:
        #     self.edit_cam_id = cameras[0][0]
        #     self.setCameraInfos()
        # else:
        self.edit_cam_id = -1
        self.setupSignalSlots()
    
    def setCamId(self, cam_id):
        self.edit_cam_id = cam_id

    def set_db_conn_cur(self, db_conn, db_cur):
        self.db_conn = db_conn
        self.db_cur = db_cur
        self.db_cur.execute(f"SELECT * FROM cameras")
        cameras = self.db_cur.fetchall()
        camera_names = [row[4] for row in cameras]
        self.camerasList.clear()
        self.camerasList.addItems(camera_names)
        self.db_conn.commit()

    def setupSignalSlots(self):
        self.editCamBtn.clicked.connect(self.edit_cam)
        self.camerasList.activated[str].connect(self.onActivated)
    
    def onActivated(self, text):
        cam_id = text.split('.')[0]
        self.edit_cam_id = cam_id
        self.setCameraInfos()
    
    def setCameraInfos(self):
        self.db_cur.execute(f"SELECT * FROM cameras WHERE id = {self.edit_cam_id}")
        camera_info = self.db_cur.fetchall()[0]
        self.db_conn.commit()
        print('camera info ', camera_info)
        if camera_info:
            self.inputCamIP.setText(camera_info[1])
            self.inputCamUsername.setText(camera_info[2])
            self.inputCamPassword.setText(camera_info[3])
            self.inputCamDisplayName.setText(str(camera_info[4]))
            self.Nx1.setText(str(camera_info[5]))
            self.Ny1.setText(str(camera_info[6]))
            self.Nx2.setText(str(camera_info[7]))
            self.Ny2.setText(str(camera_info[8]))
            self.Ex1.setText(str(camera_info[9]))
            self.Ey1.setText(str(camera_info[10]))
            self.Ex2.setText(str(camera_info[11]))
            self.Ey2.setText(str(camera_info[12]))
            self.Wx1.setText(str(camera_info[13]))
            self.Wy1.setText(str(camera_info[14]))
            self.Wx2.setText(str(camera_info[15]))
            self.Wy2.setText(str(camera_info[16]))
            self.Sx1.setText(str(camera_info[17]))
            self.Sy1.setText(str(camera_info[18]))
            self.Sx2.setText(str(camera_info[19]))
            self.Sy2.setText(str(camera_info[20]))

    def edit_cam(self):
        # self.inputCamIP.text()
        # self.inputCamUsername.text()
        # self.inputCamPassword.text()
        # self.inputCamDisplayName.text()
        self.db_cur.execute(f"""UPDATE cameras SET  
                    ip = '{self.inputCamIP.text()}', 
                    username = '{self.inputCamUsername.text()}',
                    password = '{self.inputCamPassword.text()}',
                    name = '{self.inputCamDisplayName.text()}',
                    nx1 = {self.Nx1.text()},
                    ny1 = {self.Ny1.text()},
                    nx2 = {self.Nx2.text()},
                    ny2 = {self.Ny2.text()},
                    ex1 = {self.Ex1.text()},
                    ey1 = {self.Ey1.text()},
                    ex2 = {self.Ex2.text()},
                    ey2 = {self.Ey2.text()},
                    wx1 = {self.Wx1.text()},
                    wy1 = {self.Wy1.text()},
                    wx2 = {self.Wx2.text()},
                    wy2 = {self.Wy2.text()},
                    sx1 = {self.Sx1.text()},
                    sy1 = {self.Sy1.text()},
                    sx2 = {self.Sx2.text()},
                    sy2 = {self.Sy2.text()} 
                    WHERE id={self.edit_cam_id}""")

        msg = QMessageBox()
        msg.setWindowTitle('Ogohlantirish!')
        msg.setText(f'{self.edit_cam_id} id ga ega bo\'lgan kamera bazadan o\'zgartirildi')
        msg.setIcon(QMessageBox.Information)

        x = msg.exec_()

        self.process_done_signal.emit()
        self.hide()
