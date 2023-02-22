from PySide2.QtWidgets import QApplication, QMainWindow
import pyqtgraph as pg
import sys


class ChartWindow(QMainWindow):

    def __init__(self, cam_name='No Camera', 
                       cars_data=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                       trucks_data=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                       buses_data=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                       bicycle_data=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                       mcycle_data=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]):
        super(ChartWindow, self).__init__()

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        hour = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
        # cars = [hour_zero,hour_one,hour_two,hour_three,hour_four,hour_five,hour_six,hour_seven,hour_eight,hour_nine,hour_ten,hour_eleven, hour_twelve, hour_thirteen, hour_fourteen, hour_fifteen, hour_sixteen, hour_seventeen, hour_eighteen, hour_nineteen, hour_twenty, hour_twenty_one, hour_twenty_two, hour_twenty_three]

        #Add Background colour to white
        self.graphWidget.setBackground('w')
        # Add Title
        self.graphWidget.setTitle(cam_name, color="b", size="30pt")
        # Add Axis Labels
        styles = {"color": "#f00", "font-size": "20px"}
        self.graphWidget.setLabel("left", "Num of Vehicles", **styles)
        self.graphWidget.setLabel("bottom", "Hours (H)", **styles)
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

        self.graphWidget.plot(hour, cars_data, name="Car",  pen=pen1, symbol='x', symbolSize=15, symbolBrush=('r'))
        self.graphWidget.plot(hour, trucks_data, name="Truck",  pen=pen2, symbol='+', symbolSize=15, symbolBrush=('g'))
        self.graphWidget.plot(hour, buses_data, name="Bus",  pen=pen3, symbol='o', symbolSize=15, symbolBrush=('b'))
        self.graphWidget.plot(hour, bicycle_data, name="Bicycle",  pen=pen4, symbol='o', symbolSize=15, symbolBrush=('r'))
        self.graphWidget.plot(hour, mcycle_data, name="MCycle",  pen=pen5, symbol='x', symbolSize=15, symbolBrush=('g'))
        
        # self.show()

