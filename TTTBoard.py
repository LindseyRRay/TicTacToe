#Test Python Program
import numpy as np 
import sys 


class Tic_Tac_Board(object):
	''' 3 dimensional numpy array 
	for playing tic tac toe with additional functionality'''

	def __init__(self, player1, player2, default_val=0):
		self.board = (np.arange(9).reshape(3,3))
		self.default_val= default_val
		self.board[:] = self.default_val
		self.player1 = player1
		self.player1_value = 1
		self.player2 = player2
		self.player2_value = -1

	def translate_player_symbol(self, player_symbol):
		if player_symbol == self.player1:
			return self.player1_value
		else:
			return self.player2_value

	def player_move(self, row, column, player_symbol):
		'''assigns a move to a position on the board '''
		if self.check_space(row, column):
			self.board[row, column] = self.translate_player_symbol(player_symbol)
			return False
		else:
			return True

	def copy_board_and_move(self, row, column, player_symbol):
		'''assigns a move to a position on the board and returns a new copy of the board'''
		new_board = Tic_Tac_Board(self.player1, self.player2, self.default_val)
		new_board.board = np.copy(self.board)

		new_board.player_move(row, column, player_symbol)
		return new_board
	
	def check_space(self, row, column):
		'''checks if a board position is empty'''
		if self.board[row, column] != self.default_val:	
			return False
		return True

	def check_moves(self):
		''' returns list of allowable moves (empty spaces)'''
		children = np.ravel(np.transpose(np.nonzero(self.board == self.default_val)))
		return list(zip(list(children[::2]), list(children[1:][::2])))


	def check_win(self, player_symbol):
		player_value = self.translate_player_symbol(player_symbol)

		''' checks if any of the players has won a game '''
		if np.sum([self.board[0,2], self.board[1,1], self.board[2,0]]) == (3*player_value):
			return player_value

		for i in range(0,3):
			if np.sum(self.board[i,:])== (3*player_value) or np.sum(self.board[:,i])== (3*player_value):
				return player_value
		
			elif np.trace(self.board) == 3*player_value:
				return player_value

	
		return 0

	def check_both(self):
		p1 = self.check_win("X")
		p2 = self.check_win("O")

		if p1 == 0:
			if p2 == 0:
				return 0
			return p2
		return p1

	def players_win(self):
		w = check_win(self.player1)
		if w == -1:
			return board.player2_value
		elsif

	def game_over(self):
		'' 'checks it the game has ended'''
		if self.check_win(self.player1_value) == self.player1_value:
			#print("Player 1 Wins")
			return True
		elif self.check_win(self.player2_value) == self.player2_value:
			#print("Player 2 Wins")
			return True
		elif len(self.board[self.board==0]) == 0:
			#print("Game Over - No one wins")
			return True

		else:
			return False


	def prompt_move(self):
		''' prompts players to take turns moving '''
		if np.sum(self.board) == 0:
			return 1
		else:
			return 0

	def show_board(self):
		print("\nTic Tac Toe Game\n")

		for j in range(0,3):
			for k in range(0,3):
				if self.board[j, k] == self.player1_value:
					sys.stdout.write(self.player1)
				elif self.board[j, k] == self.player2_value:
					sys.stdout.write(self.player2)
				else:
					sys.stdout.write('_')
			sys.stdout.write('\n')
		sys.stdout.write('\n')
	


if __name__ == '__main__':
	new_game = Tic_Tac_Board("X", "O")
	new_game.check_win(1)
	new_game.prompt_move()
	print(new_game.check_moves())
	new_game.show_board()
	new_game.player_move(1,1, "X")
	new_game.show_board()
	new_game.player_move(0,0,"O")
	new_game.show_board()
	new_game.player_move(1,1,"X")
	new_game.check_moves()
