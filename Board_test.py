from Board import Board
from Utils import toCell, toCells

def testDefaultState():
    b = Board()
    assert b.getTurn() == 'W'
    assert b.board[0][0] == 'WR'
    assert b.board[1][0] == 'WN'
    assert b.board[2][0] == 'WB'
    assert b.board[3][0] == 'WQ'
    assert b.board[4][0] == 'WK'
    assert b.board[5][0] == 'WB'
    assert b.board[6][0] == 'WN'
    assert b.board[7][0] == 'WR'
    assert b.board[0][7] == 'BR'
    assert b.board[1][7] == 'BN'
    assert b.board[2][7] == 'BB'
    assert b.board[3][7] == 'BQ'
    assert b.board[4][7] == 'BK'
    assert b.board[5][7] == 'BB'
    assert b.board[6][7] == 'BN'
    assert b.board[7][7] == 'BR'

    for i in range(8):
        assert b.board[i][1] == 'WP'
        assert b.board[i][6] == 'BP'

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
    b.makeMove(toCell('e2'), toCell('e4'))
    assert b.getMovesForPiece(*toCell('e4')) == [toCell('e5')]

    b.makeMove(toCell('d7'), toCell('d5'))
    assert set(b.getMovesForPiece(*toCell('d5'))) == set(toCells(['d4','e4']))

    b.makeMove(toCell('b2'), toCell('b3'))
    assert b.getMovesForPiece(*toCell('b3')) == [toCell('b4')]

    b.makeMove(toCell('c7'), toCell('c5'))
    assert b.getMovesForPiece(*toCell('c5')) == [toCell('c4')]

    b.makeMove(toCell('d2'), toCell('d3'))
    b.makeMove(toCell('c5'), toCell('c4'))
    assert set(b.getMovesForPiece(*toCell('c4'))) == set(toCells(['c3', 'b3', 'd3']))

def testGetMovesForKnightDefault():
    b = Board()
    assert set(b.getMovesForPiece(1, 0)) == set([(0, 2), (2, 2)])
    assert set(b.getMovesForPiece(6, 0)) == set([(5, 2), (7, 2)])
    assert set(b.getMovesForPiece(1, 7)) == set([(0, 5), (2, 5)])
    assert set(b.getMovesForPiece(6, 7)) == set([(5, 5), (7, 5)])

def testGetMovesForKnightAfterMove():
    b = Board()
    b.makeMove(toCell('g1'), toCell('f3'))
    assert set(b.getMovesForPiece(*toCell('f3'))) == set(toCells(['d4', 'e5', 'g5', 'h4', 'g1']))

    b.makeMove(toCell('b8'), toCell('c6'))
    assert set(b.getMovesForPiece(*toCell('c6'))) == set(toCells(['b8', 'a5', 'b4', 'd4', 'e5']))

    b.makeMove(toCell('f3'), toCell('d4'))
    assert set(b.getMovesForPiece(*toCell('d4'))) == set(toCells(['f3', 'b3', 'b5', 'c6', 'e6', 'f5']))

    b.makeMove(toCell('e7'), toCell('e5'))
    assert set(b.getMovesForPiece(*toCell('c6'))) == set(toCells(['b8', 'a5', 'b4', 'd4', 'e7']))