from Utils import *
from Board import Board

def challengePickBestCapture(bot):
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
    bot.makeMove(b)

    assert b.getPiece(6, 5) == None
    assert b.getPiece(7, 7) == 'WN'

def challengeMateInOneAvoidDraw(bot):
    for _ in range(5):
        b = Board()
        b.clear()

        str = '''BK[][][][][][]BR
                 BRBRBR[]BRBRBRBR
                 [][][][][][][][]
                 [][][][][][][][]
                 [][][][][][][][]
                 [][][][][][][][]
                 BR[][][][][][][]
                 [][][]WK[][][][]'''.replace(' ','')

        b.setBoardFromString(str)
        b.gameState.nextTurn()
        bot.makeMove(b)
        
        assert b.gameState.isCurrentPlayerInCheckmate() == True

def challengeMateInOneWithQueen(bot):
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

    bot.makeMove(b)

    assert b.gameState.isCurrentPlayerInCheckmate() == True
    assert b.getPiece(*toCell('F2')) == 'WQ'

def challengeMateInOneWithBishop(bot):
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

    bot.makeMove(b)

    assert b.gameState.isCurrentPlayerInCheckmate() == True
    assert b.getPiece(*toCell('G2')) == 'BB'

def challengeMateInOneWithPawn(bot):
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
    bot.makeMove(b)

    assert b.gameState.isCurrentPlayerInCheckmate() == True
    assert b.getPiece(*toCell('C7')) == 'WP'

def challengeMateInOneWithKnight(bot):
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
    bot.makeMove(b)

    assert b.gameState.isCurrentPlayerInCheckmate() == True
    assert b.getPiece(*toCell('B3')) == 'WN'

def challengeMateInOneWithRook(bot):
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
    bot.makeMove(b)

    assert b.gameState.isCurrentPlayerInCheckmate() == True
    assert b.getPiece(*toCell('D8')) == 'WR'

def challengeMateInOneWithPromotion(bot):
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
    bot.makeMove(b)

    assert b.gameState.isCurrentPlayerInCheckmate() == True
    assert b.getPiece(*toCell('G8')) == 'WQ'
