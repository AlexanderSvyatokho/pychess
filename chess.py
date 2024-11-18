import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        self.drawBoard(painter)

    def drawBoard(self, painter):
        startX = 0
        startY = 0
        cellSize = 40
        cellNum = 0
        blackColor = QtCore.Qt.GlobalColor.darkRed
        whiteColor = QtCore.Qt.GlobalColor.lightGray
        painter.setPen(QtCore.Qt.GlobalColor.transparent)
        
        for y in range(0, 8):
            for x in range(0, 8):
                if (cellNum + 1) % 2 == 0:
                    painter.setBrush(blackColor)
                else:
                    painter.setBrush(whiteColor)
                rectangle = QtCore.QRect(startX + x * cellSize, startY + y * cellSize, cellSize, cellSize)
                painter.drawRect(rectangle)   
                cellNum += 1
            cellNum += 1
    
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())