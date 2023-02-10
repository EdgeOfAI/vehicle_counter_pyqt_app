# Shakh)
import sys
from PySide2 import QtWidgets
from PySide2.QtCore import Signal
from qt.Add_Camera import Ui_MainWindow
from DrawLineWidget import DrawLineWidget
from PySide2.QtWidgets import QMessageBox
from yolov5.utils.dataloaders import LoadHikvisionCamera


class AddCameraWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    process_done_signal = Signal()
    def __init__(self, db_conn, db_cur):
        super(AddCameraWindow, self).__init__()
        self.db_conn = db_conn
        self.db_cur = db_cur
        self.setupUi(self)

        self.setupSignalSlots()
    
    def setupSignalSlots(self):
        self.addCamBtn.clicked.connect(self.add_cam)
    
    def set_db_conn_cur(self, db_conn, db_cur):
        self.db_conn = db_conn
        self.db_cur = db_cur

    def add_cam(self):
        # self.inputCamIP.text()
        # self.inputCamUsername.text()
        # self.inputCamPassword.text()
        # self.inputCamDisplayName.text()
        self.db_cur.execute(f"SELECT max(id) FROM cameras")
        last_id = self.db_cur.fetchone()[0]
        print(type(last_id), last_id)
        self.db_conn.commit()
        if not last_id:
            last_id = 0

        print('Cam ID:  ', f'{last_id + 1}. {self.inputCamDisplayName.text()}')
        self.db_cur.execute(f"INSERT INTO cameras VALUES ({last_id + 1}, '{self.inputCamIP.text()}', '{self.inputCamUsername.text()}', '{self.inputCamPassword.text()}', '{last_id + 1}. {self.inputCamDisplayName.text()}', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)")
        self.db_conn.commit()
        self.hide()

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
        msg.setWindowTitle('Ogohlantirish!')
        msg.setText(f'{last_id + 1} id ga ega bo\'lgan kamera bazaga qo\'shildi!')
        msg.setIcon(QMessageBox.Warning)

        x = msg.exec_()

        self.process_done_signal.emit()

