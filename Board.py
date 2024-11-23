import logging


# Stores chess board's state
class Board:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.setToDefault()

    def copy(self):
        newBoard = Board()
        newBoard.board = [col.copy() for col in self.board]
        newBoard.turn = self.turn
        newBoard.canCastle = self.canCastle.copy()
        return newBoard

    def setToDefault(self):
        self.turn = 'W'
        self.canCastle = {'W': {'K': True, 'Q': True}, 'B': {'K': True, 'Q': True}}
        self.gameState = { 
            'draw': { 'draw': False, 'reason': '' },
            'check': { 'check': False, 'who': '' },
            'checkmate': { 'checkmate': False, 'who': '' },
        }
        
        # Set up the board with pieces
        pieces = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        for i in range(8):
            self.board[i][0] = 'W' + pieces[i]
            self.board[i][1] = 'WP'
            self.board[i][6] = 'BP'
            self.board[i][7] = 'B' + pieces[i]

    def setToDefaultTest(self):
        self.turn = 'W'
        self.canCastle = {'W': {'K': True, 'Q': True}, 'B': {'K': True, 'Q': True}}
        self.gameState = { 
            'draw': { 'draw': False, 'reason': '' },
            'check': { 'check': False, 'who': '' },
            'checkmate': { 'checkmate': False, 'who': '' },
        }

        # Set up the board with pieces
        pieces = ['R', None, None, 'Q', 'K', None, None, 'R']
        for i in range(8):
            self.board[i][0] = 'W' + pieces[i] if pieces[i] else None
            self.board[i][1] = None
            self.board[i][6] = None
            self.board[i][7] = 'B' + pieces[i] if pieces[i] else None

        self.board[1][2] = 'WP'
        self.board[6][6] = 'BP'

    def getPiece(self, x, y):
        return self.board[x][y]
     
    def getTurn(self):
        return self.turn
    
    ############################################################
    # Moves handling methods
    ############################################################
    
    # Get a list of cells a piece at x, y can move to
    def getMovesForPiece(self, x, y) -> list[tuple[int, int]]:
        piece = self.board[x][y]
        if (not piece):
            logging.warning('Board: getMovesForPiece: no piece at x and y')
            return []
        
        pieceColor = self.board[x][y][0]
        moves = []

        if (piece[1] == 'P'):
            moves = self.getMovesForPawn(x, y)
        elif (piece[1] == 'R'):
            moves = self.getMovesForRook(x, y)
        elif (piece[1] == 'N'):
            moves = self.getMovesForKnight(x, y)
        elif (piece[1] == 'B'):
            moves = self.getMovesForBishop(x, y)
        elif (piece[1] == 'Q'):
            moves = self.getMovesForQueen(x, y)
        elif (piece[1] == 'K'):
            moves = self.getMovesForKing(x, y)
        else:
            logging.error('Board: getValidMovesForPiece: unknown piece type')
            return []
        
        def checkFilter(move):
            # Check if the move puts the king in check by making the forced move
            # on the copy of a board and checking if the player is in check
            boardCopy = self.copy()
            boardCopy.forceMove((x, y), move)
            return not boardCopy.isPlayerInCheck(pieceColor)
        
        # Exclude moves that put the king in check
        moves = list(filter(checkFilter, moves))
        return moves
        
    # Get a list of cells attacked by a piece at x, y
    def getCellsAttackedByPiece(self, x, y) -> list[tuple[int, int]]:
        piece = self.board[x][y]
        if (not piece):
            logging.warning('Board: getCellsAttackedByPiece: no piece at x and y')
            return []
    
        if (piece[1] == 'P'):
            return self.getCellsAttackedByPawn(x, y)
        elif (piece[1] == 'R'):
            return self.getMovesForRook(x, y)
        elif (piece[1] == 'N'):
            return self.getMovesForKnight(x, y)
        elif (piece[1] == 'B'):
            return self.getMovesForBishop(x, y)
        elif (piece[1] == 'Q'):
            return self.getMovesForQueen(x, y)
        elif (piece[1] == 'K'):
            return self.getCellsAttackedByKing(x, y)
        else:
            logging.error('Board: getCellsAttackedByPiece: unknown piece type')
            return []
    
    # Precondition (not verified): pawn at x, y
    def getMovesForPawn(self, x, y) -> list[tuple[int, int]]:
        pieceColor = self.board[x][y][0]
        moves = []
        direction = 1 if pieceColor == 'W' else -1

        if (y + direction <= 7) and (y + direction >= 0):
            if self.board[x][y + direction] == None:
                moves.append((x, y + direction))
                if pieceColor == 'W' and y == 1 and self.board[x][y + 2 * direction] == None:
                    moves.append((x, y + 2 * direction))
                if pieceColor == 'B' and y == 6 and self.board[x][y + 2 * direction] == None:
                    moves.append((x, y + 2 * direction))
            # Captures
            if x > 0 and self.board[x - 1][y + direction] and self.board[x - 1][y + direction][0] != pieceColor:
                moves.append((x - 1, y + direction))
            if x < 7 and self.board[x + 1][y + direction] and self.board[x + 1][y + direction][0] != pieceColor:
                moves.append((x + 1, y + direction))
        return moves
    
    # Precondition (not verified): pawn at x, y
    def getCellsAttackedByPawn(self, x, y) -> list[tuple[int, int]]:
        pieceColor = self.board[x][y][0]
        moves = []
        direction = 1 if pieceColor == 'W' else -1

        if (y + direction <= 7) and (y + direction >= 0):
            if x > 0:
                moves.append((x - 1, y + direction))
            if x < 7:
                moves.append((x + 1, y + direction))
        return moves
    
    # Precondition (not verified): rook at x, y
    def getMovesForRook(self, x, y) -> list[tuple[int, int]]:
        pieceColor = self.board[x][y][0]
        moves = []

        # Horizontal moves to the right
        for i in range(1, 8):
            if x + i < 8:
                if not self.board[x + i][y]:
                    moves.append((x + i, y))
                elif self.board[x + i][y][0] != pieceColor:
                    moves.append((x + i, y)) # Capture
                    break
                else:
                    break

        # Horizontal moves to the left
        for i in range(1, 8):
            if x - i >= 0:
                if not self.board[x - i][y]:
                    moves.append((x - i, y))
                elif self.board[x - i][y][0] != pieceColor:
                    moves.append((x - i, y)) # Capture
                    break
                else:
                    break   

        # Vertical moves up
        for i in range(1, 8):
            if y + i < 8:
                if not self.board[x][y + i]:
                    moves.append((x, y + i))
                elif self.board[x][y + i][0] != pieceColor:
                    moves.append((x, y + i)) # Capture
                    break
                else:
                    break

        # Vertical moves down
        for i in range(1, 8):
            if y - i >= 0:
                if not self.board[x][y - i]:
                    moves.append((x, y - i))
                elif self.board[x][y - i][0] != pieceColor:
                    moves.append((x, y - i)) # Capture
                    break
                else:
                    break   

        return moves
       
    # Precondition (not verified): knigh at x, y
    def getMovesForKnight(self, x, y) -> list[tuple[int, int]]:
        pieceColor = self.board[x][y][0]
        moves = []

        # Up moves
        if y + 2 < 8:
            if x + 1 < 8:
                if not self.board[x + 1][y + 2]:
                    moves.append((x + 1, y + 2))
                elif self.board[x + 1][y + 2][0] != pieceColor:
                    moves.append((x + 1, y + 2)) # Capture
        if y + 1 < 8:
            if x + 2 < 8:
                if not self.board[x + 2][y + 1]:
                    moves.append((x + 2, y + 1))
                elif self.board[x + 2][y + 1][0] != pieceColor:
                    moves.append((x + 2, y + 1)) # Capture
        if y - 1 >= 0:
            if x + 2 < 8:
                if not self.board[x + 2][y - 1]:
                    moves.append((x + 2, y - 1))
                elif self.board[x + 2][y - 1][0] != pieceColor:
                    moves.append((x + 2, y - 1)) # Capture
        if y - 2 >= 0:
            if x + 1 < 8:
                if not self.board[x + 1][y - 2]:
                    moves.append((x + 1, y - 2))
                elif self.board[x + 1][y - 2][0] != pieceColor:
                    moves.append((x + 1, y - 2)) # Capture

        # Down moves
        if y - 2 >= 0:
            if x - 1 >= 0:
                if not self.board[x - 1][y - 2]:
                    moves.append((x - 1, y - 2))
                elif self.board[x - 1][y - 2][0] != pieceColor:
                    moves.append((x - 1, y - 2)) # Capture
        if y - 1 >= 0:
            if x - 2 >= 0:
                if not self.board[x - 2][y - 1]:
                    moves.append((x - 2, y - 1))
                elif self.board[x - 2][y - 1][0] != pieceColor:
                    moves.append((x - 2, y - 1)) # Capture
        if y + 1 < 8:
            if x - 2 >= 0:
                if not self.board[x - 2][y + 1]:
                    moves.append((x - 2, y + 1))
                elif self.board[x - 2][y + 1][0] != pieceColor:
                    moves.append((x - 2, y + 1))
        if y + 2 < 8:
            if x - 1 >= 0:
                if not self.board[x - 1][y + 2]:
                    moves.append((x - 1, y + 2))
                elif self.board[x - 1][y + 2][0] != pieceColor:
                    moves.append((x - 1, y + 2))

        return moves
    
    # Precondition (not verified): bishop at x, y
    def getMovesForBishop(self, x, y) -> list[tuple[int, int]]:
        pieceColor = self.board[x][y][0]
        moves = []

        # Diagonal moves to the right up
        for i in range(1, 8):
            if x + i < 8 and y + i < 8:
                if not self.board[x + i][y + i]:
                    moves.append((x + i, y + i))
                elif self.board[x + i][y + i][0] != pieceColor:
                    moves.append((x + i, y + i)) # Capture
                    break
                else:
                    break

        # Diagonal moves to the left up
        for i in range(1, 8):
            if x - i >= 0 and y + i < 8:
                if not self.board[x - i][y + i]:
                    moves.append((x - i, y + i))
                elif self.board[x - i][y + i][0] != pieceColor:
                    moves.append((x - i, y + i)) # Capture
                    break
                else:
                    break

        # Diagonal moves to the right down
        for i in range(1, 8):
            if x + i < 8 and y - i >= 0:
                if not self.board[x + i][y - i]:
                    moves.append((x + i, y - i))
                elif self.board[x + i][y - i][0] != pieceColor:
                    moves.append((x + i, y - i)) # Capture
                    break
                else:
                    break

        # Diagonal moves to the left down
        for i in range(1, 8):
            if x - i >= 0 and y - i >= 0:
                if not self.board[x - i][y - i]:
                    moves.append((x - i, y - i))
                elif self.board[x - i][y - i][0] != pieceColor:
                    moves.append((x - i, y - i)) # Capture
                    break
                else:
                    break

        return moves
        
    # Precondition (not verified): queen at x, y
    def getMovesForQueen(self, x, y) -> list[tuple[int, int]]:
        return self.getMovesForRook(x, y) + self.getMovesForBishop(x, y)
    
    # Precondition (not verified): king at x, y
    def getMovesForKing(self, x, y) -> list[tuple[int, int]]:
        pieceColor = self.board[x][y][0]
        moves = self.getCellsAttackedByKing(x, y)

        # Castling
        if pieceColor == 'W':
            if self.canCastle['W']['K'] and not self.board[5][0] and not self.board[6][0] and not self.isCellUnderAttack(4, 0, 'B') and not self.isCellUnderAttack(5, 0, 'B') and not self.isCellUnderAttack(6, 0, 'B'):
                moves.append((6, 0))
            if self.canCastle['W']['Q'] and not self.board[1][0] and not self.board[2][0] and not self.board[3][0] and not self.isCellUnderAttack(4, 0, 'B') and not self.isCellUnderAttack(3, 0, 'B') and not self.isCellUnderAttack(2, 0, 'B'):
                moves.append((2, 0))
        else:
            if self.canCastle['B']['K'] and not self.board[5][7] and not self.board[6][7] and not self.isCellUnderAttack(4, 7, 'W') and not self.isCellUnderAttack(5, 7, 'W') and not self.isCellUnderAttack(6, 7, 'W'):
                moves.append((6, 7))
            if self.canCastle['B']['Q'] and not self.board[1][7] and not self.board[2][7] and not self.board[3][7] and not self.isCellUnderAttack(4, 7, 'W') and not self.isCellUnderAttack(3, 7, 'W') and not self.isCellUnderAttack(2, 7, 'W'):
                moves.append((2, 7))

        return moves
    
    # Precondition (not verified): pawn at x, y
    def getCellsAttackedByKing(self, x, y) -> list[tuple[int, int]]:
        pieceColor = self.board[x][y][0]
        moves = []

        # Up moves
        if y + 1 < 8:
            if not self.board[x][y + 1]:
                moves.append((x, y + 1))
            elif self.board[x][y + 1][0] != pieceColor:
                moves.append((x, y + 1)) # Capture
        if y + 1 < 8 and x + 1 < 8:
            if not self.board[x + 1][y + 1]:
                moves.append((x + 1, y + 1))
            elif self.board[x + 1][y + 1][0] != pieceColor:
                moves.append((x + 1, y + 1)) # Capture
        if y + 1 < 8 and x - 1 >= 0:
            if not self.board[x - 1][y + 1]:
                moves.append((x - 1, y + 1))
            elif self.board[x - 1][y + 1][0] != pieceColor:
                moves.append((x - 1, y + 1)) # Capture

        # Down moves
        if y - 1 >= 0:
            if not self.board[x][y - 1]:
                moves.append((x, y - 1))
            elif self.board[x][y - 1][0] != pieceColor:
                moves.append((x, y - 1)) # Capture
        if y - 1 >= 0 and x + 1 < 8:
            if not self.board[x + 1][y - 1]:
                moves.append((x + 1, y - 1))
            elif self.board[x + 1][y - 1][0] != pieceColor:
                moves.append((x + 1, y - 1)) # Capture
        if y - 1 >= 0 and x - 1 >= 0:
            if not self.board[x - 1][y - 1]:
                moves.append((x - 1, y - 1))
            elif self.board[x - 1][y - 1][0] != pieceColor:
                moves.append((x - 1, y - 1)) # Capture

        # Horizontal moves
        if x + 1 < 8:
            if not self.board[x + 1][y]:
                moves.append((x + 1, y))
            elif self.board[x + 1][y][0] != pieceColor:
                moves.append((x + 1, y)) # Capture
        if x - 1 >= 0:
            if not self.board[x - 1][y]:
                moves.append((x - 1, y))
            elif self.board[x - 1][y][0] != pieceColor:
                moves.append((x - 1, y)) # Capture

        return moves
    
    # precondition (not verified): king at x, y; castling is possible
    def castle(self, kingX, kingY, side):
        pieceColor = self.board[kingX][kingY][0]
        if side == 'K':
            self.forceMove((kingX, kingY), (kingX + 2, kingY))
            self.forceMove((kingX + 3, kingY), (kingX + 1, kingY))
        elif side == 'Q':
            self.forceMove((kingX, kingY), (kingX - 2, kingY))
            self.forceMove((kingX - 4, kingY), (kingX - 1, kingY))
        
        self.canCastle[pieceColor]['K'] = False
        self.canCastle[pieceColor]['Q'] = False

    def getValidMoves(self, playerColor):
        moves = []
        for y in range(0, 8):
            for x in range(0, 8):
                piece = self.board[x][y]
                if piece and piece[0] == playerColor:
                    moves += self.getMovesForPiece(x, y)
        return moves
    
    def isCellUnderAttack(self, x, y, attackerColor):
        for i in range(0, 8):
            for j in range(0, 8):
                piece = self.board[i][j]
                if piece and piece[0] == attackerColor:
                    moves = self.getCellsAttackedByPiece(i, j)
                    if (x, y) in moves:
                        return True
        return False
    
    def isPlayerInCheck(self, playerColor):
        for y in range(0, 8):
            for x in range(0, 8):
                piece = self.board[x][y]
                if piece and piece[0] == playerColor and piece[1] == 'K':
                    return self.isCellUnderAttack(x, y, self.oppositeColor(playerColor))
                
    def hasValidMoves(self, playerColor):
        for y in range(0, 8):
            for x in range(0, 8):
                piece = self.board[x][y]
                if piece and piece[0] == playerColor:
                    if self.getMovesForPiece(x, y):
                        return True
        return False
    
    def promotePawns(self):
        # Autopromote pawns on the last rows to queens
        for y in range(0, 8):
            for x in range(0, 8):
                piece = self.board[x][y]
                if piece and piece[1] == 'P' and (y == 0 or y == 7):
                    self.board[x][y] = piece[0] + 'Q'
                
    # Moves a piece from fromCell to toCell without checking if the move is valid
    # Precondition (not verified): piece at x, y
    def forceMove(self, fromCell: tuple[int, int], toCell: tuple[int, int]):
        self.board[toCell[0]][toCell[1]] = self.board[fromCell[0]][fromCell[1]]
        self.board[fromCell[0]][fromCell[1]] = None
        self.promotePawns()
                
    ############################################################
    # Turn specific methods
    ############################################################

    # Attempts to make a move for the piece at fromCell to toCell. If the move is invalid, does nothing.
    # Changes the turn if the move is valid.
    def makeMove(self, fromCell: tuple[int, int], toCell: tuple[int, int]):
        piece = self.getPiece(fromCell[0], fromCell[1]) 
        pieceColor = piece[0]

        if (not piece):
            logging.warning(f'Board: makeMove: No piece at {fromCell[0], fromCell[1]}')
            return
        
        if (not piece or piece[0] != self.turn):
            logging.warning(f'Board: makeMove: Attempted to move opponent\'s piece {fromCell[0], fromCell[1]}. Turn: {self.turn}. Piece: {piece}')
            return
        
        validMoves = self.getMovesForPiece(fromCell[0], fromCell[1])
        if toCell not in validMoves:
            logging.warning(f'Board: makeMove: Invalid move for a piece at {fromCell[0], fromCell[1]}')
            return
        
        if piece[1] == 'K' and abs(fromCell[0] - toCell[0]) >= 2:
            # Castling
            self.castle(fromCell[0], fromCell[1], 'K' if toCell[0] > fromCell[0] else 'Q')
        else:
            # Update castling rights

            # King moves
            if piece[1] == 'K':
                self.canCastle[self.turn]['K'] = False
                self.canCastle[self.turn]['Q'] = False

            # Rook moves
            if piece[1] == 'R':
                if pieceColor == 'W':
                    if fromCell == (0, 0):
                        self.canCastle[self.turn]['Q'] = False
                    elif fromCell == (7, 0):
                        self.canCastle[self.turn]['K'] = False
                else:
                    if fromCell == (0, 7):
                        self.canCastle[self.turn]['Q'] = False
                    elif fromCell == (7, 7):
                        self.canCastle[self.turn]['K'] = False

            self.board[toCell[0]][toCell[1]] = self.board[fromCell[0]][fromCell[1]]
            self.board[fromCell[0]][fromCell[1]] = None
        
        self.promotePawns()
        self.nextTurn()

    def nextTurn(self):
        self.turn = 'W' if self.turn == 'B' else 'B'

    def isCurrentPlayerInCheck(self):
        return self.isPlayerInCheck(self.turn)
    
    def isCurrentPlayerInCheckmate(self):
        return self.isPlayerInCheck(self.turn) and not self.hasValidMoves(self.turn)

    def isStalemate(self):
        return not self.isPlayerInCheck(self.turn) and not self.hasValidMoves(self.turn)

    def isDrawByInsufficientMaterial(self):
        # Draw by insufficient material is if there is no way to end the game in checkmate:
        # - Only kings left
        # - King and single bishop
        # - King and single knight
        whitePieces = []
        blackPieces = []
        for y in range(0, 8):
            for x in range(0, 8):
                piece = self.board[x][y]
                if piece and piece[1] != 'K':
                    if piece[1] == 'P' or piece[1] == 'Q' or piece[1] == 'R':
                        return False
                    
                    if piece[0] == 'W':
                        whitePieces.append(piece)
                    else:
                        blackPieces.append(piece)

        return len(whitePieces) <= 1 and len(blackPieces) <= 1

    def isDraw(self):
        return  self.isStalemate() or self.isDrawByInsufficientMaterial()

    ############################################################
    # Utility methods
    ############################################################
    def oppositeColor(self, color):
        return 'W' if color == 'B' else 'B'

    def printState(self):
        print('Board state:')
        print(f'Turn: {self.turn}')
        print(f'Can Castle: {self.canCastle}')

    def __str__(self):
        str = ''
        for y in range(0, 8):
            for x in range(0, 8):
                pc = self.board[x][7 - y]
                str += pc if pc else '[]'
            str += '\n'
        return str
