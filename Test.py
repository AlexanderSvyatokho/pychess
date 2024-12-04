from Board import Board
from BotBase import BotBase
from BotDepth1 import BotDepth1
from BotDepthN import BotDepthN

from TestUtils import * 

b = Board()
b.clear()

str = '''[][][][][][][][]
         [][][][][][][][]
         [][][][][][][][]
         [][][][][][][][]
         [][][]BK[][][][]
         [][][][][][][][]
         [][][][][][]BQ[]
         [][][]WK[][][][]'''.replace(' ','')

b.setBoardFromString(str)
b.gameState.turn = 'B'

print(b.getBoardAsString())

bot = BotDepthN(2)
bot.makeMove(b)

print(b.getBoardAsString())

b.getValidMoves('W')

print(f'Is in check: {b.gameState.isCurrentPlayerInCheck()}')

b.makeMove(toCell('D1'), toCell('E1'))
bot.makeMove(b) 

print(b.getBoardAsString())
