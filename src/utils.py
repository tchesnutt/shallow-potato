import os
import chess.pgn
import json
import pickle
import numpy as np
from bunch import Bunch

PIECE_TO_INDEX = {
    'P': 0,
    'R': 1,
    'N': 2,
    'B': 3,
    'Q': 4,
    'K': 5,
}
INDEX_TO_PIECE = {
    0: 'P',
    1: 'R',
    2: 'N',
    3: 'B',
    4: 'Q',
    5: 'K',
}
CART_TO_UCI_CELL = {
    0: 'a',
    1: 'b',
    2: 'c',
    3: 'd',
    4: 'e',
    5: 'f',
    6: 'g',
    7: 'h',
}

UCI_CELL_TO_CART = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
    'f': 5,
    'g': 6,
    'h': 7,
}

TRAIN_FILE_TYPES = ['Picker_X', 'P_X', 'K_X', 'B_X', 'R_X', 'Q_X',
                    'N_X', 'Picker_Y', 'P_Y', 'K_Y', 'B_Y', 'R_Y', 'Q_Y', 'N_Y']

MATRIX_SIZE = (8, 8, 6)

TRAIN_FILE_LEN_PATH = './data/parsed/train/train_file_len.json'

VALID_FILE_LEN_PATH = './data/parsed/validation/valid_file_len.json'



def parse_games(file_name):
    """return type list[...games]
    takes in a string and parses all games in that file
    """
    pgn_file = open(file_name, encoding='utf-8', errors='replace')
    game = chess.pgn.read_game(pgn_file)
    game_list = []
    while game:
        game_list.append(game)
        game = chess.pgn.read_game(pgn_file)
    return game_list



def cartesian_to_uci_cell(coordinates):
    """return type string
    ex.
        coordinates = [0, 0]
        result = a8
    """
    return CART_TO_UCI_CELL[coordinates[1]] + str(8 - coordinates[0])



def uci_cell_to_cartesian(uci_cell):
    """ex. 
        uci_cell = f8
        result = (5, 0)
    """
    return  (8 - int(uci_cell[1]), UCI_CELL_TO_CART[uci_cell[0]])



def board_to_matrix(board):
    """return type numpy arraylike
    takes in a chess.board and returns a 8,8,6 representation of the board
    """
    board = np.array(list(str(board).replace('\n', '').replace(' ', ''))).reshape((8, 8))
    matrix = np.zeros(MATRIX_SIZE)

    for i in range(MATRIX_SIZE[0]):
        for j in range(MATRIX_SIZE[1]):
            piece = board[i,j]
            if piece == ".":
                continue
            if piece.isupper():
                matrix[i, j, PIECE_TO_INDEX[piece]] = 1
            else:
                matrix[i, j, PIECE_TO_INDEX[piece.upper()]] = -1

    return matrix



def flip(matrix):
    """returns a matrix rotated about the horizontal plane
    also inverts the peice designation betweeflatten_coord_to_target_arrayn white and black
    """
    matrix = matrix[::-1, :, :]
    whites = np.where(matrix == 1)
    blacks = np.where(matrix == -1)
    matrix[whites] = -1
    matrix[blacks] = 1
    return matrix



def flip_cart_coords(coord):
    """
    returns cartestian coordinates rotated about the horizontal plane
    """
    return (8 - coord[0] -1, coord[1])



def coord_to_prob_dist(coord, layer):
    """
    returns 8x8x6 prob distribution for a coordinate
    """
    x, y = coord
    matrix = np.zeros(MATRIX_SIZE)
    matrix[x, y, layer] = 1
    matrix = np.rollaxis(matrix, 2, 0)
    return matrix



def flatten_coord(coord):
	return ((8 * coord[0]) + coord[1])



def flatten_coord_to_target_array(flat_coord_list):
    target = []
    for flat_coord in flat_coord_list:
        target_array = np.zeros(64)
        target_array[flat_coord] = 1
        target.append(target_array)
    return target



def get_config_from_json(json_file):
    with open(json_file, 'r') as c_file:
        c_dict = json.load(c_file)
    config = Bunch(c_dict)

    return config, c_dict



def process_config(json_file):
    config, _ = get_config_from_json(json_file)
    return config



def load_data_file(file_name):
    file = open(file_name, 'rb')

    return pickle.load(file)