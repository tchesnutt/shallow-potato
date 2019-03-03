import chess.pgn


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

UCI_CELL_TO_CART= {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
    'f': 5,
    'g': 6,
    'h': 7,
}


# parses games from a pgn file and returns a list of games


def parse_games(file_name):
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
        result = [5, 0]
    """
    return  [8 - int(uci_cell[1]), UCI_CELL_TO_CART[uci_cell[0]]]