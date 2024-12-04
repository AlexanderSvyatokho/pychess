from Board import Board
from BotDepth1 import BotDepth1
from Utils import *

def testPickBestCapture():
    b = Board()
    b.clear()

    str = '''WQ[][][][][][]BQ
             WK[][][][][][][]
             [][][][][][]WN[]
             [][][][]BB[][][]
             [][][][][][][][]
             [][][][][][][][]
             WB[][][][]BK[][]
             []BR[][][][][]BR'''.replace(' ','')

    b.setBoardFromString(str)

    bot = BotDepth1()
    bot.makeMove(b)

    assert b.getPiece(6, 5) == None
    assert b.getPiece(7, 7) == 'WN'

def testMateInOneAvoidDraw():
    for _ in range(5):
        b = Board()
        b.clear()

        b.board[0][7] = 'BK'
        b.board[3][1] = 'WK'
        b.board[0][6] = 'BR'
        b.board[1][6] = 'BR'
        b.board[2][6] = 'BR'
        b.board[4][6] = 'BR'
        b.board[5][6] = 'BR'
        b.board[6][6] = 'BR'
        b.board[7][6] = 'BR'
        b.board[7][7] = 'BR'
        b.board[0][1] = 'BR'

        assert b.makeMove((3, 1), (3, 0))
        bot = BotDepth1()
        bot.makeMove(b)
        
        assert b.gameState.isCurrentPlayerInCheckmate() == True

def testMateInOneWithQueen():
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

    bot = BotDepth1()
    bot.makeMove(b)

    assert b.gameState.isCurrentPlayerInCheckmate() == True
    assert b.getPiece(*toCell('F2')) == 'WQ'

def testMateInOneWithBishop():
    b = Board()
    b.clear()

    str = '''[][][][][][][][]
             [][][][][][][][]
             [][][][][][][][]
             [][][][][][][][]
             [][][][][][][][]
             [][][][][][][]BB
             [][][][][]BK[]WP
             WQ[][][][][][]WK'''.replace(' ','')

    b.setBoardFromString(str)
    b.gameState.nextTurn()

    bot = BotDepth1()
    bot.makeMove(b)

    assert b.gameState.isCurrentPlayerInCheckmate() == True
    assert b.getPiece(*toCell('G2')) == 'BB'

def testMateInOneWithPawn():
    b = Board()
    b.clear()

    str = '''BRBK[][][][][][]
             []BP[][][][][][]
             []WPWP[][][][][]
             [][][][][][][][]
             [][][][][][]WBWK
             [][][][][][][][]
             [][][][][][][][]
             [][][][][][][][]'''.replace(' ','')

    b.setBoardFromString(str)

    bot = BotDepth1()
    bot.makeMove(b)

    assert b.gameState.isCurrentPlayerInCheckmate() == True
    assert b.getPiece(*toCell('C7')) == 'WP'

def testMateInOneWithKnight():
    b = Board()
    b.clear()

    str = '''[][][][][][][][]
             [][][][][][][][]
             [][][][][][][][]
             [][]WN[][][][][]
             [][][][][][][][]
             [][][][][][][][]
             BP[]WK[][][][][]
             BK[][][][][][][]'''.replace(' ','')

    b.setBoardFromString(str)

    bot = BotDepth1()
    bot.makeMove(b)

    assert b.gameState.isCurrentPlayerInCheckmate() == True
    assert b.getPiece(*toCell('B3')) == 'WN'

def testMateInOneWithRook():
    b = Board()
    b.clear()

    str = '''[][][][][][]BK[]
             [][][][][]BPBPBP
             [][][][][][][][]
             [][][][][][][][]
             [][][][][][][][]
             [][][][][][][]BQ
             [][]WK[][][][][]
             [][][]WR[][][][]'''.replace(' ','')

    b.setBoardFromString(str)

    bot = BotDepth1()
    bot.makeMove(b)

    assert b.gameState.isCurrentPlayerInCheckmate() == True
    assert b.getPiece(*toCell('D8')) == 'WR'

def testMateInOneWithPromotion():
    b = Board()
    b.clear()

    str = '''[][][][][][][][]
             [][][][][][]WPBK
             [][][][][][][][]
             [][][]WB[][][]WK
             [][][][][][][][]
             [][][][][][][][]
             [][]BR[][][][][]
             [][][]BR[][][][]'''.replace(' ','')

    b.setBoardFromString(str)

    bot = BotDepth1()
    bot.makeMove(b)

    assert b.gameState.isCurrentPlayerInCheckmate() == True
    assert b.getPiece(*toCell('G8')) == 'WQ'