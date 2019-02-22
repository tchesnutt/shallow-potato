import chess.pgn
import numpy as np


# parses games from a pgn file and returns a list of games
def parse_games(file_name):
    pgn_file = open(file_name, encoding='utf-8', errors='replace')
    game = chess.pgn.read_game(pgn_file)
    game_list = []
    while game:
        game_list.append(game)
        game = chess.pgn.read_game(pgn_file)
    return game_list

