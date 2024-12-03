from Board import Board
from BotDepthN import BotDepthN

# def testMateInOneAvoidDraw():

#     for _ in range(5):
#         b = Board()
#         b.clear()

#         b.board[0][7] = 'BK'
#         b.board[3][1] = 'WK'
#         b.board[0][6] = 'BR'
#         b.board[1][6] = 'BR'
#         b.board[2][6] = 'BR'
#         b.board[4][6] = 'BR'
#         b.board[5][6] = 'BR'
#         b.board[6][6] = 'BR'
#         b.board[7][6] = 'BR'
#         b.board[7][7] = 'BR'
#         b.board[0][1] = 'BR'

#         assert b.makeMove((3, 1), (3, 0))
#         bot = BotDepthN(1)
#         bot.makeMove(b)
        
#         assert b.gameState.isCurrentPlayerInCheckmate() == True

# def testPickBestCapture():

#     b = Board()
#     b.clear()

#     str = '''WQ[][][][][][]BQ
#              WK[][][][][][][]
#              [][][][][][]WN[]
#              [][][][]BB[][][]
#              [][][][][][][][]
#              [][][][][][][][]
#              WB[][][][]BK[][]
#              []BR[][][][][]BR'''.replace(' ','')

#     b.setBoardFromString(str)

#     bot = BotDepthN(1)
#     bot.makeMove(b)

#     assert b.getPiece(6, 5) == None
#     assert b.getPiece(7, 7) == 'WN'