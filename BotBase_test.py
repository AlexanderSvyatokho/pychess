from Board import Board
from BotBase import BotBase

def testSelectSignificantMoves():
        b = Board()
        b.clear()

        b.board[6][4] = 'BK'
        b.board[1][1] = 'BR'
        b.board[4][2] = 'BB'
        b.board[2][6] = 'WP'
        b.board[1][3] = 'WP'
        b.board[2][4] = 'WB'
        b.board[3][2] = 'WN'
        b.board[4][0] = 'WR'
        b.board[6][7] = 'WR'
        b.board[6][6] = 'WK'
        b.board[7][1] = 'WP'

        assert b.gameState.turn == 'W'

        moves = b.getValidMoves('W')

        bot = BotBase()
        significantMoves = bot.selectSignificantMoves(b, moves)

        expectedMoves = [
            ((4, 0), (4, 2)),   # WR captures BB
            ((4, 0), (6, 0)),   # WR checks BK
            ((2, 4), (4, 2)),   # WB captures BB
            ((2, 4), (4, 6)),   # WB checks BK
            ((3, 2), (1, 1)),   # WN captures BR
            ((2, 6), (2, 7)),   # WP promotes
            ((6, 6), (7, 7)),   # Discovered check after WK moves
            ((6, 6), (7, 6)),   # Discovered check after WK moves
            ((6, 6), (5, 7)),   # Discovered check after WK moves
            ((6, 6), (5, 6)),   # Discovered check after WK moves
            ((7, 1), (7, 3)),   # WP checks WK
        ]

        assert set(significantMoves) == set(expectedMoves)
