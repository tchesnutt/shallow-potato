import tensorflow as tf


class Train:
    def __init__(self, model, config):
        self.model = model
        self.data = None
        self.config = config
        self.init = tf.group(tf.global_variables_initializer(), tf.local_variables_initializer())

    def train(self):
        raise NotImplementedError

    def train_step(self):
        raise NotImplementedError
