'''
Class for loading and manipulating chess games in PGN format
'''

import chess


class gameLib:
    '''
    A container for storing multiple chess games in PGN format from file.

    Games are stored in chess.pgn.Game objects.
    '''
    def __init__(file = None):
        games = []
        if file:
            self.parse_file(file)

    def parse_file(file_path):
        '''
        Read in a PGN file at 'file_path' and add each game to 'games' list.
        '''
        with open(file_path) as pgn:
            while pgn:
                self.games.append(chess.pgn.read_game(pgn))

