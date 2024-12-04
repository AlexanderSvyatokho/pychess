from Board import Board
from Constants import *

# Base class for all bots
class BotBase:
    def __init__(self):
        pass

    def makeMove(self, board: Board):
        pass

    # Selects only moves that are worth considering: captures, promotions, checks
    def selectSignificantMoves(self, board: Board, moves: list[tuple[tuple[int, int], tuple[int, int]]]) -> list[tuple[tuple[int, int], tuple[int, int]]]:
        return self.sortMovesBySignificance(board, moves, True)
    
    def sortMovesBySignificance(self, board: Board, moves: list[tuple[tuple[int, int], tuple[int, int]]], removeInsignificant: bool = False) -> list[tuple[tuple[int, int], tuple[int, int]]]:
        
        # Picked moves with their scores: [((from, to), score)]
        significantMovesWithScore = []
        for move in moves:

            # Capture move
            capturedPiece = board.getPiece(*move[1])
            if capturedPiece != None:
                significantMovesWithScore.append((move, PIECE_VALUES.get(capturedPiece)))

            # Promotion
            if board.getPiece(*move[0])[1] == 'P' and move[1][1] == 7:
                significantMovesWithScore.append((move, 8))

            boardCopy = board.copy()
            boardCopy.makeMove(move[0], move[1], False)

            # Check and checkmate
            if boardCopy.isCurrentPlayerInCheck():
                if boardCopy.isCurrentPlayerInCheckmate():
                    significantMovesWithScore.append((move, 1000))
                else:
                    significantMovesWithScore.append((move, 3))

            # Draw
            if boardCopy.isDraw():
                significantMovesWithScore.append((move, 100))

            if not removeInsignificant:
                significantMovesWithScore.append((move, 0))

        significantMovesWithScore.sort(key=lambda x: x[1], reverse=True)
        filteredMoves = [move[0] for move in significantMovesWithScore]
        return filteredMoves