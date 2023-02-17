
from typing import Tuple
from PySide2.QtCore import QPoint, QUrl, Signal, Slot
# from PyQt5 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QFileDialog, QMessageBox, QErrorMessage, QWidget, QMainWindow
from PySide2.QtGui import QImage, QPixmap, Qt, QIcon
from qt.Ui_Form import Ui_Form
import numpy as np
import cv2, os, math
import pyqtgraph as pg

from model import Model

from qt.add_camera_view_controller import AddCameraWindow
from qt.remove_camera_view_controller import RemoveCameraWindow
from qt.edit_camera_view_controller import EditCameraWindow
from qt.show_calendar_view_controller import ShowCalendarWindow


class ViewController(QWidget, Ui_Form):
    startInferenceSignal = Signal()
    startCountingSignal = Signal()
    startCountingAnalysisSignal = Signal()

    def __init__(self, model, conn, cur):
        super().__init__()
        self.model = model
        self.setupUi(self)
        self.inputVideoFile = ''
        self.outputVideoFile = ''
        self.outputDataFile = ''
        self.cacheDataFile = ''
        self.maskFile = ''
        # self.carPreviewTable.setHorizontalHeaderLabels(['Preview', 'ID']) # Shakh
        # self.truckPreviewTable.setHorizontalHeaderLabels(['Preview', 'ID'])
        self.frameView.ui.histogram.hide()
        self.frameView.ui.roiBtn.hide()
        self.frameView.ui.menuBtn.hide()
        self.frameView.view.setMouseEnabled(False,False)
        self.imgMask = None
        
        self.visualizeMarkerStart = QPoint(200,200)
        self.visualizeMarkerEnd = QPoint(500,500)
        self.visualizeMarker = pg.LineROI(self.visualizeMarkerStart, self.visualizeMarkerEnd, 50)
        self.finishLine = pg.RectROI((200,200), (200,200), rotatable=True, resizable=True)
        # self.CARDINAL_SIDES = ['North', 'East', 'West', 'South']

        # sqlite3 db files
        self.db_conn = conn
        self.db_cur = cur
        self.is_refresh_clicked = 0

        self.add_cam_window = AddCameraWindow(self.db_conn, self.db_cur)
        self.remove_camera_window = RemoveCameraWindow(self.db_conn, self.db_cur)
        self.edit_camera_window = EditCameraWindow(self.db_conn, self.db_cur)
        self.show_calendar_window = ShowCalendarWindow(self.db_conn, self.db_cur)
        self.setupSignalSlots()

    def setupSignalSlots(self):
        # self.loadVideoBtn.clicked.connect(self.openVideoFile)

        # self.setOutputFileBtn.clicked.connect(self.getOutputFileName)
        self.startInferenceBtn.clicked.connect(self.startInference)
        self.startInferenceSignal.connect(self.model.startInference)
        # self.updateDbSignal.connect(self.update_db)
        self.addCamBtn.clicked.connect(self.openAddCamWindow)
        self.editCameraBtn.clicked.connect(self.openEditCamWindow)
        self.removeCameraBtn.clicked.connect(self.openRemoveCamWindow)
        self.showDataBtn.clicked.connect(self.openShowCalendarWindow)
        self.model.frame_update_signal.connect(self.updateFrame)
        self.refreshCamerasBtn.clicked.connect(self.updateCameraDropDown)
        self.comboBox.activated[str].connect(self.onActivated)
        # self.model.max_frame_update_signal.connect(self.updateMaxFrameNum)
        # self.loadCacheBtn.clicked.connect(self.openCacheFile)
        # self.countBtn.clicked.connect(self.startCounting)
        # self.startCountingSignal.connect(self.model.startCounting)
        # self.countAnalyzeBtn.clicked.connect(self.startCountingAnalysis)
        # self.startCountingAnalysisSignal.connect(self.model.startCountingAnalysis)
        self.model.vehicle_count_signal.connect(self.updateVehicleCount)
        self.model.process_done_signal.connect(self.onProcessDone)
        self.add_cam_window.process_done_signal.connect(self.onCamBtnsClosed)
        self.remove_camera_window.process_done_signal.connect(self.onCamBtnsClosed)
        self.edit_camera_window.process_done_signal.connect(self.onCamBtnsClosed)
        self.stopProcessBtn.clicked.connect(self.stopProcess)
        # self.drawMaskBtn.clicked.connect(self.drawMask)
        # self.resetMaskBtn.clicked.connect(self.resetMask)
        # self.setMaskFileBtn.clicked.connect(self.openMaskFile)
        # self.saveMaskBtn.clicked.connect(self.saveMask)

        # self.yFilterVectorSpn.valueChanged.connect(self.updateVectorDirectionLabel)
        # self.countMethodCmb.currentIndexChanged.connect(self.countingMethodSwitcher.setCurrentIndex)
        # self.frameSlider.valueChanged.connect(self.model.previewFrame)
        # self.visualizeChk.toggled.connect(self.visualizeCountingParam)
        # self.finishLineChk.toggled.connect(self.showFinishLine)

#====================== File Dialog Functions =====================
    def onActivated(self, text):
        cam_id = text.split('.')[0]
        print(cam_id)
        self.db_cur.execute(f"SELECT * FROM cameras WHERE id = {cam_id}")
        camera_info = self.db_cur.fetchall()
        print(camera_info)
        cardinal_direction_points = [
                                        [[camera_info[0][5], camera_info[0][6]], [camera_info[0][7], camera_info[0][8]]], # north
                                        [[camera_info[0][9], camera_info[0][10]], [camera_info[0][11], camera_info[0][12]]], # east
                                        [[camera_info[0][13], camera_info[0][14]], [camera_info[0][15],camera_info[0][16]]], # west
                                        [[camera_info[0][17], camera_info[0][18]], [camera_info[0][19], camera_info[0][20]]] # south
                                    ]
        self.model.setCameraInfo(camera_info[0][0], camera_info[0][1], camera_info[0][2], camera_info[0][3], camera_info[0][4], cardinal_direction_points)

    def openShowCalendarWindow(self):
        self.show_calendar_window.set_db_conn_cur(self.db_conn, self.db_cur)
        self.show_calendar_window.show()

    def update_db(self, query):
        self.db_cur.execute(query)
        self.db_conn.commit()

    def showPopup(self, message):
        msg = QMessageBox()
        msg.setWindowTitle('Ogohlantirish!')
        msg.setText(message)
        msg.setIcon(QMessageBox.Warning)

        x = msg.exec_()
    
    def onCamBtnsClosed(self):
        # self.showPopup(message)
        self.db_cur.execute(f"SELECT * FROM cameras")
        cameras = self.db_cur.fetchall()
        self.enableControls(False)
        if cameras:
            first_cam_id = cameras[0][0]
            self.db_cur.execute(f"SELECT * FROM cameras WHERE id = {first_cam_id}")
            camera_info = self.db_cur.fetchall()
            print(camera_info)
            cardinal_direction_points = [
                                            [[camera_info[0][5], camera_info[0][6]], [camera_info[0][7], camera_info[0][8]]], # north
                                            [[camera_info[0][9], camera_info[0][10]], [camera_info[0][11], camera_info[0][12]]], # east
                                            [[camera_info[0][13], camera_info[0][14]], [camera_info[0][15],camera_info[0][16]]], # west
                                            [[camera_info[0][17], camera_info[0][18]], [camera_info[0][19], camera_info[0][20]]] # south
                                        ]
            self.model.setCameraInfo(camera_info[0][0], camera_info[0][1], camera_info[0][2], camera_info[0][3], camera_info[0][4], cardinal_direction_points)
        else:
            self.showPopup('Bazada kameralar topilmadi. Iltimos oldin kamera qo\'shing')
        
    def openAddCamWindow(self):
        print('Opening camera add window')
        self.db_cur.execute(f"SELECT * FROM cameras")
        num_added_cameras = len(self.db_cur.fetchall())
        print(type(num_added_cameras), num_added_cameras)
        if num_added_cameras >= 3:
            self.showPopup('Kameralar soni 4taga teng. Boshqa kamera qo\'sha olmaysiz')
            return None
        self.add_cam_window.set_db_conn_cur(self.db_conn, self.db_cur)
        self.enableControls(False)
        self.add_cam_window.show()
    
    def openRemoveCamWindow(self):
        print('Opening camera remove window')
        self.db_cur.execute(f"SELECT * FROM cameras")
        cameras = self.db_cur.fetchall()
        num_added_cameras = len(cameras)
        print(type(num_added_cameras), num_added_cameras)
        if not num_added_cameras:
            self.showPopup('Bazada kameralar topilmadi. Iltimos oldin kamera qo\'shing')
            return None
        first_cam_id = cameras[0][0]
        self.remove_camera_window.setCamId(first_cam_id)
        self.remove_camera_window.set_db_conn_cur(self.db_conn, self.db_cur)
        self.enableControls(False)
        self.remove_camera_window.show()
    
    def openEditCamWindow(self):
        print('Opening camera Edit window')
        self.db_cur.execute(f"SELECT * FROM cameras")
        cameras = self.db_cur.fetchall()
        num_added_cameras = len(cameras)
        print(type(num_added_cameras), num_added_cameras)
        if not num_added_cameras:
            self.showPopup('Bazada kameralar topilmadi. Iltimos oldin kamera qo\'shing')
            return None
        first_cam_id = cameras[0][0]
        self.edit_camera_window.setCamId(first_cam_id)
        self.edit_camera_window.set_db_conn_cur(self.db_conn, self.db_cur)
        self.edit_camera_window.setCameraInfos()
        self.enableControls(False)
        self.edit_camera_window.show()
    
    def updateCameraDropDown(self):
        self.db_cur.execute(f"SELECT * FROM cameras")
        cameras = self.db_cur.fetchall()
        camera_names = [row[4] for row in cameras]
        if not self.is_refresh_clicked and cameras:
            print('Refresh pressed and camera id set to : ', camera_names[0].split('.')[0])
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


    @Slot(int,int,int,np.ndarray)
    def updateVehicleCount(self, class_id, uid, count, img, row_num, preview_num):
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
        print(class_id, uid, count, row_num, preview_num)
        if row_num == '00':  # NN
            if class_id == 1:
                self.truckCount.display(count)
                # table = self.truckPreviewTable
            elif class_id == 2:
                self.carCount.display(count)
                # table = self.carPreviewTable
            elif class_id == 3:
                self.busCount.display(count)
                # table = self.busPreviewTable
            elif class_id == 4:
                self.NNbicycleCount.display(count)
            elif class_id == 5:
                self.NNmcycle.display(count)
            else:
                return
        elif row_num == '01':  # NE
            if class_id == 1:
                self.NEtruckCount.display(count)
                # table = self.truckPreviewTable
            elif class_id == 2:
                self.NEcarCount.display(count)
                # table = self.carPreviewTable
            elif class_id == 3:
                self.NEbusCount.display(count)
                # table = self.busPreviewTable
            elif class_id == 4:
                self.NEbicycleCount.display(count)
            elif class_id == 5:
                self.NEmcycle.display(count)
            else:
                return
        elif row_num == '02':  # NW
            if class_id == 1:
                self.NWtruckCount.display(count)
                # table = self.truckPreviewTable
            elif class_id == 2:
                self.NWcarCount.display(count)
                # table = self.carPreviewTable
            elif class_id == 3:
                self.NWbusCount.display(count)
                # table = self.busPreviewTable
            elif class_id == 4:
                self.NWbicycleCount.display(count)
            elif class_id == 5:
                self.NWmcycle.display(count)
            else:
                return
        elif row_num == '03':  # NS
            if class_id == 1:
                self.NStruckCount.display(count)
                # table = self.truckPreviewTable
            elif class_id == 2:
                self.NScarCount.display(count)
                # table = self.carPreviewTable
            elif class_id == 3:
                self.NSbusCount.display(count)
                # table = self.busPreviewTable
            elif class_id == 4:
                self.NSbicycleCount.display(count)
            elif class_id == 5:
                self.NSmcycle.display(count)
            else:
                return
        elif row_num == '10':  # EN
            if class_id == 1:
                self.ENtruckCount.display(count)
                # table = self.truckPreviewTable
            elif class_id == 2:
                self.ENcarCount.display(count)
                # table = self.carPreviewTable
            elif class_id == 3:
                self.ENbusCount.display(count)
                # table = self.busPreviewTable
            elif class_id == 4:
                self.ENbicycleCount.display(count)
            elif class_id == 5:
                self.ENmcycle.display(count)
            else:
                return
        elif row_num == '11':  # EE
            if class_id == 1:
                self.EEtruckCount.display(count)
                # table = self.truckPreviewTable
            elif class_id == 2:
                self.EEcarCount.display(count)
                # table = self.carPreviewTable
            elif class_id == 3:
                self.EEbusCount.display(count)
                # table = self.busPreviewTable
            elif class_id == 4:
                self.EEbicycleCount.display(count)
            elif class_id == 5:
                self.EEmcycle.display(count)
            else:
                return
        elif row_num == '12':  # EW
            if class_id == 1:
                self.EWtruckCount.display(count)
                # table = self.truckPreviewTable
            elif class_id == 2:
                self.EWcarCount.display(count)
                # table = self.carPreviewTable
            elif class_id == 3:
                self.EWbusCount.display(count)
                # table = self.busPreviewTable
            elif class_id == 4:
                self.EWbicycleCount.display(count)
            elif class_id == 5:
                self.EWmcycle.display(count)
            else:
                return
        elif row_num == '13':  # ES
            if class_id == 1:
                self.EStruckCount.display(count)
                # table = self.truckPreviewTable
            elif class_id == 2:
                self.EScarCount.display(count)
                # table = self.carPreviewTable
            elif class_id == 3:
                self.ESbusCount.display(count)
                # table = self.busPreviewTable
            elif class_id == 4:
                self.ESbicycleCount.display(count)
            elif class_id == 5:
                self.ESmcycle.display(count)
            else:
                return
        elif row_num == '20':  # WN
            if class_id == 1:
                self.WNtruckCount.display(count)
                # table = self.truckPreviewTable
            elif class_id == 2:
                self.WNcarCount.display(count)
                # table = self.carPreviewTable
            elif class_id == 3:
                self.WNbusCount.display(count)
                # table = self.busPreviewTable
            elif class_id == 4:
                self.WNbicycleCount.display(count)
            elif class_id == 5:
                self.WNmcycle.display(count)
            else:
                return
        elif row_num == '21':  # WE
            if class_id == 1:
                self.WEtruckCount.display(count)
                # table = self.truckPreviewTable
            elif class_id == 2:
                self.WEcarCount.display(count)
                # table = self.carPreviewTable
            elif class_id == 3:
                self.WEbusCount.display(count)
                # table = self.busPreviewTable
            elif class_id == 4:
                self.WEbicycleCount.display(count)
            elif class_id == 5:
                self.WEmcycle.display(count)
            else:
                return
        elif row_num == '22':  # WW
            print('I am in row 22')
            if class_id == 1:
                print('Before truck count')
                self.WWtruckCount.display(count)
                print('After truck count')
                # table = self.truckPreviewTable
                print('After table update')
            elif class_id == 2:
                self.WWcarCount.display(count)
                # table = self.carPreviewTable
            elif class_id == 3:
                self.WWbusCount.display(count)
                # table = self.busPreviewTable
            elif class_id == 4:
                self.WWbicycleCount.display(count)
            elif class_id == 5:
                self.WWmcycle.display(count)
            else:
                return
        elif row_num == '23':  # WS
            if class_id == 1:
                self.WStruckCount.display(count)
                # table = self.truckPreviewTable
            elif class_id == 2:
                self.WScarCount.display(count)
                # table = self.carPreviewTable
            elif class_id == 3:
                self.WSbusCount.display(count)
                # table = self.busPreviewTable
            elif class_id == 4:
                self.WSbicycleCount.display(count)
            elif class_id == 5:
                self.WSmcycle.display(count)
            else:
                return
        elif row_num == '30':  # SN
            if class_id == 1:
                self.SNtruckCount.display(count)
                # table = self.truckPreviewTable
            elif class_id == 2:
                self.SNcarCount.display(count)
                # table = self.carPreviewTable
            elif class_id == 3:
                self.SNbusCount.display(count)
                # table = self.busPreviewTable
            elif class_id == 4:
                self.SNbicycleCount.display(count)
            elif class_id == 5:
                self.SNmcycle.display(count)
            else:
                return
        elif row_num == '31':  # SE
            if class_id == 1:
                self.SEtruckCount.display(count)
                # table = self.truckPreviewTable
            elif class_id == 2:
                self.SEcarCount.display(count)
                # table = self.carPreviewTable
            elif class_id == 3:
                self.SEbusCount.display(count)
                # table = self.busPreviewTable
            elif class_id == 4:
                self.SEbicycleCount.display(count)
            elif class_id == 5:
                self.SEmcycle.display(count)
            else:
                return
        elif row_num == '32':  # SW
            if class_id == 1:
                self.SWtruckCount.display(count)
                # table = self.truckPreviewTable
            elif class_id == 2:
                self.SWcarCount.display(count)
                # table = self.carPreviewTable
            elif class_id == 3:
                self.SWbusCount.display(count)
                # table = self.busPreviewTable
            elif class_id == 4:
                self.SWbicycleCount.display(count)
            elif class_id == 5:
                self.SWmcycle.display(count)
            else:
                return
        elif row_num == '33':  # SS
            if class_id == 1:
                self.SStruckCount.display(count)
                # table = self.truckPreviewTable
            elif class_id == 2:
                self.SScarCount.display(count)
                # table = self.carPreviewTable
            elif class_id == 3:
                self.SSbusCount.display(count)
                # table = self.busPreviewTable
            elif class_id == 4:
                self.SSbicycleCount.display(count)
            elif class_id == 5:
                self.SSmcycle.display(count)
            else:
                return
        
        # if class_id == 1:
        #     self.truckCount.display(count)
        #     table = self.truckPreviewTable
        # elif class_id == 2:
        #     self.carCount.display(count)
        #     table = self.carPreviewTable
        # elif class_id == 3:
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
        self.enableControls(False)
        print('before inference:  ', self.db_cur)
        self.model.update_db_conn_cur(self.db_conn, self.db_cur)
        self.startInferenceSignal.emit()
    
    def stopProcess(self):
        self.db_conn = self.model.db_conn
        self.db_cur = self.model.db_cur
        self.model.stopInference()
        self.model.stopCountingAnalysis()
        self.enableControls(True)

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
        self.mediaGBox.setEnabled(state)
        self.cameraEditBox.setEnabled(state)
        self.addCamBtn.setEnabled(state)
        self.editCameraBtn.setEnabled(state)
        self.removeCameraBtn.setEnabled(state)

    def onProcessDone(self):
        self.enableControls(True)

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

