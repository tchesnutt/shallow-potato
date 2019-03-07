import numpy as np
import chess


class ValidateData:
	def __init__(self, games):
		self.games = games
		self.x_train = None

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

			for m_i, move in moves:
				if m_i % 2 == 1:
					