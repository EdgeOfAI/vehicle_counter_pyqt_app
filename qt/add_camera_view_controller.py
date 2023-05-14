# Shakh)
import sys, cv2
from PySide2 import QtWidgets
from PySide2.QtGui import QIcon
from PySide2.QtCore import Signal, QCoreApplication
from qt.Add_Camera import Ui_MainWindow
from DrawLineWidget import DrawLineWidget
from DrawDynamicLine import DrawDynamicLineWidget
from PySide2.QtWidgets import QMessageBox, QAction
from yolov5.utils.dataloaders import LoadHikvisionCamera
from qt.set_distances_view_controller import SetDistanceWindow


class AddCameraWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    process_done_signal = Signal()
    set_distance_signal = Signal(int, list)
    def __init__(self, db_conn, db_cur, icon_path, text_translator, draw_color):
        super(AddCameraWindow, self).__init__()
        self.db_conn = db_conn
        self.db_cur = db_cur
        self.icon_path = icon_path
        self.aboutToQuit = QAction("Quit", self)
        self.text_translator = text_translator
        self.draw_color = draw_color
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
    
    def updateEditedLines(self, cam_id):
        print('Cam ID:  ', cam_id)
        if cam_id > 0:
            self.set_distance_window = SetDistanceWindow(self.icon_path, self.text_translator, cam_id)
            self.set_distance_window.process_done_signal.connect(self.updateDatabase)
            self.set_distance_window.show()

    def updateDatabase(self, cam_id, side_distances):
        if cam_id > 0:
            # [[[1010, 317], [1711, 321]], [[1863, 373], [2313, 657]], [[739, 387], [380, 790]], [[397, 901], [2461, 921]]]
            aa, ab, ac, ad, ba, bb, bc, bd, ca, cb, cc, cd, da, db, dc ,dd = side_distances
            print('Side distances:  ', side_distances)
            cardinal_points = self.draw_dynamic_line_widget.getPolygonPoints()
            print('Cardinal points:   ', cardinal_points)
            self.db_cur.execute(f"""UPDATE cameras SET  
                                nx1 = {cardinal_points[0][0][0] if 1 <= len(cardinal_points) else 0} ,
                                ny1 = {cardinal_points[0][0][1] if 1 <= len(cardinal_points) else 0} ,
                                nx2 = {cardinal_points[0][1][0] if 1 <= len(cardinal_points) else 0} ,
                                ny2 = {cardinal_points[0][1][1] if 1 <= len(cardinal_points) else 0} ,
                                ex1 = {cardinal_points[1][0][0] if 2 <= len(cardinal_points) else 0} ,
                                ey1 = {cardinal_points[1][0][1] if 2 <= len(cardinal_points) else 0} ,
                                ex2 = {cardinal_points[1][1][0] if 2 <= len(cardinal_points) else 0} ,
                                ey2 = {cardinal_points[1][1][1] if 2 <= len(cardinal_points) else 0} ,
                                wx1 = {cardinal_points[2][0][0] if 3 <= len(cardinal_points) else 0} ,
                                wy1 = {cardinal_points[2][0][1] if 3 <= len(cardinal_points) else 0} ,
                                wx2 = {cardinal_points[2][1][0] if 3 <= len(cardinal_points) else 0} ,
                                wy2 = {cardinal_points[2][1][1] if 3 <= len(cardinal_points) else 0} ,
                                sx1 = {cardinal_points[3][0][0] if 4 <= len(cardinal_points) else 0} ,
                                sy1 = {cardinal_points[3][0][1] if 4 <= len(cardinal_points) else 0} ,
                                sx2 = {cardinal_points[3][1][0] if 4 <= len(cardinal_points) else 0} ,
                                sy2 = {cardinal_points[3][1][1] if 4 <= len(cardinal_points) else 0} ,
                                aa = {aa} ,
                                ab = {ab} ,
                                ac = {ac} ,
                                ad = {ad} ,
                                ba = {ba} ,
                                bb = {bb} ,
                                bc = {bc} ,
                                bd = {bd} ,
                                ca = {ca} ,
                                cb = {cb} ,
                                cc = {cc} ,
                                cd = {cd} ,
                                da = {da} ,
                                db = {db} ,
                                dc = {dc} ,
                                dd = {dd} 
                                WHERE id={cam_id}""")
            print('Updated!!!', cardinal_points)

            self.set_distance_signal.emit(cam_id, side_distances)

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
            self.db_cur.execute(f"INSERT INTO cameras VALUES ({last_id + 1}, '{self.inputCamIP.text()}', '{self.inputCamUsername.text()}', '{self.inputCamPassword.text()}', '{last_id + 1}. {self.inputCamDisplayName.text()}', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)")
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
            # rtsp_stream = f'rtsp://{self.cam_username}:{self.cam_password}@{self.cam_ip}:554/Streaming/channels/101'
            # vcap = cv2.VideoCapture(rtsp_stream)
            # ret, frame = vcap.read()
            frame = dataset.get_frame()
            self.draw_dynamic_line_widget = DrawDynamicLineWidget(frame, last_id + 1)
            self.draw_dynamic_line_widget.closed_signal.connect(self.updateEditedLines)
            self.draw_dynamic_line_widget.show()
            # self.draw_line_widget = DrawLineWidget(frame, self.db_conn, self.db_cur, added_cam_id=last_id+1, draw_color=self.draw_color)
            # cv2.imshow('Image', self.draw_line_widget.show_image())
            self.cardinal_direction_points = self.draw_dynamic_line_widget.getPolygonPoints()

            msg = QMessageBox()
            msg.setWindowTitle(self.text_translator.information)
            msg.setText(f'ID={last_id + 1} '+self.text_translator.add_camera_popup_success)
            msg.setWindowIcon(QIcon(self.icon_path))
            msg.setIcon(QMessageBox.Warning)

        except Exception as err:
            b = bytes(str(err), encoding = 'utf-8')
            msg = QMessageBox()
            msg.setWindowIcon(QIcon(self.icon_path))
            msg.setWindowTitle('Error!')
            msg.setText(str(b, encoding = 'utf-8')+self.text_translator.add_camera_popup_error)
            msg.setIcon(QMessageBox.Warning)

        self.process_done_signal.emit()
        self.hide()
        x = msg.exec_()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", self.text_translator.add_cam_window_title, None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", self.text_translator.add_cam_window_cam_ip, None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", self.text_translator.add_cam_window_cam_username, None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", self.text_translator.add_cam_window_cam_password, None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", self.text_translator.add_cam_window_cam_display_name, None))
        self.addCamBtn.setText(QCoreApplication.translate("MainWindow", self.text_translator.add_cam_window_add_cam_btn, None))
