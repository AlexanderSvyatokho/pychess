from Board import Board

# Base class for all bots
class BotBase:
    def __init__(self):
        pass

    def makeMove(self, board: Board):
        pass

    # Selects only moves that are worth considering: captures, promotions, checks
    def selectSignificantMoves(self, board: Board, moves: list[tuple[tuple[int, int], tuple[int, int]]]) -> list[tuple[tuple[int, int], tuple[int, int]]]:
        filteredMoves = []
        for move in moves:

            # Capture move
            if board.getPiece(*move[1]) != None:
                filteredMoves.append(move)

            # Promotion
            if board.getPiece(*move[0])[1] == 'P' and move[1][1] == 7:
                filteredMoves.append(move)

            # Check
            boardCopy = board.copy()
            boardCopy.makeMove(move[0], move[1], False)
            if boardCopy.isCurrentPlayerInCheck():
                filteredMoves.append(move)

        return filteredMoves
    