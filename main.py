import sys
import logging

from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QGridLayout, QStatusBar

from BoardWidget import BoardWidget
from GameControlWidget import GameControlWidget

from Board import Board
from BotRandom import BotRandom
from BotThread import BotThread
from Constants import *

logging.basicConfig(level=logging.DEBUG)

class PyChess(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.board = Board()
        self.bot = None
        self.boardWidget = BoardWidget(self.board)
        self.gameControl = GameControlWidget()
        self.statusBar = QStatusBar(self)
        self.statusBar.showMessage('Welcome to PyChess!')
        
        mainLayout = QGridLayout()
        mainLayout.addWidget(self.boardWidget, 0, 0)
        mainLayout.addWidget(self.gameControl, 0, 1)
        mainLayout.addWidget(self.statusBar, 1, 0, 1, 2)
        self.setLayout(mainLayout)
        self.setWindowTitle('PyChess')

        self.gameControl.newGameStarted.connect(self.onNewGame)
        self.boardWidget.moveMadeByPlayer.connect(self.onMoveMadeByPlayer)

    @QtCore.Slot()
    def onNewGame(self, opponent):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle('New Game')
        msgBox.setIcon(QtWidgets.QMessageBox.Question)
        msgBox.setText('Are you sure you want to start a new game?')
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        ret = msgBox.exec()

        if ret == QtWidgets.QMessageBox.Yes:
            self.board.reset()
            if opponent == OpponentType.BOT_RANDOM.value:
                self.bot = BotRandom()
            else:
                self.bot = None
            self.boardWidget.update()

    @QtCore.Slot()
    def onMoveMadeByPlayer(self):
        if self.bot:
            # Run the bot in a separate thread to avoid blocking the UI
            self.botThread = BotThread(self.bot, self.board)
            self.botThread.finished.connect(self.onBotMoveReady)
            self.botThread.start()

        self.statusBar.showMessage(f'Score: {self.board.gameState.score}')

    @QtCore.Slot()
    def onBotMoveReady(self):
        self.boardWidget.update()
        self.botThread.quit()
        self.botThread.wait()
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = PyChess()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())