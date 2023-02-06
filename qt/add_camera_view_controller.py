# Shakh)
import sys
from PySide2 import QtWidgets
from qt.Add_Camera import Ui_MainWindow


class AddCameraWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, db_conn, db_cur):
        super(AddCameraWindow, self).__init__()
        self.db_conn = db_conn
        self.db_cur = db_cur
        self.setupUi(self)
        self.show()

        self.setupSignalSlots()
    
    def setupSignalSlots(self):
        self.addCamBtn.clicked.connect(self.add_cam)
    
    

    def add_cam(self):
        # self.inputCamIP.text()
        # self.inputCamUsername.text()
        # self.inputCamPassword.text()
        # self.inputCamDisplayName.text()
        self.db_cur.execute(f"SELECT max(id) FROM cameras")
        last_id = self.db_cur.fetchone()[0]
        print(type(last_id), last_id)
        self.db_conn.commit()

        self.db_cur.execute(f"INSERT INTO cameras VALUES ({last_id + 1}, '{self.inputCamIP.text()}', '{self.inputCamUsername.text()}', '{self.inputCamPassword.text()}', '{self.inputCamDisplayName.text()}')")
        self.db_conn.commit()
