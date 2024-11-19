import sys
from PySide6 import QtWidgets
from PySide6.QtCore import Qt, QRect
from PySide6.QtGui import QPainter, QColor

from Board import Board;
from BoardImages import BoardImages;
from Constants import CELL_SIZE

class BoardWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.board = Board()
        self.boardImages = BoardImages(CELL_SIZE)
        self.selectedCell = None

    def paintEvent(self, event):
        painter = QPainter(self)
        self.drawBoard(painter)
        self.drawPieces(painter)  
    
    def mouseReleaseEvent(self, event):
        x = int(event.position().x() // CELL_SIZE)
        y = int(7 - event.position().y() // CELL_SIZE)

        pieceClicked = self.board.getPiece(x, y)

        if self.selectedCell and pieceClicked == None:
            self.board.movePiece(self.selectedCell, (x, y))
            self.selectedCell = None
        else:
            if self.selectedCell != (x, y) and pieceClicked and pieceClicked[0] == self.board.getTurn():
                self.selectedCell = (x, y)
            else:
                self.selectedCell = None

        self.update()
        
    def drawBoard(self, painter):
        startX = startY = 0
        blackColor = QColor(180, 136, 100)
        blackColorSelected = QColor(216, 195, 84)
        whiteColor = QColor(234, 214, 177)
        whiteColorSelected = QColor(243, 234, 122)
        painter.setPen(Qt.GlobalColor.transparent)
        
        for y in range(0, 8):
            for x in range(0, 8):
                if (x + y) % 2 == 0:
                    painter.setBrush(whiteColor if self.selectedCell != (x, 7 - y) else whiteColorSelected)
                else:
                    painter.setBrush(blackColor if self.selectedCell != (x, 7 - y) else blackColorSelected)
                rectangle = QRect(startX + x * CELL_SIZE, startY + y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                painter.drawRect(rectangle)

    def drawPieces(self, painter):
        for y in range(0, 8):
            for x in range(0, 8):
                piece = self.board.getPiece(x, 7 - y)
                if piece:
                    painter.drawImage(x * CELL_SIZE, y * CELL_SIZE, self.boardImages.getImage(piece))