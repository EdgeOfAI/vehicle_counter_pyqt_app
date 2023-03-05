import os
import datetime
import xlsxwriter
from pathlib import Path
from PySide2 import QtWidgets
from PySide2.QtGui import QIcon
from qt.Show_Calendar import Ui_MainWindow
from PySide2.QtCore import Signal, QCoreApplication
from qt.ChartWindow import ChartWindow, BarChartWindow


class ShowCalendarWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    process_done_signal = Signal()
    def __init__(self, db_conn, db_cur, qss_file, icon_path, text_translator):
        super(ShowCalendarWindow, self).__init__()
        self.qss_file = qss_file
        self.db_conn = db_conn
        self.db_cur = db_cur
        self.icon_path = icon_path
        self.text_translator = text_translator
        self.setupUi(self)
        self.setCameraComboBox()
        self.onSelectionChange()
        self.setupSignalSlots()
    
    def setCamId(self, cam_id):
        self.remove_cam_id = cam_id
    
    def setTextTranslator(self, text_translator):
        self.text_translator = text_translator
    
    def closeEvent(self, event):
        self.process_done_signal.emit()
        event.accept()
    
    def showPopup(self, message):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle('Information!')
        msg.setWindowIcon(QIcon(self.icon_path))
        msg.setText(message)
        msg.setIcon(QtWidgets.QMessageBox.Information)
        x = msg.exec_()
    
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
        self.downloadExcelDataBtn.clicked.connect(self.createExcelData)
        self.calendarWidget.selectionChanged.connect(self.onSelectionChange)

    def onSelectionChange(self):
        # self.inputCamIP.text()
        # self.inputCamUsername.text()
        # self.inputCamPassword.text()
        # self.inputCamDisplayName.text()
        selected_date = str(self.calendarWidget.selectedDate().toString())
        week_day, month, day, year = selected_date.split(' ')[0], selected_date.split(' ')[1], selected_date.split(' ')[2], selected_date.split(' ')[3]      
        if self.text_translator.lang == 'uz':
            week_day = self.text_translator.week_days[week_day]
            month = self.text_translator.months[month]
        
        selected_date = f'{week_day} {month} {day} {year}'
        # print(selected_date)
        # print(dir(selected_date))
        # print(month)
        self.label.setText(selected_date)

        # self.process_done_signal.emit()
        # self.hide()
    
    def createExcelData(self):

        cardinal_sides = ['AA', 'AB', 'AC', 'AD', 'BA', 'BB', 'BC', 'BD', 'CA', 'CB', 'CC', 'CD', 'DA', 'DB', 'DC', 'DD']
        in_sides = [self.text_translator.a_in, self.text_translator.b_in, self.text_translator.c_in, self.text_translator.d_in]
        out_sides = [self.text_translator.a_out, self.text_translator.b_out, self.text_translator.c_out, self.text_translator.d_out]
        cam_name = self.comboBox.currentText()
        self.excels_folder = 'downloaded_excel_files'
        end_time = self.timeEdit_2.time()
        start_time = self.timeEdit.time()

        start_hour = f'0{start_time.hour()}' if len(str(start_time.hour())) == 1 else start_time.hour()
        start_minute = f'0{start_time.minute()}' if len(str(start_time.minute())) == 1 else start_time.minute()
        start_second = f'0{start_time.second()}' if len(str(start_time.second())) == 1 else start_time.second()

        end_hour = f'0{end_time.hour()}' if len(str(end_time.hour())) == 1 else end_time.hour()
        end_minute = f'0{end_time.minute()}' if len(str(end_time.minute())) == 1 else end_time.minute()
        end_second = f'0{end_time.second()}' if len(str(end_time.second())) == 1 else end_time.second()

        start_time_str = f'{start_hour}:{start_minute}:{start_second}'
        end_time_str = f'{end_hour}:{end_minute}:{end_second}'
        # print(start_time_str, end_time_str, 'Got from start and end time editors')
        if not Path(self.excels_folder).exists():
            os.makedirs(self.excels_folder)
        excel_file_name = os.path.join(self.excels_folder, f'{datetime.datetime.now()}_{cam_name}_{self.label.text()}.xlsx').replace('\\', '/').replace(' ', '').replace(':', '-')
        workbook = xlsxwriter.Workbook(excel_file_name)

        cardinal_worksheet = workbook.add_worksheet(self.text_translator.cardinalwise)
        trucks_worksheet = workbook.add_worksheet(self.text_translator.linechart_trucks)
        cars_worksheet = workbook.add_worksheet(self.text_translator.linechart_cars)
        buses_worksheet = workbook.add_worksheet(self.text_translator.linechart_buses)
        bicycles_worksheet = workbook.add_worksheet(self.text_translator.linechart_bicycles)
        motorcycles_worksheet = workbook.add_worksheet(self.text_translator.linechart_motorcycles)
        total_worksheet = workbook.add_worksheet(self.text_translator.total)

        cardinal_truck_data, cardinal_car_data, cardinal_bus_data, cardinal_bicycle_data, cardinal_mcycle_data = self.get_cardinalwise_data(start_time_str, end_time_str, get_all_data=True)
        cf = workbook.add_format({'bg_color': 'yellow'})
        for i in range(len(cardinal_truck_data)+1):
            if i == 0:
                cardinal_worksheet.write(0, i, '')
                cardinal_worksheet.write(1, i, self.text_translator.linechart_trucks)
                cardinal_worksheet.write(2, i, self.text_translator.linechart_cars)
                cardinal_worksheet.write(3, i, self.text_translator.linechart_buses)
                cardinal_worksheet.write(4, i, self.text_translator.linechart_bicycles)
                cardinal_worksheet.write(5, i, self.text_translator.linechart_motorcycles)
                cardinal_worksheet.write(6, i, self.text_translator.total)
            else:
                cardinal_side = cardinal_sides[i-1]
                truck_data = len(cardinal_truck_data[i-1])
                car_data = len(cardinal_car_data[i-1])
                bus_data = len(cardinal_bus_data[i-1])
                bicycle_data = len(cardinal_bicycle_data[i-1])
                mcycle_data = len(cardinal_mcycle_data[i-1])
                total = sum([truck_data, car_data, bus_data, bicycle_data, mcycle_data])
                cardinal_worksheet.write(0, i, cardinal_side)
                cardinal_worksheet.write(1, i, truck_data, cf if truck_data else workbook.add_format())
                cardinal_worksheet.write(2, i, car_data, cf if car_data else workbook.add_format())
                cardinal_worksheet.write(3, i, bus_data, cf if bus_data else workbook.add_format())
                cardinal_worksheet.write(4, i, bicycle_data, cf if bicycle_data else workbook.add_format())
                cardinal_worksheet.write(5, i, mcycle_data, cf if mcycle_data else workbook.add_format())
                cardinal_worksheet.write(6, i, total, cf if total else workbook.add_format())
        
        for i in range(5):
            if i == 0:
                trucks_worksheet.write(0, i, '', cf)
                trucks_worksheet.write(1, i, in_sides[0], cf)
                trucks_worksheet.write(2, i, in_sides[1], cf)
                trucks_worksheet.write(3, i, in_sides[2], cf)
                trucks_worksheet.write(4, i, in_sides[3], cf)

                cars_worksheet.write(0, i, '', cf)
                cars_worksheet.write(1, i, in_sides[0], cf)
                cars_worksheet.write(2, i, in_sides[1], cf)
                cars_worksheet.write(3, i, in_sides[2], cf)
                cars_worksheet.write(4, i, in_sides[3], cf)

                buses_worksheet.write(0, i, '', cf)
                buses_worksheet.write(1, i, in_sides[0], cf)
                buses_worksheet.write(2, i, in_sides[1], cf)
                buses_worksheet.write(3, i, in_sides[2], cf)
                buses_worksheet.write(4, i, in_sides[3], cf)

                bicycles_worksheet.write(0, i, '', cf)
                bicycles_worksheet.write(1, i, in_sides[0], cf)
                bicycles_worksheet.write(2, i, in_sides[1], cf)
                bicycles_worksheet.write(3, i, in_sides[2], cf)
                bicycles_worksheet.write(4, i, in_sides[3], cf)

                motorcycles_worksheet.write(0, i, '', cf)
                motorcycles_worksheet.write(1, i, in_sides[0], cf)
                motorcycles_worksheet.write(2, i, in_sides[1], cf)
                motorcycles_worksheet.write(3, i, in_sides[2], cf)
                motorcycles_worksheet.write(4, i, in_sides[3], cf)

                total_worksheet.write(0, i, '', cf)
                total_worksheet.write(1, i, in_sides[0], cf)
                total_worksheet.write(2, i, in_sides[1], cf)
                total_worksheet.write(3, i, in_sides[2], cf)
                total_worksheet.write(4, i, in_sides[3], cf)

            else:
                truck_data_a = cardinal_truck_data[i-1]
                truck_data_b = cardinal_truck_data[i-1+4]
                truck_data_c = cardinal_truck_data[i-1+8]
                truck_data_d = cardinal_truck_data[i-1+12]

                car_data_a = cardinal_car_data[i-1]
                car_data_b = cardinal_car_data[i-1+4]
                car_data_c = cardinal_car_data[i-1+8]
                car_data_d = cardinal_car_data[i-1+12]

                bus_data_a = cardinal_bus_data[i-1]
                bus_data_b = cardinal_bus_data[i-1+4]
                bus_data_c = cardinal_bus_data[i-1+8]
                bus_data_d = cardinal_bus_data[i-1+12]

                bicycle_data_a = cardinal_bicycle_data[i-1]
                bicycle_data_b = cardinal_bicycle_data[i-1+4]
                bicycle_data_c = cardinal_bicycle_data[i-1+8]
                bicycle_data_d = cardinal_bicycle_data[i-1+12]

                mcycle_data_a = cardinal_mcycle_data[i-1]
                mcycle_data_b = cardinal_mcycle_data[i-1+4]
                mcycle_data_c = cardinal_mcycle_data[i-1+8]
                mcycle_data_d = cardinal_mcycle_data[i-1+12]

                total_a = sum([len(truck_data_a), len(car_data_a), len(bus_data_a), len(bicycle_data_a), len(mcycle_data_a)])
                total_b = sum([len(truck_data_b), len(car_data_b), len(bus_data_b), len(bicycle_data_b), len(mcycle_data_b)])
                total_c = sum([len(truck_data_c), len(car_data_c), len(bus_data_c), len(bicycle_data_c), len(mcycle_data_c)])
                total_d = sum([len(truck_data_d), len(car_data_d), len(bus_data_d), len(bicycle_data_d), len(mcycle_data_d)])

                trucks_worksheet.write(0, i, out_sides[i-1], cf)
                trucks_worksheet.write(1, i, len(truck_data_a))
                trucks_worksheet.write(2, i, len(truck_data_b))
                trucks_worksheet.write(3, i, len(truck_data_c))
                trucks_worksheet.write(4, i, len(truck_data_d))

                cars_worksheet.write(0, i, out_sides[i-1], cf)
                cars_worksheet.write(1, i, len(car_data_a))
                cars_worksheet.write(2, i, len(car_data_b))
                cars_worksheet.write(3, i, len(car_data_c))
                cars_worksheet.write(4, i, len(car_data_d))

                buses_worksheet.write(0, i, out_sides[i-1], cf)
                buses_worksheet.write(1, i, len(bus_data_a))
                buses_worksheet.write(2, i, len(bus_data_b))
                buses_worksheet.write(3, i, len(bus_data_c))
                buses_worksheet.write(4, i, len(bus_data_d))

                bicycles_worksheet.write(0, i, out_sides[i-1], cf)
                bicycles_worksheet.write(1, i, len(bicycle_data_a))
                bicycles_worksheet.write(2, i, len(bicycle_data_b))
                bicycles_worksheet.write(3, i, len(bicycle_data_c))
                bicycles_worksheet.write(4, i, len(bicycle_data_d))

                motorcycles_worksheet.write(0, i, out_sides[i-1], cf)
                motorcycles_worksheet.write(1, i, len(mcycle_data_a))
                motorcycles_worksheet.write(2, i, len(mcycle_data_b))
                motorcycles_worksheet.write(3, i, len(mcycle_data_c))
                motorcycles_worksheet.write(4, i, len(mcycle_data_d))

                total_worksheet.write(0, i, out_sides[i-1], cf)
                total_worksheet.write(1, i, total_a)
                total_worksheet.write(2, i, total_b)
                total_worksheet.write(3, i, total_c)
                total_worksheet.write(4, i, total_d)


        self.showPopup(f'{excel_file_name} '+self.text_translator.excel_data_written_success)
        workbook.close()
    
    def get_cardinalwise_data(self,start_time_str='00:00:00', end_time_str='23:59:59', get_all_data=False):
        cam_name = self.comboBox.currentText()
        cam_id = cam_name.split('.')[0]
        selected_date = self.calendarWidget.selectedDate().toString()
        selected_date = datetime.datetime.strptime(' '.join(selected_date.split(' ')[1:]), '%b %d %Y')

        selected_month = f'0{selected_date.month}' if len(str(selected_date.month)) == 1 else selected_date.month
        selected_day = f'0{selected_date.day}' if len(str(selected_date.day)) == 1 else selected_date.day

        start_date_time = f'{selected_date.year}-{selected_month}-{selected_day} {start_time_str}'
        end_date_time = f'{selected_date.year}-{selected_month}-{selected_day} {end_time_str}'
        self.db_cur.execute(f"SELECT * FROM vehicles WHERE camera_id = {cam_id} and `time` >= '{start_date_time}' and `time` <= '{end_date_time}'")
        vehicles = self.db_cur.fetchall()
        # N_in = [vehicle for vehicle in vehicles if vehicle[8]=='North' and datetime.datetime.fromisoformat(vehicle[11]).day == selected_date.day and datetime.datetime.fromisoformat(vehicle[11]).month == selected_date.month and datetime.datetime.fromisoformat(vehicle[11]).year == selected_date.year]
        # E_in = [vehicle for vehicle in vehicles if vehicle[8] == 'East' and datetime.datetime.fromisoformat(vehicle[11]).day == selected_date.day and datetime.datetime.fromisoformat(vehicle[11]).month == selected_date.month and datetime.datetime.fromisoformat(vehicle[11]).year == selected_date.year]
        # W_in = [vehicle for vehicle in vehicles if vehicle[8] == 'West' and datetime.datetime.fromisoformat(vehicle[11]).day == selected_date.day and datetime.datetime.fromisoformat(vehicle[11]).month == selected_date.month and datetime.datetime.fromisoformat(vehicle[11]).year == selected_date.year]
        # S_in = [vehicle for vehicle in vehicles if vehicle[8] == 'South' and datetime.datetime.fromisoformat(vehicle[11]).day == selected_date.day and datetime.datetime.fromisoformat(vehicle[11]).month == selected_date.month and datetime.datetime.fromisoformat(vehicle[11]).year == selected_date.year]

        N_in = [vehicle for vehicle in vehicles if vehicle[8] == 'North']
        E_in = [vehicle for vehicle in vehicles if vehicle[8] == 'East']
        W_in = [vehicle for vehicle in vehicles if vehicle[8] == 'West']
        S_in = [vehicle for vehicle in vehicles if vehicle[8] == 'South']

        NN = [vehicle for vehicle in N_in if vehicle[9] == 'North']
        NE = [vehicle for vehicle in N_in if vehicle[9] == 'East']
        NW = [vehicle for vehicle in N_in if vehicle[9] == 'West']
        NS = [vehicle for vehicle in N_in if vehicle[9] == 'South']

        EN = [vehicle for vehicle in E_in if vehicle[9] == 'North']
        EE = [vehicle for vehicle in E_in if vehicle[9] == 'East']
        EW = [vehicle for vehicle in E_in if vehicle[9] == 'West']
        ES = [vehicle for vehicle in E_in if vehicle[9] == 'South']

        WN = [vehicle for vehicle in W_in if vehicle[9] == 'North']
        WE = [vehicle for vehicle in W_in if vehicle[9] == 'East']
        WW = [vehicle for vehicle in W_in if vehicle[9] == 'West']
        WS = [vehicle for vehicle in W_in if vehicle[9] == 'South']

        SN = [vehicle for vehicle in S_in if vehicle[9] == 'North']
        SE = [vehicle for vehicle in S_in if vehicle[9] == 'East']
        SW = [vehicle for vehicle in S_in if vehicle[9] == 'West']
        SS = [vehicle for vehicle in S_in if vehicle[9] == 'South']

        NN_truck = [vehicle for vehicle in NN if vehicle[10] == 1]
        NE_truck = [vehicle for vehicle in NE if vehicle[10] == 1]
        NW_truck = [vehicle for vehicle in NW if vehicle[10] == 1]
        NS_truck = [vehicle for vehicle in NS if vehicle[10] == 1]
        EN_truck = [vehicle for vehicle in EN if vehicle[10] == 1]
        EE_truck = [vehicle for vehicle in EE if vehicle[10] == 1]
        EW_truck = [vehicle for vehicle in EW if vehicle[10] == 1]
        ES_truck = [vehicle for vehicle in ES if vehicle[10] == 1]
        WN_truck = [vehicle for vehicle in WN if vehicle[10] == 1]
        WE_truck = [vehicle for vehicle in WE if vehicle[10] == 1]
        WW_truck = [vehicle for vehicle in WW if vehicle[10] == 1]
        WS_truck = [vehicle for vehicle in WS if vehicle[10] == 1]
        SN_truck = [vehicle for vehicle in SN if vehicle[10] == 1]
        SE_truck = [vehicle for vehicle in SE if vehicle[10] == 1]
        SW_truck = [vehicle for vehicle in SW if vehicle[10] == 1]
        SS_truck = [vehicle for vehicle in SS if vehicle[10] == 1]

        NN_car = [vehicle for vehicle in NN if vehicle[10] == 2]
        NE_car = [vehicle for vehicle in NE if vehicle[10] == 2]
        NW_car = [vehicle for vehicle in NW if vehicle[10] == 2]
        NS_car = [vehicle for vehicle in NS if vehicle[10] == 2]
        EN_car = [vehicle for vehicle in EN if vehicle[10] == 2]
        EE_car = [vehicle for vehicle in EE if vehicle[10] == 2]
        EW_car = [vehicle for vehicle in EW if vehicle[10] == 2]
        ES_car = [vehicle for vehicle in ES if vehicle[10] == 2]
        WN_car = [vehicle for vehicle in WN if vehicle[10] == 2]
        WE_car = [vehicle for vehicle in WE if vehicle[10] == 2]
        WW_car = [vehicle for vehicle in WW if vehicle[10] == 2]
        WS_car = [vehicle for vehicle in WS if vehicle[10] == 2]
        SN_car = [vehicle for vehicle in SN if vehicle[10] == 2]
        SE_car = [vehicle for vehicle in SE if vehicle[10] == 2]
        SW_car = [vehicle for vehicle in SW if vehicle[10] == 2]
        SS_car = [vehicle for vehicle in SS if vehicle[10] == 2]

        NN_bus = [vehicle for vehicle in NN if vehicle[10] == 3]
        NE_bus = [vehicle for vehicle in NE if vehicle[10] == 3]
        NW_bus = [vehicle for vehicle in NW if vehicle[10] == 3]
        NS_bus = [vehicle for vehicle in NS if vehicle[10] == 3]
        EN_bus = [vehicle for vehicle in EN if vehicle[10] == 3]
        EE_bus = [vehicle for vehicle in EE if vehicle[10] == 3]
        EW_bus = [vehicle for vehicle in EW if vehicle[10] == 3]
        ES_bus = [vehicle for vehicle in ES if vehicle[10] == 3]
        WN_bus = [vehicle for vehicle in WN if vehicle[10] == 3]
        WE_bus = [vehicle for vehicle in WE if vehicle[10] == 3]
        WW_bus = [vehicle for vehicle in WW if vehicle[10] == 3]
        WS_bus = [vehicle for vehicle in WS if vehicle[10] == 3]
        SN_bus = [vehicle for vehicle in SN if vehicle[10] == 3]
        SE_bus = [vehicle for vehicle in SE if vehicle[10] == 3]
        SW_bus = [vehicle for vehicle in SW if vehicle[10] == 3]
        SS_bus = [vehicle for vehicle in SS if vehicle[10] == 3]

        NN_bicycle = [vehicle for vehicle in NN if vehicle[10] == 4]
        NE_bicycle = [vehicle for vehicle in NE if vehicle[10] == 4]
        NW_bicycle = [vehicle for vehicle in NW if vehicle[10] == 4]
        NS_bicycle = [vehicle for vehicle in NS if vehicle[10] == 4]
        EN_bicycle = [vehicle for vehicle in EN if vehicle[10] == 4]
        EE_bicycle = [vehicle for vehicle in EE if vehicle[10] == 4]
        EW_bicycle = [vehicle for vehicle in EW if vehicle[10] == 4]
        ES_bicycle = [vehicle for vehicle in ES if vehicle[10] == 4]
        WN_bicycle = [vehicle for vehicle in WN if vehicle[10] == 4]
        WE_bicycle = [vehicle for vehicle in WE if vehicle[10] == 4]
        WW_bicycle = [vehicle for vehicle in WW if vehicle[10] == 4]
        WS_bicycle = [vehicle for vehicle in WS if vehicle[10] == 4]
        SN_bicycle = [vehicle for vehicle in SN if vehicle[10] == 4]
        SE_bicycle = [vehicle for vehicle in SE if vehicle[10] == 4]
        SW_bicycle = [vehicle for vehicle in SW if vehicle[10] == 4]
        SS_bicycle = [vehicle for vehicle in SS if vehicle[10] == 4]

        NN_mcycle = [vehicle for vehicle in NN if vehicle[10] == 5]
        NE_mcycle = [vehicle for vehicle in NE if vehicle[10] == 5]
        NW_mcycle = [vehicle for vehicle in NW if vehicle[10] == 5]
        NS_mcycle = [vehicle for vehicle in NS if vehicle[10] == 5]
        EN_mcycle = [vehicle for vehicle in EN if vehicle[10] == 5]
        EE_mcycle = [vehicle for vehicle in EE if vehicle[10] == 5]
        EW_mcycle = [vehicle for vehicle in EW if vehicle[10] == 5]
        ES_mcycle = [vehicle for vehicle in ES if vehicle[10] == 5]
        WN_mcycle = [vehicle for vehicle in WN if vehicle[10] == 5]
        WE_mcycle = [vehicle for vehicle in WE if vehicle[10] == 5]
        WW_mcycle = [vehicle for vehicle in WW if vehicle[10] == 5]
        WS_mcycle = [vehicle for vehicle in WS if vehicle[10] == 5]
        SN_mcycle = [vehicle for vehicle in SN if vehicle[10] == 5]
        SE_mcycle = [vehicle for vehicle in SE if vehicle[10] == 5]
        SW_mcycle = [vehicle for vehicle in SW if vehicle[10] == 5]
        SS_mcycle = [vehicle for vehicle in SS if vehicle[10] == 5]

        if get_all_data:
            return [NN_truck, NE_truck, NW_truck, NS_truck, EN_truck, EE_truck, EW_truck, ES_truck, WN_truck, WE_truck, WW_truck, WS_truck, SN_truck, SE_truck, SW_truck, SS_truck], \
                   [NN_car, NE_car, NW_car, NS_car, EN_car, EE_car, EW_car, ES_car, WN_car, WE_car, WW_car, WS_car, SN_car, SE_car, SW_car, SS_car], \
                   [NN_bus, NE_bus, NW_bus, NS_bus, EN_bus, EE_bus, EW_bus, ES_bus, WN_bus, WE_bus, WW_bus, WS_bus, SN_bus, SE_bus, SW_bus, SS_bus], \
                   [NN_bicycle, NE_bicycle, NW_bicycle, NS_bicycle, EN_bicycle, EE_bicycle, EW_bicycle, ES_bicycle, WN_bicycle, WE_bicycle, WW_bicycle, WS_bicycle, SN_bicycle, SE_bicycle, SW_bicycle, SS_bicycle], \
                   [NN_mcycle, NE_mcycle, NW_mcycle, NS_mcycle, EN_mcycle, EE_mcycle, EW_mcycle, ES_mcycle, WN_mcycle, WE_mcycle, WW_mcycle, WS_mcycle, SN_mcycle, SE_mcycle, SW_mcycle, SS_mcycle], \

        return [len(NN), len(NE), len(NW), len(NS), len(EN), len(EE), len(EW), len(ES), len(WN), len(WE), len(WW), len(WS), len(SN), len(SE), len(SW), len(SS)]
    
    def showCardinalwiseData(self):
        data = self.get_cardinalwise_data()

        self.bar_chart_window = BarChartWindow(self.icon_path, self.qss_file, 'Cardinalwise Data | Bar Chart', data, self.comboBox.currentText())
        # self.bar_chart_window.show()

    def showLineChart(self):
        # print('Button clicked')
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
        # print(
        #     len([car_hour_0,car_hour_1,car_hour_2, car_hour_3, car_hour_4, car_hour_5, car_hour_6, car_hour_7, car_hour_8, car_hour_9, car_hour_10, car_hour_11, car_hour_12, car_hour_13, car_hour_14, car_hour_15, car_hour_16, car_hour_17, car_hour_18, car_hour_19, car_hour_20, car_hour_21, car_hour_22, car_hour_23]),
        #     len([truck_hour_0, truck_hour_1, truck_hour_2, truck_hour_3, truck_hour_4, truck_hour_5, truck_hour_6, truck_hour_7, truck_hour_8, truck_hour_9, truck_hour_10, truck_hour_11, truck_hour_12, truck_hour_13, truck_hour_14, truck_hour_15, truck_hour_16, truck_hour_17, truck_hour_18, truck_hour_19, truck_hour_20, truck_hour_21, truck_hour_22, truck_hour_23]),
        #     len([bus_hour_0, bus_hour_1, bus_hour_2, bus_hour_3, bus_hour_4, bus_hour_5, bus_hour_6, bus_hour_7, bus_hour_8, bus_hour_9, bus_hour_10, bus_hour_11, bus_hour_12, bus_hour_13, bus_hour_14, bus_hour_15, bus_hour_16, bus_hour_17, bus_hour_18, bus_hour_19, bus_hour_20, bus_hour_21, bus_hour_22, bus_hour_23]),
        #     len([bicycle_hour_0, bicycle_hour_1, bicycle_hour_2, bicycle_hour_3, bicycle_hour_4, bicycle_hour_5, bicycle_hour_6, bicycle_hour_7, bicycle_hour_8, bicycle_hour_9, bicycle_hour_10, bicycle_hour_11, bicycle_hour_12, bicycle_hour_13, bicycle_hour_14, bicycle_hour_15, bicycle_hour_16, bicycle_hour_17, bicycle_hour_18, bicycle_hour_19, bicycle_hour_20, bicycle_hour_21, bicycle_hour_22, bicycle_hour_23]),
        #     len([mcycle_hour_0, mcycle_hour_1, mcycle_hour_2, mcycle_hour_3, mcycle_hour_4, mcycle_hour_5, mcycle_hour_6, mcycle_hour_7, mcycle_hour_8, mcycle_hour_9, mcycle_hour_10, mcycle_hour_11, mcycle_hour_12, mcycle_hour_13, mcycle_hour_14, mcycle_hour_15, mcycle_hour_16, mcycle_hour_17, mcycle_hour_18, mcycle_hour_19, mcycle_hour_20, mcycle_hour_21, mcycle_hour_22, mcycle_hour_23])
        # )
        self.chart_window = ChartWindow(
                                        cam_name if cam_name else 'No Cam',
                                        [car_hour_0,car_hour_1,car_hour_2, car_hour_3, car_hour_4, car_hour_5, car_hour_6, car_hour_7, car_hour_8, car_hour_9, car_hour_10, car_hour_11, car_hour_12, car_hour_13, car_hour_14, car_hour_15, car_hour_16, car_hour_17, car_hour_18, car_hour_19, car_hour_20, car_hour_21, car_hour_22, car_hour_23],
                                        [truck_hour_0, truck_hour_1, truck_hour_2, truck_hour_3, truck_hour_4, truck_hour_5, truck_hour_6, truck_hour_7, truck_hour_8, truck_hour_9, truck_hour_10, truck_hour_11, truck_hour_12, truck_hour_13, truck_hour_14, truck_hour_15, truck_hour_16, truck_hour_17, truck_hour_18, truck_hour_19, truck_hour_20, truck_hour_21, truck_hour_22, truck_hour_23],
                                        [bus_hour_0, bus_hour_1, bus_hour_2, bus_hour_3, bus_hour_4, bus_hour_5, bus_hour_6, bus_hour_7, bus_hour_8, bus_hour_9, bus_hour_10, bus_hour_11, bus_hour_12, bus_hour_13, bus_hour_14, bus_hour_15, bus_hour_16, bus_hour_17, bus_hour_18, bus_hour_19, bus_hour_20, bus_hour_21, bus_hour_22, bus_hour_23],
                                        [bicycle_hour_0, bicycle_hour_1, bicycle_hour_2, bicycle_hour_3, bicycle_hour_4, bicycle_hour_5, bicycle_hour_6, bicycle_hour_7, bicycle_hour_8, bicycle_hour_9, bicycle_hour_10, bicycle_hour_11, bicycle_hour_12, bicycle_hour_13, bicycle_hour_14, bicycle_hour_15, bicycle_hour_16, bicycle_hour_17, bicycle_hour_18, bicycle_hour_19, bicycle_hour_20, bicycle_hour_21, bicycle_hour_22, bicycle_hour_23],
                                        [mcycle_hour_0, mcycle_hour_1, mcycle_hour_2, mcycle_hour_3, mcycle_hour_4, mcycle_hour_5, mcycle_hour_6, mcycle_hour_7, mcycle_hour_8, mcycle_hour_9, mcycle_hour_10, mcycle_hour_11, mcycle_hour_12, mcycle_hour_13, mcycle_hour_14, mcycle_hour_15, mcycle_hour_16, mcycle_hour_17, mcycle_hour_18, mcycle_hour_19, mcycle_hour_20, mcycle_hour_21, mcycle_hour_22, mcycle_hour_23],
                                        self.text_translator
                                        )
        self.chart_window.setWindowIcon(QIcon(self.icon_path))
        self.chart_window.setStyleSheet(self.qss_file)
        self.chart_window.setWindowTitle(self.text_translator.linlechart_title)
        self.chart_window.show()

    def retranslateUi(self, MainWindow):
        selected_date = str(self.calendarWidget.selectedDate().toString())
        week_day, month, day, year = selected_date.split(' ')[0], selected_date.split(' ')[1], selected_date.split(' ')[2], selected_date.split(' ')[3]      
        if self.text_translator.lang == 'uz':
            week_day = self.text_translator.week_days[week_day]
            month = self.text_translator.months[month]
        
        selected_date = f'{week_day} {month} {day} {year}'

        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", self.text_translator.show_calendar_window_title, None))
        self.label.setText(QCoreApplication.translate("MainWindow", selected_date, None))
        self.showDataBtn.setText(QCoreApplication.translate("MainWindow", self.text_translator.show_calendar_window_show_data_hourly, None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", self.text_translator.show_calendar_window_show_data_cardinalwise, None))
        self.downloadExcelDataBtn.setText(QCoreApplication.translate("MainWindow", self.text_translator.show_calendar_window_download_excel_data, None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", self.text_translator.show_calendar_window_start_time, None))
        self.timeEdit_2.setDisplayFormat(QCoreApplication.translate("MainWindow", u"h:mm:ss", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", self.text_translator.show_calendar_window_end_time, None))
        self.timeEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"h:mm:ss", None))
