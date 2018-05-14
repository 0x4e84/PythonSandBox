from PyQt5.QtCore import (QLineF, QPointF, QRectF, Qt)
from PyQt5.QtWidgets import QWidget, QGraphicsItem, QStyleOptionGraphicsItem
from PyQt5.QtGui import QBrush, QColor, QPainter


class GridItem(QGraphicsItem):
    def __init__(self, width, height, step):
        super().__init__()
        self.width = width
        self.height = height
        self.step = step

    def paint(self, painter: QPainter, option: 'QStyleOptionGraphicsItem', widget: QWidget = ...):
        painter.setPen(Qt.black)
        for i in range (self.width+1):
            painter.drawLine(i*self.step, 0, i*self.step, self.height*self.step)
        for j in range (self.height+1):
            painter.drawLine(0, j*self.step, self.width*self.step, j*self.step)

    def boundingRect(self):
        return QRectF(0, 0, self.width*self.step, self.height*self.step)