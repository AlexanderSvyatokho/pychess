import random, time, logging
from Board import Board
from BotBase import BotBase

# Makes a move that gives the best score taken into account best possible
# response of the opponent (1 depth)
class BotDepthN(BotBase):
    
    recordedTimes = []

    def __init__(self, maxDepth: int):
        super().__init__()
        self.maxDepth = maxDepth if maxDepth > 0 else 1

    def makeMove(self, board: Board):
        start = time.time()

        self.makeIteration(board, 0)

        timeTaken = time.time() - start  
        self.recordedTimes.append(timeTaken)
        avgTime = sum(self.recordedTimes) / len(self.recordedTimes)
        logging.info(f'Bot stats:: time taken: {round(timeTaken, 3)}, avg time: {round(avgTime, 3)}')
        
    def makeIteration(self, board: Board, depth: int):
        logging.info(f'makeIteration: depth={depth}')
        myColor = board.getTurn()

        if depth >= self.maxDepth:
            if myColor == 'W':
                return -board.gameState.materialScore
            return board.gameState.materialScore
       
        validMoves = board.getValidMoves(myColor)
        random.shuffle(validMoves) # Randomize moves to avoid always picking the first one
        moves = self.selectSignificantMoves(board, validMoves)
        
        if (depth == 0 and len(moves) < 10):
            moves.extend(validMoves[:10 - len(moves)])

        if(len(moves) > 0):
            bestMove = moves[0]
            # From all possible moves, pick the one that gives the worst maximum score for the opponent
            worstOpponentScore = 1000000
            for move in moves:
                boardCopy = board.copy()
                boardCopy.makeMove(move[0], move[1], False)
                
                bestOpponentScore = -1000000
                opponentMoves = boardCopy.getValidMoves('W' if myColor == 'B' else 'B')
                opponentMoves = self.selectSignificantMoves(boardCopy, opponentMoves)
                random.shuffle(opponentMoves)

                for opponentMove in opponentMoves:
                    boardCopy2 = boardCopy.copy()
                    boardCopy2.makeMove(opponentMove[0], opponentMove[1], False)
                    #score = boardCopy2.gameState.materialScore
                    score = self.makeIteration(boardCopy2, depth + 1)
                    
                    if score and score > bestOpponentScore:
                        bestOpponentScore = score
                
                # If the opponent has no valid moves (checkmate or draw) use the current score
                if len(opponentMoves) == 0:
                    score = boardCopy.gameState.materialScore
                    if myColor == 'W':
                        score = -score
                    if score > bestOpponentScore:
                        bestOpponentScore = score

                if worstOpponentScore > bestOpponentScore:
                    worstOpponentScore = bestOpponentScore
                    bestMove = move

            if depth == 0:
                board.makeMove(bestMove[0], bestMove[1])
            
            return worstOpponentScore
        else:
            if myColor == 'W':
                return -board.gameState.materialScore
            return board.gameState.materialScore