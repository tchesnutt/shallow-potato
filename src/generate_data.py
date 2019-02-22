from utils import *

path = "./games/magnus.pgn"

game_list = parse_games(path)


for game in game_list:
    # do stuff