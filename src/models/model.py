import tensorflow as tf


class Model:
    def __init__(self, config):
        self.config = config

    def construct(self):
        raise NotImplementedError        

    def init_saver(self):
        raise NotImplementedError

    