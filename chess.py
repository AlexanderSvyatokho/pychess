import sys
import random
from PySide6 import QtWidgets
from PySide6.QtWidgets import QGridLayout
from PySide6.QtCore import Qt, QRect
from PySide6.QtGui import QPainter

from Board import Board
from BoardWidget import BoardWidget
from BoardImages import BoardImages
from Constants import CELL_SIZE

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.board = BoardWidget()

        main_layout = QGridLayout()
        main_layout.addWidget(self.board, 0, 0)
        self.setLayout(main_layout)
        self.setWindowTitle("Chess")

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())