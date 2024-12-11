from Board import Board
from Constants import *

# Base class for all bots
class BotBase:
    def __init__(self):
        pass

    def makeMove(self, board: Board):
        pass

    # Selects only moves that are worth considering: captures, promotions, checks, etc.
    def selectSignificantMoves(self, board: Board, moves: list[tuple[tuple[int, int], tuple[int, int]]]) -> list[tuple[tuple[int, int], tuple[int, int]]]:
        return self.sortMovesBySignificance(board, moves, True)
    
    def sortMovesBySignificance(self, board: Board, moves: list[tuple[tuple[int, int], tuple[int, int]]], removeInsignificant: bool = False) -> list[tuple[tuple[int, int], tuple[int, int]]]:
        
        # Picked moves with their significance scores: [((from, to), score)]
        significantMovesWithScore = []
        for move in moves:

            # Capture move
            capturedPiece = board.getPiece(*move[1])
            if capturedPiece != None:
                multiplier = 1
                if len(board.gameState.halfMoves):
                    lastMove = board.gameState.halfMoves[-1]
                    # Prioritize recaptures and captures of moved pieces
                    if lastMove[1] == move[1]:
                        multiplier = 1.5  
                significantMovesWithScore.append((move, multiplier * PIECE_VALUES.get(capturedPiece)))

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
    
    def getBoardScore(self, board: Board, color: str) -> int:
        score = board.gameState.materialScore
        additionalScore = 0        

        # Add score for castling and penalize for loosing the right to castle
        castlingScore = 1 if board.gameState.getCastled(color) else 0
        if board.gameState.getCastled(color) == False and board.gameState.getCanCastle(color, 'K') == False:
            castlingScore = -1

        # To do: add more factors to the score

        additionalScore += castlingScore
        if color == 'B':
            additionalScore = -additionalScore

        return score + additionalScore