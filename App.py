import sys
import sqlite3
from PySide2.QtCore import Qt, QThread
from PySide2.QtWidgets import QApplication
from qt.view_controller import ViewController
from PySide2 import QtCore
from model import Model
import pyqtgraph as pg
import qtmodern.styles

QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True) #enable highdpi scaling
QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True) #use highdpi icons
pg.setConfigOptions(imageAxisOrder='row-major') #pyqtgraph default uses column major, resulting in rotated images

class App(QApplication):
    def __init__(self, sys_argv):
        super().__init__()
        qss_file = QtCore.QFile("style.qss")
        # qss = QtCore.QTextStream(qss_file)
        # print(qss.readAll())
        # self.setStyleSheet(qss.readAll())
        # create database
        conn = sqlite3.connect("main.db", check_same_thread=False)
        cur = conn.cursor()

        # create tables
        try:
            cur.execute("""CREATE TABLE cameras (
                    id integer, 
                    ip text, 
                    username text,
                    password text,
                    name text,
                    nx1 integer,
                    ny1 integer,
                    nx2 integer,
                    ny2 integer,
                    ex1 integer,
                    ey1 integer,
                    ex2 integer,
                    ey2 integer,
                    wx1 integer,
                    wy1 integer,
                    wx2 integer,
                    wy2 integer,
                    sx1 integer,
                    sy1 integer,
                    sx2 integer,
                    sy2 integer
                )""")
        except Exception as err:
            print('Error:  ', err)

        conn.commit()

        try:
            cur.execute("""CREATE TABLE vehicles (
                    id integer, 
                    initial_centroid_x int,
                    initial_centroid_y int,
                    prev_centroid_x int,
                    prev_centroid_y int,
                    prev_frame_num int,
                    dist int,
                    counted BOOLEAN,
                    in_cardinal_side text, 
                    out_cardinal_side text,
                    type int,
                    time timestamp,
                    camera_id int,
                    row_id text
                )""")
        except Exception as err:
            print('Error:  ', err)

        conn.commit()

        self.modelThread = QThread()
        self.model = Model(conn, cur)
        self.model.moveToThread(self.modelThread)
        self.modelThread.start()
        self.modelThread.setPriority(QThread.HighestPriority)
        qss_file = open('style.qss').read()
        self.viewController = ViewController(self.model, conn, cur, qss_file)
        # self.viewController.setStyleSheet(open('style.qss').read())
        self.viewController.show()

if __name__ == '__main__':
    app = App(sys.argv)
    qtmodern.styles.light(app)
    sys.exit(app.exec_())