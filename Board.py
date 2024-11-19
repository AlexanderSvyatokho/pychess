import logging


# Stores chess board's state
class Board:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.setToDefault()

    def setToDefault(self):
        self.turn = 'W'
        pieces = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        for i in range(8):
            self.board[i][0] = 'W' + pieces[i]
            self.board[i][1] = 'WP'
            self.board[i][6] = 'BP'
            self.board[i][7] = 'B' + pieces[i]

    def getPiece(self, x, y):
        return self.board[x][y]
     
    def getTurn(self):
        return self.turn
    
    def getValidMovesForPiece(self, x, y):
        piece = self.getPiece(x, y)
        if (not piece):
            logging.warning('Board: getValidMovesForPiece: no piece at x and y')
            return []
        
        if (piece[0] != self.turn): 
            logging.warning('Board: getValidMovesForPiece: attempted to move opponent\'s piece')
            return []
    
        if (piece[1] == 'P'):
            return self.getValidMovesForPawn(x, y)
        elif (piece[1] == 'R'):
            return self.getValidMovesForRook(x, y)
        
        return []
    
    def getValidMovesForPawn(self, x, y):
        piece = self.getPiece(x, y)
        if (not piece or piece[1] != 'P'):
            logging.warning(f'Board: getValidMovesForPawn: no pawn at {x, y}')
            return []
    
        moves = []
        direction = 1 if self.turn == 'W' else -1

        if (y + direction <= 7) and (y + direction >= 0):
            if self.board[x][y + direction] == None:
                moves.append((x, y + direction))
                if self.turn == 'W' and y == 1 and self.board[x][y + 2 * direction] == None:
                    moves.append((x, y + 2 * direction))
                if self.turn == 'B' and y == 6 and self.board[x][y + 2 * direction] == None:
                    moves.append((x, y + 2 * direction))
            # Captures
            if x > 0 and self.board[x - 1][y + direction] and self.board[x - 1][y + direction][0] != self.turn:
                moves.append((x - 1, y + direction))
            if x < 7 and self.board[x + 1][y + direction] and self.board[x + 1][y + direction][0] != self.turn:
                moves.append((x + 1, y + direction))
        return moves
    
    def getValidMovesForRook(self, x, y):
        piece = self.getPiece(x, y)
        if (not piece or piece[1] != 'R'):
            logging.warning(f'Board: getValidMovesForRook: no rook at {x, y}')
            return []
    
        moves = []

        # Horizontal moves to the right
        for i in range(1, 8):
            if x + i < 8:
                if not self.board[x + i][y]:
                    moves.append((x + i, y))
                elif self.board[x + i][y][0] != self.turn:
                    moves.append((x + i, y)) # Capture
                    break
                else:
                    break

        # Horizontal moves to the left
        for i in range(1, 8):
            if x - i >= 0:
                if not self.board[x - i][y]:
                    moves.append((x - i, y))
                elif self.board[x - i][y][0] != self.turn:
                    moves.append((x - i, y)) # Capture
                    break
                else:
                    break   

        # Vertical moves up
        for i in range(1, 8):
            if y + i < 8:
                if not self.board[x][y + i]:
                    moves.append((x, y + i))
                elif self.board[x][y + i][0] != self.turn:
                    moves.append((x, y + i)) # Capture
                    break
                else:
                    break

        # Vertical moves down
        for i in range(1, 8):
            if y - i >= 0:
                if not self.board[x][y - i]:
                    moves.append((x, y - i))
                elif self.board[x][y - i][0] != self.turn:
                    moves.append((x, y - i)) # Capture
                    break
                else:
                    break   

        return moves
    
    def movePiece(self, fromCell, toCell):
        piece = self.getPiece(fromCell[0], fromCell[1])
        if (not piece or piece[0] != self.turn):
            logging.warning(f'Board: movePiece: Attempted to move an invalid piece at {fromCell[0], fromCell[1]}')
            return
        
        validMoves = self.getValidMovesForPiece(fromCell[0], fromCell[1])
        if toCell not in validMoves:
            logging.warning(f'Board: movePiece: Invalid move for a piece at {fromCell[0], fromCell[1]}')
            return
        
        self.board[toCell[0]][toCell[1]] = self.board[fromCell[0]][fromCell[1]]
        self.board[fromCell[0]][fromCell[1]] = None
        self.nextTurn()

    def nextTurn(self):
        self.turn = 'W' if self.turn == 'B' else 'B'

    def __str__(self):
        str = ''
        for y in range(0, 8):
            for x in range(0, 8):
                pc = self.board[x][7 - y]
                str += pc if pc else '[]'
            str += '\n'
        return str
