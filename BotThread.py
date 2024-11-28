
from PySide6 import QtCore

class BotThread(QtCore.QThread):

    def __init__(self, bot, board):
        super().__init__()
        self.bot = bot
        self.board = board

    def run(self):
        self.bot.makeMove(self.board)