from Board import Board
from Utils import toCell, toCells

def testDefaultState():
    b = Board()
    assert b.getTurn() == 'W'
    assert b.getPiece(0,0) == 'WR'
    assert b.getPiece(1, 0) == 'WN'
    assert b.getPiece(2, 0) == 'WB'
    assert b.getPiece(3, 0) == 'WQ'
    assert b.getPiece(4, 0) == 'WK'
    assert b.getPiece(5, 0) == 'WB'
    assert b.getPiece(6, 0) == 'WN'
    assert b.getPiece(7, 0) == 'WR'
    assert b.getPiece(0, 7) == 'BR'
    assert b.getPiece(1, 7) == 'BN'
    assert b.getPiece(2, 7) == 'BB'
    assert b.getPiece(3, 7) == 'BQ'
    assert b.getPiece(4, 7) == 'BK'
    assert b.getPiece(5, 7) == 'BB'
    assert b.getPiece(6, 7) == 'BN'
    assert b.getPiece(7, 7) == 'BR'

    for i in range(8):
        assert b.getPiece(i, 1) == 'WP'
        assert b.getPiece(i, 6) == 'BP'

def testGetPiece():
    b = Board()
    assert b.getPiece(*toCell('a1')) == 'WR'
    assert b.getPiece(*toCell('h8')) == 'BR'

def testGetMovesForPawnDefault():
    b = Board()
    assert set(b.getMovesForPiece(0, 1)) == set([(0, 2), (0, 3)])
    assert set(b.getMovesForPiece(2, 6)) == set([(2, 5), (2, 4)])
    assert set(b.getMovesForPiece(4, 1)) == set([(4, 2), (4, 3)])
    assert set(b.getMovesForPiece(*toCell('f7'))) == set([toCell('f6'), toCell('f5')])

def testGetMovesForPawnAfterMove():
    b = Board()
    assert b.makeMove(toCell('e2'), toCell('e4'))
    assert b.getMovesForPiece(*toCell('e4')) == [toCell('e5')]

    assert b.makeMove(toCell('d7'), toCell('d5'))
    assert set(b.getMovesForPiece(*toCell('d5'))) == set(toCells(['d4','e4']))

    assert b.makeMove(toCell('b2'), toCell('b3'))
    assert b.getMovesForPiece(*toCell('b3')) == [toCell('b4')]

    assert b.makeMove(toCell('c7'), toCell('c5'))
    assert b.getMovesForPiece(*toCell('c5')) == [toCell('c4')]

    assert b.makeMove(toCell('d2'), toCell('d3'))
    assert b.makeMove(toCell('c5'), toCell('c4'))
    assert set(b.getMovesForPiece(*toCell('c4'))) == set(toCells(['c3', 'b3', 'd3']))

def testGetMovesForKnightDefault():
    b = Board()
    assert set(b.getMovesForPiece(1, 0)) == set([(0, 2), (2, 2)])
    assert set(b.getMovesForPiece(6, 0)) == set([(5, 2), (7, 2)])
    assert set(b.getMovesForPiece(1, 7)) == set([(0, 5), (2, 5)])
    assert set(b.getMovesForPiece(6, 7)) == set([(5, 5), (7, 5)])

def testGetMovesForKnightAfterMove():
    b = Board()
    assert b.makeMove(toCell('g1'), toCell('f3'))
    assert set(b.getMovesForPiece(*toCell('f3'))) == set(toCells(['d4', 'e5', 'g5', 'h4', 'g1']))

    assert b.makeMove(toCell('b8'), toCell('c6'))
    assert set(b.getMovesForPiece(*toCell('c6'))) == set(toCells(['b8', 'a5', 'b4', 'd4', 'e5']))

    assert b.makeMove(toCell('f3'), toCell('d4'))
    assert set(b.getMovesForPiece(*toCell('d4'))) == set(toCells(['f3', 'b3', 'b5', 'c6', 'e6', 'f5']))

    assert b.makeMove(toCell('e7'), toCell('e5'))
    assert set(b.getMovesForPiece(*toCell('c6'))) == set(toCells(['b8', 'a5', 'b4', 'd4', 'e7']))

def testGetMovesForBishopDefault():
    b = Board()
    assert b.getMovesForPiece(*toCell('c1')) == []
    assert b.getMovesForPiece(*toCell('f1')) == []
    assert b.getMovesForPiece(*toCell('c8')) == []
    assert b.getMovesForPiece(*toCell('f8')) == []

def testGetMovesForBishopAfterMove():
    b = Board()
    assert b.makeMove(toCell('g2'), toCell('g3'))
    assert set(b.getMovesForPiece(*toCell('f1'))) == set(toCells(['g2', 'h3']))

    assert b.makeMove(toCell('b7'), toCell('b6'))
    assert set(b.getMovesForPiece(*toCell('c8'))) == set(toCells(['b7', 'a6']))

    assert b.makeMove(toCell('f1'), toCell('g2'))
    assert set(b.getMovesForPiece(*toCell('g2'))) == set(toCells(['f3', 'e4', 'd5', 'c6', 'b7', 'a8', 'f1', 'h3']))

    assert b.makeMove(toCell('c8'), toCell('b7'))
    assert set(b.getMovesForPiece(*toCell('b7'))) == set(toCells(['c6', 'd5', 'e4', 'f3', 'g2', 'a6', 'c8']))

def testGetMovesForRookDefault():
    b = Board()
    assert b.getMovesForPiece(*toCell('a1')) == []
    assert b.getMovesForPiece(*toCell('h1')) == []
    assert b.getMovesForPiece(*toCell('a8')) == []
    assert b.getMovesForPiece(*toCell('h8')) == []

def testGetMovesForRookAfterMove():
    b = Board()
    assert b.makeMove(toCell('a2'), toCell('a4'))
    assert set(b.getMovesForPiece(*toCell('a1'))) == set(toCells(['a2', 'a3']))

    assert b.makeMove(toCell('h7'), toCell('h5'))
    assert set(b.getMovesForPiece(*toCell('h8'))) == set(toCells(['h7', 'h6']))

    assert b.makeMove(toCell('a1'), toCell('a3'))
    assert set(b.getMovesForPiece(*toCell('a3'))) == set(toCells(['a1', 'a2', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3']))

    assert b.makeMove(toCell('h8'), toCell('h6'))
    assert set(b.getMovesForPiece(*toCell('h6'))) == set(toCells(['h8', 'h7', 'g6', 'f6', 'e6', 'd6', 'c6', 'b6', 'a6']))

def testGetMovesForQueenDefault():
    b = Board()
    assert b.getMovesForPiece(*toCell('d1')) == []
    assert b.getMovesForPiece(*toCell('d8')) == []

def testGetMovesForQueenAfterMove():
    b = Board()
    assert b.makeMove(toCell('e2'), toCell('e4'))
    assert set(b.getMovesForPiece(*toCell('d1'))) == set(toCells(['e2', 'f3', 'g4', 'h5']))

    assert b.makeMove(toCell('c7'), toCell('c6'))
    assert set(b.getMovesForPiece(*toCell('d8'))) == set(toCells(['c7', 'b6', 'a5']))

    assert b.makeMove(toCell('d1'), toCell('g4'))
    assert set(b.getMovesForPiece(*toCell('g4'))) == set(toCells(['d1', 'e2', 'f3', 'h5', 'h3', 'f5', 'e6', 'd7', 'g3', 'g5', 'g6', 'g7', 'h4', 'f4']))

def testGetMovesForKingDefault():
    b = Board()
    assert b.getMovesForPiece(*toCell('e1')) == []
    assert b.getMovesForPiece(*toCell('e8')) == []

def testGetMovesForKingAfterMove():
    b = Board()
    assert b.makeMove(toCell('e2'), toCell('e4'))
    assert set(b.getMovesForPiece(*toCell('e1'))) == set(toCells(['e2']))

    assert b.makeMove(toCell('e7'), toCell('e6'))
    assert set(b.getMovesForPiece(*toCell('e8'))) == set(toCells(['e7']))

    assert b.makeMove(toCell('e1'), toCell('e2'))
    assert set(b.getMovesForPiece(*toCell('e2'))) == set(toCells(['e1', 'e3', 'd3', 'f3']))

    assert b.makeMove(toCell('e8'), toCell('e7'))
    assert set(b.getMovesForPiece(*toCell('e7'))) == set(toCells(['e8', 'd6', 'f6']))

def testGetMovesForKingCastleShort():
    b = Board()
    assert b.makeMove(toCell('g2'), toCell('g3'))
    assert b.makeMove(toCell('g7'), toCell('g6'))
    assert b.makeMove(toCell('f1'), toCell('g2'))
    assert b.makeMove(toCell('f8'), toCell('g7'))
    assert b.makeMove(toCell('g1'), toCell('f3'))
    assert b.makeMove(toCell('g8'), toCell('f6'))

    assert set(b.getMovesForPiece(*toCell('e1'))) == set(toCells(['f1', 'g1']))
    assert set(b.getMovesForPiece(*toCell('e8'))) == set(toCells(['f8', 'g8']))

    b.makeMove(toCell('e1'), toCell('g1'))
    assert b.gameState.getCanCastle('W', 'K') == False
    assert b.gameState.getCanCastle('W', 'Q') == False
    assert set(b.getMovesForPiece(*toCell('g1'))) == set(toCells(['h1']))

    b.makeMove(toCell('e8'), toCell('g8'))
    assert b.gameState.getCanCastle('B', 'K') == False
    assert b.gameState.getCanCastle('B', 'Q') == False
    assert set(b.getMovesForPiece(*toCell('g8'))) == set(toCells(['h8']))

def testGetMovesForKingCastleLong():
    b = Board()
    assert b.makeMove(toCell('b2'), toCell('b3'))
    assert b.makeMove(toCell('b7'), toCell('b6'))
    assert b.makeMove(toCell('c1'), toCell('b2'))
    assert b.makeMove(toCell('c8'), toCell('b7'))
    assert b.makeMove(toCell('b1'), toCell('c3'))
    assert b.makeMove(toCell('b8'), toCell('c6'))
    assert b.makeMove(toCell('e2'), toCell('e3'))
    assert b.makeMove(toCell('e7'), toCell('e6'))
    assert b.makeMove(toCell('d1'), toCell('e2'))
    assert b.makeMove(toCell('d8'), toCell('e7'))

    assert set(b.getMovesForPiece(*toCell('e1'))) == set(toCells(['d1', 'c1']))
    assert set(b.getMovesForPiece(*toCell('e8'))) == set(toCells(['d8', 'c8']))
    
    assert b.makeMove(toCell('e1'), toCell('c1'))
    assert b.gameState.getCanCastle('W', 'K') == False
    assert b.gameState.getCanCastle('W', 'Q') == False
    assert set(b.getMovesForPiece(*toCell('c1'))) == set(toCells(['b1']))

    b.makeMove(toCell('e8'), toCell('c8'))
    assert b.gameState.getCanCastle('B', 'K') == False
    assert b.gameState.getCanCastle('B', 'Q') == False
    assert set(b.getMovesForPiece(*toCell('c8'))) == set(toCells(['b8']))

def testFoolsMate():
    b = Board()
    assert b.makeMove(toCell('f2'), toCell('f3'))
    assert b.makeMove(toCell('e7'), toCell('e5'))
    assert b.makeMove(toCell('g2'), toCell('g4'))
    assert b.makeMove(toCell('d8'), toCell('h4'))
    assert b.isCurrentPlayerInCheckmate() == True

def testLegalTrap():
    b = Board()
    assert b.makeMove(toCell('e2'), toCell('e4'))
    assert b.makeMove(toCell('e7'), toCell('e5'))
    assert b.makeMove(toCell('f1'), toCell('c4'))
    assert b.makeMove(toCell('d7'), toCell('d6'))
    assert b.makeMove(toCell('g1'), toCell('f3'))
    assert b.makeMove(toCell('b8'), toCell('c6'))
    assert b.makeMove(toCell('b1'), toCell('c3'))
    assert b.makeMove(toCell('c8'), toCell('g4'))
    assert b.makeMove(toCell('f3'), toCell('e5'))
    assert b.makeMove(toCell('g4'), toCell('d1'))
    assert b.makeMove(toCell('c4'), toCell('f7'))
    assert b.isCurrentPlayerInCheck() == True
    assert set(b.getMovesForPiece(*toCell('e8'))) == set(toCells(['e7']))
    assert b.makeMove(toCell('e8'), toCell('e7'))
    assert b.makeMove(toCell('c3'), toCell('d5'))
    assert b.isCurrentPlayerInCheckmate() == True

def testScoreUpdates():
    b = Board()
    assert b.gameState.materialScore == 0
    assert b.makeMove(toCell('e2'), toCell('e4'))
    assert b.gameState.materialScore == 0
    assert b.makeMove(toCell('d7'), toCell('d5'))
    assert b.gameState.materialScore == 0
    assert b.makeMove(toCell('e4'), toCell('d5'))
    assert b.gameState.materialScore == 1
    assert b.makeMove(toCell('b8'), toCell('c6'))
    assert b.gameState.materialScore == 1
    assert b.makeMove(toCell('d5'), toCell('c6'))
    assert b.gameState.materialScore == 4
    assert b.makeMove(toCell('e7'), toCell('e5'))
    assert b.gameState.materialScore == 4
    assert b.makeMove(toCell('c6'), toCell('b7'))
    assert b.gameState.materialScore == 5
    assert b.makeMove(toCell('e5'), toCell('e4'))
    assert b.gameState.materialScore == 5
    assert b.makeMove(toCell('b7'), toCell('a8'))
    assert b.gameState.materialScore == 18 # 5 + 9 for Q + 5 for taken rook - 1 for promoted pawn
    assert b.makeMove(toCell('d8'), toCell('d5'))
    assert b.gameState.materialScore == 18 
    assert b.makeMove(toCell('g1'), toCell('f3'))
    assert b.gameState.materialScore == 18 
    assert b.makeMove(toCell('e4'), toCell('f3'))
    assert b.gameState.materialScore == 15
    assert b.makeMove(toCell('b1'), toCell('c3'))
    assert b.gameState.materialScore == 15
    assert b.makeMove(toCell('d5'), toCell('a8'))
    assert b.gameState.materialScore == 6 # 15 - 9 for taken queen
    assert b.makeMove(toCell('d1'), toCell('f3'))
    assert b.gameState.materialScore == 7
    assert b.makeMove(toCell('a8'), toCell('d5'))
    assert b.gameState.materialScore == 7
    assert b.makeMove(toCell('f1'), toCell('c4'))
    assert b.gameState.materialScore == 7
    assert b.makeMove(toCell('d5'), toCell('d8'))
    assert b.gameState.materialScore == 7
    assert b.makeMove(toCell('f3'), toCell('f7'))
    assert b.gameState.materialScore == 1000 

def testSetBoardFromString():
    str = '''WQ[][][][][][]BQ
             WK[][][][][][][]
             [][][][][][]WN[]
             [][][][]BB[][][]
             [][][][][][][][]
             [][][][][][][][]
             WB[][][][]BK[][]
             []BR[][][][][]BR'''.replace(' ','')
    
    b = Board()
    b.setBoardFromString(str)
    assert b.getBoardAsString().strip() == str
    assert b.getPiece(*toCell('f2')) == 'BK'