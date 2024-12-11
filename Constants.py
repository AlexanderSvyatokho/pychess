from enum import Enum

CELL_SIZE = 70

class DrawType(Enum):
    STALEMATE = 'Stalemate'
    INSUFFICIENT_MATERIAL = 'InsufficientMaterial'

class OpponentType(Enum):
    HUMAN = 'Human vs Human'
    BOT_RANDOM = 'Bot [1]: Random'
    BOT_GREEDY = 'Bot [2]: Greedy Silly'
    BOT_DEPTH1 = 'Bot [3]: Depth 1'
    BOT_DEPTH2 = 'Bot [4]: Depth 2'
    BOT_DEPTH3 = 'Bot [5]: Depth 3 - Slow!'

PIECE_VALUES = {
    'P': 1,
    'N': 3,
    'B': 3,
    'R': 5,
    'Q': 9,
    'WP': 1,
    'WN': 3,
    'WB': 3,
    'WR': 5,
    'WQ': 9,
    'BP': 1,
    'BN': 3,
    'BB': 3,
    'BR': 5,
    'BQ': 9
}