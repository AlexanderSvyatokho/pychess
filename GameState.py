import copy

class GameState:
    def __init__(self):
        self.setToDefault()

    def setToDefault(self):
        self.turn = 'W'
        self.score = 0
        self.castleState = {'W': {'K': True, 'Q': True}, 'B': {'K': True, 'Q': True}}
        self.gameState = { 
            'draw': { 'draw': False, 'reason': '' },
            'check': { 'check': False, 'who': '' },
            'checkmate': { 'checkmate': False, 'who': '' },
        }
    
    def copy(self):
        newGameState = GameState()
        newGameState.turn = self.turn
        newGameState.score = self.score
        newGameState.castleState = copy.deepcopy(self.castleState)
        newGameState.gameState = copy.deepcopy(self.gameState)
        return newGameState
    
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

    def isCurrentPlayerInCheck(self):
        return self.gameState['check'] == {'check': True, 'who': self.turn}
    
    def isCurrentPlayerInCheckmate(self):
        return self.gameState['checkmate'] == {'checkmate': True, 'who': self.turn}

    def isDraw(self):
        return self.gameState['draw']['draw'] == True

    def setDraw(self, reason: str):
        self.gameState['draw']['draw'] = True
        self.gameState['draw']['reason'] = reason

    def setCheck(self, who: str, state: bool):
        self.gameState['check']['check'] = state
        self.gameState['check']['who'] = who

    def setCheckmate(self, who: str):
        self.gameState['checkmate']['checkmate'] = True
        self.gameState['checkmate']['who'] = who        

    def isGameOngoing(self):
        return self.gameState['checkmate']['checkmate'] == False and self.gameState['draw']['draw'] == False