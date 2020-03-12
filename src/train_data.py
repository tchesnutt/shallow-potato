import numpy as np
import chess

from utils import *


class TrainData:
    __slots__ = TRAIN_DATA_SLOTS
    def __init__(self, games):
        self.games = games
        self.init_data()



    def init_data(self):
        for data_name in TRAIN_FILE_TYPES:
            self.__setattr__(data_name, [])



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
                uci_move = move.uci()

                from_uci, to_uci = uci_move[:2], uci_move[2:4]
                from_cart, to_cart = uci_cell_to_cartesian(
                    from_uci), uci_cell_to_cartesian(to_uci)
                m = board_to_matrix(board)

                if winner == 0:
                    m = flip(m)
                    from_cart = flip_cart_coords(from_cart)
                    to_cart = flip_cart_coords(to_cart)

                index = np.where(m[from_cart] != 0)
                piece = INDEX_TO_PIECE[index[0][0]]

                m = np.rollaxis(m, 2, 0)
                from_cart_flattened = flatten_coord(from_cart)
                to_cart_flattened = flatten_coord(to_cart)

                piece_x = "self." + piece + "_X"
                piece_y = "self." + piece + "_Y"
                piece_x = eval(piece_x)
                piece_y = eval(piece_y)

                self.Picker_X.append(m)
                self.Picker_Y.append(from_cart_flattened)
                piece_x.append(m)
                piece_y.append(to_cart_flattened)
                
                board.push(move)
