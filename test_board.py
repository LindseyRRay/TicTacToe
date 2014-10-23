#series of tests for TicTacToe Board
import unittest
import board as b
import numpy as np
import minimax as ai


class TestTTT (unittest.TestCase):

    def test_winner(self):
        game = b.Board()
        game.board[0,0] = 1
        game.board[0,1] = 1
        game.board[0,2] = 1
        game.board[2,0] = -1
        game.board[2,1] = -1

        self.assertEqual(1, game.findWinner())   


    def test_game_over(self):
        game = b.Board()
        game.board[0,0] = 1
        game.board[0,1] = 1
        game.board[0,2] = 1
        game.board[2,0] = -1
        game.board[2,1] = -1

        self.assertEqual(True, game.isGameOver())           

    def test_User_Move_Choice(self):
        game = b.Board()
        for row in range(0,3):
            for col in range(0,3):
                test_a = game.copyThenPerformMove(row, col, 1)
                test_b = game.copyThenPerformMove(row, col, 1)
                print("Row: %s" % row)
                print("col: %s" % col)
                
                self.assertEqual(np.array_equal(test_a.board, test_b.board), True)


    def test_first_move(self):
        game = b.Board()
        game.board[0,0] = 1
        game.board[0,1] = 1
        game.board[2,0] = -1
        game.board[2,1] = -1
        print(game.whoseMove())
        top_move, _, count = ai.Optimal_Game_Strategy(game, 0)

        self.assertEqual(top_move, (0,2))  
        


if __name__ == '__main__':
    unittest.main()

