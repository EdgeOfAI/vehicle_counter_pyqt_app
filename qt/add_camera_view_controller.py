# Shakh)
import sys
from PySide2 import QtWidgets
from PySide2.QtGui import QIcon
from PySide2.QtCore import Signal, QCoreApplication
from qt.Add_Camera import Ui_MainWindow
from DrawLineWidget import DrawLineWidget
from PySide2.QtWidgets import QMessageBox, QAction
from yolov5.utils.dataloaders import LoadHikvisionCamera


class AddCameraWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    process_done_signal = Signal()
    def __init__(self, db_conn, db_cur, icon_path, text_translator):
        super(AddCameraWindow, self).__init__()
        self.db_conn = db_conn
        self.db_cur = db_cur
        self.icon_path = icon_path
        self.aboutToQuit = QAction("Quit", self)
        self.text_translator = text_translator
        self.setupUi(self)

        self.setupSignalSlots()
    
    def setTextTranslator(self, text_translator):
        self.text_translator = text_translator
    
    def setupSignalSlots(self):
        self.addCamBtn.clicked.connect(self.add_cam)
        self.aboutToQuit.triggered.connect(self.closeEvent)
    
    def closeEvent(self, event):
        # print('Close window pressed')
        self.process_done_signal.emit()
        event.accept()
    
    def clearInputs(self):
        self.inputCamIP.clear()
        self.inputCamUsername.clear()
        self.inputCamPassword.clear()
        self.inputCamDisplayName.clear()
    
    def set_db_conn_cur(self, db_conn, db_cur):
        self.db_conn = db_conn
        self.db_cur = db_cur

    def add_cam(self):
        try:
            # self.inputCamIP.text()
            # self.inputCamUsername.text()
            # self.inputCamPassword.text()
            # self.inputCamDisplayName.text()
            self.db_cur.execute(f"SELECT max(id) FROM cameras")
            last_id = self.db_cur.fetchone()[0]
            # print(type(last_id), last_id)
            self.db_conn.commit()
            if not last_id:
                last_id = 0

            # print('Cam ID:  ', f'{last_id + 1}. {self.inputCamDisplayName.text()}')
            self.db_cur.execute(f"INSERT INTO cameras VALUES ({last_id + 1}, '{self.inputCamIP.text()}', '{self.inputCamUsername.text()}', '{self.inputCamPassword.text()}', '{last_id + 1}. {self.inputCamDisplayName.text()}', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)")
            self.db_conn.commit()

            dataset = LoadHikvisionCamera(
                                            self.inputCamIP.text() if self.inputCamIP.text().startswith('http') else f'http://{self.inputCamIP.text()}',
                                            self.inputCamUsername.text(),
                                            self.inputCamPassword.text(),
                                            f'{last_id + 1}. {self.inputCamDisplayName.text()}',
                                            last_id+1,
                                            [640, 640],
                                            32,
                                            False
                                        )
            frame = dataset.get_frame()
            self.draw_line_widget = DrawLineWidget(frame, self.db_conn, self.db_cur, added_cam_id=last_id+1)
            self.cardinal_direction_points = self.draw_line_widget.list_coordinates

            msg = QMessageBox()
            msg.setWindowTitle(self.text_translator.information)
            msg.setText(f'ID={last_id + 1} '+self.text_translator.add_camera_popup_success)
            msg.setWindowIcon(QIcon(self.icon_path))
            msg.setIcon(QMessageBox.Warning)

            x = msg.exec_()
        except Exception as err:
            b = bytes(str(err), encoding = 'utf-8')
            msg = QMessageBox()
            msg.setWindowIcon(QIcon(self.icon_path))
            msg.setWindowTitle('Error!')
            msg.setText(str(b, encoding = 'utf-8')+self.text_translator.add_camera_popup_error)
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()
        self.process_done_signal.emit()
        self.hide()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", self.text_translator.add_cam_window_title, None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", self.text_translator.add_cam_window_cam_ip, None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", self.text_translator.add_cam_window_cam_username, None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", self.text_translator.add_cam_window_cam_password, None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", self.text_translator.add_cam_window_cam_display_name, None))
        self.addCamBtn.setText(QCoreApplication.translate("MainWindow", self.text_translator.add_cam_window_add_cam_btn, None))
