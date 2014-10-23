#!/usr/bin/env python3

#################
# Local Imports #
import board as b
import pdb

########
# Code #

# Finding the optimal move for a given board.
def Optimal_Game_Strategy(board, move_count=0):
    move_count += 1
    player_value = -1
    best_score = 2
    best_move = (-2, -2)

    if board.whoseMove() == board.p1:
        player_value = 1
        best_score = -2


#Recursive Base Case
    if board.isGameOver():
        best_score = board.findWinner()
        return None, best_score, move_count
        pdb.set_trace()
        print("Base Case")
    
    else:
        print("No Base Case")
        score_history = list()
        move_history = list()
        for move in board.findMoves():
            print("Move =  %s,%s" %(move[0], move[1]))
            newBoard = board.copyThenPerformMove(move[0], move[1], player_value)
            _, score, move_count = Optimal_Game_Strategy(newBoard, move_count)
        #Append score to score history
            score_history.append(score)
            move_history.append(move)

            if board.whoseMove() == player_value:
                if score > best_score:
                    best_score = score
                    best_move = move
            else:
                if score < best_score:
                    best_score = score
                    best_move = move
        #Add checking for case if all cases are equally bad then select one at random
        #pdb.set_trace()
        if set(score_history) in [set([0]), set([-1*player_value])]:
            best_score = score_history[0]
            best_move = move_history[0]

    return best_move, best_score, move_count

###########
# Testing #
if __name__ == '__main__':
    board = b.Board()

    board.performMove(0, 0, board.p1)
    board.performMove(0, 2, board.p1)
    board.performMove(2, 1, board.p2)

    top_move, best_score, move_count = Optimal_Game_Strategy(board, 0)
    print(top_move)
    print(best_score)
    print(move_count)
