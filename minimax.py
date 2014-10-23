#!/usr/bin/env python3

#################
# Local Imports #
import board as b

########
# Code #

# Finding the optimal move for a given board.
def optimalGameStrategy(board, moveCount=0):
    moveCount += 1
    bestScore = 2
    bestMove = (-2, -2)

    if board.whoseMove() == b.BoardState.p1:
        bestScore = -2

    if board.isGameOver():
        score = board.findWinner()
        if score == b.BoardState.p2:
            bestScore = score

        return None, bestScore, moveCount
    else:
        moves = board.findMoves()
        for move in moves:
            newBoard = board.copyThenPerformMove(move[0], move[1], b.BoardState.p2)
            _, score, moveCount = optimalGameStrategy(newBoard, moveCount)

            if board.whoseMove() == b.BoardState.p1:
                if score > bestScore:
                    bestScore = score
                    bestMove = move
            else:
                if score < bestScore:
                    bestScore = score
                    bestMove = move

    return bestMove, bestScore, moveCount

###########
# Testing #
if __name__ == '__main__':
    board = b.Board()

    board.performMove(0, 0, b.BoardState.p1)
    board.performMove(0, 2, b.BoardState.p1)
    board.performMove(2, 1, b.BoardState.p2)

    topMove, bestScore, moveCount = optimalGameStrategy(board, 0)
    print(topMove)
    print(bestScore)
    print(moveCount)
