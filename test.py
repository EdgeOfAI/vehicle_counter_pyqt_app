from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor, QPen, QImage
from PyQt5.QtCore import Qt, QPoint, QRect

class Line:
    def __init__(self, start, end):
        self.line_start = start
        self.line_end = end
        self.circle_start = QRect(start.x()-7, start.y()-7, 14, 14)
        self.circle_end = QRect(end.x()-7, end.y()-7, 14, 14)
        self.start_hovered = False
        self.end_hovered = False
        self.color = QColor(0, 0, 0)
        
    def draw(self, painter):
        pen = QPen()
        pen.setWidth(15)
        pen.setColor(self.color)
        painter.setPen(pen)
        painter.drawLine(self.line_start, self.line_end)

        # draw circles
        painter.setBrush(QColor(255, 255, 255))
        painter.drawEllipse(self.circle_start)
        painter.drawEllipse(self.circle_end)

        # change circle color if mouse hovers over it
        if self.start_hovered:
            painter.setBrush(QColor(255, 0, 0))
            painter.drawEllipse(self.circle_start)
        elif self.end_hovered:
            painter.setBrush(QColor(0, 0, 255))
            painter.drawEllipse(self.circle_end)

    def mousePressEvent(self, event):
        if self.circle_start.contains(event.pos()):
            self.start_hovered = True
        elif self.circle_end.contains(event.pos()):
            self.end_hovered = True

    def mouseMoveEvent(self, event):
        if self.start_hovered:
            self.line_start = event.pos()
            self.circle_start.moveTo(event.pos().x()-7, event.pos().y()-7)
        elif self.end_hovered:
            self.line_end = event.pos()
            self.circle_end.moveTo(event.pos().x()-7, event.pos().y()-7)

    def mouseReleaseEvent(self, event):
        self.start_hovered = False
        self.end_hovered = False

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 800, 600)
        self.lines = [Line(QPoint(100, 100), QPoint(200, 200)), 
                      Line(QPoint(300, 300), QPoint(400, 400)),
                      Line(QPoint(500, 500), QPoint(600, 600)),
                      Line(QPoint(700, 100), QPoint(600, 200))]
        self.background_image = QImage("image.png")

    def paintEvent(self, event):
        painter = QPainter(self)
        # draw background image
        painter.drawImage(0, 0, self.background_image)

        # draw lines
        for line in self.lines:
            line.draw(painter)

    def mousePressEvent(self, event):
        for line in self.lines:
            line.mousePressEvent(event)

    def mouseMoveEvent(self, event):
        for line in self.lines:
            line.mouseMoveEvent(event)
        self.update()

    def mouseReleaseEvent(self, event):
        for line in self.lines:
            line.mouseReleaseEvent(event)
        self.update()

if __name__ == "__main__":
    app = QApplication([])
    widget = MyWidget()
    widget.show()
    app.exec_()