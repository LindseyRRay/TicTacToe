import TTTBoard as tt
import pdb as pdb


def Optimal_Game_Strategy(board, count_moves):
	count_moves += 1
	possible_moves = board.check_moves()

	best_score = 2
	player_symbol="O"
	best_move=(-2,-2)

	if board.prompt_move():
		best_score = -2
		player_symbol="X"


	if board.game_over():
		best_score = board.check_win("X")
		score2 = board.check_win("O")
		
		if best_score == 0:
			if score2 != 0:
				best_score = score2
		return None, best_score, count_moves

	else:
		for move in possible_moves:
			new_board = board.copy_board_and_move(move[0], move[1], player_symbol)
			_, score, count_moves = Optimal_Game_Strategy(new_board, count_moves)
		#add in something to make the algorithm smarter
			
			#Check if anything is an absolute best score
			if board.prompt_move():
				if score > best_score:
					best_score = score
					best_move = move

			else:
				if score < best_score:
					best_score = score
					best_move = move

	return best_move, best_score, count_moves

if __name__ == '__main__':
	game = tt.Tic_Tac_Board("X", "O")
	game.board[0,0] = 1
	game.board[0,2] = 1

	game.board[2,1] = -1

	top_move, _, count = Optimal_Game_Strategy(game, 0)

	print(top_move)


