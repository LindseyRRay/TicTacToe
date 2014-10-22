#!/usr/bin/env python3

##################
# Global Imports #
import numpy as np
import sys

########
# Code #

# Creating an enum for board state.
class BoardState:
    p1  =  1
    p2  = -1
    nil =  0

    # Checking if a value is part of the enum.
    def validate(v):
        return v == BoardState.p1 or v == BoardState.p2 or v == BoardState.nil

    # Deriving the win value from the input value.
    def winValue(v):
        if BoardState.validate(v):
            return v * 3
        else:
            return 0

# A class to represent a tic-tac-toe board.
class Board:
    def __init__(self, board=None):
        if board == None:
            self.__board    = np.arange(9).reshape(3, 3)
            self.__board[:] = BoardState.nil
        else:
            self.__board = board

    # Copying this board into another board.
    def copy(self):
        return Board(np.copy(self.__board))

    # Checking if a player has won.
    #   * Returns BoardState.p1 if player 1 has won.
    #   * Returns BoardState.p2 if player 2 has won.
    #   * Returns BoardState.nil if no one has won.
    def winState(self):
        for pv in [BoardState.p1, BoardState.p2]:
            wpv = BoardState.winValue(pv)

            for i in range(0, 3):
                if self.getRowValue(i) == wpv:
                    return pv
                elif self.getColValue(i) == wpv:
                    return pv
                elif self.getDiagTLBR() == wpv:
                    return pv
                elif self.getDiagTRBL() == wpv:
                    return pv

        return BoardState.nil

    # Checking if the game is over.
    def gameOver(self):
        if self.winState():
            return True
        for s in np.nditer(self.__board):
            if s != BoardState.nil:
                return False
        return True

    # Returning a copied board with 
    def copySet(self, row, col, val):
        nb = self.copy()
        nb.setState(row, col, val)
        return nb

    # Getting the state witin the board.
    def getState(self, row, col):
        return self.__board[row, col]

    # Checking the row value for a given row.
    def getRowValue(self, row):
        return np.sum(self.__board[row, :])

    # Checking the col value for a given col.
    def getColValue(self, col):
        return np.sum(self.__board[:, col])

    # Getting the diagonal value, top-left to bottom-right.
    def getDiagTLBR(self):
        return np.sum([self.getState(0, 0),
                       self.getState(1, 1),
                       self.getState(2, 2)])

    # Getting the diagonal value, top-right to bottom-left.
    def getDiagTRBL(self):
        return np.sum([self.getState(0, 2),
                       self.getState(1, 1),
                       self.getState(2, 0)])

    # Checking if a state is empty.
    def isEmpty(self, row, col):
        return self.getState(row, col) == BoardState.nil

    # Setting a state within the board.
    def setState(self, row, col, val):
        if not BoardState.validate(val):
            return False
        elif row < 0 or col < 0 or row >= 3 or col >= 3:
            return False
        elif not self.isEmpty(row, col):
            return False
        else:
            self.__board[row, col] = val
            return True

###########
# Testing #
def toChar(n):
    if n == BoardState.p1:
        return 'X'
    elif n == BoardState.p2:
        return 'O'
    return '.'

if __name__ == "__main__":
    print("(( Testing the Tic-Tac-Toe board. ))")

    b = Board()

    b.setState(0, 0, BoardState.p1)
    b.setState(1, 1, BoardState.p1)
    b.setState(2, 2, BoardState.p1)

    b.setState(1, 0, BoardState.p2)
    b.setState(2, 0, BoardState.p2)
    b.setState(2, 1, BoardState.p2)

    print(toChar(b.winState()))
    print("----------")
    print(b.gameOver())
    print("----------")

    for row in range(0, 3):
        for col in range(0, 3):
            print(toChar(b.getState(row, col)), end="")
        print()
