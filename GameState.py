class GameState:
    def __init__(self):
        self.setToDefault()

    def setToDefault(self):
        self.turn = 'W'
        self.halfMoves = []
        self.materialScore = 0
        self.canCastle = {'W': {'K': True, 'Q': True}, 'B': {'K': True, 'Q': True}}
        self.castled = {'W': False, 'B': False}
        self.gameState = { 
            'draw': { 'draw': False, 'reason': '' },
            'check': { 'check': False, 'who': '' },
            'checkmate': { 'checkmate': False, 'who': '' },
        }
    
    def copy(self):
        # Not using deepcopy because it's too slow based on the profiling
        newGameState = GameState()
        newGameState.turn = self.turn
        newGameState.halfMoves = self.halfMoves.copy()
        newGameState.materialScore = self.materialScore
        newGameState.canCastle = {
            'W': self.canCastle['W'].copy(),
            'B': self.canCastle['B'].copy()
        }
        newGameState.castled = self.castled.copy()
        newGameState.gameState = {
            'draw': self.gameState['draw'].copy(),
            'check': self.gameState['check'].copy(),
            'checkmate': self.gameState['checkmate'].copy()
        }
        return newGameState
    
    def nextTurn(self):
        self.turn = 'W' if self.turn == 'B' else 'B'

    def getCanCastle(self, color: str, side: str = 'KQ'):
        if(side == 'KQ'):
            return self.canCastle[color]['K'] or self.canCastle[color]['Q']
        return self.canCastle[color][side]
    
    def setCannotCastle(self, color: str, side: str = 'KQ'):
        if(side == 'K' or side == 'Q'):
            self.canCastle[color][side] = False
        elif(side == 'KQ'):
            self.canCastle[color]['K'] = False
            self.canCastle[color]['Q'] = False

    def getCasted(self, color: str):
        return self.castled[color]
    
    def setCastled(self, color: str):
        self.castled[color] = True

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