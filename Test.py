import logging 
import cProfile

from Board import Board
from BotBase import BotBase
from BotDepth1 import BotDepth1
from BotDepthN import BotDepthN

from TestUtils import * 

logging.basicConfig(level=logging.DEBUG)

def func():
    b = Board()
    b.clear()

    str = '''BRBNBBBQBKBB[]BR
             BP[][][]BPBPBPBP
             []BP[][][]BN[][]
             [][]BPBP[][][][]
             [][]WPWP[][][][]
             []WP[][][]WN[][]
             WP[][][]WPWPWPWP
             WRWNWBWQWKWB[]WR'''.replace(' ','')

    b.setBoardFromString(str)

    bot = BotDepthN(2)
    bot.makeMove(b)

    print(b.getBoardAsString())

for i in range(5):
   func()
    

# 4.6

# 2.7

# 2.55

# cProfile.run('func()')