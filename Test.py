from Board import Board
from BotBase import BotBase
from BotDepth1 import BotDepth1
from BotDepthN import BotDepthN

b = Board()
b.clear()

str = '''[][][][][][][][]
        []WK[][][][][][]
        [][][][][][][][]
        [][][][][][][][]
        [][][][]WN[][][]
        [][][][][][]WQ[]
        [][][][][][][][]
        [][][][][]BK[][]'''.replace(' ','')

b.setBoardFromString(str)

print(b.getBoardAsString())

bot = BotDepthN(1)
bot.makeMove(b)

print(b.getBoardAsString())

print(b.gameState.isCurrentPlayerInCheckmate())
