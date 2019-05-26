import chess.pgn
import numpy as np

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

TRAIN_FILE_TYPES = ['picker_x', 'p_x', 'K_x', 'B_x', 'R_x', 'Q_x',
                    'N_x', 'picker_y', 'P_y', 'K_y', 'B_y', 'R_y', 'Q_y', 'N_y']

MATRIX_SIZE = (8, 8, 6)

def parse_games(file_name):
    """
    return type list[...games]
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
    """
    return type string
    ex.
        coordinates = [0, 0]
        result = a8
    """
    return CART_TO_UCI_CELL[coordinates[1]] + str(8 - coordinates[0])

def uci_cell_to_cartesian(uci_cell):
    """
    ex. 
        uci_cell = f8
        result = (5, 0)
    """
    return  (8 - int(uci_cell[1]), UCI_CELL_TO_CART[uci_cell[0]])

def board_to_matrix(board):
    """
    return type numpy arraylike
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
    """
    returns a matrix rotated about the horizontal plane
    also inverts the peice designation between white and black
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