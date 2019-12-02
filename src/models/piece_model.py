import numpy as np
import tensorflow as tf

from models.model import Model


class Piece(Model):
    def __init__(self, config):
        super(Piece, self).__init__(config)
        self.construct()
        self.init_saver()


    def construct(self):
        model = tf.keras.Sequential()
        model.add(tf.keras.layers.Conv2D(96, (3, 3), strides=1,  activation='relu', input_shape=(6, 8, 8), padding="same", data_format="channels_first" ))
        model.add(tf.keras.layers.Dense(256, activation=None))
        model.add(tf.keras.layers.Dense(8, activation='softmax'))
        model.summary()
        self.model = model


    def init_saver(self):
        return NotImplemented
        # self.saver = tf.compat.v1.train.Saver(max_to_keep=self.config.max_to_keep)

    def save(self, sess):
        # TODO: put model name in here
        print('Saving model...')
        # self.saver.save(sess, self.config.path)
