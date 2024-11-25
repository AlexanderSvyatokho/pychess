import copy

class GameState:
    def __init__(self):
        self.setToDefault()

    def setToDefault(self):
        self.turn = 'W'
        self.castleState = {'W': {'K': True, 'Q': True}, 'B': {'K': True, 'Q': True}}
        self.gameState = { 
            'draw': { 'draw': False, 'reason': '' },
            'check': { 'check': False, 'who': '' },
            'checkmate': { 'checkmate': False, 'who': '' },
        }
    
    def copy(self):
        newGameState = GameState()
        newGameState.turn = self.turn
        newGameState.castleState = copy.deepcopy(self.castleState)
        newGameState.gameState = copy.deepcopy(self.gameState)
        return newGameState

    def getTurn(self):
        return self.turn
    
    def nextTurn(self):
        self.turn = 'W' if self.turn == 'B' else 'B'
    
    def getCanCastle(self, color: str, side: str):
        return self.castleState[color][side]
    
    def setCannotCastle(self, color: str, side: str = 'KQ'):
        if(side == 'K' or side == 'Q'):
            self.castleState[color][side] = False
        elif(side == 'KQ'):
            self.castleState[color]['K'] = False
            self.castleState[color]['Q'] = False    
            