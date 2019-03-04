import os
from utils import *



percentage = input('Enter what percent of data to use for validation.\nHit ENTER to default to 20\n')
if percentage == "":
	percentage = "20"


train_games = []
validate_games = []

for file_name in os.listdir("./data/openings"):
	if file_name.endswith(".pgn"):
		print('Parsing: ' + file_name)
		games = parse_games("./data/openings/" + file_name)
		num_g = len(games)
		print(str(num_g) + " games parsed")
		j = 100 / int(percentage)
		
		for g_i, game in enumerate(games):
			if g_i % j == 0:
				validate_games.append(game)
			else:
				train_games.append(game)