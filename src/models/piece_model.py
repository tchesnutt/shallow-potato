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
        model.add(tf.keras.layers.Conv2D(64, (3, 3), strides=1,  activation='relu', input_shape=(6, 8, 8), padding="same", data_format="channels_first", use_bias=False))
        model.add(tf.keras.layers.MaxPooling2D((1,1)))
        model.add(tf.keras.layers.Flatten())
        model.add(tf.keras.layers.Dense(64, activation='softmax'))
        model.summary()
        self.model = model



    def init_saver(self):
        return NotImplemented



    def save(self, sess):
        print('Saving model...')
        self.model.save()
