import sys
import logging

from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QGridLayout, QStatusBar

from BoardWidget import BoardWidget
from GameControlWidget import GameControlWidget

from Constants import *
from Board import Board
from BotThread import BotThread
from BotRandom import BotRandom
from BotGreedy import BotGreedy
from BotDepth1 import BotDepth1

logging.basicConfig(level=logging.DEBUG)

class PyChess(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.board = Board()
        self.board.clear()
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

        userConfirmed = True

        if len(self.board.gameState.halfMoves) > 0:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle('New Game')
            msgBox.setIcon(QtWidgets.QMessageBox.Question)
            msgBox.setText('Are you sure you want to start a new game?')
            msgBox.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            ret = msgBox.exec()
            userConfirmed = ret == QtWidgets.QMessageBox.Yes

        if userConfirmed:
            self.board.reset()
            if opponent == OpponentType.BOT_RANDOM.value:
                self.bot = BotRandom()
            elif opponent == OpponentType.BOT_GREEDY.value:
                self.bot = BotGreedy()
            elif opponent == OpponentType.BOT_DEPTH1.value:
                self.bot = BotDepth1()
            else:
                self.bot = None
            self.boardWidget.update()
            self.updateUIAfterMove()

    @QtCore.Slot()
    def onMoveMadeByPlayer(self):
        if self.bot and self.board.gameState.isGameOngoing():
            # Run the bot in a separate thread to avoid blocking the UI
            self.botThread = BotThread(self.bot, self.board)
            self.botThread.finished.connect(self.onMoveMadeByBot)
            self.botThread.start()
        self.updateUIAfterMove()

    @QtCore.Slot()
    def onMoveMadeByBot(self):
        self.boardWidget.update()
        self.botThread.quit()
        self.botThread.wait()
        self.updateUIAfterMove()

    def updateUIAfterMove(self):
        self.statusBar.showMessage(f'Move: {len(self.board.gameState.halfMoves) // 2 + 1} | Score: {self.board.gameState.materialScore}')
        self.gameControl.updateGamesMoves(self.board.gameState)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = PyChess()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())