import json
import tensorflow as tf


class Train:
    __slots__ = ['model', 'config']
    def __init__(self, model, config):
        self.model = model
        self.config = config



    def train(self):
        raise NotImplementedError



    def train_step(self):
        raise NotImplementedError



    def get_num_samples_file_pairs(self, file_pairs, path):
        with open(path) as json_len_file:
            file_len = json.load(json_len_file)
            samples = 0
            for pair in file_pairs:
                x, y = pair
                x = x.split("/")[-1]
                samples += file_len[x]
            
        return samples
                