import numpy as np
import chess
from utils import board_to_matrix, flip


class ValidateData:
    def __init__(self, games):
        self.games = games
        self.x_valid = []

    def process(self):
        for _, game in enumerate(self.games):
            board = chess.Board()
            moves = game.mainline_moves()

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
                m = board_to_matrix(board)

                if winner == 0:
                    m = flip(m)

                m = np.rollaxis(m, 2, 0)

                self.x_valid.append(m)

                board.push(move)
