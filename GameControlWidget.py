from PySide6 import QtWidgets, QtCore

from Constants import *
from GameState import GameState
from Utils import *

class GameControlWidget(QtWidgets.QWidget):
    
    newGameStarted = QtCore.Signal(object)

    def __init__(self):
        super().__init__()

        # New game group box
        self.gbNewGame = QtWidgets.QGroupBox('New Game')
        self.btnNewGame = QtWidgets.QPushButton('Start New Game')
        self.btnNewGame.clicked.connect(self.btnNewGameClicked)
        self.txtSelectOpponent = QtWidgets.QLabel('Select Opponent', alignment=QtCore.Qt.AlignLeft)
        self.cmbOpponent = QtWidgets.QComboBox()
        self.cmbOpponent.addItem(OpponentType.HUMAN.value)
        self.cmbOpponent.addItem(OpponentType.BOT_RANDOM.value)
        self.cmbOpponent.addItem(OpponentType.BOT_GREEDY.value)
        self.cmbOpponent.addItem(OpponentType.BOT_DEPTH1.value)
        self.cmbOpponent.addItem(OpponentType.BOT_DEPTH2.value)
        self.cmbOpponent.addItem(OpponentType.BOT_DEPTH3.value)
        self.cmbOpponent.setCurrentIndex(self.cmbOpponent.count() - 2)
      
        self.vboxNewGame = QtWidgets.QVBoxLayout()
        self.vboxNewGame.addWidget(self.txtSelectOpponent)
        self.vboxNewGame.addWidget(self.cmbOpponent)
        self.vboxNewGame.addWidget(self.btnNewGame)
        
        self.gbNewGame.setLayout(self.vboxNewGame)

        # Moves list group box
        self.gbGameMoves = QtWidgets.QGroupBox('Game Moves')
        self.lstGameMoves = QtWidgets.QListWidget(self)
       
        self.vboxMovesList = QtWidgets.QVBoxLayout()
        self.vboxMovesList.addWidget(self.lstGameMoves)
        
        self.gbGameMoves.setLayout(self.vboxMovesList)

        # Layout        
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.gbNewGame)
        self.layout.addWidget(self.gbGameMoves)

    @QtCore.Slot()
    def btnNewGameClicked(self):
        opponent = self.cmbOpponent.currentText()
        self.newGameStarted.emit(opponent)

    def updateGamesMoves(self, gameState: GameState):
        self.lstGameMoves.clear()

        textToAdd = ''
        for i in range(len(gameState.halfMoves)):
            if i % 2 == 0:
                textToAdd = f'{i//2 + 1}: {fromCell(gameState.halfMoves[i][0])}-{fromCell(gameState.halfMoves[i][1])}'
                if i == len(gameState.halfMoves) - 1:
                    QtWidgets.QListWidgetItem(textToAdd, self.lstGameMoves)
            else:
                textToAdd += f' {fromCell(gameState.halfMoves[i][0])}-{fromCell(gameState.halfMoves[i][1])}'
                QtWidgets.QListWidgetItem(textToAdd, self.lstGameMoves)
