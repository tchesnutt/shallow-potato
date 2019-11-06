import tensorflow as tf


class Train:
    def __init__(self, model, config):
        self.model = model
        self.data = None
        self.config = config
        self.init = tf.group(tf.compat.v1.global_variables_initializer(), tf.compat.v1.local_variables_initializer())

    def train(self):
        raise NotImplementedError

    def train_step(self):
        raise NotImplementedError
