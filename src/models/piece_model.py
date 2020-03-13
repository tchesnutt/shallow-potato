import numpy as np
import tensorflow as tf

from models.model import Model


class Piece(Model):
    def __init__(self, config):
        super(Piece, self).__init__(config)
        self.construct()



    def construct(self):
        model = tf.keras.Sequential()
        model.add(tf.keras.layers.Conv2D(64, (3, 3), strides=1,  activation='relu', input_shape=(8, 8, 6), padding="same", data_format="channels_last", use_bias=False))
        model.add(tf.keras.layers.MaxPooling2D((1,1)))
        model.add(tf.keras.layers.Flatten())
        model.add(tf.keras.layers.Dense(64, activation='softmax'))
        model.summary()
        self.model = model



    def save(self):
        print('Saving model...')
        path = self.config.save_path + self.config.exp_name
        self.model.save(path)
