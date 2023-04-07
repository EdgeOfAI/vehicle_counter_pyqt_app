from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor, QPen, QImage, QFont
from PyQt5.QtCore import Qt, QPoint, QRect
from config import side_names


class Line:
    def __init__(self, start, end):
        self.line_start = start
        self.line_end = end
        self.circle_start = QRect(start.x()-7, start.y()-7, 14, 14)
        self.circle_end = QRect(end.x()-7, end.y()-7, 14, 14)
        self.start_hovered = False
        self.end_hovered = False
        self.color = QColor(0, 255, 0)
        self.line_name = ''
        
    def draw(self, painter, line_letter):
        pen = QPen()
        pen.setWidth(15)
        pen.setColor(self.color)
        painter.setPen(pen)
        painter.drawLine(self.line_start, self.line_end)

        # draw circles
        painter.setBrush(QColor(0, 255, 0))
        painter.drawEllipse(self.circle_start)
        painter.drawEllipse(self.circle_end)

        # change circle color if mouse hovers over it
        if self.start_hovered:
            painter.setBrush(QColor(255, 0, 0))
            painter.drawEllipse(self.circle_start)
        elif self.end_hovered:
            painter.setBrush(QColor(0, 0, 255))
            painter.drawEllipse(self.circle_end)
        
        # # add text at the center of the line
        font = QFont()
        font.setPointSize(25)
        font.setBold(True)
        painter.setPen(QColor(255, 0, 0)) 
        center_x = (self.line_start.x() + self.line_end.x()) / 2
        center_y = (self.line_start.y() + self.line_end.y()) / 2
        painter.setFont(font)
        self.center_point = QPoint(center_x, center_y)
        self.line_name = line_letter
        painter.drawText(self.center_point, self.line_name)

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

class DrawDynamicLineWidget(QMainWindow):
    def __init__(self, image, max_lines=4):
        super().__init__()
        self.scale = 2
        self.width = int(image.shape[1] / self.scale)
        self.height = int(image.shape[0] / self.scale)
        self.setGeometry(100, 100, self.width, self.height)
        self.lines = []
        self.background_image = QImage(self.convert_cv2_qimage(image))
        self.background_image = self.background_image.scaled(self.width, self.height)
        self.max_lines = max_lines
        self.current_line = None
    
    def convert_cv2_qimage(self, cv_image):
        height, width, channel = cv_image.shape
        bytes_per_line = 3 * width
        q_image = QImage(cv_image.data, width, height, bytes_per_line, QImage.Format_RGB888)
        return q_image.rgbSwapped()

    def paintEvent(self, event):
        painter = QPainter(self)
        # draw background image
        painter.drawImage(0, 0, self.background_image)

        # draw lines
        for i, line in enumerate(self.lines):
            line.draw(painter, side_names[i])

    def mousePressEvent(self, event):
        if len(self.lines) < self.max_lines:
            # create a new line
            line = Line(event.pos(), event.pos())
            self.lines.append(line)
            self.current_line = line
            line.mousePressEvent(event)
        else:
            # check if any existing line was clicked
            for line in self.lines:
                if line.circle_start.contains(event.pos()):
                    self.current_line = line
                    line.mousePressEvent(event)
                    break
                elif line.circle_end.contains(event.pos()):
                    self.current_line = line
                    line.mousePressEvent(event)
                    break

    def mouseMoveEvent(self, event):
        if self.current_line is not None:
            self.current_line.mouseMoveEvent(event)
            self.update()

    def mouseReleaseEvent(self, event):
        if self.current_line is not None:
            self.current_line.mouseReleaseEvent(event)
            print(self.current_line.line_start, self.current_line.line_end)
            self.current_line = None
            self.update()
    
    def getPolygonPoints(self):
        points = []
        for line in self.lines:
            start_point = [line.line_start.x()*self.scale, line.line_start.y()*self.scale]
            end_point = [line.line_end.x()*self.scale, line.line_end.y()*self.scale]
            line_points = [start_point, end_point]
            points.append(line_points)
        return points

if __name__ == "__main__":
    app = QApplication([])
    widget = DrawDynamicLineWidget()
    widget.show()
    app.exec_()
