import random
from Board import Board
from BotBase import BotBase

# Makes a move that gives the best score taken into account best possible
# response of the opponent (1 depth)
class BotDepth1(BotBase):
    def __init__(self):
        super().__init__()

    def makeMove(self, board: Board):
        myColor = board.getTurn()
        moves = board.getValidMoves(myColor)
        random.shuffle(moves) # Randomize moves to avoid always picking the first one

        if(len(moves) > 0):
            bestMove = moves[0]
            # From all possible moves, pick the one that gives the worst maximum score for the opponent
            worstOpponentScore = 1000000
            for move in moves:
                boardCopy = board.copy()
                boardCopy.makeMove(move[0], move[1])

                bestOpponentScore = -1000000
                opponentMoves = boardCopy.getValidMoves('W' if myColor == 'B' else 'B')
                random.shuffle(opponentMoves)
                for opponentMove in opponentMoves:
                    boardCopy2 = boardCopy.copy()
                    boardCopy2.makeMove(opponentMove[0], opponentMove[1])
                    score = boardCopy2.gameState.score
                    if myColor == 'W':
                        score = -score
                    if score > bestOpponentScore:
                        bestOpponentScore = score

                if worstOpponentScore > bestOpponentScore:
                    worstOpponentScore = bestOpponentScore
                    bestMove = move
  
            board.makeMove(bestMove[0], bestMove[1])
        