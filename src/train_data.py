import numpy as np
import chess


class TrainData:
	def __init__(self, games):
		self.games = games
		self.x_train = None
		self.y_train = None
		self.x_e = None
		self.y_e = None
		self.x_K = None
		self.y_K = None
		self.x_B = None
		self.y_B = None
		self.x_R = None
		self.y_R = None
		self.x_Q = None
		self.y_Q = None
		self.x_N = None
		self.y_N = None

	def process():
		for _, game in enumerate(self.games):
			board = chess.Board()
			moves = game.moves

			
			result = game.headers["Result"]
			if result[0] == "1":
				board.push(moves.f(moves.start.variations[0]))
				moves = enumerate(moves, 1)
			else:
				moves = enumerate(moves)

			# Board object:
			# r n b q k b n r
			# p p p p p p p p
			# . . . . . . . .
			# . . . . . . . .
			# . . . . . . . .
			# . . . . . . . .
			# P P P P P P P P
			# R N B Q K B N R

			# iterate through winner's moves
			for m_i, move in moves:
				uci_move = move.uci()
				
				from_uci, to_uci = uci_move[:2], uci_move[2:4]
				board.push(move)