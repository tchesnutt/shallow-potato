import tensorflow as tf
import numpy as np

from trainers.train import Train
from utils import load_data_file, flatten_coord_to_target_array, TRAIN_FILE_LEN_PATH, VALID_FILE_LEN_PATH



class PieceTrainer(Train):
    def __init__(self, sess, model, config):
        super(PieceTrainer, self).__init__(model, config)
        self.sess = sess

    
    def prep_train(self):
        self.model.model.compile(loss='mean_squared_error', optimizer='sgd')


    def train(self, train_file_pairs, valid_file_pairs):
        train_file_pairs = list(train_file_pairs)
        valid_file_pairs = list(valid_file_pairs)
        
        train_gen = self.generate_data_from_file_pair(train_file_pairs)
        valid_gen = self.generate_data_from_file_pair(valid_file_pairs)

        train_SPE = self.get_num_samples_file_pairs(train_file_pairs, TRAIN_FILE_LEN_PATH)
        valid_SPE = self.get_num_samples_file_pairs(valid_file_pairs, VALID_FILE_LEN_PATH)

        history = self.model.model.fit_generator(
            train_gen,
            epochs=1,
            steps_per_epoch=train_SPE,
            validation_data=valid_gen,
            validation_steps=valid_SPE)

        print(history)


    def generate_data_from_file_pair(self, file_pairs):
        counter = 0
        while True:
            file_pair = file_pairs[counter]
            counter = (counter + 1) % len(file_pairs)

            x, y_flat = (load_data_file(file_pair[0]), load_data_file(file_pair[1]))
            y = flatten_coord_to_target_array(y_flat)

            # TODO: investigate having to np.array the inputs. This feels strange.
            x = np.asarray(x)
            y = np.asarray(y)

            yield (x, y)