from enum import Enum

CELL_SIZE = 70

class DrawType(Enum):
    STALEMATE = 'Stalemate'
    INSUFFICIENT_MATERIAL = 'InsufficientMaterial'

class OpponentType(Enum):
    HUMAN = 'Human vs Human'
    BOT_RANDOM = 'Bot: Random'