import sys
import logging

from PySide6 import QtWidgets
from PySide6.QtWidgets import QGridLayout

from BoardWidget import BoardWidget
from Constants import CELL_SIZE

logging.basicConfig(level=logging.DEBUG)

class PyChess(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.board = BoardWidget()

        main_layout = QGridLayout()
        main_layout.addWidget(self.board, 0, 0)
        self.setLayout(main_layout)
        self.setWindowTitle("Chess")

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = PyChess()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())