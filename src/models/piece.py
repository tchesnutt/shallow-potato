import numpy as np
import tensorflow as tf

from model import Model



class Piece(Model):
    def __init__(self, config):
        super(Piece, self).__init__(config)
        self.construct()
        self.init_saver()

    def construct(self):
        # Shape [batch, in_depth, in_height, in_width, in_channels]
        input_layer = tf.placeholder(int, [-1, 6, 8, 8, 1])

        conv1 = tf.layers.conv2d(
            inputs=input_layer,
            filters=96,
            kernel_size=[3],
            strides=1,
            padding="same",
            activation=tf.nn.relu,
        )

        conv2 = tf.layers.conv2d(
            inputs=conv1,
            filters=256,
            kernel_size=[3],
            strides=1,
            padding="same",
            activation=tf.nn.relu,
        )

        conv3 = tf.layers.conv2d(
            inputs=conv2,
            filters=384,
            kernel_size=[3],
            strides=1,
            padding="same",
            activation=tf.nn.relu,
        )

        affine = tf.contrib.layers.fully_connected(
            inputs=conv3,
            num_outputs=64,
            activation_fn=None,
        )

        self.probs = tf.nn.softmax(
            affine,
            axis=1,
        )