from Board import Board
from BotBase import BotBase

b = Board()
b.clear()

str = '''[]BQ[][][][]BNBK
         [][][][][][]BPBP
         [][][][][][][][]
         [][][][][]BR[][]
         [][][][][][][][]
         [][][][][][][][]
         BN[][][][][][][]
         WKWQ[][][][][][]'''.replace(' ','')

b.setBoardFromString(str)
moves = b.getValidMoves('W')

bot = BotBase()
significantMoves = bot.selectSignificantMoves(b, moves)

print(significantMoves)