from Utils import *

def testOppositeColor():
    assert oppositeColor('W') == 'B'
    assert oppositeColor('B') == 'W'

def testToCell():
    assert toCell('a1') == (0, 0)
    assert toCell('h1') == (7, 0)
    assert toCell('a8') == (0, 7)
    assert toCell('h8') == (7, 7)
    assert toCell('B3') == (1, 2)
    assert toCell('F6') == (5, 5)

def testToCells():
    assert toCells(['a2']) == [(0, 1)]
    assert toCells(['h2', 'd4', 'G6']) == [(7, 1), (3, 3), (6, 5)]

def testFromCell():
    assert fromCell((0, 0)) == 'a1'
    assert fromCell((7, 0)) == 'h1'
    assert fromCell((0, 7)) == 'a8'
    assert fromCell((7, 7)) == 'h8'
    assert fromCell((1, 2)) == 'b3'
    assert fromCell((5, 5)) == 'f6'