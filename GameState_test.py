from GameState import GameState
from Constants import *

def testDefaultState():
    gs = GameState()
    assert gs.turn == 'W'
    assert gs.getCanCastle('W', 'K') == True
    assert gs.getCanCastle('B', 'K') == True

def testCopyState():
    gs = GameState()
    gs.turn = 'B'
    gs.halfMoves = [((0,1), (0,3))]
    gs.score = 100
    gs.setCannotCastle('W', 'K')
    gs.setCheck('W', True)
    gs.setDraw(DrawType.STALEMATE)

    gsCopy = gs.copy()
    assert gsCopy.turn == 'B'
    assert gsCopy.halfMoves == [((0,1), (0,3))]
    assert gsCopy.score == 100  
    assert gsCopy.getCanCastle('W', 'K') == False
    assert gsCopy.getCanCastle('W', 'Q') == True
    assert gsCopy.getCanCastle('B', 'K') == True
    assert gsCopy.getCanCastle('B', 'Q') == True

def testTurn():
    gs = GameState()
    assert gs.turn == 'W'
    gs.nextTurn()
    assert gs.turn == 'B'
    gs.nextTurn()
    assert gs.turn == 'W'   

def testSetCannotCastle():
    gs = GameState()

    gs.setCannotCastle('W', 'K')
    assert gs.getCanCastle('W', 'K') == False
    assert gs.getCanCastle('W', 'Q') == True
    assert gs.getCanCastle('B', 'K') == True
    assert gs.getCanCastle('B', 'Q') == True

    gs.setCannotCastle('W', 'Q')
    assert gs.getCanCastle('W', 'K') == False
    assert gs.getCanCastle('W', 'Q') == False
    assert gs.getCanCastle('B', 'K') == True
    assert gs.getCanCastle('B', 'Q') == True

    gs.setCannotCastle('B', 'KQ')
    assert gs.getCanCastle('W', 'K') == False
    assert gs.getCanCastle('W', 'Q') == False
    assert gs.getCanCastle('B', 'K') == False
    assert gs.getCanCastle('B', 'Q') == False

def testSetCheck():
    gs = GameState()
    assert gs.isCurrentPlayerInCheck() == False
    gs.setCheck('W', True)
    assert gs.isCurrentPlayerInCheck() == True
    gs.setCheck('W', False)
    assert gs.isCurrentPlayerInCheck() == False

def testSetCheckmate():
    gs = GameState()
    assert gs.isCurrentPlayerInCheckmate() == False
    gs.setCheckmate('W')
    assert gs.isCurrentPlayerInCheckmate() == True

def testSetDraw():
    gs = GameState()
    assert gs.isDraw() == False
    gs.setDraw(DrawType.STALEMATE)
    assert gs.isDraw() == True

def testIsGameOngoingAfterCheck():
    gs = GameState()
    assert gs.isGameOngoing()
    
    gs.setCheck('W', True)
    assert gs.isGameOngoing()

    gs.setCheck('B', True)
    gs.setCheck('W', False)
    assert gs.isGameOngoing()

def testIsGameOngoingAfterCheckMate():
    gs = GameState()
    gs.setCheckmate('B')
    assert gs.isGameOngoing() == False

def testIsGameOngoingAfterDraw():
    gs = GameState()
    gs.setDraw(DrawType.INSUFFICIENT_MATERIAL)
    assert gs.isGameOngoing() == False