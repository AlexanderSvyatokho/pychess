import logging
from GameState import GameState
from Utils import oppositeColor
from Constants import *

# Stores chess board's state
class Board:
    def __init__(self):
        self.board = [None for _ in range(64)]
        self.gameState = GameState()
        self.setToDefault()

    def clear(self):
        self.board = [None for _ in range(64)]

    def copy(self):
        newBoard = Board()
        newBoard.board = self.board.copy()
        newBoard.gameState = self.gameState.copy()
        return newBoard

    def setToDefault(self):
        # self.setToDefaultTest()
        # return
    
        self.gameState.setToDefault()
        
        # Set up the board with pieces
        self.board = [None for _ in range(64)]
        pieces = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        for i in range(8):
            self.board[i] = 'W' + pieces[i]
            self.board[i + 8 * 1] = 'WP'
            self.board[i + 8 * 6] = 'BP'
            self.board[i + 8 * 7] = 'B' + pieces[i]

    def setToDefaultTest(self):
        self.gameState.setToDefault()

        # Set up the board with pieces
        str = '''[][][][]BK[][]BR
                 [][][][][]BPBPBP
                 [][][][][][][][]
                 [][][][][][][][]
                 [][][][][][][][]
                 [][][][][][][][]
                 [][][][][][][][]
                 [][][][]WK[]WR[]'''.replace(' ','')
        
        self.setBoardFromString(str) 

    def reset(self):
        self.setToDefault()

    def getPiece(self, x, y):
        return self.board[x + 8 * y]
     
    def getTurn(self):
        return self.gameState.turn
    
    ############################################################
    # Moves handling methods
    ############################################################
    
    # Get a list of cells a piece at x, y can move to
    def getMovesForPiece(self, x, y) -> list[tuple[int, int]]:
        piece = self.board[x + 8 * y]
        if (not piece):
            logging.warning('Board: getMovesForPiece: no piece at x and y')
            return []
        
        pieceColor = self.board[x + 8 * y][0]
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
            logging.error('Board: getMovesForPiece: unknown piece type')
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
        piece = self.board[x + 8 * y]
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
        
    def isCellAttackedByPiece(self, pieceCell: tuple[int, int], cellToCheck: tuple[int, int]) -> bool:
        pieceX, pieceY = pieceCell
        piece = self.board[pieceX + 8 * pieceY]
        if (not piece):
            logging.warning('Board: isCellAttackedByPiece: no piece at x and y')
            return False
    
        if (piece[1] == 'P'):
            return self.isCellAttackedByPawn(pieceCell, cellToCheck)
        elif (piece[1] == 'R'):
            return self.isCellAttackedByRook(pieceCell, cellToCheck)
        elif (piece[1] == 'N'):
            return self.isCellAttackedByKnight(pieceCell, cellToCheck)
        elif (piece[1] == 'B'):
            return self.isCellAttackedByBishop(pieceCell, cellToCheck)
        elif (piece[1] == 'Q'):
            return self.isCellAttackedByQueen(pieceCell, cellToCheck)
        elif (piece[1] == 'K'):
            return self.isCellAttackedByKing(pieceCell, cellToCheck)
        else:
            logging.error('Board: isCellAttackedByPiece: unknown piece type')
            return False
    
    # Precondition (not verified): pawn at x, y
    def getMovesForPawn(self, x, y) -> list[tuple[int, int]]:
        pieceColor = self.board[x + 8 * y][0]
        moves = []
        direction = 1 if pieceColor == 'W' else -1

        if (y + direction <= 7) and (y + direction >= 0):
            if self.board[x + 8 * (y + direction)] == None:
                moves.append((x, y + direction))
                if pieceColor == 'W' and y == 1 and self.board[x + 8 * (y + 2 * direction)] == None:
                    moves.append((x, y + 2 * direction))
                if pieceColor == 'B' and y == 6 and self.board[x + 8 * (y + 2 * direction)] == None:
                    moves.append((x, y + 2 * direction))
            # Captures
            if x > 0 and self.board[x - 1 + 8 * (y + direction)] and self.board[x - 1 + 8 * (y + direction)][0] != pieceColor:
                moves.append((x - 1, y + direction))
            if x < 7 and self.board[x + 1 + 8 * (y + direction)] and self.board[x + 1 + 8 * (y + direction)][0] != pieceColor:
                moves.append((x + 1, y + direction))
        return moves
    
    # Precondition (not verified): pawn at x, y
    def getCellsAttackedByPawn(self, x, y) -> list[tuple[int, int]]:
        pieceColor = self.board[x + 8 * y][0]
        moves = []
        direction = 1 if pieceColor == 'W' else -1

        if (y + direction <= 7) and (y + direction >= 0):
            if x > 0:
                moves.append((x - 1, y + direction))
            if x < 7:
                moves.append((x + 1, y + direction))
        return moves

    # Precondition (not verified): pawn at x, y
    def isCellAttackedByPawn(self, pieceCell: tuple[int, int], cellToCheck: tuple[int, int]) -> bool:
        pieceX, pieceY = pieceCell
        pieceColor = self.board[pieceX + 8 * pieceY][0]
        direction = 1 if pieceColor == 'W' else -1

        if cellToCheck in [(pieceX - 1, pieceY + direction), (pieceX + 1, pieceY + direction)]:
            return True

        return False
    
    # Precondition (not verified): rook at x, y
    def getMovesForRook(self, x, y) -> list[tuple[int, int]]:
        pieceColor = self.board[x + 8 * y][0]
        moves = []

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in directions:
            for i in range(1, 8):
                nx, ny = x + i * dx, y + i * dy
                if 0 <= nx < 8 and 0 <= ny < 8:
                    if not self.board[nx + 8 * ny]:
                        moves.append((nx, ny))
                    elif self.board[nx + 8 * ny][0] != pieceColor:
                        moves.append((nx, ny))  # Capture
                        break
                    else:
                        break
                else:
                    break

        return moves
    
    # Precondition (not verified): rook at x, y
    def isCellAttackedByRook(self, pieceCell: tuple[int, int], cellToCheck: tuple[int, int]) -> bool:
        pieceX, pieceY = pieceCell

        # If a piece is not on the same row or column, it cannot attack the cell
        if pieceX != cellToCheck[0] and pieceY != cellToCheck[1]:
            return False

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in directions:
            for i in range(1, 8):
                nx, ny = pieceX + i * dx, pieceY + i * dy
                if 0 <= nx < 8 and 0 <= ny < 8:
                    if (nx, ny) == cellToCheck:
                        return True
                    if self.board[nx + 8 * ny]:
                        break
                else:
                    break

        return False
       
    # Precondition (not verified): knight at x, y
    def getMovesForKnight(self, x, y) -> list[tuple[int, int]]:
        pieceColor = self.board[x + 8 * y][0]
        moves = []
        knightMoves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

        for dx, dy in knightMoves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 8 and 0 <= ny < 8:
                if not self.board[nx + 8 * ny] or self.board[nx + 8 * ny][0] != pieceColor:
                    moves.append((nx, ny))

        return moves
    
    # Precondition (not verified): knight at x, y
    def isCellAttackedByKnight(self, pieceCell: tuple[int, int], cellToCheck: tuple[int, int]) -> bool:
        pieceX, pieceY = pieceCell

        if cellToCheck in [(pieceX + 2, pieceY + 1), (pieceX + 1, pieceY + 2), (pieceX - 1, pieceY + 2), (pieceX - 2, pieceY + 1), (pieceX - 2, pieceY - 1), (pieceX - 1, pieceY - 2), (pieceX + 1, pieceY - 2), (pieceX + 2, pieceY - 1)]: 
            return True

        return False
    
    # Precondition (not verified): bishop at x, y
    def getMovesForBishop(self, x, y) -> list[tuple[int, int]]:
        pieceColor = self.board[x + 8 * y][0]
        moves = []

        directions = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
        for dx, dy in directions:
            for i in range(1, 8):
                nx, ny = x + i * dx, y + i * dy
                if 0 <= nx < 8 and 0 <= ny < 8:
                    if not self.board[nx + 8 * ny]:
                        moves.append((nx, ny))
                    elif self.board[nx + 8 * ny][0] != pieceColor:
                        moves.append((nx, ny))  # Capture
                        break
                    else:
                        break
                else:
                    break

        return moves
    
    # Precondition (not verified): bishop at x, y
    def isCellAttackedByBishop(self, pieceCell: tuple[int, int], cellToCheck: tuple[int, int]) -> bool:
        pieceX, pieceY = pieceCell

        # If a piece is not on the same diagonal, it cannot attack the cell
        if abs(pieceX - cellToCheck[0]) != abs(pieceY - cellToCheck[1]):
            return False

        directions = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
        for dx, dy in directions:
            for i in range(1, 8):
                nx, ny = pieceX + i * dx, pieceY + i * dy
                if 0 <= nx < 8 and 0 <= ny < 8:
                    if (nx, ny) == cellToCheck:
                        return True
                    if self.board[nx + 8 * ny]:
                        break
                else:
                    break

        return False
        
    # Precondition (not verified): queen at x, y
    def getMovesForQueen(self, x, y) -> list[tuple[int, int]]:
        return self.getMovesForRook(x, y) + self.getMovesForBishop(x, y)
    
    # Precondition (not verified): queen at x, y
    def isCellAttackedByQueen(self, pieceCell: tuple[int, int], cellToCheck: tuple[int, int]) -> bool:
        return self.isCellAttackedByRook(pieceCell, cellToCheck) or self.isCellAttackedByBishop(pieceCell, cellToCheck)
    
    # Precondition (not verified): king at x, y
    def getMovesForKing(self, x, y) -> list[tuple[int, int]]:
        pieceColor = self.board[x + 8 * y][0]
        moves = self.getCellsAttackedByKing(x, y)

        # Castling
        if pieceColor == 'W':
            if (x, y) == (4, 0):
                if self.gameState.getCanCastle('W','K') and not self.board[5 + 8 * 0] and not self.board[6 + 8 * 0] and not self.areCellsUnderAttack([(4, 0), (5, 0), (6, 0)], 'B'):
                    moves.append((6, 0))
                if self.gameState.getCanCastle('W','Q') and not self.board[1 + 8 * 0] and not self.board[2 + 8 * 0] and not self.board[3 + 8 * 0] and not self.areCellsUnderAttack([(4, 0), (3, 0), (2, 0)], 'B'):
                    moves.append((2, 0))
        else:
            if (x, y) == (4, 7):
                if self.gameState.getCanCastle('B','K') and not self.board[5 + 8 * 7] and not self.board[6 + 8 * 7] and not self.areCellsUnderAttack([(4, 7), (5, 7), (6, 7)], 'W'):
                    moves.append((6, 7))
                if self.gameState.getCanCastle('B','Q') and not self.board[1 + 8 * 7] and not self.board[2 + 8 * 7] and not self.board[3 + 8 * 7] and not self.areCellsUnderAttack([(4, 7), (3, 7), (2, 7)], 'W'):
                    moves.append((2, 7))

        return moves
    
    # Precondition (not verified): king at x, y
    def getCellsAttackedByKing(self, x, y) -> list[tuple[int, int]]:
        pieceColor = self.board[x + 8 * y][0]
        moves = []

        directions = [(0, 1), (1, 1), (-1, 1), (0, -1), (1, -1), (-1, -1), (1, 0), (-1, 0)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 8 and 0 <= ny < 8:
                if not self.board[nx + 8 * ny] or self.board[nx + 8 * ny][0] != pieceColor:
                    moves.append((nx, ny))

        return moves
    
    # Precondition (not verified): king at x, y
    def isCellAttackedByKing(self, pieceCell: tuple[int, int], cellToCheck: tuple[int, int]) -> bool:
        if abs(pieceCell[0] - cellToCheck[0]) <= 1 and abs(pieceCell[1] - cellToCheck[1]) <= 1:
            return True
        
        return False
    
    # precondition (not verified): king at x, y; castling is possible
    def castle(self, kingX, kingY, side):
        pieceColor = self.board[kingX + 8 * kingY][0]
        if side == 'K':
            self.forceMove((kingX, kingY), (kingX + 2, kingY))
            self.forceMove((kingX + 3, kingY), (kingX + 1, kingY))
        elif side == 'Q':
            self.forceMove((kingX, kingY), (kingX - 2, kingY))
            self.forceMove((kingX - 4, kingY), (kingX - 1, kingY))
        
        self.gameState.setCannotCastle(pieceColor)
        self.gameState.setCastled(pieceColor)

    # Get a list of all valid moves for a player as a list of tuples (fromCell, toCell)
    def getValidMoves(self, playerColor) -> list[tuple[tuple[int, int], tuple[int, int]]]:
        moves = []
        for i in range(0, 64):
            piece = self.board[i]
            if piece and piece[0] == playerColor:
                x = i % 8
                y = i // 8
                pieceMoves = self.getMovesForPiece(x, y)
                for move in pieceMoves:
                    moves.append(((x, y), move))
        return moves
    
    def isCellUnderAttack(self, x, y, attackerColor):
        for i in range(0, 64):
            piece = self.board[i]
            if piece and piece[0] == attackerColor:
                pieceX = i % 8
                pieceY = i // 8
                if self.isCellAttackedByPiece((pieceX, pieceY), (x, y)):
                    return True
        return False
    
    # Returns True if any of the cells in the list are under attack by the attackerColor
    def areCellsUnderAttack(self, cells: list[tuple[int, int]], attackerColor):
        for cell in cells:
            if self.isCellUnderAttack(cell[0], cell[1], attackerColor):
                return True
            
        return False
    
    def isPlayerInCheck(self, playerColor):
        opponentColor = oppositeColor(playerColor)
        for i in range(0, 64):
            piece = self.board[i]
            pieceX = i % 8
            pieceY = i // 8
            if piece and piece[0] == playerColor and piece[1] == 'K':
                return self.isCellUnderAttack(pieceX, pieceY, opponentColor)
                
    def hasValidMoves(self, playerColor):
        for i in range(0, 64):
            piece = self.board[i]
            if piece and piece[0] == playerColor:
                pieceX = i % 8
                pieceY = i // 8
                if self.getMovesForPiece(pieceX, pieceY):
                    return True
        return False
    
    def promotePawns(self):
        # Autopromote pawns on the last rows to queens
        for i in range(0, 64):
            piece = self.board[i]
            pieceY = i // 8
            if piece and piece[1] == 'P' and (pieceY == 0 or pieceY == 7):
                self.board[i] = piece[0] + 'Q'
                
    # Moves a piece from fromCell to toCell without checking if the move is valid
    # Precondition (not verified): piece at x, y
    def forceMove(self, fromCell: tuple[int, int], toCell: tuple[int, int]):
        self.board[toCell[0] + 8 * toCell[1]] = self.board[fromCell[0] + 8 * fromCell[1]]
        self.board[fromCell[0] + 8 * fromCell[1]] = None
        self.promotePawns()
                
    ############################################################
    # Turn specific methods
    ############################################################

    # Attempts to make a move for the piece at fromCell to toCell. If the move is invalid, does nothing
    # and returns False. Changes the turn if the move is valid and returns True.
    # If validateMove is False, the move is made without checking if it is valid (faster performance).
    def makeMove(self, fromCell: tuple[int, int], toCell: tuple[int, int], validateMove: bool = True):
        if (self.gameState.isGameOngoing() == False):
            logging.warning('Board: makeMove: Game is not ongoing')
            return False

        piece = self.getPiece(fromCell[0], fromCell[1]) 

        if (not piece):
            logging.warning(f'Board: makeMove: No piece at {fromCell[0], fromCell[1]}')
            return False
        
        pieceColor = piece[0]
        
        if (not piece or piece[0] != self.getTurn()):
            logging.warning(f'Board: makeMove: Attempted to move opponent\'s piece {fromCell[0], fromCell[1]}. Turn: {self.getTurn()}. Piece: {piece}')
            return False
        
        if (validateMove):
            validMoves = self.getMovesForPiece(fromCell[0], fromCell[1])
            if toCell not in validMoves:
                logging.warning(f'Board: makeMove: Invalid move for a piece at {fromCell[0], fromCell[1]}')
                return False
        
        if piece[1] == 'K' and abs(fromCell[0] - toCell[0]) >= 2:
            # Castling
            self.castle(fromCell[0], fromCell[1], 'K' if toCell[0] > fromCell[0] else 'Q')
        else:
            # Update castling rights

            # King moves
            if piece[1] == 'K':
                self.gameState.setCannotCastle(self.getTurn())

            # Rook moves
            if piece[1] == 'R':
                if pieceColor == 'W':
                    if fromCell == (0, 0):
                        self.gameState.setCannotCastle(self.getTurn(), 'Q')
                    elif fromCell == (7, 0):
                        self.gameState.setCannotCastle(self.getTurn(), 'K')
                else:
                    if fromCell == (0, 7):
                        self.gameState.setCannotCastle(self.getTurn(), 'Q')
                    elif fromCell == (7, 7):
                        self.gameState.setCannotCastle(self.getTurn(), 'K')

            self.board[toCell[0] + 8 * toCell[1]] = self.board[fromCell[0] + 8 * fromCell[1]]
            self.board[fromCell[0] + 8 * fromCell[1]] = None
        
        if piece[1] == 'P':
            self.promotePawns()
        self.gameState.halfMoves.append((fromCell, toCell))
        self.gameState.nextTurn()
        self.updateGameState()

        return True
    
    def updateGameState(self):
        self.updateCheckCheckmateStalemateState()
        self.updateDrawState()
        self.updateMaterialScore()

    def updateCheckCheckmateStalemateState(self):
        isInCheck = self.isPlayerInCheck(self.getTurn())
        hasValidMoves = self.hasValidMoves(self.getTurn())

        self.gameState.setCheck(self.getTurn(), isInCheck)

        if isInCheck and not hasValidMoves:
            self.gameState.setCheckmate(self.getTurn())
            return

        if not isInCheck and not hasValidMoves:
            self.gameState.setDraw(DrawType.STALEMATE)

    def updateDrawState(self):
        if self.checkDrawByInsufficientMaterial():
            self.gameState.setDraw(DrawType.INSUFFICIENT_MATERIAL)
    
    def checkDrawByInsufficientMaterial(self):
        # Draw by insufficient material is if there is no way to end the game in checkmate:
        # - Only kings left
        # - King and single bishop
        # - King and single knight
        whitePieces = []
        blackPieces = []
        for y in range(0, 8):
            for x in range(0, 8):
                piece = self.board[x + 8 * y]
                if piece and piece[1] != 'K':
                    if piece[1] == 'P' or piece[1] == 'Q' or piece[1] == 'R':
                        return False
                    
                    if piece[0] == 'W':
                        whitePieces.append(piece)
                    else:
                        blackPieces.append(piece)

        return len(whitePieces) <= 1 and len(blackPieces) <= 1

    def isCurrentPlayerInCheck(self):
        return self.gameState.isCurrentPlayerInCheck()
    
    def isCurrentPlayerInCheckmate(self):
        return self.gameState.isCurrentPlayerInCheckmate()

    def isDraw(self):
        return  self.gameState.isDraw()
    
    # Precondition: checkmate and check states are updated
    def updateMaterialScore(self):
        if self.isCurrentPlayerInCheckmate():
            if self.getTurn() == 'B':
                self.gameState.materialScore = 1000
            else:
                self.gameState.materialScore = -1000
            return
        
        if self.isDraw():
            self.gameState.materialScore = 0
            return

        # Calculate the score based on the pieces left
        score = 0
        for i in range(0, 64):
            piece = self.board[i]
            pieceValue = PIECE_VALUES.get(piece)
            if pieceValue:
                score += (pieceValue if piece[0] == 'W' else -pieceValue)

        self.gameState.materialScore = score

    ############################################################
    # Utility methods
    ############################################################
    def printState(self):
        print('Board state:')
        print(f'Turn: {self.getTurn()}')
        print(f'Can Castle: {self.gameState.canCastle}')

    def getBoardAsString(self):
        str = ''
        for y in range(0, 8):
            for x in range(0, 8):
                pc = self.board[x + 8 * (7 - y)]
                str += pc if pc else '[]'
            str += '\n'
        return str
    
    def setBoardFromString(self, boardStr):
        rows = boardStr.split('\n')
        for y in range(0, 8):
            for x in range(0, 8):
                self.board[x + 8 * (7 - y)] = rows[y][x * 2:x * 2 + 2]
                if self.board[x + 8 * (7 - y)] == '[]':
                    self.board[x + 8 * (7 - y)] = None

        if self.board[4 +  8 * 0] != 'WK':
            self.gameState.setCannotCastle('W')

        if self.board[4 + 8 * 7] != 'BK':
            self.gameState.setCannotCastle('B')
     
    def __str__(self):
        return self.getBoardAsString()
