import os
from utils import *


game_list = []

for filename in os.listdir("./data/openings"):
    if filename.endswith(".pgn"):
        game_list.append(parse_games(path))


for game in game_list:
    # do stuff