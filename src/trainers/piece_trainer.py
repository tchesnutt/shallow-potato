import tensorflow as tf

from train import Train

class PieceTrainer(Train):
    def __init__(self, model, data, config):
        super(PieceTrainer, self).__init__(model, data, config)
    