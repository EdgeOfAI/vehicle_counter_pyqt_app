from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtGui import QIcon
import pyqtgraph as pg
import random
import sys


class ChartWindow(QMainWindow):

    def __init__(self, cam_name='No Camera', 
                       cars_data=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                       trucks_data=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                       buses_data=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                       bicycle_data=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                       mcycle_data=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                       van_data=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                       text_translator=None):
        super(ChartWindow, self).__init__()

        self.text_translator = text_translator
        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        hour = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
        # cars_data = random.sample(range(20, 100), 24)
        # cars_data = [random.randint(20, 100) for i in range(0, 24)]
        # trucks_data = [random.randint(1, 10) for i in range(0, 24)]
        # buses_data = [random.randint(1, 30) for i in range(0, 24)]
        # bicycle_data = [random.randint(1, 5) for i in range(0, 24)]
        # mcycle_data = [random.randint(1, 14) for i in range(0, 24)] 

        # cars = [hour_zero,hour_one,hour_two,hour_three,hour_four,hour_five,hour_six,hour_seven,hour_eight,hour_nine,hour_ten,hour_eleven, hour_twelve, hour_thirteen, hour_fourteen, hour_fifteen, hour_sixteen, hour_seventeen, hour_eighteen, hour_nineteen, hour_twenty, hour_twenty_one, hour_twenty_two, hour_twenty_three]

        #Add Background colour to white
        self.graphWidget.setBackground('w')
        # Add Title
        self.graphWidget.setTitle(cam_name, color="b", size="30pt")
        # Add Axis Labels
        styles = {"color": "#f00", "font-size": "20px"}
        self.graphWidget.setLabel("left", self.text_translator.linechart_num_of_vehicles, **styles)
        self.graphWidget.setLabel("bottom", self.text_translator.linechart_hours, **styles)
        #Add legend
        self.graphWidget.addLegend()
        #Add grid
        self.graphWidget.showGrid(x=True, y=True)
        #Set Range
        self.graphWidget.setXRange(0, 10, padding=0)
        self.graphWidget.setYRange(20, 55, padding=0)

        pen1 = pg.mkPen(color=(255, 0, 0))
        pen2 = pg.mkPen(color=(0, 255, 0))
        pen3 = pg.mkPen(color=(0, 0, 255))
        pen4 = pg.mkPen(color=(255, 0, 0))
        pen5 = pg.mkPen(color=(0, 255, 0))
        pen6 = pg.mkPen(color=(0, 0, 255))

        self.graphWidget.plot(hour, cars_data, name=f"{self.text_translator.linechart_cars} {sum(cars_data)}",  pen=pen1, symbol='x', symbolSize=15, symbolBrush=('r'))
        self.graphWidget.plot(hour, trucks_data, name=f"{self.text_translator.linechart_trucks} {sum(trucks_data)}",  pen=pen2, symbol='+', symbolSize=15, symbolBrush=('g'))
        self.graphWidget.plot(hour, buses_data, name=f"{self.text_translator.linechart_buses} {sum(buses_data)}",  pen=pen3, symbol='o', symbolSize=15, symbolBrush=('b'))
        self.graphWidget.plot(hour, bicycle_data, name=f"{self.text_translator.linechart_bicycles} {sum(bicycle_data)}",  pen=pen4, symbol='o', symbolSize=15, symbolBrush=('r'))
        self.graphWidget.plot(hour, mcycle_data, name=f"{self.text_translator.linechart_motorcycles} {sum(mcycle_data)}",  pen=pen5, symbol='x', symbolSize=15, symbolBrush=('g'))
        self.graphWidget.plot(hour, van_data, name=f"{self.text_translator.linechart_van} {sum(van_data)}",  pen=pen6, symbol='+', symbolSize=15, symbolBrush=('b'))
        
        # self.show()
    
    def setTextTranslator(self, text_translator):
        self.text_translator = text_translator


class BarChartWindow(QMainWindow):
    def __init__(self, icon_path, qss_file, window_title, y, camera_name):
        super(BarChartWindow, self).__init__()

        pg.setConfigOption('background', 'w')
        self.win = pg.plot()
        self.win.setWindowIcon(QIcon(icon_path))
        self.win.setStyleSheet(qss_file)
        self.win.setWindowTitle(window_title)
        self.win.setTitle(camera_name)

        # y = [random.randint(259, 583) for i in range(16)]
        x = ['AA', 'AB', 'AC', 'AD', 'BA', 'BB', 'BC', 'BD', 'CA', 'CB', 'CC', 'CD', 'DA', 'DB', 'DC', 'DD']
        xval = list(range(1,len(x)+1))

        ticks=[]
        for i, item in enumerate(x):
            ticks.append( (xval[i], item) )
        ticks = [ticks]

        self.win.showGrid(x=True, y=True)

        bg1 = pg.BarGraphItem(x=xval, height=y, width=0.6, brush='b')
        self.win.addItem(bg1)
        ax = self.win.getAxis('bottom')
        ax.setTicks(ticks)

