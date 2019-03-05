import os
import pickle

from train_data import *
from valid_data import *
from utils import *

"""
Generating data
	Read a file in
		split those file's games into training and validation games (consistently the same way)
		read those games into TrainData and ValidateData instances
		append those results onto master np arrays
		
		every three files pickle out master np arrays and clear
"""


percentage = input('Enter what percent of data to use for validation.\nHit ENTER to default to 20\n')
if percentage == "":
	percentage = "20"


file_count = 0
num_g = 0

x_train, y_train = [], []
x_e, y_e = [], []
x_K, y_K = [], []
x_B, y_B = [], []
x_R, y_R = [], []
x_Q, y_Q = [], []
x_N, y_N = [], []

train_file_types = ['train', 'e', 'K', 'B', 'R', 'Q', 'N']


for file_name in os.listdir("./data/openings"):
	if file_name.endswith(".pgn"):
		train_games = []
		validate_games = []

		print('Parsing: ' + file_name)
		games = parse_games("./data/openings/" + file_name)
		num_g += len(games)
		print(str(num_g) + " games parsed")
		j = 100 / int(percentage)
		
		for g_i, game in enumerate(games):
			if g_i % j == 0:
				validate_games.append(game)
			else:
				train_games.append(game)
		
		if file_count % 3 == 0:
			trainer = TrainData(train_games)
			validator = ValidatData(validate_games)
			
			trainer.process()
			validator.process()



			# print("Saving training data")
			# training_file = open("training_data%d" % (file_count / 3), 'wb')
			# pickle.dump(train_games, training_file)
			# training_file.close()
			
			# print("Saving validation data")
			# validation_file = open("validation_data%d" % (file_count / 3), 'wb')
			# pickle.dump(validate_games, validation_file)
			# validation_file.close()

			train_games, validate_games = [], []
		file_count += 1