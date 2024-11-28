import random
import time
from Board import Board
from BotBase import BotBase

# Makes a move that gives the best score immediately (0.5 depth)
class BotGreedy(BotBase):
    def __init__(self):
        super().__init__()

    def makeMove(self, board: Board):
        myColor = board.getTurn()
        moves = board.getValidMoves(myColor)
        random.shuffle(moves) # Randomize moves to avoid always picking the first one

        if(len(moves) > 0):
            bestMove = moves[0]
            bestScore = -1000000
            for move in moves:
                boardCopy = board.copy()
                boardCopy.makeMove(move[0], move[1])
                score = boardCopy.gameState.score
                if myColor == 'B':
                    score = -score
                if score > bestScore:
                    bestScore = score
                    bestMove = move

            time.sleep(0.3) # Imitate thinking
            board.makeMove(bestMove[0], bestMove[1])
        