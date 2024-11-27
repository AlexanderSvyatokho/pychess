from PySide6 import QtWidgets, QtCore

from Constants import *

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
      
        self.vboxNewGame = QtWidgets.QVBoxLayout()
        self.vboxNewGame.addWidget(self.txtSelectOpponent)
        self.vboxNewGame.addWidget(self.cmbOpponent)
        self.vboxNewGame.addWidget(self.btnNewGame)
        
        self.gbNewGame.setLayout(self.vboxNewGame)

        # Moves list group box
        # self.gbGameMoves = QtWidgets.QGroupBox('Game Moves')
        # self.lstGameMoves = QtWidgets.QListWidget(self)
        # QtWidgets.QListWidgetItem('1: e2-e4 e7-e5', self.lstGameMoves)
        # QtWidgets.QListWidgetItem('2: e2-e4 e7-e5', self.lstGameMoves)
        # QtWidgets.QListWidgetItem('3: e2-e4 e7-e5', self.lstGameMoves)
        # QtWidgets.QListWidgetItem('3: ToDo ToDo', self.lstGameMoves)
       
        # self.vboxMovesList = QtWidgets.QVBoxLayout()
        # self.vboxMovesList.addWidget(self.lstGameMoves)
        
        # self.gbGameMoves.setLayout(self.vboxMovesList)

        # Layout        
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.gbNewGame)
        # self.layout.addWidget(self.gbGameMoves)
        self.layout.addStretch(1)

    @QtCore.Slot()
    def btnNewGameClicked(self):
        opponent = self.cmbOpponent.currentText()
        self.newGameStarted.emit(opponent)