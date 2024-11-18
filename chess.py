import sys
import random
from PySide6 import QtWidgets
from PySide6.QtCore import Qt, QRect
from PySide6.QtGui import QPainter, QImage

CELL_SIZE = 50
class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

    def paintEvent(self, event):
        painter = QPainter(self)
        self.drawBoard(painter)

        img = QImage()
        img.load("resources/imgs/rook-b.png")
        img = img.scaled(CELL_SIZE, CELL_SIZE, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        painter.drawImage(0, 0, img)

        img2 = QImage()
        img2.load("resources/imgs/knight-b.png")
        img2 = img2.scaled(CELL_SIZE, CELL_SIZE, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        painter.drawImage(CELL_SIZE, 0, img2)
        

    def drawBoard(self, painter):
        startX = 0
        startY = 0
        cellNum = 0
        blackColor = Qt.GlobalColor.darkRed
        whiteColor = Qt.GlobalColor.lightGray
        painter.setPen(Qt.GlobalColor.transparent)
        
        for y in range(0, 8):
            for x in range(0, 8):
                if (cellNum + 1) % 2 == 0:
                    painter.setBrush(blackColor)
                else:
                    painter.setBrush(whiteColor)
                rectangle = QRect(startX + x * CELL_SIZE, startY + y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                painter.drawRect(rectangle)   
                cellNum += 1
            cellNum += 1
    
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())