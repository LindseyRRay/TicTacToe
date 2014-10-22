import unittest
import TTTBoard as tt
import minimax as ai
import numpy as np 
import pdb as pdb

class TestTTT (unittest.TestCase):

	def test_first_move(self):
		game = tt.Tic_Tac_Board("X", "O")
		game.board[0,0] = 1
		game.board[0,1] = 1
		game.board[2,0] = -1
		game.board[2,1] = -1
		top_move, _, count = ai.Optimal_Game_Strategy(game, 0)

		self.assertEqual(top_move, (0,2))
	
	def test_correct_space(self):
		game = tt.Tic_Tac_Board("X", "O")
		
		[game.board[i,j] for i in range(0,3) for j in range(0,3)]

		for i in range(0,3):
			for j in range(0,3):
				self.assertRaises(ValueError, game.player_move(i, j,"X"))

	def test_User_Move_Choice(self):
		game = tt.Tic_Tac_Board("X", "O")
		for row in range(0,3):
			for col in range(0,3):
				test_a = game.copy_board_and_move(row, col, "X")
				test_b = game.copy_board_and_move(row, col, "X")
				print("Row: %s" % row)
				print("col: %s" % col)
				
				self.assertEqual(np.array_equal(test_a.board, test_b.board), True)
	
	def test_second_move(self):
		game = tt.Tic_Tac_Board("X", "O")

		game.board[0,0] = 1
		game.board[0,2] = 1
		game.board[2,0] = -1
		pdb.set_trace()
		top_move, _, _ = ai.Optimal_Game_Strategy(game, 3)

		self.assertEqual(top_move, (0,1))


	def test_third_move(self):
		game = tt.Tic_Tac_Board("X", "O")

		game.board[0,0] = 1
		game.board[0,2] = 1
		game.board[0,1] = -1
		game.board[1,1] = -1
		top_move, _, _ = ai.Optimal_Game_Strategy(game, 4)

		self.assertEqual(top_move, (2,1))
		


if __name__ == '__main__':
	unittest.main()

