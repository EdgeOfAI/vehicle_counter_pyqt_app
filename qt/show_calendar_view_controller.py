import sys
import datetime
import pyqtgraph as pg
from PySide2 import QtWidgets
from PySide2.QtCore import Signal
from qt.Show_Calendar import Ui_MainWindow
from qt.ChartWindow import ChartWindow, BarChartWindow
from DrawLineWidget import DrawLineWidget
from PySide2.QtWidgets import QMessageBox, QAction
from PySide2.QtCore import QCoreApplication
from PySide2.QtGui import QIcon
from yolov5.utils.dataloaders import LoadHikvisionCamera


class ShowCalendarWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    process_done_signal = Signal()
    def __init__(self, db_conn, db_cur, qss_file, icon_path):
        super(ShowCalendarWindow, self).__init__()
        self.qss_file = qss_file
        self.db_conn = db_conn
        self.db_cur = db_cur
        self.icon_path = icon_path
        self.setupUi(self)
        self.setCameraComboBox()
        self.setupSignalSlots()
    
    def setCamId(self, cam_id):
        self.remove_cam_id = cam_id
    
    def closeEvent(self, event):
        self.process_done_signal.emit()
        event.accept()
    
    def setCameraComboBox(self):
        self.db_cur.execute(f"SELECT * FROM cameras")
        cameras = self.db_cur.fetchall()
        camera_names = [row[4] for row in cameras]
        camera_names_with_default = ['0. Video'] + camera_names
        self.comboBox.clear()
        self.comboBox.addItems(camera_names_with_default)

    def set_db_conn_cur(self, db_conn, db_cur):
        self.db_conn = db_conn
        self.db_cur = db_cur
        self.setCameraComboBox()

    def setupSignalSlots(self):
        self.showDataBtn.clicked.connect(self.showLineChart)
        self.pushButton.clicked.connect(self.showCardinalwiseData)
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
    
    def showCardinalwiseData(self):
        cam_name = self.comboBox.currentText()
        cam_id = cam_name.split('.')[0]
        selected_date = self.calendarWidget.selectedDate().toString()
        selected_date = datetime.datetime.strptime(' '.join(selected_date.split(' ')[1:]), '%b %d %Y')
        self.db_cur.execute(f"SELECT * FROM vehicles WHERE camera_id = {cam_id}")
        vehicles = self.db_cur.fetchall()
        N_in = [vehicle for vehicle in vehicles if vehicle[8]=='North' and datetime.datetime.fromisoformat(vehicle[11]).day == selected_date.day and datetime.datetime.fromisoformat(vehicle[11]).month == selected_date.month and datetime.datetime.fromisoformat(vehicle[11]).year == selected_date.year]
        E_in = [vehicle for vehicle in vehicles if vehicle[8] == 'East' and datetime.datetime.fromisoformat(vehicle[11]).day == selected_date.day and datetime.datetime.fromisoformat(vehicle[11]).month == selected_date.month and datetime.datetime.fromisoformat(vehicle[11]).year == selected_date.year]
        W_in = [vehicle for vehicle in vehicles if vehicle[8] == 'West' and datetime.datetime.fromisoformat(vehicle[11]).day == selected_date.day and datetime.datetime.fromisoformat(vehicle[11]).month == selected_date.month and datetime.datetime.fromisoformat(vehicle[11]).year == selected_date.year]
        S_in = [vehicle for vehicle in vehicles if vehicle[8] == 'South' and datetime.datetime.fromisoformat(vehicle[11]).day == selected_date.day and datetime.datetime.fromisoformat(vehicle[11]).month == selected_date.month and datetime.datetime.fromisoformat(vehicle[11]).year == selected_date.year]

        NN = len([vehicle for vehicle in N_in if vehicle[9] == 'North'])
        NE = len([vehicle for vehicle in N_in if vehicle[9] == 'East'])
        NW = len([vehicle for vehicle in N_in if vehicle[9] == 'West'])
        NS = len([vehicle for vehicle in N_in if vehicle[9] == 'South'])

        EN = len([vehicle for vehicle in E_in if vehicle[9] == 'North'])
        EE = len([vehicle for vehicle in E_in if vehicle[9] == 'East'])
        EW = len([vehicle for vehicle in E_in if vehicle[9] == 'West'])
        ES = len([vehicle for vehicle in E_in if vehicle[9] == 'South']) 

        WN = len([vehicle for vehicle in W_in if vehicle[9] == 'North'])
        WE = len([vehicle for vehicle in W_in if vehicle[9] == 'East'])
        WW = len([vehicle for vehicle in W_in if vehicle[9] == 'West'])
        WS = len([vehicle for vehicle in W_in if vehicle[9] == 'South'])

        SN = len([vehicle for vehicle in S_in if vehicle[9] == 'North'])
        SE = len([vehicle for vehicle in S_in if vehicle[9] == 'East'])
        SW = len([vehicle for vehicle in S_in if vehicle[9] == 'West'])
        SS = len([vehicle for vehicle in S_in if vehicle[9] == 'South'])

        data = [NN, NE, NW, NS, EN, EE, EW, ES, WN, WE, WW, WS, SN, SE, SW, SS]

        self.bar_chart_window = BarChartWindow(self.icon_path, self.qss_file, 'Cardinalwise Data | Bar Chart', data)
        # self.bar_chart_window.show()
    
    def showLineChart(self):
        print('Button clicked')
        cam_name = self.comboBox.currentText()
        cam_id = cam_name.split('.')[0]
        selected_date = self.calendarWidget.selectedDate().toString()
        selected_date = datetime.datetime.strptime(' '.join(selected_date.split(' ')[1:]), '%b %d %Y')
        self.db_cur.execute(f"SELECT * FROM vehicles WHERE camera_id = {cam_id}")
        vehicles = self.db_cur.fetchall()
        vehicles = [vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).day == selected_date.day and datetime.datetime.fromisoformat(vehicle[11]).month == selected_date.month and datetime.datetime.fromisoformat(vehicle[11]).year == selected_date.year]
        car_hour_0 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 0 and vehicle[10] == 2])
        car_hour_1= len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 1 and vehicle[10] == 2])
        car_hour_2 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 2 and vehicle[10] == 2])
        car_hour_3 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 3 and vehicle[10] == 2])
        car_hour_4 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 4 and vehicle[10] == 2])
        car_hour_5 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 5 and vehicle[10] == 2])
        car_hour_6 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 6 and vehicle[10] == 2])
        car_hour_7 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 7 and vehicle[10] == 2])
        car_hour_8 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 8 and vehicle[10] == 2])
        car_hour_9 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 9 and vehicle[10] == 2])
        car_hour_10 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 10 and vehicle[10] == 2])
        car_hour_11 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 11 and vehicle[10] == 2])
        car_hour_12 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 12 and vehicle[10] == 2])
        car_hour_13 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 13 and vehicle[10] == 2])
        car_hour_14 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 14 and vehicle[10] == 2])
        car_hour_15 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 15 and vehicle[10] == 2])
        car_hour_16 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 16 and vehicle[10] == 2])
        car_hour_17 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 17 and vehicle[10] == 2])
        car_hour_18 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 18 and vehicle[10] == 2])
        car_hour_19 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 19 and vehicle[10] == 2])
        car_hour_20 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 20 and vehicle[10] == 2])
        car_hour_21 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 21 and vehicle[10] == 2])
        car_hour_22 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 22 and vehicle[10] == 2])
        car_hour_23 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 23 and vehicle[10] == 2])

        truck_hour_0 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 0 and vehicle[10] == 1])
        truck_hour_1= len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 1 and vehicle[10] == 1])
        truck_hour_2 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 2 and vehicle[10] == 1])
        truck_hour_3 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 3 and vehicle[10] == 1])
        truck_hour_4 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 4 and vehicle[10] == 1])
        truck_hour_5 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 5 and vehicle[10] == 1])
        truck_hour_6 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 6 and vehicle[10] == 1])
        truck_hour_7 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 7 and vehicle[10] == 1])
        truck_hour_8 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 8 and vehicle[10] == 1])
        truck_hour_9 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 9 and vehicle[10] == 1])
        truck_hour_10 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 10 and vehicle[10] == 1])
        truck_hour_11 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 11 and vehicle[10] == 1])
        truck_hour_12 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 12 and vehicle[10] == 1])
        truck_hour_13 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 13 and vehicle[10] == 1])
        truck_hour_14 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 14 and vehicle[10] == 1])
        truck_hour_15 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 15 and vehicle[10] == 1])
        truck_hour_16 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 16 and vehicle[10] == 1])
        truck_hour_17 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 17 and vehicle[10] == 1])
        truck_hour_18 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 18 and vehicle[10] == 1])
        truck_hour_19 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 19 and vehicle[10] == 1])
        truck_hour_20 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 20 and vehicle[10] == 1])
        truck_hour_21 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 21 and vehicle[10] == 1])
        truck_hour_22 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 22 and vehicle[10] == 1])
        truck_hour_23 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 23 and vehicle[10] == 1])

        bus_hour_0 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 0 and vehicle[10] == 3])
        bus_hour_1= len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 1 and vehicle[10] == 3])
        bus_hour_2 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 2 and vehicle[10] == 3])
        bus_hour_3 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 3 and vehicle[10] == 3])
        bus_hour_4 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 4 and vehicle[10] == 3])
        bus_hour_5 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 5 and vehicle[10] == 3])
        bus_hour_6 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 6 and vehicle[10] == 3])
        bus_hour_7 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 7 and vehicle[10] == 3])
        bus_hour_8 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 8 and vehicle[10] == 3])
        bus_hour_9 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 9 and vehicle[10] == 3])
        bus_hour_10 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 10 and vehicle[10] == 3])
        bus_hour_11 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 11 and vehicle[10] == 3])
        bus_hour_12 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 12 and vehicle[10] == 3])
        bus_hour_13 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 13 and vehicle[10] == 3])
        bus_hour_14 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 14 and vehicle[10] == 3])
        bus_hour_15 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 15 and vehicle[10] == 3])
        bus_hour_16 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 16 and vehicle[10] == 3])
        bus_hour_17 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 17 and vehicle[10] == 3])
        bus_hour_18 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 18 and vehicle[10] == 3])
        bus_hour_19 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 19 and vehicle[10] == 3])
        bus_hour_20 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 20 and vehicle[10] == 3])
        bus_hour_21 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 21 and vehicle[10] == 3])
        bus_hour_22 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 22 and vehicle[10] == 3])
        bus_hour_23 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 23 and vehicle[10] == 3])

        bicycle_hour_0 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 0 and vehicle[10] == 4])
        bicycle_hour_1= len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 1 and vehicle[10] == 4])
        bicycle_hour_2 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 2 and vehicle[10] == 4])
        bicycle_hour_3 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 3 and vehicle[10] == 4])
        bicycle_hour_4 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 4 and vehicle[10] == 4])
        bicycle_hour_5 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 5 and vehicle[10] == 4])
        bicycle_hour_6 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 6 and vehicle[10] == 4])
        bicycle_hour_7 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 7 and vehicle[10] == 4])
        bicycle_hour_8 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 8 and vehicle[10] == 4])
        bicycle_hour_9 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 9 and vehicle[10] == 4])
        bicycle_hour_10 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 10 and vehicle[10] == 4])
        bicycle_hour_11 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 11 and vehicle[10] == 4])
        bicycle_hour_12 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 12 and vehicle[10] == 4])
        bicycle_hour_13 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 13 and vehicle[10] == 4])
        bicycle_hour_14 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 14 and vehicle[10] == 4])
        bicycle_hour_15 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 15 and vehicle[10] == 4])
        bicycle_hour_16 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 16 and vehicle[10] == 4])
        bicycle_hour_17 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 17 and vehicle[10] == 4])
        bicycle_hour_18 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 18 and vehicle[10] == 4])
        bicycle_hour_19 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 19 and vehicle[10] == 4])
        bicycle_hour_20 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 20 and vehicle[10] == 4])
        bicycle_hour_21 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 21 and vehicle[10] == 4])
        bicycle_hour_22 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 22 and vehicle[10] == 4])
        bicycle_hour_23 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 23 and vehicle[10] == 4])

        mcycle_hour_0 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 0 and vehicle[10] == 5])
        mcycle_hour_1= len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 1 and vehicle[10] == 5])
        mcycle_hour_2 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 2 and vehicle[10] == 5])
        mcycle_hour_3 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 3 and vehicle[10] == 5])
        mcycle_hour_4 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 4 and vehicle[10] == 5])
        mcycle_hour_5 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 5 and vehicle[10] == 5])
        mcycle_hour_6 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 6 and vehicle[10] == 5])
        mcycle_hour_7 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 7 and vehicle[10] == 5])
        mcycle_hour_8 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 8 and vehicle[10] == 5])
        mcycle_hour_9 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 9 and vehicle[10] == 5])
        mcycle_hour_10 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 10 and vehicle[10] == 5])
        mcycle_hour_11 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 11 and vehicle[10] == 5])
        mcycle_hour_12 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 12 and vehicle[10] == 5])
        mcycle_hour_13 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 13 and vehicle[10] == 5])
        mcycle_hour_14 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 14 and vehicle[10] == 5])
        mcycle_hour_15 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 15 and vehicle[10] == 5])
        mcycle_hour_16 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 16 and vehicle[10] == 5])
        mcycle_hour_17 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 17 and vehicle[10] == 5])
        mcycle_hour_18 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 18 and vehicle[10] == 5])
        mcycle_hour_19 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 19 and vehicle[10] == 5])
        mcycle_hour_20 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 20 and vehicle[10] == 5])
        mcycle_hour_21 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 21 and vehicle[10] == 5])
        mcycle_hour_22 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 22 and vehicle[10] == 5])
        mcycle_hour_23 = len([vehicle for vehicle in vehicles if datetime.datetime.fromisoformat(vehicle[11]).hour == 23 and vehicle[10] == 5])
        # print(times)
        # times = [ for vehicle in vehicles]
        print(
            len([car_hour_0,car_hour_1,car_hour_2, car_hour_3, car_hour_4, car_hour_5, car_hour_6, car_hour_7, car_hour_8, car_hour_9, car_hour_10, car_hour_11, car_hour_12, car_hour_13, car_hour_14, car_hour_15, car_hour_16, car_hour_17, car_hour_18, car_hour_19, car_hour_20, car_hour_21, car_hour_22, car_hour_23]),
            len([truck_hour_0, truck_hour_1, truck_hour_2, truck_hour_3, truck_hour_4, truck_hour_5, truck_hour_6, truck_hour_7, truck_hour_8, truck_hour_9, truck_hour_10, truck_hour_11, truck_hour_12, truck_hour_13, truck_hour_14, truck_hour_15, truck_hour_16, truck_hour_17, truck_hour_18, truck_hour_19, truck_hour_20, truck_hour_21, truck_hour_22, truck_hour_23]),
            len([bus_hour_0, bus_hour_1, bus_hour_2, bus_hour_3, bus_hour_4, bus_hour_5, bus_hour_6, bus_hour_7, bus_hour_8, bus_hour_9, bus_hour_10, bus_hour_11, bus_hour_12, bus_hour_13, bus_hour_14, bus_hour_15, bus_hour_16, bus_hour_17, bus_hour_18, bus_hour_19, bus_hour_20, bus_hour_21, bus_hour_22, bus_hour_23]),
            len([bicycle_hour_0, bicycle_hour_1, bicycle_hour_2, bicycle_hour_3, bicycle_hour_4, bicycle_hour_5, bicycle_hour_6, bicycle_hour_7, bicycle_hour_8, bicycle_hour_9, bicycle_hour_10, bicycle_hour_11, bicycle_hour_12, bicycle_hour_13, bicycle_hour_14, bicycle_hour_15, bicycle_hour_16, bicycle_hour_17, bicycle_hour_18, bicycle_hour_19, bicycle_hour_20, bicycle_hour_21, bicycle_hour_22, bicycle_hour_23]),
            len([mcycle_hour_0, mcycle_hour_1, mcycle_hour_2, mcycle_hour_3, mcycle_hour_4, mcycle_hour_5, mcycle_hour_6, mcycle_hour_7, mcycle_hour_8, mcycle_hour_9, mcycle_hour_10, mcycle_hour_11, mcycle_hour_12, mcycle_hour_13, mcycle_hour_14, mcycle_hour_15, mcycle_hour_16, mcycle_hour_17, mcycle_hour_18, mcycle_hour_19, mcycle_hour_20, mcycle_hour_21, mcycle_hour_22, mcycle_hour_23])
        )
        self.chart_window = ChartWindow(
                                        cam_name if cam_name else 'No Cam',
                                        [car_hour_0,car_hour_1,car_hour_2, car_hour_3, car_hour_4, car_hour_5, car_hour_6, car_hour_7, car_hour_8, car_hour_9, car_hour_10, car_hour_11, car_hour_12, car_hour_13, car_hour_14, car_hour_15, car_hour_16, car_hour_17, car_hour_18, car_hour_19, car_hour_20, car_hour_21, car_hour_22, car_hour_23],
                                        [truck_hour_0, truck_hour_1, truck_hour_2, truck_hour_3, truck_hour_4, truck_hour_5, truck_hour_6, truck_hour_7, truck_hour_8, truck_hour_9, truck_hour_10, truck_hour_11, truck_hour_12, truck_hour_13, truck_hour_14, truck_hour_15, truck_hour_16, truck_hour_17, truck_hour_18, truck_hour_19, truck_hour_20, truck_hour_21, truck_hour_22, truck_hour_23],
                                        [bus_hour_0, bus_hour_1, bus_hour_2, bus_hour_3, bus_hour_4, bus_hour_5, bus_hour_6, bus_hour_7, bus_hour_8, bus_hour_9, bus_hour_10, bus_hour_11, bus_hour_12, bus_hour_13, bus_hour_14, bus_hour_15, bus_hour_16, bus_hour_17, bus_hour_18, bus_hour_19, bus_hour_20, bus_hour_21, bus_hour_22, bus_hour_23],
                                        [bicycle_hour_0, bicycle_hour_1, bicycle_hour_2, bicycle_hour_3, bicycle_hour_4, bicycle_hour_5, bicycle_hour_6, bicycle_hour_7, bicycle_hour_8, bicycle_hour_9, bicycle_hour_10, bicycle_hour_11, bicycle_hour_12, bicycle_hour_13, bicycle_hour_14, bicycle_hour_15, bicycle_hour_16, bicycle_hour_17, bicycle_hour_18, bicycle_hour_19, bicycle_hour_20, bicycle_hour_21, bicycle_hour_22, bicycle_hour_23],
                                        [mcycle_hour_0, mcycle_hour_1, mcycle_hour_2, mcycle_hour_3, mcycle_hour_4, mcycle_hour_5, mcycle_hour_6, mcycle_hour_7, mcycle_hour_8, mcycle_hour_9, mcycle_hour_10, mcycle_hour_11, mcycle_hour_12, mcycle_hour_13, mcycle_hour_14, mcycle_hour_15, mcycle_hour_16, mcycle_hour_17, mcycle_hour_18, mcycle_hour_19, mcycle_hour_20, mcycle_hour_21, mcycle_hour_22, mcycle_hour_23]
                                        )
        self.chart_window.setWindowIcon(QIcon(self.icon_path))
        self.chart_window.setStyleSheet(self.qss_file)
        self.chart_window.setWindowTitle("Daily and Hourly data | Line Chart")
        self.chart_window.show()
