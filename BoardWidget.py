import sys
from PySide6 import QtWidgets
from PySide6.QtCore import Qt, QRect
from PySide6.QtGui import QPainter

from Board import Board;
from BoardImages import BoardImages;
from Constants import CELL_SIZE

class BoardWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.board = Board()
        self.boardImages = BoardImages(CELL_SIZE)

    def paintEvent(self, event):
        painter = QPainter(self)
        self.drawBoard(painter)
        self.drawPieces(painter)  
    
    def mouseReleaseEvent(self, event):
        print(f"Mouse clicked at {event.position().x()}, {event.position().y()}")

    def drawBoard(self, painter):
        startX = 0
        startY = 0
        blackColor = Qt.GlobalColor.darkRed
        whiteColor = Qt.GlobalColor.lightGray
        painter.setPen(Qt.GlobalColor.transparent)
        
        for y in range(0, 8):
            for x in range(0, 8):
                if (x + y) % 2 == 0:
                    painter.setBrush(whiteColor)
                else:
                    painter.setBrush(blackColor)
                rectangle = QRect(startX + x * CELL_SIZE, startY + y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                painter.drawRect(rectangle)

    def drawPieces(self, painter):
        for y in range(0, 8):
            for x in range(0, 8):
                pc = self.board.getPiece(x, 7 - y)
                if pc:
                    painter.drawImage(x * CELL_SIZE, y * CELL_SIZE, self.boardImages.getImage(pc))