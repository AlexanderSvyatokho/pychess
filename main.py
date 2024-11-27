import sys
import logging

from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QGridLayout

from BoardWidget import BoardWidget
from GameControlWidget import GameControlWidget

from Board import Board
from Constants import CELL_SIZE

logging.basicConfig(level=logging.DEBUG)

class PyChess(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.board = Board()
        self.boardWidget = BoardWidget(self.board)
        self.gameControl = GameControlWidget()

        main_layout = QGridLayout()
        main_layout.addWidget(self.boardWidget, 0, 0)
        main_layout.addWidget(self.gameControl, 0, 1)
        self.setLayout(main_layout)
        self.setWindowTitle("Chess")

        self.gameControl.newGameStarted.connect(self.onNewGame)

    @QtCore.Slot()
    def onNewGame(self, opponent):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("New Game")
        msgBox.setIcon(QtWidgets.QMessageBox.Question)
        msgBox.setText("Are you sure you want to start a new game?")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        ret = msgBox.exec()

        if ret == QtWidgets.QMessageBox.Yes:
            self.board.reset()
            self.boardWidget.update()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = PyChess()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())