import os
import pickle
import json

from train_data import *
from validate_data import *
from utils import *

"""
Generating data
	Read a file in
		split those file's games into training and validation games (consistently the same way)
		read those games into TrainData and ValidateData instances
		append those results onto master np arrays
		
		every three files pickle out master np arrays and clear
"""


percentage = input(
    'Enter what percent of data to use for validation.\nHit ENTER to default to 20\n')
if percentage == "":
    percentage = "20"

file_count = 0
num_g = 0
train_file_len = {}
valid_file_len = {}

for file_name in os.listdir("./data/games"):
    if file_name.endswith(".pgn"):
        train_games = []
        validate_games = []

        print('Parsing: ' + file_name)
        games = parse_games("./data/games/" + file_name)
        num_g += len(games)
        print(str(num_g) + " games parsed")
        j = 100 / int(percentage)

        for g_i, game in enumerate(games):
            if g_i % j == 0:
                validate_games.append(game)
            else:
                train_games.append(game)

        trainer = TrainData(train_games)
        validator = TrainData(validate_games)

        trainer.process()
        validator.process()

        for file_type in TRAIN_FILE_TYPES:
            file_name = f"{file_type}_{file_count}"
            call = f"trainer.{file_type}"

            print("Saving train file: " + file_name)
            sample_list = eval(call)
            sample_len = len(sample_list)
            train_file_len[file_name] = sample_len
            training_file = open("./data/parsed/train/" + file_name, 'wb')
            pickle.dump(sample_list, training_file)
            training_file.close()


            validation_name = f"{file_type}_{file_count}"
            call = f"validator.{file_type}"

            print("Saving valid file: " + validation_name)
            sample_list = eval(call)            
            sample_len = len(sample_list)
            valid_file_len[validation_name] = sample_len
            validation_file = open("./data/parsed/validation/" + validation_name, 'wb')
            pickle.dump(sample_list, validation_file)
            validation_file.close()

        file_count += 1

with open('./data/parsed/train/train_file_len.json', "w") as t_fp:
    json.dump(train_file_len, t_fp)

with open('./data/parsed/validation/valid_file_len.json', "w") as v_fp:
    json.dump(valid_file_len, v_fp)