#!/usr/bin/env python3

#################
# Local Imports #
import board as b
import pdb
import sys


########
# Code #

# Finding the optimal move for a given board.
def Optimal_Game_Strategy(board, move_count=0):
    #print(board.board)
    move_count += 1
    player_value = -1
    best_score = 2
    best_move = (-2, -2)
    best_move_count = sys.maxsize

    if board.whoseMove()==1:
        player_value = 1
        best_score = -2


#Recursive Base Case
    if board.isGameOver():
        best_score = board.findWinner()       
        #print("Base Case")
        return None, player_value, move_count
    
    else:
        for move in board.findMoves():
            #print("Move =  %s,%s" %(move[0], move[1]))
            new_board = board.copyThenPerformMove(move[0], move[1], player_value)
            _, score, move_count = Optimal_Game_Strategy(new_board, move_count)
        #Append score to score history
            #score_history.append(score)
           # move_history.append(move)

            if board.whoseMove()==1:
                if score > best_score or (score == best_score and move_count < best_move_count):
                    best_score = score
                    best_move = move
                    best_move_count = move_count
            else:
                if score < best_score or (score == best_score and move_count < best_move_count):
                    best_score = score
                    best_move = move
                    best_move_count = move_count

    return best_move, best_score, move_count

###########
# Testing #
if __name__ == '__main__':
    board = b.Board()

    board.performMove(0, 0, board.p1)
    board.performMove(0, 2, board.p1)
    board.performMove(2, 1, board.p2)
    board.performMove(2, 2, board.p2)

    top_move, best_score, move_count = Optimal_Game_Strategy(board, 0)
    print(top_move)
    print(best_score)
    print(move_count)
