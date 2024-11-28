from enum import Enum

CELL_SIZE = 70

class DrawType(Enum):
    STALEMATE = 'Stalemate'
    INSUFFICIENT_MATERIAL = 'InsufficientMaterial'

class OpponentType(Enum):
    HUMAN = 'Human vs Human'
    BOT_RANDOM = 'Bot [1]: Random'
    BOT_GREEDY = 'Bot [2]: Greedy Silly'
    BOT_DEPTH1= 'Bot [3]: Depth One'