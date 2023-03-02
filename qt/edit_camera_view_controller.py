# Shakh)
import sys
from PySide2 import QtWidgets
from PySide2.QtGui import QIcon
from qt.EditCameraUI import Ui_MainWindow
from DrawLineWidget import DrawLineWidget
from PySide2.QtWidgets import QMessageBox, QAction
from PySide2.QtCore import Signal, QCoreApplication
from yolov5.utils.dataloaders import LoadHikvisionCamera


class EditCameraWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    process_done_signal = Signal()
    def __init__(self, db_conn, db_cur, icon_path, text_translator):
        super(EditCameraWindow, self).__init__()
        self.db_conn = db_conn
        self.db_cur = db_cur
        self.icon_path = icon_path
        self.text_translator = text_translator
        self.aboutToQuit = QAction("Quit", self)
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
    
    def closeEvent(self, event):
        self.process_done_signal.emit()
        event.accept()

    def setupSignalSlots(self):
        self.editCamBtn.clicked.connect(self.edit_cam)
        self.camerasList.activated[str].connect(self.onActivated)
        self.aboutToQuit.triggered.connect(self.closeEvent)
    
    def onActivated(self, text):
        cam_id = text.split('.')[0]
        self.edit_cam_id = cam_id
        self.setCameraInfos()
    
    def setCameraInfos(self):
        self.db_cur.execute(f"SELECT * FROM cameras WHERE id = {self.edit_cam_id}")
        camera_info = self.db_cur.fetchall()[0]
        self.db_conn.commit()
        # print('camera info ', camera_info)
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
        msg.setWindowTitle('Warning!')
        msg.setWindowIcon(QIcon(self.icon_path))
        msg.setText(f'Camera with {self.edit_cam_id} id changed on database')
        msg.setIcon(QMessageBox.Information)

        x = msg.exec_()

        self.process_done_signal.emit()
        self.hide()
    
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Edit Camera", None))
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
