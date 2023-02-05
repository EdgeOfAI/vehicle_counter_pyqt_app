# Shakh)
import sys
from PySide2 import QtWidgets
from qt.Add_Camera import Ui_MainWindow


class AddCameraWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(AddCameraWindow, self).__init__()
        self.setupUi(self)
        self.show()

        self.setupSignalSlots()
    
    def setupSignalSlots(self):
        self.addCamBtn.clicked.connect(self.add_cam)

    def add_cam(self):
        self.inputCamIP.text()
        self.inputCamUsername.text()
