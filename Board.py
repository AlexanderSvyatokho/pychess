
# Stores chess board's state
class Board:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.setToDefault()

    def setToDefault(self):
        pieces = ["R", "N", "B", "Q", "K", "B", "N", "R"]
        for i in range(8):
            self.board[i][0] = "W" + pieces[i]
            self.board[i][1] = "WP"
            self.board[i][6] = "BP"
            self.board[i][7] = "B" + pieces[i]

    def getPiece(self, row, col):
        return self.board[row][col]

    def __str__(self):
        str = ''
        for y in range(0, 8):
            for x in range(0, 8):
                pc = self.board[x][7 - y]
                str += pc if pc else '[]'
            str += '\n'
        return str
