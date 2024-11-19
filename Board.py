
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

    def getPiece(self, col, row):
        return self.board[col][row]
    
    def getTurn(self):
        return self.turn
    
    def movePiece(self, fromCell, toCell):
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
