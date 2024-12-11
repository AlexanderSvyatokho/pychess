from Utils import *
from Board import Board

    # str = '''[][][][][][][][]
    #          [][][][][][][][]
    #          [][][][][][][][]
    #          [][][][][][][][]
    #          [][][][][][][][]
    #          [][][][][][][][]
    #          [][][][][][][][]
    #          [][][][][][][][]'''.replace(' ','')

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

def challengeMateInTwoWithRook(bot):
    b = Board()
    b.clear()

    str = '''[][][][][]BK[][]
             [][][][][]BP[]BP
             [][][][][]WP[][]
             [][][]WK[][][][]
             [][][][][][][][]
             [][][][][][][][]
             BP[][][]WR[][][]
             []BR[][][][]WR[]'''.replace(' ','')

    b.setBoardFromString(str)
    bot.makeMove(b) # Expected: WR for G1 moves to G8 with check

    assert b.gameState.isCurrentPlayerInCheck() == True
    assert b.getPiece(*toCell('G8')) == 'WR'

    b.makeMove(toCell('F8'), toCell('G8')) # King captures the rook, the only valid move
    bot.makeMove(b) # Expected: WR for E2 moves to E8 with checkmate

    assert b.gameState.isCurrentPlayerInCheckmate() == True
    assert b.getPiece(*toCell('E8')) == 'WR'

def challengeMateInTwoWithRookAndKing(bot):
    b = Board()
    b.clear()

    str = '''[][][][][][][][]
             [][][][][][][]WK
             [][][][][]BKBR[]
             [][][][][][][][]
             [][][][][][][][]
             [][][][][][][][]
             [][][][][][][][]
             [][][][][][][][]'''.replace(' ','')

    b.setBoardFromString(str)
    b.gameState.turn = 'B'

    bot.makeMove(b) # Expected: BK F6 to F7

    assert b.gameState.isCurrentPlayerInCheck() == False
    assert b.getPiece(*toCell('F7')) == 'BK'

    assert b.getValidMoves('W') == [(toCell('H7'), toCell('H8'))]
    b.makeMove(toCell('H7'), toCell('H8'))

    bot.makeMove(b) # Expected: BR G6 to H6 with checkmate
    assert b.gameState.isCurrentPlayerInCheckmate() == True
    assert b.getPiece(*toCell('H6')) == 'BR'

def challengeMateInTwoWithBishopAndPawn(bot):
    b = Board()
    b.clear()

    str = '''[][][][][][][][]
             [][][][][]WK[]BK
             [][][][][][][][]
             [][][][][][]WP[]
             [][][][][]WB[][]
             [][][][][][][][]
             [][][][][][][][]
             [][][][][][][][]'''.replace(' ','')

    b.setBoardFromString(str)
    b.gameState.turn = 'W'

    bot.makeMove(b) # Expected: WP G5 to G6

    assert b.gameState.isCurrentPlayerInCheck() == True
    assert b.getPiece(*toCell('G6')) == 'WP'

    assert b.getValidMoves('B') == [(toCell('H7'), toCell('H8'))]
    b.makeMove(toCell('H7'), toCell('H8'))

    bot.makeMove(b) # Expected: WB F4 to E5
    assert b.gameState.isCurrentPlayerInCheckmate() == True
    assert b.getPiece(*toCell('E5')) == 'WB'

def challengeMateInTwoWithKnightAndKing(bot):
    b = Board()
    b.clear()

    str = '''[][][][][][][][]
             [][][][][][][][]
             [][][][][][][][]
             [][][][][][][][]
             [][][][][][][][]
             BP[][][][][][][]
             [][]WK[]WN[][][]
             BK[][][][][][][]'''.replace(' ','')

    b.setBoardFromString(str)
    b.gameState.turn = 'W'

    bot.makeMove(b) # Expected: WN E2 to C1

    assert b.gameState.isCurrentPlayerInCheck() == False
    assert b.getPiece(*toCell('C1')) == 'WN'

    assert b.getValidMoves('B') == [(toCell('A3'), toCell('A2'))]
    b.makeMove(toCell('A3'), toCell('A2'))

    bot.makeMove(b) # Expected: WN C1 to B3 with checkmate
    assert b.gameState.isCurrentPlayerInCheckmate() == True
    assert b.getPiece(*toCell('B3')) == 'WN'

def challengeMateInTwoWithQueenAndKing(bot):
    b = Board()
    b.clear()

    str = '''[][][][][][][][]
             [][][][][][][][]
             [][][][][][][][]
             [][][]BP[][][][]
             [][][]BK[][]BP[]
             [][][][][][][][]
             [][][][][][]BQ[]
             [][][]WK[][][][]'''.replace(' ','')

    b.setBoardFromString(str)
    b.gameState.turn = 'B'

    bot.makeMove(b) # Expected: BK D4 to D3

    assert b.gameState.isCurrentPlayerInCheck() == False
    assert b.getPiece(*toCell('D3')) == 'BK'

    assert b.getValidMoves('W') == [(toCell('D1'), toCell('E1')), (toCell('D1'), toCell('C1'))]
    b.makeMove(toCell('D1'), toCell('E1'))
    bot.makeMove(b) 

    assert b.gameState.isCurrentPlayerInCheckmate() == True
    assert b.getPiece(*toCell('E2')) == 'BQ' or b.getPiece(*toCell('G1')) == 'BQ'

def castlingPriority(bot):
    b = Board()
    b.clear()

    # Set up the board with pieces
    str = '''[][][][]BK[][]BR
             [][][][][]BPBPBP
             [][][][][][][][]
             [][][][][][][][]
             [][][][][][][][]
             [][][][][][][][]
             [][][][][][][][]
             [][][]WK[][]WR[]'''.replace(' ','')

    b.setBoardFromString(str)
    b.gameState.turn = 'B'

    assert b.gameState.getCanCastle('W', 'KQ') == False
    assert b.gameState.getCastled('W') == False
    assert b.gameState.getCanCastle('B', 'KQ') == True
    assert b.gameState.getCastled('B') == False

    bot.makeMove(b) # Expected: 0-0

    assert b.gameState.getCastled('B') == True
    assert b.getPiece(*toCell('G8')) == 'BK'
