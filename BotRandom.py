import random
import time
from Board import Board
from BotBase import BotBase

# Makes a random move from all possible moves
class BotRandom(BotBase):
    def __init__(self):
        super().__init__()

    def makeMove(self, board: Board):
        moves = board.getValidMoves(board.getTurn())
        if(len(moves) > 0):
            rnd = random.randint(0, len(moves) - 1)
            time.sleep(0.3) # Imitate thinking
            board.makeMove(moves[rnd][0], moves[rnd][1])
        