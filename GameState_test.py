from GameState import GameState

def testDefaultState():
    gs = GameState()
    assert gs.turn == 'W'
    assert gs.getCanCastle('W', 'K') == True
    assert gs.getCanCastle('B', 'K') == True

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
