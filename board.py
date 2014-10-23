#!/usr/bin/env python3

##################
# Global Imports #
import numpy as np

########
# Code #

# The class to represent a board.
class Board(object):

	def __init__(self):
		self.p1  =  1
		self.p2  = -1
		self.nil =  0	
		self.board = np.arange(9).reshape(3, 3)
		self.board[:] = self.nil

	# Checking if a space in the board is empty.
	def isEmpty(self, row, col):
		return self.board[row, col] == self.nil

	# Validating that a number is valid for the board.
	def validate(self, n):
		return n in [self.p1, self.p2]

	# Checking if a player can perform a move.
	def canMove(self, row, col, val):
		if self.validate(val) and all(x in range(3) for x in [row, col]) and self.isEmpty(row, col):
			return True
		return False


	# Checking whose move it is.
	def whoseMove(self):
		if np.sum(self.board) == 0:
			return self.p1
		else:
			return self.p2

	# Doing a move for the player.
	def performMove(self, row, col, val):
		if self.canMove(row, col, val):
			self.board[row, col] = val
			return True
		return False
			

	# Making a copy of the board and then writing a value to it.
	def copyThenPerformMove(self, row, col, val):
		'''assigns a move to a position on the board and returns a new copy of the board'''
		new_board = Board()
		new_board.board = np.copy(self.board)

		new_board.performMove(row, col, val)
		return new_board

	# Finding all possible moves on a board.
	def findMoves(self):
		return ((x, y) for x in range(3)
					   for y in range(3)
					   if self.isEmpty(x, y))

	# Finding a winner.
	def findWinner(self):
		for p in [self.p1, self.p2]:
			w = p * 3
			
			if np.trace(self.board) == w:
				return p
			elif np.sum([self.board[0, 2],
				         self.board[1, 1],
						 self.board[2, 0]]) == w:
				return p
			
			for i in range(3):
				if np.sum(self.board[i, :]) == w or np.sum(self.board[:, i]) == w:
					return p

		return self.nil

	# Checking if the game is over.
	def isGameOver(self):
		return self.findWinner() != 0 or len(list(self.findMoves())) == 0





