import sys
import pyqtgraph as pg
from PySide2 import QtWidgets
from PySide2.QtCore import Signal
from qt.Show_Calendar import Ui_MainWindow
from qt.ChartWindow import ChartWindow
from DrawLineWidget import DrawLineWidget
from PySide2.QtWidgets import QMessageBox, QAction
from yolov5.utils.dataloaders import LoadHikvisionCamera


class ShowCalendarWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    process_done_signal = Signal()
    def __init__(self, db_conn, db_cur):
        super(ShowCalendarWindow, self).__init__()
        self.db_conn = db_conn
        self.db_cur = db_cur
        self.setupUi(self)
        self.setupSignalSlots()
    
    def setCamId(self, cam_id):
        self.remove_cam_id = cam_id

    def set_db_conn_cur(self, db_conn, db_cur):
        self.db_conn = db_conn
        self.db_cur = db_cur

    def setupSignalSlots(self):
        self.showDataBtn.clicked.connect(self.showLineChart)
        self.calendarWidget.selectionChanged.connect(self.onSelectionChange)

    def onSelectionChange(self):
        # self.inputCamIP.text()
        # self.inputCamUsername.text()
        # self.inputCamPassword.text()
        # self.inputCamDisplayName.text()
        selected_date = self.calendarWidget.selectedDate()
        print(selected_date)
        print(dir(selected_date))
        self.label.setText(str(selected_date.toString()))

        # self.process_done_signal.emit()
        # self.hide()
    
    def showLineChart(self):
        print('Button clicked')
        self.chart_window = ChartWindow()
        self.chart_window.show()
