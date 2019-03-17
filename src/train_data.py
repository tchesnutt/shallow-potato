import numpy as np
import chess
from utils import *


class TrainData:
	def __init__(self, games):
		self.games = games
		self.x_train = np.empty()
		self.y_train = np.empty()
		self.x_e = np.empty()
		self.y_e = np.empty()
		self.x_K = np.empty()
		self.y_K = np.empty()
		self.x_B = np.empty()
		self.y_B = np.empty()
		self.x_R = np.empty()
		self.y_R = np.empty()
		self.x_Q = np.empty()
		self.y_Q = np.empty()
		self.x_N = np.empty()
		self.y_N = np.empty()

	def process(self):
		for _, game in enumerate(self.games):
			board = chess.Board()
			moves = game.moves

			
			result = game.headers["Result"]
			if result[0] == "1":
				# black winner 
				winner = 0
			else:
				# white winner 
				winner = 1

			for m_i, move in enumerate(moves):
				if m_i % 2 == winner:
					pass
				uci_move = move.uci()
				
				from_uci, to_uci = uci_move[:2], uci_move[2:4]
				from_cart, to_cart = uci_cell_to_cartesian(from_uci), uci_cell_to_cartesian(to_uci)
				m = board_to_matrix(board)

				if winner = 0:
					m = flip(m)
					from_cart = flip_cart_coords(from_cart)
					to_cart = flip_cart_coords(to_cart)
				
				
				index = np.where(m[from_cart] != 0)
				piece = INDEX_TO_PIECE[index]

				piece_x = "self.x_%d" % piece
				piece_y = "self.y_%d" % piece
				piece_x = eval(piece_x)
				piece_y = eval(piece_y)

				self.x_train.append(m)
				self.x_train.append(from_cart)
				self.piece_x.append(m)
				self.piece_y.append(to_cart)

				board.push(move)
