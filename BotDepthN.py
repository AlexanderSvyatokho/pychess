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

        self.makeMoveRecursive(board, 0)

        timeTaken = time.time() - start  
        self.recordedTimes.append(timeTaken)
        avgTime = sum(self.recordedTimes) / len(self.recordedTimes)
        logging.info(f'Bot stats:: time taken: {round(timeTaken, 3)}, avg time: {round(avgTime, 3)}')

    def maxMovesForDepth(self, depth: int):
        if depth == 0:
            return 15
        elif depth == 1:
            return 10
        elif depth == 2:
            return 5
        else:
            return 3
        
    def makeMoveRecursive(self, board: Board, depth: int):
        #logging.info(f'makeIteration: depth={depth}')
        myColor = board.getTurn()
        maxMovesForDepth = self.maxMovesForDepth(depth)

        if depth >= self.maxDepth:
            return board.gameState.materialScore
       
        validMoves = []
        if (board.gameState.isGameOngoing()):
            validMoves = board.getValidMoves(myColor)
            random.shuffle(validMoves) # Randomize moves to avoid always picking the first one

        moves = self.selectSignificantMoves(board, validMoves)

        # print(f'Depth={depth}, significant moves count ={len(moves)}, significant moves ={moves}')
        
        # If we are at the root node and there are few significant moves, consider more moves
        minMovesForDepth0 = 60
        if (depth == 0 and len(moves) < minMovesForDepth0):
            for vm in validMoves:
                if vm not in moves:
                    moves.append(vm)
                    if len(moves) >= minMovesForDepth0:
                        break

        if (depth >= 0 and len(moves) > maxMovesForDepth):
            moves = moves[:maxMovesForDepth]

        # print(f'Depth={depth}, selected moves count ={len(moves)}, selected moves ={moves}')

        if(len(moves) > 0):
            bestMove = moves[0]
            # From all possible moves, pick the one that gives the worst maximum score for the opponent
            worstOpponentScore = 1000000
            for move in moves:
                bestResponseOpponentScore = -1000000

                boardCopy = board.copy()
                boardCopy.makeMove(move[0], move[1], False)

                validOpponentMoves = []

                if (boardCopy.gameState.isGameOngoing()):
                    validOpponentMoves = boardCopy.getValidMoves('W' if myColor == 'B' else 'B')
                    random.shuffle(validOpponentMoves)

                opponentMoves = self.selectSignificantMoves(boardCopy, validOpponentMoves)
                opponentMoves = opponentMoves[:maxMovesForDepth]
                
                # If there are no significant responses for the opponent, consider some random moves
                minOpponentsMoves = 5
                if (len(opponentMoves) < minOpponentsMoves):
                    for vm in validOpponentMoves:
                        if vm not in opponentMoves:
                            opponentMoves.append(vm)
                            if len(opponentMoves) >= minOpponentsMoves:
                                break

                # print(f'opponentMoves for move {move}: depth={depth}, moves count ={len(opponentMoves)}, opponentMoves ={opponentMoves}')

                # If the opponent has no valid moves (checkmate or draw) use the current score
                if len(opponentMoves) == 0:
                    score = boardCopy.gameState.materialScore
                    # print(f'Found mate or draw with move: {move}, score: {score}')
                    if myColor == 'W':
                        score = -score
                    if score > bestResponseOpponentScore:
                        bestResponseOpponentScore = score
                else:
                    for opponentMove in opponentMoves:
                        boardCopy2 = boardCopy.copy()
                        boardCopy2.makeMove(opponentMove[0], opponentMove[1], False)
                        score = self.makeMoveRecursive(boardCopy2, depth + 1)
                        if myColor == 'W':
                            score = -score
                        if score > bestResponseOpponentScore:
                            bestResponseOpponentScore = score

                        if score and score > bestResponseOpponentScore:
                            bestResponseOpponentScore = score

                if worstOpponentScore > bestResponseOpponentScore:
                    worstOpponentScore = bestResponseOpponentScore
                    bestMove = move

            if depth == 0:
                # print(f'Making move: {bestMove}')
                board.makeMove(bestMove[0], bestMove[1], False)
                return 
            
            # print(f'Returning to parent node!')

            return -worstOpponentScore if myColor == 'W' else worstOpponentScore
        else:
            return board.gameState.materialScore