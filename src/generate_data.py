import os
import pickle
import json
import time
import itertools
import gc
from multiprocessing.dummy import Pool as tp

from train_data import *
from validate_data import *
from utils import *

"""Generating data
	Read a file in
		split those file's games into training and validation games (consistently the same way)
		read those games into TrainData and ValidateData instances
		append those results onto master np arrays
"""

def game_file_parser(file_name, percentage, train_file_len, valid_file_len, name):
    print(f"Thread {name} starting, input={file_name}")

    if file_name.endswith(".pgn"):
        train_games = []
        validate_games = []

        games = parse_games("./data/openings/" + file_name)
        count = len(games)
        print(f"Parsing: {file_name}, {count} games")

        j = 100 / int(percentage)
        for g_i, game in enumerate(games):
            if g_i % j == 0:
                validate_games.append(game)
            else:
                train_games.append(game)

        del games

        trainer = TrainData(train_games)
        validator = TrainData(validate_games)

        del train_games
        del validate_games

        trainer.process()
        validator.process()

        for file_type in TRAIN_FILE_TYPES:
            train_file_name = f"{file_type}_T_{file_name}"
            call = f"trainer.{file_type}"

            print("Saving train file: " + train_file_name)
            sample_list = eval(call)
            sample_len = len(sample_list)
            train_file_len[train_file_name] = sample_len
            training_file = open("./data/parsed/train/" + train_file_name, 'wb')
            pickle.dump(sample_list, training_file)
            training_file.close()

            validation_name = f"{file_type}_V_{file_name}"
            call = f"validator.{file_type}"

            print("Saving valid file: " + validation_name)
            sample_list = eval(call)            
            sample_len = len(sample_list)
            valid_file_len[validation_name] = sample_len
            validation_file = open("./data/parsed/validation/" + validation_name, 'wb')
            pickle.dump(sample_list, validation_file)
            validation_file.close()


        trainer.clear_data()
        validator.clear_data()
        del trainer
        del validator

        n = gc.collect()
        print("Number of unreachable objects collected by GC:", n)

    print(f"Thread {name} ending")


if __name__ == "__main__":
    percentage = input(
        'Enter what percent of data to use for validation.\nHit ENTER to default to 20\n')
    if percentage == "":
        percentage = "20"


    train_file_len = {}
    valid_file_len = {}
    game_files = os.listdir("./data/openings")
    pool_number = 3
    args = zip(game_files, itertools.repeat(percentage), itertools.repeat(train_file_len), itertools.repeat(valid_file_len), itertools.count(1)) 
    pool = tp(pool_number)
    start_time = time.time()
    pool.starmap(game_file_parser, args)
    print("%s seconds" % (time.time() - start_time))

    with open('./data/parsed/train/train_file_len.json', "w") as t_fp:
        json.dump(train_file_len, t_fp)

    with open('./data/parsed/validation/valid_file_len.json', "w") as v_fp:
        json.dump(valid_file_len, v_fp)