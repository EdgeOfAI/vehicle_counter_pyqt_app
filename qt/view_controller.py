from pathlib import Path
from typing import Tuple
from PySide2.QtCore import QPoint, Signal, Slot, QCoreApplication
# from PyQt5 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QFileDialog, QMessageBox, QWidget
from PySide2.QtGui import QImage, QPixmap, Qt, QIcon
from qt.Ui_Form import Ui_Form
import numpy as np
import cv2, os, math
import pyqtgraph as pg
from config import home

from DrawLineWidget import DrawLineWidget
from DrawDynamicLine import DrawDynamicLineWidget
from qt.add_camera_view_controller import AddCameraWindow
from qt.remove_camera_view_controller import RemoveCameraWindow
from qt.edit_camera_view_controller import EditCameraWindow
from qt.show_calendar_view_controller import ShowCalendarWindow
from yolov5.utils.dataloaders import LoadHikvisionCamera


class ViewController(QWidget, Ui_Form):
    startInferenceSignal = Signal()
    startCountingSignal = Signal()
    startCountingAnalysisSignal = Signal()
    startCountInSignal = Signal()

    def __init__(self, model, conn, cur, qss_file, text_translator, draw_color):
        super().__init__()
        self.model = model
        self.video_source = None
        self.draw_color = draw_color
        self.text_translator = text_translator
        self.setStyleSheet(qss_file)
        self.icon_path = 'icon.png'
        self.setWindowIcon(QIcon(self.icon_path))
        self.setupUi(self)
        self.inputVideoFile = ''
        self.outputVideoFile = ''
        self.outputDataFile = ''
        self.cacheDataFile = ''
        self.maskFile = ''
        self.frameView.ui.histogram.hide()
        self.frameView.ui.roiBtn.hide()
        self.frameView.ui.menuBtn.hide()
        self.frameView.view.setMouseEnabled(False,False)
        self.imgMask = None
        
        self.visualizeMarkerStart = QPoint(200,200)
        self.visualizeMarkerEnd = QPoint(500,500)
        self.visualizeMarker = pg.LineROI(self.visualizeMarkerStart, self.visualizeMarkerEnd, 50)
        self.finishLine = pg.RectROI((200,200), (200,200), rotatable=True, resizable=True)

        # sqlite3 db files
        self.db_conn = conn
        self.db_cur = cur
        self.use_video = False
        self.is_refresh_clicked = 0

        self.add_cam_window = AddCameraWindow(self.db_conn, self.db_cur, self.icon_path, self.text_translator, self.draw_color)
        self.remove_camera_window = RemoveCameraWindow(self.db_conn, self.db_cur, self.icon_path, self.text_translator)
        self.edit_camera_window = EditCameraWindow(self.db_conn, self.db_cur, self.icon_path, self.text_translator)
        self.show_calendar_window = ShowCalendarWindow(self.db_conn, self.db_cur, qss_file, self.icon_path, self.text_translator)
        self.db_cur.execute(f"SELECT * FROM cameras")
        cameras = self.db_cur.fetchall()
        if len(cameras):
            draw_line = True
            camera_info = cameras[0]
            print(camera_info)
            cam_ip = camera_info[1]
            username = camera_info[2]
            password = camera_info[3]

            try:

                dataset = LoadHikvisionCamera(
                                                cam_ip if cam_ip.startswith('http') else f'http://{cam_ip}',
                                                username,
                                                password,
                                                f'dataset',
                                                1,
                                                [640, 640],
                                                32,
                                                False
                                            )
                # rtsp_stream = f'rtsp://{self.cam_username}:{self.cam_password}@{self.cam_ip}:554/Streaming/channels/101'
                # vcap = cv2.VideoCapture(rtsp_stream)
                # ret, frame = vcap.read()
                frame = dataset.get_frame()
                # print(camera_info)
                cardinal_direction_points = [
                                                [[camera_info[5], camera_info[6]], [camera_info[7], camera_info[8]]], # north
                                                [[camera_info[9], camera_info[10]], [camera_info[11], camera_info[12]]], # east
                                                [[camera_info[13], camera_info[14]], [camera_info[15],camera_info[16]]], # west
                                                [[camera_info[17], camera_info[18]], [camera_info[19], camera_info[20]]] # south
                                            ]
            except Exception as err:
                print('Error!', err)
                draw_line = False

        self.draw_dynamic_line_widget = DrawDynamicLineWidget(frame, 1, cardinal_direction_points) if draw_line else DrawDynamicLineWidget(None)

        self.add_cam_window.setStyleSheet(qss_file)
        self.remove_camera_window.setStyleSheet(qss_file)
        self.edit_camera_window.setStyleSheet(qss_file)
        self.show_calendar_window.setStyleSheet(qss_file)

        self.add_cam_window.setWindowIcon(QIcon(self.icon_path))
        self.remove_camera_window.setWindowIcon(QIcon(self.icon_path))
        self.edit_camera_window.setWindowIcon(QIcon(self.icon_path))
        self.show_calendar_window.setWindowIcon(QIcon(self.icon_path))

        self.sidewiseCountMatrixDisplay.setCurrentIndex(5)

        self.updateCameraDropDown()
        self.setupSignalSlots()

    def setupSignalSlots(self):
        self.startInferenceBtn.clicked.connect(self.startInference)
        self.startInferenceSignal.connect(self.model.startInference)
        self.addCamBtn.clicked.connect(self.openAddCamWindow)
        self.editCameraBtn.clicked.connect(self.openEditCamWindow)
        self.removeCameraBtn.clicked.connect(self.openRemoveCamWindow)
        self.changeSidePositionsBtn.clicked.connect(self.changeSidePosition)
        self.showDataBtn.clicked.connect(self.openShowCalendarWindow)
        self.model.frame_update_signal.connect(self.updateFrame)
        self.comboBox.activated[str].connect(self.onActivated)
        self.languageChooser.activated[str].connect(self.onLanguageChange)
        self.checkBox.stateChanged.connect(self.checkboxChanged)
        self.model.vehicle_count_signal.connect(self.updateVehicleCount)
        self.model.vehicle_in_count_signal.connect(self.updateInCount)
        self.model.process_done_signal.connect(self.onProcessDone)
        self.draw_dynamic_line_widget.closed_signal.connect(self.updateEditedLines)
        self.add_cam_window.process_done_signal.connect(self.onCamBtnsClosed)
        self.remove_camera_window.process_done_signal.connect(self.onCamBtnsClosed)
        self.edit_camera_window.process_done_signal.connect(self.onCamBtnsClosed)
        self.show_calendar_window.process_done_signal.connect(self.onCamBtnsClosed)
        self.stopProcessBtn.clicked.connect(self.stopProcess)

#====================== File Dialog Functions =====================
    def updateEditedLines(self, cam_id):
        print('Cam ID:  ', cam_id)
        if cam_id > 0:
            # [[[1010, 317], [1711, 321]], [[1863, 373], [2313, 657]], [[739, 387], [380, 790]], [[397, 901], [2461, 921]]]
            cardinal_points = self.draw_dynamic_line_widget.getPolygonPoints()
            print(cardinal_points)
            self.db_cur.execute(f"""UPDATE cameras SET  
                                nx1 = {cardinal_points[0][0][0]},
                                ny1 = {cardinal_points[0][0][1]},
                                nx2 = {cardinal_points[0][1][0]},
                                ny2 = {cardinal_points[0][1][1]},
                                ex1 = {cardinal_points[1][0][0]},
                                ey1 = {cardinal_points[1][0][1]},
                                ex2 = {cardinal_points[1][1][0]},
                                ey2 = {cardinal_points[1][1][1]},
                                wx1 = {cardinal_points[2][0][0]},
                                wy1 = {cardinal_points[2][0][1]},
                                wx2 = {cardinal_points[2][1][0]},
                                wy2 = {cardinal_points[2][1][1]},
                                sx1 = {cardinal_points[3][0][0]},
                                sy1 = {cardinal_points[3][0][1]},
                                sx2 = {cardinal_points[3][1][0]},
                                sy2 = {cardinal_points[3][1][1]} 
                                WHERE id={cam_id}""")
            print('Updated!!!', cardinal_points)

    def onActivated(self, text):
        cam_id = text.split('.')[0]
        # print(cam_id)
        self.db_cur.execute(f"SELECT * FROM cameras WHERE id = {cam_id}")
        camera_info = self.db_cur.fetchall()
        # print(camera_info)
        cardinal_direction_points = [
                                        [[camera_info[0][5], camera_info[0][6]], [camera_info[0][7], camera_info[0][8]]], # north
                                        [[camera_info[0][9], camera_info[0][10]], [camera_info[0][11], camera_info[0][12]]], # east
                                        [[camera_info[0][13], camera_info[0][14]], [camera_info[0][15],camera_info[0][16]]], # west
                                        [[camera_info[0][17], camera_info[0][18]], [camera_info[0][19], camera_info[0][20]]] # south
                                    ]
        self.model.setCameraInfo(camera_info[0][0], camera_info[0][1], camera_info[0][2], camera_info[0][3], camera_info[0][4], cardinal_direction_points)
    
    def onLanguageChange(self, text):
        if text == 'English':
            self.text_translator.translateToEnglish()
        elif text == "O'zbek":
            self.text_translator.translateToUzbek()
        self.retranslateUi(self)
        self.add_cam_window.setTextTranslator(self.text_translator)
        self.add_cam_window.retranslateUi(self.add_cam_window)
        self.edit_camera_window.setTextTranslator(self.text_translator)
        self.edit_camera_window.retranslateUi(self.add_cam_window)
        self.remove_camera_window.setTextTranslator(self.text_translator)
        self.remove_camera_window.retranslateUi(self.add_cam_window)
        self.show_calendar_window.setTextTranslator(self.text_translator)
        self.show_calendar_window.retranslateUi(self.add_cam_window)
    
    def changeSidePosition(self):
        is_camera = False
        if self.checkBox.isChecked():
            print('self.', self.video_source[0])
            f = cv2.VideoCapture(self.video_source[0])
            rval, frame = f.read()
            f.release()
        else:
            is_camera = True
            cam_id = str(self.comboBox.currentText()).split('.')[0]
            self.db_cur.execute(f"SELECT * FROM cameras WHERE id = {cam_id}")
            camera_info = self.db_cur.fetchall()

            # print(camera_info)
            cardinal_direction_points = [
                                            [[camera_info[0][5], camera_info[0][6]], [camera_info[0][7], camera_info[0][8]]], # north
                                            [[camera_info[0][9], camera_info[0][10]], [camera_info[0][11], camera_info[0][12]]], # east
                                            [[camera_info[0][13], camera_info[0][14]], [camera_info[0][15],camera_info[0][16]]], # west
                                            [[camera_info[0][17], camera_info[0][18]], [camera_info[0][19], camera_info[0][20]]] # south
                                        ]
            
            print('CamID:  ', cam_id, cardinal_direction_points)
            ip = camera_info[0][1]
            username = camera_info[0][2]
            password = camera_info[0][3]
            camera_name = camera_info[0][4]
            dataset = LoadHikvisionCamera(
                        ip if ip.startswith('http') else f'http://{ip}',
                        username,
                        password,
                        f'{camera_name}',
                        camera_name.split('.')[0],
                        [640, 640],
                        32,
                        False
                    )
            # rtsp_stream = f'rtsp://{self.cam_username}:{self.cam_password}@{self.cam_ip}:554/Streaming/channels/101'
            # vcap = cv2.VideoCapture(rtsp_stream)
            # ret, frame = vcap.read()
            frame = dataset.get_frame()

        print('Before')
        print('Camid:  ', self.draw_dynamic_line_widget.cam_id, self.draw_dynamic_line_widget.lines)

        if self.draw_dynamic_line_widget.cam_id != 0:
            self.draw_dynamic_line_widget = DrawDynamicLineWidget(frame, cam_id if is_camera else 0, cardinal_direction_points if is_camera else None)
            self.draw_dynamic_line_widget.closed_signal.connect(self.updateEditedLines)
        elif self.draw_dynamic_line_widget.cam_id == 0 and not self.draw_dynamic_line_widget.lines:
            self.draw_dynamic_line_widget = DrawDynamicLineWidget(frame, cam_id if is_camera else 0, cardinal_direction_points if is_camera else None)
            self.draw_dynamic_line_widget.closed_signal.connect(self.updateEditedLines)
        
        print('after')
        print('Camid:  ', self.draw_dynamic_line_widget.cam_id, self.draw_dynamic_line_widget.lines)

        self.draw_dynamic_line_widget.show()
            # self.draw_line_widget = DrawLineWidget(frame, self.db_conn, self.db_cur, added_cam_id=last_id+1, draw_color=self.draw_color)
            # cv2.imshow('Image', self.draw_line_widget.show_image())
    
    def checkboxChanged(self):
        if self.checkBox.isChecked():
            self.use_video = True
            self.enableControls(False)
            self.showDataBtn.setEnabled(True)
            if home:
                root = 'D:/'
            else:
                root = '/home/yeoju/'
            self.video_source = QFileDialog.getOpenFileName(self, "Open Video", '/home/yeoju', "mp4 (*.mp4)")
            # self.source = [os.path.join(videos_root, video_name) for video_name in os.listdir(videos_root) if Path(video_name).suffix in  ['.mp4', '.avi']]
            # source = r'F:\vehicle_count\14,03,2023\24 Format 02.12\ch01_00000000007000000 00_00_44-00_06_54.mp4'            
            self.changeSidePosition()
            # self.draw_line_widget = DrawLineWidget(frame, self.db_conn, self.db_cur, draw_color=self.draw_color)
            # cv2.imshow('Image', self.draw_line_widget.show_image())
            # self.model.cardinal_direction_points = [[[1010, 317], [1711, 321]], [[1863, 373], [2313, 657]], [[739, 387], [380, 790]], [[397, 901], [2461, 921]]]
            self.startInferenceBtn.setEnabled(True)
            self.changeSidePositionsBtn.setEnabled(True)
        else:
            self.video_source = None
            self.use_video = False
            self.enableControls(True)
            cam_id = str(self.comboBox.currentText()).split('.')[0]
            self.db_cur.execute(f"SELECT * FROM cameras WHERE id = {cam_id}")
            camera_info = self.db_cur.fetchall()

            # print(camera_info)
            cardinal_direction_points = [
                                            [[camera_info[0][5], camera_info[0][6]], [camera_info[0][7], camera_info[0][8]]], # north
                                            [[camera_info[0][9], camera_info[0][10]], [camera_info[0][11], camera_info[0][12]]], # east
                                            [[camera_info[0][13], camera_info[0][14]], [camera_info[0][15],camera_info[0][16]]], # west
                                            [[camera_info[0][17], camera_info[0][18]], [camera_info[0][19], camera_info[0][20]]] # south
                                        ]
            
            print('CamID:  ', cam_id, cardinal_direction_points)
            ip = camera_info[0][1]
            username = camera_info[0][2]
            password = camera_info[0][3]
            camera_name = camera_info[0][4]
            dataset = LoadHikvisionCamera(
                        ip if ip.startswith('http') else f'http://{ip}',
                        username,
                        password,
                        f'{camera_name}',
                        camera_name.split('.')[0],
                        [640, 640],
                        32,
                        False
                    )
            # rtsp_stream = f'rtsp://{self.cam_username}:{self.cam_password}@{self.cam_ip}:554/Streaming/channels/101'
            # vcap = cv2.VideoCapture(rtsp_stream)
            # ret, frame = vcap.read()
            frame = dataset.get_frame()
            self.draw_dynamic_line_widget = DrawDynamicLineWidget(frame, cam_id, cardinal_direction_points)
            self.draw_dynamic_line_widget.closed_signal.connect(self.updateEditedLines)

    def openShowCalendarWindow(self):
        self.enableControls(False)
        self.checkBox.setEnabled(False)
        self.stopProcessBtn.setEnabled(False)
        self.show_calendar_window.set_db_conn_cur(self.db_conn, self.db_cur)
        self.show_calendar_window.show()

    def update_db(self, query):
        self.db_cur.execute(query)
        self.db_conn.commit()

    def showPopup(self, message):
        msg = QMessageBox()
        msg.setWindowTitle(self.text_translator.warning)
        msg.setWindowIcon(QIcon(self.icon_path))
        msg.setText(message)
        msg.setIcon(QMessageBox.Warning)

        x = msg.exec_()

    def onCamBtnsClosed(self):
        self.updateCameraDropDown()
        self.enableControls(True)
        self.checkBox.setEnabled(True)
        self.stopProcessBtn.setEnabled(True)
        print('Stop_couunting', self.model.stop_counting)
        self.model.stop_counting = False
        if self.model.stop_counting:
            self.startInferenceBtn.setEnabled(False)
            self.changeSidePositionsBtn.setEnabled(False)
        if self.use_video:
            self.add_cam_window.setEnabled(False)
            self.edit_camera_window.setEnabled(False)
            self.remove_camera_window.setEnabled(False)
            self.comboBox.setEnabled(False)
        else:
            self.add_cam_window.setEnabled(True)
            self.edit_camera_window.setEnabled(True)
            self.remove_camera_window.setEnabled(True)
            self.comboBox.setEnabled(True)
            self.changeSidePositionsBtn.setEnabled(True)
        self.model.stop_countin = True
        
    def openAddCamWindow(self):
        # print('Opening camera add window')
        self.db_cur.execute(f"SELECT * FROM cameras")
        num_added_cameras = len(self.db_cur.fetchall())
        # print(type(num_added_cameras), num_added_cameras)
        if num_added_cameras >= 3:
            self.showPopup(self.text_translator.num_cameras_exceeded)
            return None
        self.add_cam_window.set_db_conn_cur(self.db_conn, self.db_cur)
        self.enableControls(False)
        self.checkBox.setEnabled(False)
        self.stopProcessBtn.setEnabled(False)
        self.add_cam_window.clearInputs()
        self.add_cam_window.show()
    
    def openRemoveCamWindow(self):
        # print('Opening camera remove window')
        self.db_cur.execute(f"SELECT * FROM cameras")
        cameras = self.db_cur.fetchall()
        num_added_cameras = len(cameras)
        # print(type(num_added_cameras), num_added_cameras)
        if not num_added_cameras:
            self.showPopup(self.text_translator.no_cameras_found_error)
            return None
        first_cam_id = cameras[0][0]
        self.remove_camera_window.setCamId(first_cam_id)
        self.remove_camera_window.set_db_conn_cur(self.db_conn, self.db_cur)
        self.enableControls(False)
        self.checkBox.setEnabled(False)
        self.stopProcessBtn.setEnabled(False)
        self.remove_camera_window.show()
    
    def openEditCamWindow(self):
        # print('Opening camera Edit window')
        self.db_cur.execute(f"SELECT * FROM cameras")
        cameras = self.db_cur.fetchall()
        num_added_cameras = len(cameras)
        # print(type(num_added_cameras), num_added_cameras)
        if not num_added_cameras:
            self.showPopup(self.text_translator.no_cameras_found_error)
            return None
        first_cam_id = cameras[0][0]
        self.edit_camera_window.setCamId(first_cam_id)
        self.edit_camera_window.set_db_conn_cur(self.db_conn, self.db_cur)
        self.edit_camera_window.setCameraInfos()
        self.enableControls(False)
        self.checkBox.setEnabled(False)
        self.stopProcessBtn.setEnabled(False)
        self.edit_camera_window.show()

    def updateCameraDropDown(self):
        self.db_cur.execute(f"SELECT * FROM cameras")
        cameras = self.db_cur.fetchall()
        camera_names = [row[4] for row in cameras]
        if not self.is_refresh_clicked and cameras:
            # print('Refresh pressed and camera id set to : ', camera_names[0].split('.')[0])
            cardinal_direction_points = [
                                            [[cameras[0][5], cameras[0][6]], [cameras[0][7], cameras[0][8]]], # north
                                            [[cameras[0][9], cameras[0][10]], [cameras[0][11], cameras[0][12]]], # east
                                            [[cameras[0][13], cameras[0][14]], [cameras[0][15],cameras[0][16]]], # west
                                            [[cameras[0][17], cameras[0][18]], [cameras[0][19], cameras[0][20]]] # south
                                        ]
            self.model.setCameraInfo(cameras[0][0], cameras[0][1], cameras[0][2], cameras[0][3], cameras[0][4], cardinal_direction_points)
            self.is_refresh_clicked = 1
        self.comboBox.clear()
        self.comboBox.addItems(camera_names)
        self.db_conn.commit()

    def openVideoFile(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Video", '', "mp4 (*.mp4)")
        if (file_path != ''):
            self.setVideo(file_path)

    def openCacheFile(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Yolov5 Model", '', "pt (*.pt)")
        if (file_path != ''):
            self.setCacheData(file_path)

    def getOutputFileName(self):
        file_path, _ = QFileDialog().getSaveFileName()
        if file_path != '':
            self.setOutputFile(file_path)

    def openMaskFile(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Mask File", '', "hdf (*.h5)")
        if file_path != '':
            self.model.setMaskFile(file_path)
            self.maskFile = file_path
            self.maskFileLbl.setText(self.maskFile)
            self.imgMask = self.model.getMask()
            img = self.frameView.imageItem.image.copy()
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            self.maskPreview = cv2.bitwise_and(img, img, mask=self.imgMask)

    def saveMask(self):
        if self.imgMask is None:
            QMessageBox.warning(self, 'Error', 'Mask not drawn yet!')
            return
        if self.maskFile == '':
            file_path, _ = QFileDialog().getSaveFileName()
            if file_path != '':        
                self.maskFile = file_path
                self.maskFileLbl.setText(self.maskFile)    
        self.model.saveMask(self.maskFile, self.imgMask)

#======================= Setting Data sources ========================

    def setVideo(self, file_path):
        self.inputVideoFile = file_path
        self.inputVideoFileLabel.setText(file_path)
        self.model.setInputVideoPath(self.inputVideoFile)

        # set the output file name to match as well
        self.setOutputFile(file_path)

    def setOutputFile(self, file_path):
        if '.mp4' in file_path:
            file_path = file_path.replace('.mp4', '')
        self.outputVideoFile = file_path + '.avi'
        self.outputDataFile = file_path + '.h5'
        self.outputFileLabel.setText(file_path)
        self.model.setOutputVideoPath(self.outputVideoFile)
        self.model.setOutputDataPath(self.outputDataFile)

    def setCacheData(self, file_path):
        self.cacheDataFile = file_path
        self.cacheDataLabel.setText(file_path)
        self.model.setCacheDataPath(file_path)        

#================= Vehicle Counting Functions =========================

    @Slot(bool)
    def showFinishLine(self, checked):
        if checked:
            self.frameView.addItem(self.finishLine)
            # self.finishLine.sigRegionChangeFinished.connect(self.getFinishLineBounds)
        else:
            self.frameView.removeItem(self.finishLine)


    @Slot(bool)
    def visualizeCountingParam(self, checked):
        if checked:
            # add arrow with length defined in distance
            self.frameView.addItem(self.visualizeMarker)
            self.visualizeMarker.sigRegionChangeFinished.connect(self.updateCountingParams)

        else:
            self.frameView.view.removeItem(self.visualizeMarker)


    def getMarkerPos(self) -> Tuple[QPoint, QPoint]:
        positions = self.visualizeMarker.getSceneHandlePositions()
        start = positions[0][1]
        end = positions[1][1]

        # convert to image coordinate system
        start = self.frameView.getView().mapSceneToView(start)
        start = self.frameView.getView().mapFromViewToItem(self.frameView.imageItem, start)
        end = self.frameView.getView().mapSceneToView(end)
        end = self.frameView.getView().mapFromViewToItem(self.frameView.imageItem, end)
        return start, end

    def updateCountingParams(self):
        width = self.visualizeMarker.size()[1]
        start, end = self.getMarkerPos()

        # calculate filter distance from line length
        dist = math.dist([start.x(), start.y()], [end.x(), end.y()])

        # calculate x & y filter values from line vector
        dx = (end - start).x()
        dy = (end - start).y()

        self.distFilterSpn.setValue(dist)
        self.xFilterVectorSpn.setValue(dx)
        self.yFilterVectorSpn.setValue(dy)
        self.widthFilterVectorSpn.setValue(width)

    def updateVectorDirectionLabel(self):
        if self.yFilterVectorSpn.value() > 0:
            self.vectorDirectionLbl.setText('DOWN')
        else:
            self.vectorDirectionLbl.setText('UP')

    def startCounting(self):
        if self.cacheDataFile != '':
            self.prepareforAnalysis()
            self.startCountingSignal.emit()
        else:
            QMessageBox.warning(self, 'Error', 'No cache file selected!')

    def startCountingAnalysis(self):
        if self.cacheDataFile != '':
            self.prepareforAnalysis()
            self.startCountingAnalysisSignal.emit()
        else:
            QMessageBox.warning(self, 'Error', 'No cache file selected!')
    
    def set_zero_vehicle_matrix(self):
            self.NNtotal.display(0)
            self.truckCount.display(0)
            self.carCount.display(0)
            self.NNbusCount.display(0)
            self.NNbicycleCount.display(0)
            self.NNmcycleCount.display(0)
            self.NEtotal.display(0)
            self.NEtruckCount.display(0)
            self.NEcarCount.display(0)
            self.NEbusCount.display(0)
            self.NEbicycleCount.display(0)
            self.NEmcycleCount.display(0)
            self.NWtotal.display(0)
            self.NWtruckCount.display(0)
            self.NWcarCount.display(0)
            self.NWbusCount.display(0)
            self.NWbicycleCount.display(0)
            self.NWmcycleCount.display(0)
            self.NStotal.display(0)
            self.NStruckCount.display(0)
            self.NScarCount.display(0)
            self.NSbusCount.display(0)
            self.NSbicycleCount.display(0)
            self.NSmcycleCount.display(0)
            self.ENtotal.display(0)
            self.ENtruckCount.display(0)
            self.ENcarCount.display(0)
            self.ENbusCount.display(0)
            self.ENbicycleCount.display(0)
            self.ENmcycleCount.display(0)
            self.EEtotal.display(0)
            self.EEtruckCount.display(0)
            self.EEcarCount.display(0)
            self.EEbusCount.display(0)
            self.EEbicycleCount.display(0)
            self.EEmcycleCount.display(0)
            self.EWtotal.display(0)
            self.EWtruckCount.display(0)
            self.EWcarCount.display(0)
            self.EWbusCount.display(0)
            self.EWbicycleCount.display(0)
            self.EWmcycleCount.display(0)
            self.EStotal.display(0)
            self.EStruckCount.display(0)
            self.EScarCount.display(0)
            self.ESbusCount.display(0)
            self.ESbicycleCount.display(0)
            self.ESmcycleCount.display(0)
            self.WNtotal.display(0)
            self.WNtruckCount.display(0)
            self.WNcarCount.display(0)
            self.WNbusCount.display(0)
            self.WNbicycleCount.display(0)
            self.WNmcycleCount.display(0)
            self.WEtotal.display(0)
            self.WEtruckCount.display(0)
            self.WEcarCount.display(0)
            self.WEbusCount.display(0)
            self.WEbicycleCount.display(0)
            self.WEmcycleCount.display(0)
            self.WWtotal.display(0)
            self.WWtruckCount.display(0)
            self.WWcarCount.display(0)
            self.WWbusCount.display(0)
            self.WWbicycleCount.display(0)
            self.WWmcycleCount.display(0)
            self.WStotal.display(0)
            self.WStruckCount.display(0)
            self.WScarCount.display(0)
            # table = self.carPreviewTable
            self.WSbusCount.display(0)
            # table = self.busPreviewTable
            self.WSbicycleCount.display(0)
            self.WSmcycleCount.display(0)
            self.SNtotal.display(0)
            self.SNtruckCount.display(0)
            # table = self.truckPreviewTable
            self.SNcarCount.display(0)
            # table = self.carPreviewTable
            self.SNbusCount.display(0)
            # table = self.busPreviewTable
            self.SNbicycleCount.display(0)
            self.SNmcycleCount.display(0)
            self.SEtotal.display(0)
            self.SEtruckCount.display(0)
            # table = self.truckPreviewTable
            self.SEcarCount.display(0)
            # table = self.carPreviewTable
            self.SEbusCount.display(0)
            # table = self.busPreviewTable
            self.SEbicycleCount.display(0)
            self.SEmcycleCount.display(0)
            self.SWtotal.display(0)
            self.SWtruckCount.display(0)
            # table = self.truckPreviewTable
            self.SWcarCount.display(0)
            # table = self.carPreviewTable
            self.SWbusCount.display(0)
            # table = self.busPreviewTable
            self.SWbicycleCount.display(0)
            self.SWmcycleCount.display(0)
            self.SStotal.display(0)
            self.SStruckCount.display(0)
            self.SScarCount.display(0)
            self.SSbusCount.display(0)
            self.SSbicycleCount.display(0)
            self.SSmcycleCount.display(0)

            self.aInCount.display(0)
            self.bInCount.display(0)
            self.cInCount.display(0)
            self.dInCount.display(0)
    
    @Slot(int)
    def updateInCount(self, side_id):
        if side_id == 0:  # a side
            self.aInCount.display(self.aInCount.intValue()+1)
        elif side_id == 1:  # b side
            self.bInCount.display(self.bInCount.intValue()+1)
        elif side_id == 2:  # c side
            self.cInCount.display(self.cInCount.intValue()+1)
        elif side_id == 3:  # d side
            self.dInCount.display(self.dInCount.intValue()+1)
        return
        

    @Slot(int,int,int,np.ndarray)
    def updateVehicleCount(self, class_id, uid, count, img, row_num, preview_num):
        '''
        class_id 5 == van not motorcycle
        class_id 2 == bicycle
        class_id 3 == motorcycle

        '''

        # self.truckCount.display(count)
        # self.carCount.display(count)
        # self.busCount.display(count)
        # self.NEtruckCount.display(count)
        # self.NEcarCount.display(count)
        # self.NEbusCount.display(count)
        # self.NWtruckCount.display(count)
        # self.NWcarCount.display(count)
        # self.NWbusCount.display(count)
        # self.NStruckCount.display(count)
        # self.NScarCount.display(count)
        # self.NSbusCount.display(count)
        # self.ENtruckCount.display(count)
        # self.ENcarCount.display(count)
        # self.ENbusCount.display(count)
        # self.EEtruckCount.display(count)
        # self.EEcarCount.display(count)
        # self.EEbusCount.display(count)
        # self.EWtruckCount.display(count)
        # self.EWcarCount.display(count)
        # self.EWbusCount.display(count)
        # self.EStruckCount.display(count)
        # self.EScarCount.display(count)
        # self.ESbusCount.display(count)
        # self.WNtruckCount.display(count)
        # self.WNcarCount.display(count)
        # self.WNbusCount.display(count)
        # self.WEtruckCount.display(count)
        # self.WEcarCount.display(count)
        # self.WEbusCount.display(count)
        # self.WWtruckCount.display(count)
        # self.WWcarCount.display(count)
        # self.WWbusCount.display(count)
        # self.WStruckCount.display(count)
        # self.WScarCount.display(count)
        # self.WSbusCount.display(count)
        # self.SNtruckCount.display(count)
        # self.SNcarCount.display(count)
        # self.SNbusCount.display(count)
        # self.SEtruckCount.display(count)
        # self.SEcarCount.display(count)
        # self.SEbusCount.display(count)
        # self.SWtruckCount.display(count)
        # self.SWcarCount.display(count)
        # self.SWbusCount.display(count)
        # self.SStruckCount.display(count)
        # self.SScarCount.display(count)
        # self.SSbusCount.display(count)

        # print('I am in update function')
        # print(class_id, uid, count, row_num, preview_num)

        if row_num == '00':  # NN
            self.NNtotal.display(count)
            if class_id == 6:
                self.truckCount.display(self.truckCount.intValue()+1)
                # table = self.truckPreviewTable
            elif class_id == 1:
                self.carCount.display(self.carCount.intValue()+1)
                # table = self.carPreviewTable
            elif class_id == 4:
                self.NNbusCount.display(self.NNbusCount.intValue()+1)
                # table = self.busPreviewTable
            elif class_id == 2 or class_id == 3:
                self.NNbicycleCount.display(self.NNbicycleCount.intValue()+1)
            elif class_id == 5:
                self.NNmcycleCount.display(self.NNmcycleCount.intValue()+1)
            else:
                return
        elif row_num == '01':  # NE
            self.NEtotal.display(count)
            if class_id == 6:
                self.NEtruckCount.display(self.NEtruckCount.intValue()+1)
                # table = self.truckPreviewTable
            elif class_id == 1:
                self.NEcarCount.display(self.NEcarCount.intValue()+1)
                # table = self.carPreviewTable
            elif class_id == 4:
                self.NEbusCount.display(self.NEbusCount.intValue()+1)
                # table = self.busPreviewTable
            elif class_id == 2 or class_id == 3:
                self.NEbicycleCount.display(self.NEbicycleCount.intValue()+1)
            elif class_id == 5:
                self.NEmcycleCount.display(self.NEmcycleCount.intValue()+1)
            else:
                return
        elif row_num == '02':  # NW
            self.NWtotal.display(count)
            if class_id == 6:
                self.NWtruckCount.display(self.NWtruckCount.intValue()+1)
                # table = self.truckPreviewTable
            elif class_id == 1:
                self.NWcarCount.display(self.NWcarCount.intValue()+1)
                # table = self.carPreviewTable
            elif class_id == 4:
                self.NWbusCount.display(self.NWbusCount.intValue()+1)
                # table = self.busPreviewTable
            elif class_id == 2 or class_id == 3:
                self.NWbicycleCount.display(self.NWbicycleCount.intValue()+1)
            elif class_id == 5:
                self.NWmcycleCount.display(self.NWmcycleCount.intValue()+1)
            else:
                return
        elif row_num == '03':  # NS
            self.NStotal.display(count)
            if class_id == 6:
                self.NStruckCount.display(self.NStruckCount.intValue()+1)
                # table = self.truckPreviewTable
            elif class_id == 1:
                self.NScarCount.display(self.NScarCount.intValue()+1)
                # table = self.carPreviewTable
            elif class_id == 4:
                self.NSbusCount.display(self.NSbusCount.intValue()+1)
                # table = self.busPreviewTable
            elif class_id == 2 or class_id == 3:
                self.NSbicycleCount.display(self.NSbicycleCount.intValue()+1)
            elif class_id == 5:
                self.NSmcycleCount.display(self.NSmcycleCount.intValue()+1)
            else:
                return
        elif row_num == '10':  # EN
            self.ENtotal.display(count)
            if class_id == 6:
                self.ENtruckCount.display(self.ENtruckCount.intValue()+1)
                # table = self.truckPreviewTable
            elif class_id == 1:
                self.ENcarCount.display(self.ENcarCount.intValue()+1)
                # table = self.carPreviewTable
            elif class_id == 4:
                self.ENbusCount.display(self.ENbusCount.intValue()+1)
                # table = self.busPreviewTable
            elif class_id == 2 or class_id == 3:
                self.ENbicycleCount.display(self.ENbicycleCount.intValue()+1)
            elif class_id == 5:
                self.ENmcycleCount.display(self.ENmcycleCount.intValue()+1)
            else:
                return
        elif row_num == '11':  # EE
            self.EEtotal.display(count)
            if class_id == 6:
                self.EEtruckCount.display(self.EEtruckCount.intValue()+1)
                # table = self.truckPreviewTable
            elif class_id == 1:
                self.EEcarCount.display(self.EEcarCount.intValue()+1)
                # table = self.carPreviewTable
            elif class_id == 4:
                self.EEbusCount.display(self.EEbusCount.intValue()+1)
                # table = self.busPreviewTable
            elif class_id == 2 or class_id == 3:
                self.EEbicycleCount.display(self.EEbicycleCount.intValue()+1)
            elif class_id == 5:
                self.EEmcycleCount.display(self.EEmcycleCount.intValue()+1)
            else:
                return
        elif row_num == '12':  # EW
            self.EWtotal.display(count)
            if class_id == 6:
                self.EWtruckCount.display(self.EWtruckCount.intValue()+1)
                # table = self.truckPreviewTable
            elif class_id == 1:
                self.EWcarCount.display(self.EWcarCount.intValue()+1)
                # table = self.carPreviewTable
            elif class_id == 4:
                self.EWbusCount.display(self.EWbusCount.intValue()+1)
                # table = self.busPreviewTable
            elif class_id == 2 or class_id == 3:
                self.EWbicycleCount.display(self.EWbicycleCount.intValue()+1)
            elif class_id == 5:
                self.EWmcycleCount.display(self.EWmcycleCount.intValue()+1)
            else:
                return
        elif row_num == '13':  # ES
            self.EStotal.display(count)
            if class_id == 6:
                self.EStruckCount.display(self.EStruckCount.intValue()+1)
                # table = self.truckPreviewTable
            elif class_id == 1:
                self.EScarCount.display(self.EScarCount.intValue()+1)
                # table = self.carPreviewTable
            elif class_id == 4:
                self.ESbusCount.display(self.ESbusCount.intValue()+1)
                # table = self.busPreviewTable
            elif class_id == 2 or class_id == 3:
                self.ESbicycleCount.display(self.ESbicycleCount.intValue()+1)
            elif class_id == 5:
                self.ESmcycleCount.display(self.ESmcycleCount.intValue()+1)
            else:
                return
        elif row_num == '20':  # WN
            self.WNtotal.display(count)
            if class_id == 6:
                self.WNtruckCount.display(self.WNtruckCount.intValue()+1)
                # table = self.truckPreviewTable
            elif class_id == 1:
                self.WNcarCount.display(self.WNcarCount.intValue()+1)
                # table = self.carPreviewTable
            elif class_id == 4:
                self.WNbusCount.display(self.WNbusCount.intValue()+1)
                # table = self.busPreviewTable
            elif class_id == 2 or class_id == 3:
                self.WNbicycleCount.display(self.WNbicycleCount.intValue()+1)
            elif class_id == 5:
                self.WNmcycleCount.display(self.WNmcycleCount.intValue()+1)
            else:
                return
        elif row_num == '21':  # WE
            self.WEtotal.display(count)
            if class_id == 6:
                self.WEtruckCount.display(self.WEtruckCount.intValue()+1)
                # table = self.truckPreviewTable
            elif class_id == 1:
                self.WEcarCount.display(self.WEcarCount.intValue()+1)
                # table = self.carPreviewTable
            elif class_id == 4:
                self.WEbusCount.display(self.WEbusCount.intValue()+1)
                # table = self.busPreviewTable
            elif class_id == 2 or class_id == 3:
                self.WEbicycleCount.display(self.WEbicycleCount.intValue()+1)
            elif class_id == 5:
                self.WEmcycleCount.display(self.WEmcycleCount.intValue()+1)
            else:
                return
        elif row_num == '22':  # WW
            self.WWtotal.display(count)
            if class_id == 6:
                self.WWtruckCount.display(self.WWtruckCount.intValue()+1)
                # table = self.truckPreviewTable
            elif class_id == 1:
                self.WWcarCount.display(self.WWcarCount.intValue()+1)
                # table = self.carPreviewTable
            elif class_id == 4:
                self.WWbusCount.display(self.WWbusCount.intValue()+1)
                # table = self.busPreviewTable
            elif class_id == 2 or class_id == 3:
                self.WWbicycleCount.display(self.WWbicycleCount.intValue()+1)
            elif class_id == 5:
                self.WWmcycleCount.display(self.WWmcycleCount.intValue()+1)
            else:
                return
        elif row_num == '23':  # WS
            self.WStotal.display(count)
            if class_id == 6:
                self.WStruckCount.display(self.WStruckCount.intValue()+1)
                # table = self.truckPreviewTable
            elif class_id == 1:
                self.WScarCount.display(self.WScarCount.intValue()+1)
                # table = self.carPreviewTable
            elif class_id == 4:
                self.WSbusCount.display(self.WSbusCount.intValue()+1)
                # table = self.busPreviewTable
            elif class_id == 2 or class_id == 3:
                self.WSbicycleCount.display(self.WSbicycleCount.intValue()+1)
            elif class_id == 5:
                self.WSmcycleCount.display(self.WSmcycleCount.intValue()+1)
            else:
                return
        elif row_num == '30':  # SN
            self.SNtotal.display(count)
            if class_id == 6:
                self.SNtruckCount.display(self.SNtruckCount.intValue()+1)
                # table = self.truckPreviewTable
            elif class_id == 1:
                self.SNcarCount.display(self.SNcarCount.intValue()+1)
                # table = self.carPreviewTable
            elif class_id == 4:
                self.SNbusCount.display(self.SNbusCount.intValue()+1)
                # table = self.busPreviewTable
            elif class_id == 2 or class_id == 3:
                self.SNbicycleCount.display(self.SNbicycleCount.intValue()+1)
            elif class_id == 5:
                self.SNmcycleCount.display(self.SNmcycleCount.intValue()+1)
            else:
                return
        elif row_num == '31':  # SE
            self.SEtotal.display(count)
            if class_id == 6:
                self.SEtruckCount.display(self.SEtruckCount.intValue()+1)
                # table = self.truckPreviewTable
            elif class_id == 1:
                self.SEcarCount.display(self.SEcarCount.intValue()+1)
                # table = self.carPreviewTable
            elif class_id == 4:
                self.SEbusCount.display(self.SEbusCount.intValue()+1)
                # table = self.busPreviewTable
            elif class_id == 2 or class_id == 3:
                self.SEbicycleCount.display(self.SEbicycleCount.intValue()+1)
            elif class_id == 5:
                self.SEmcycleCount.display(self.SEmcycleCount.intValue()+1)
            else:
                return
        elif row_num == '32':  # SW
            self.SWtotal.display(count)
            if class_id == 6:
                self.SWtruckCount.display(self.SWtruckCount.intValue()+1)
                # table = self.truckPreviewTable
            elif class_id == 1:
                self.SWcarCount.display(self.SWcarCount.intValue()+1)
                # table = self.carPreviewTable
            elif class_id == 4:
                self.SWbusCount.display(self.SWbusCount.intValue()+1)
                # table = self.busPreviewTable
            elif class_id == 2 or class_id == 3:
                self.SWbicycleCount.display(self.SWbicycleCount.intValue()+1)
            elif class_id == 5:
                self.SWmcycleCount.display(self.SWmcycleCount.intValue()+1)
            else:
                return
        elif row_num == '33':  # SS
            self.SStotal.display(count)
            if class_id == 6:
                self.SStruckCount.display(self.SStruckCount.intValue()+1)
                # table = self.truckPreviewTable
            elif class_id == 1:
                self.SScarCount.display(self.SScarCount.intValue()+1)
                # table = self.carPreviewTable
            elif class_id == 4:
                self.SSbusCount.display(self.SSbusCount.intValue()+1)
                # table = self.busPreviewTable
            elif class_id == 2 or class_id == 3:
                self.SSbicycleCount.display(self.SSbicycleCount.intValue()+1)
            elif class_id == 5:
                self.SSmcycleCount.display(self.SSmcycleCount.intValue()+1)
            else:
                return
        
        # if class_id == 6:
        #     self.truckCount.display(count)
        #     table = self.truckPreviewTable
        # elif class_id == 1:
        #     self.carCount.display(count)
        #     table = self.carPreviewTable
        # elif class_id == 4:
        #     self.busCount.display(count)
        #     table = self.busPreviewTable
        # else:
        #     return
        # print(preview_num, 'preview_num')
        # item = QTableWidgetItem()
        # pixmap = self.convert_cv_qt(img, 100, 100)
        # item.setData(Qt.DecorationRole, pixmap)
        # table.setItem(preview_num-1,0,item)
        # item = QTableWidgetItem(str(uid))
        # table.setItem(preview_num-1,1,item)

#================== Inference Functions ======================

    def startInference(self):
        self.prepareforAnalysis()
        self.set_zero_vehicle_matrix()
        self.enableControls(False)
        self.changeSidePositionsBtn.setEnabled(False)
        self.showDataBtn.setEnabled(True)
        # print('before inference:  ', self.db_cur)
        self.model.update_db_conn_cur(self.db_conn, self.db_cur)
        self.model.use_video = self.checkBox.isChecked()
        self.model.text_translator = self.text_translator
        if self.checkBox.isChecked():
            self.model.cardinal_direction_points = self.draw_dynamic_line_widget.getPolygonPoints()
        else:
            cam_id = str(self.comboBox.currentText()).split('.')[0]
            self.setCardinalPoints(cam_id)
        if self.use_video:
            self.model.source = self.video_source[0]
        # self.model.cardinal_direction_points = [[[1010, 317], [1711, 321]], [[1863, 373], [2313, 657]], [[739, 387], [380, 790]], [[397, 901], [2461, 921]]]
        self.startInferenceSignal.emit()
    
    def setCardinalPoints(self, cam_id):
        if int(cam_id) > 0:
            print(cam_id)
            self.db_cur.execute(f"SELECT * FROM cameras WHERE id = {cam_id}")
            camera_info = self.db_cur.fetchall()
            # print(camera_info)
            cardinal_direction_points = [
                                            [[camera_info[0][5], camera_info[0][6]], [camera_info[0][7], camera_info[0][8]]], # north
                                            [[camera_info[0][9], camera_info[0][10]], [camera_info[0][11], camera_info[0][12]]], # east
                                            [[camera_info[0][13], camera_info[0][14]], [camera_info[0][15],camera_info[0][16]]], # west
                                            [[camera_info[0][17], camera_info[0][18]], [camera_info[0][19], camera_info[0][20]]] # south
                                        ]
            self.model.setCameraInfo(camera_info[0][0], camera_info[0][1], camera_info[0][2], camera_info[0][3], camera_info[0][4], cardinal_direction_points)
        else:
            self.model.cardinal_direction_points = self.draw_dynamic_line_widget.getPolygonPoints()
    
    def stopProcess(self):
        self.db_conn = self.model.db_conn
        self.db_cur = self.model.db_cur
        self.model.stopInference()
        self.model.stopCountingAnalysis()
        # print('Use video:  ', self.use_video)
        self.enableControls(True)
        self.changeSidePositionsBtn.setEnabled(True)
        if self.use_video:
            # print('Use video true')
            self.startInferenceBtn.setEnabled(True)
            self.changeSidePositionsBtn.setEnabled(True)
            self.addCamBtn.setEnabled(False)
            self.removeCameraBtn.setEnabled(False)
            self.editCameraBtn.setEnabled(False)


#================== Masking Functions ======================

    def resetMask(self):
        if self.frameView.imageItem.image is None:
            QMessageBox.warning(self, 'Error', 'No image to mask!')
            return
        img = self.frameView.imageItem.image.copy()
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.maskPreview = img
        cv2.imshow('Mask', self.maskPreview)
        self.imgMask = np.ones(self.frameView.imageItem.image.shape[:2], dtype = np.uint8)

    def drawMask(self):
        if self.imgMask is None:
            self.resetMask()
        self.drawing = False
        cv2.namedWindow('Mask')
        cv2.setMouseCallback('Mask', self.maskMouse)
        cv2.imshow('Mask', self.maskPreview)    

    def maskMouse(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.drawing = True
            cv2.circle(self.maskPreview, (x,y), self.maskStokeSpn.value(), [0,0,0], -1)
            cv2.circle(self.imgMask, (x,y), self.maskStokeSpn.value(), 0, -1)

        elif event == cv2.EVENT_MOUSEMOVE:
            if self.drawing == True:
                cv2.circle(self.maskPreview, (x, y), self.maskStokeSpn.value(), [0,0,0], -1)
                cv2.circle(self.imgMask, (x, y), self.maskStokeSpn.value(), 0, -1)

        elif event == cv2.EVENT_LBUTTONUP:
            if self.drawing == True:
                self.drawing = False
                cv2.circle(self.maskPreview, (x, y), self.maskStokeSpn.value(), [0,0,0], -1)
                cv2.circle(self.imgMask, (x, y), self.maskStokeSpn.value(), 0, -1)
        cv2.imshow('Mask', self.maskPreview)
        

#=================== Helper Functions =========================

    def prepareforAnalysis(self):
        # set parameters
        # self.model.setParams(
        #     {
        #         'mask'          : self.imgMask,
        #         'iou_thresh'    : self.iouThreshSpn.value(),
        #         'score_thresh'  : self.scoreThreshSpn.value(),
        #         'cos_dist'      : self.cosineDistSpn.value(),
        #         'x_vect'        : self.xFilterVectorSpn.value(),
        #         'y_vect'        : self.yFilterVectorSpn.value(),
        #         'filt_width'    : self.widthFilterVectorSpn.value(),
        #         'filt_dist'     : self.distFilterSpn.value(),
        #         'filt_frames'   : self.skipFrameFilterSpn.value(),
        #         'finish_frames' : self.finishLineFramesSpn.value(),
        #         'finish_line'   : self.getFinishLineBounds(),
        #     }
        # )

        # clear the preview table
        # self.carPreviewTable.clear()
        # self.truckPreviewTable.clear()

        # self.enableControls(False)
        return False

    def getFinishLineBounds(self):
        pos = self.finishLine.viewPos()
        if pos is None:
            return [0,0,0,0]

        size = self.finishLine.size()

        return [int(pos.x()), int(pos.y()), int(size.x()), int(size.y())]

        # print('start vis: ' + str(size.x()) + ',' + str(size.y()))
        # print('###########################')

    def enableControls(self, state=True):
        self.startInferenceBtn.setEnabled(state)
        # self.cameraEditBox.setEnabled(state)
        self.showDataBtn.setEnabled(state)
        self.changeSidePositionsBtn.setEnabled(state)
        if not self.use_video:
            self.addCamBtn.setEnabled(state)
            self.editCameraBtn.setEnabled(state)
            self.removeCameraBtn.setEnabled(state)
            self.comboBox.setEnabled(state)
            # self.mediaGBox.setEnabled(state)
        else:
            self.addCamBtn.setEnabled(False)
            self.editCameraBtn.setEnabled(False)
            self.removeCameraBtn.setEnabled(False)
            self.comboBox.setEnabled(False)
            # self.mediaGBox.setEnabled(False)

    def onProcessDone(self):
        self.enableControls(True)
        self.changeSidePositionsBtn.setEnabled(True)

    @Slot(int)
    def updateMaxFrameNum(self, frame_num):
        self.maxFrameNum.setText(str(frame_num))
        self.frameSlider.setMaximum(frame_num)

    @Slot(np.ndarray, int)
    def updateFrame(self, cv_img, frame_num):
        self.frameView.view.setXRange(0, cv_img.shape[1])
        self.frameView.view.setYRange(0, cv_img.shape[0])
        self.frameView.imageItem.setImage(cv_img)
        # self.frameNum.setText(str(frame_num))
    
    def convert_cv_qt(self, rgb_image, width, height):
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(width, height, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", self.text_translator.main_window_title, None))
        self.languageChooser.setItemText(0, QCoreApplication.translate("Form", u"English", None))
        self.languageChooser.setItemText(1, QCoreApplication.translate("Form", u"O'zbek", None))

        self.addCamBtn.setText(QCoreApplication.translate("Form", self.text_translator.add_camera_btn, None))
        self.editCameraBtn.setText(QCoreApplication.translate("Form", self.text_translator.edit_camera_btn, None))
        self.removeCameraBtn.setText(QCoreApplication.translate("Form", self.text_translator.remove_camera_btn, None))
        self.changeSidePositionsBtn.setText(QCoreApplication.translate("Form", self.text_translator.change_position, None))
        self.showDataBtn.setText(QCoreApplication.translate("Form", self.text_translator.show_data_btn, None))
        self.videoSwitcher.setTitle("")
        self.mediaGBox.setTitle("")
        self.comboBox.setCurrentText("")
        self.stopProcessBtn.setText(QCoreApplication.translate("Form", self.text_translator.stop_process_btn, None))
        self.startInferenceBtn.setText(QCoreApplication.translate("Form", self.text_translator.start_inference_btn, None))
        self.checkBox.setText(QCoreApplication.translate("Form", self.text_translator.use_video_checkbox, None))
        self.label_39.setText(QCoreApplication.translate("Form", self.text_translator.d_in, None))
        self.label_42.setText(QCoreApplication.translate("Form", self.text_translator.c_in, None))
        self.label_53.setText(QCoreApplication.translate("Form", self.text_translator.b_out, None))
        self.label_52.setText(QCoreApplication.translate("Form", self.text_translator.c_out, None))
        self.label_48.setText(QCoreApplication.translate("Form", self.text_translator.b_in, None))
        self.label_55.setText(QCoreApplication.translate("Form", self.text_translator.d_out, None))
        self.label_9.setText(QCoreApplication.translate("Form", self.text_translator.a_in, None))
        self.label_2.setText(QCoreApplication.translate("Form", self.text_translator.a_out, None))
        self.sidewiseCountMatrixDisplay.setTabText(self.sidewiseCountMatrixDisplay.indexOf(self.carTab), QCoreApplication.translate("Form", self.text_translator.cars, None))
        self.label_30.setText(QCoreApplication.translate("Form", self.text_translator.c_in, None))
        self.label_31.setText(QCoreApplication.translate("Form", self.text_translator.d_in, None))
        self.label_23.setText(QCoreApplication.translate("Form", self.text_translator.a_out, None))
        self.label_32.setText(QCoreApplication.translate("Form", self.text_translator.b_in, None))
        self.label_4.setText(QCoreApplication.translate("Form", self.text_translator.d_out, None))
        self.label_24.setText(QCoreApplication.translate("Form", self.text_translator.b_out, None))
        self.label_25.setText(QCoreApplication.translate("Form", self.text_translator.c_out, None))
        self.label_11.setText(QCoreApplication.translate("Form", self.text_translator.a_in, None))
        self.sidewiseCountMatrixDisplay.setTabText(self.sidewiseCountMatrixDisplay.indexOf(self.busTab), QCoreApplication.translate("Form", self.text_translator.buses, None))
        self.label_28.setText(QCoreApplication.translate("Form", self.text_translator.c_in, None))
        self.label_29.setText(QCoreApplication.translate("Form", self.text_translator.d_in, None))
        self.label_27.setText(QCoreApplication.translate("Form", self.text_translator.b_in, None))
        self.label_8.setText(QCoreApplication.translate("Form", self.text_translator.a_in, None))
        self.label_21.setText(QCoreApplication.translate("Form", self.text_translator.a_out, None))
        self.label_22.setText(QCoreApplication.translate("Form", self.text_translator.b_out, None))
        self.label_20.setText(QCoreApplication.translate("Form", self.text_translator.c_out, None))
        self.label_3.setText(QCoreApplication.translate("Form", self.text_translator.d_out, None))
        self.sidewiseCountMatrixDisplay.setTabText(self.sidewiseCountMatrixDisplay.indexOf(self.bicycleTab), QCoreApplication.translate("Form", self.text_translator.bicycles, None))
        self.label_33.setText(QCoreApplication.translate("Form", self.text_translator.c_in, None))
        self.label_34.setText(QCoreApplication.translate("Form", self.text_translator.d_in, None))
        self.label_35.setText(QCoreApplication.translate("Form", self.text_translator.b_in, None))
        self.label_12.setText(QCoreApplication.translate("Form", self.text_translator.a_in, None))
        self.label_26.setText(QCoreApplication.translate("Form", self.text_translator.a_out, None))
        self.label_36.setText(QCoreApplication.translate("Form", self.text_translator.b_out, None))
        self.label_37.setText(QCoreApplication.translate("Form", self.text_translator.c_out, None))
        self.label_6.setText(QCoreApplication.translate("Form", self.text_translator.d_out, None))
        self.sidewiseCountMatrixDisplay.setTabText(self.sidewiseCountMatrixDisplay.indexOf(self.mcycleTab), QCoreApplication.translate("Form", self.text_translator.motorcycles, None))
        self.label_49.setText(QCoreApplication.translate("Form", self.text_translator.b_in, None))
        self.label_38.setText(QCoreApplication.translate("Form", self.text_translator.c_out, None))
        self.label_43.setText(QCoreApplication.translate("Form", self.text_translator.d_out, None))
        self.label_10.setText(QCoreApplication.translate("Form", self.text_translator.a_in, None))
        self.label_40.setText(QCoreApplication.translate("Form", self.text_translator.b_out, None))
        self.label_46.setText(QCoreApplication.translate("Form", self.text_translator.c_in, None))
        self.label_47.setText(QCoreApplication.translate("Form", self.text_translator.d_in, None))
        self.label_5.setText(QCoreApplication.translate("Form", self.text_translator.a_out, None))
        self.sidewiseCountMatrixDisplay.setTabText(self.sidewiseCountMatrixDisplay.indexOf(self.truckTab), QCoreApplication.translate("Form", self.text_translator.trucks, None))
        self.label_41.setText(QCoreApplication.translate("Form", self.text_translator.d_in, None))
        self.label_44.setText(QCoreApplication.translate("Form", self.text_translator.c_in, None))
        self.label_54.setText(QCoreApplication.translate("Form", self.text_translator.b_out, None))
        self.label_56.setText(QCoreApplication.translate("Form", self.text_translator.c_out, None))
        self.label_50.setText(QCoreApplication.translate("Form", self.text_translator.b_in, None))
        self.label_57.setText(QCoreApplication.translate("Form", self.text_translator.d_out, None))
        self.label_13.setText(QCoreApplication.translate("Form", self.text_translator.a_in, None))
        self.label_7.setText(QCoreApplication.translate("Form", self.text_translator.a_out, None))
        self.aInLabel.setText(QCoreApplication.translate("Form", self.text_translator.a_in, None))
        self.bInLabel.setText(QCoreApplication.translate("Form", self.text_translator.b_in, None))
        self.cInLabel.setText(QCoreApplication.translate("Form", self.text_translator.c_in, None))
        self.dInLabel.setText(QCoreApplication.translate("Form", self.text_translator.d_in, None))
        self.sidewiseCountMatrixDisplay.setTabText(self.sidewiseCountMatrixDisplay.indexOf(self.tab), QCoreApplication.translate("Form", self.text_translator.total, None))   
