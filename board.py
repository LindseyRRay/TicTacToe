#!/usr/bin/env python3

##################
# Global Imports #
import numpy as np

########
# Code #

# Effectively an enum of board states.
class BoardState:
	p1  =  1
	p2  = -1
	nil =  0

	# Validating that a number is valid for the board.
	def validate(n):
		return n == BoardState.p1 or n == BoardState.p2 or n == BoardState.p3

# The class to represent a board.
class Board:
	def __init__(self, board=None):
		if board is None:
			self.board = np.arange(9).reshape(3, 3)
			self.board[:] = BoardState.nil
		else:
			self.board = board

	# Copying this board into another board.
	def copy(self):
		return Board(np.copy(self.board))

	# Checking if a space in the board is empty.
	def isEmpty(self, row, col):
		return self.board[row, col] == BoardState.nil

	# Checking if a player can perform a move.
	def canMove(self, row, col, val):
		if not BoardState.validate(val):
			return False
		elif not self.isEmpty(row, col):
			return False
		elif row < 0 or row >= 3 or col < 0 or col >= 3:
			return False
		else:
			return True

	# Doing a move for the player.
	def performMove(self, row, col, val):
		if not self.canMove(row, col, val):
			return False
		self.board[row, col] = val
		return True

	# Making a copy of the board and then writing a value to it.
	def copyThenPerformMove(self, row, col, val):
		nb = self.copy()
		nb.performMove(row, col, val)
		return nb

	# Finding all possible moves on a board.
	def findMoves(self):
		return [(x, y) for x in range(0, 3)
					   for y in range(0, 3)
					   if self.isEmpty(x, y)]

	# Finding a winner.
	def findWinner(self):
		for p in [BoardState.p1, BoardState.p2]:
			w = p * 3
			
			if np.sum([self.board[0, 0],
				       self.board[1, 1],
					   self.board[2, 2]]) == w:
				return p
			elif np.sum([self.board[0, 2],
				         self.board[1, 1],
						 self.board[2, 0]]) == w:
				return p
			
			for i in range(0, 3):
				if np.sum(board[i, :]) == w or np.sum(board[:, i]) == w:
					return p

		return BoardState.nil

	# Checking if the game is over.
	def isGameOver(self):
		return self.findWinner() != 0 or len(self.findMoves()) == 0
