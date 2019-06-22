import tensorflow as tf


class Train:
    def __init__(self, model, config):
        self.model = model
        self.data = None
        self.config = config

    def train(self):
        raise NotImplementedError

    def train_step(self):
        raise NotImplementedError
