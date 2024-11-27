from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import Qt, QRect, QPoint
from PySide6.QtGui import QPainter, QColor

from Board import Board
from BoardImages import BoardImages
from Constants import CELL_SIZE

class BoardWidget(QtWidgets.QWidget):

    moveMadeByPlayer = QtCore.Signal(object)

    def __init__(self, board: Board):
        super().__init__()
        self.setFixedSize(CELL_SIZE * 8, CELL_SIZE * 8)
        self.board = board
        self.boardImages = BoardImages(CELL_SIZE)
        self.selectedCell = None
        self.possibleMoves = []

    def paintEvent(self, event):
        painter = QPainter(self)
        self.drawBoard(painter)
        self.drawPieces(painter)  
        self.drawPossibleMoves(painter)    
    
    def mouseReleaseEvent(self, event):
        x = int(event.position().x() // CELL_SIZE)
        y = int(7 - event.position().y() // CELL_SIZE)

        if (x < 0 or x > 7 or y < 0 or y > 7):
            return
        
        cellClicked = self.board.getPiece(x, y)

        if self.selectedCell:
            moveMade = self.board.makeMove(self.selectedCell, (x, y))
            self.selectedCell = None
            self.possibleMoves = []
            if moveMade:
                self.moveMadeByPlayer.emit(None)
        else:
            if self.selectedCell != (x, y) and cellClicked and cellClicked[0] == self.board.getTurn():
                self.selectedCell = (x, y)
                self.possibleMoves = self.board.getMovesForPiece(x, y)
            else:
                self.selectedCell = None
                self.possibleMoves = []

        self.update()
        
    def drawBoard(self, painter: QPainter):
        startX = startY = 0
        blackColor = QColor(180, 136, 100)
        blackColorSelected = QColor(216, 195, 84)
        whiteColor = QColor(234, 214, 177)
        whiteColorSelected = QColor(243, 234, 122)
        inCheckColor = QColor(255, 0, 0, 100)
        painter.setPen(Qt.GlobalColor.transparent)
        
        for y in range(0, 8):
            for x in range(0, 8):
                if (x + y) % 2 == 0:
                    painter.setBrush(whiteColor if self.selectedCell != (x, 7 - y) else whiteColorSelected)
                else:
                    painter.setBrush(blackColor if self.selectedCell != (x, 7 - y) else blackColorSelected)
                rectangle = QRect(startX + x * CELL_SIZE, startY + y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                painter.drawRect(rectangle)
                if self.board.getPiece(x, 7 - y) == (self.board.getTurn() + 'K') and self.board.isCurrentPlayerInCheck():
                    painter.setBrush(inCheckColor)
                    painter.drawRect(rectangle)

    def drawPieces(self, painter: QPainter):
        for y in range(0, 8):
            for x in range(0, 8):
                piece = self.board.getPiece(x, 7 - y)
                if piece:
                    if piece == (self.board.getTurn() + 'K') and self.board.isCurrentPlayerInCheckmate():
                        painter.drawImage(x * CELL_SIZE, y * CELL_SIZE, self.boardImages.getImage(piece+'#'))
                    elif piece[1] == 'K' and self.board.isDraw():
                        painter.drawImage(x * CELL_SIZE, y * CELL_SIZE, self.boardImages.getImage(piece+'='))
                    else:
                        painter.drawImage(x * CELL_SIZE, y * CELL_SIZE, self.boardImages.getImage(piece))

    def drawPossibleMoves(self, painter: QPainter):
        for move in self.possibleMoves:
            painter.setBrush(QColor(0, 0, 0, 100))
            painter.setPen(Qt.GlobalColor.transparent)
            painter.drawEllipse(QPoint(move[0] * CELL_SIZE + 0.5 * CELL_SIZE, (7 - move[1]) * CELL_SIZE + 0.5 * CELL_SIZE), CELL_SIZE / 4, CELL_SIZE / 4)