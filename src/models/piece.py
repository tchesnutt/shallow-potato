import numpy as np
import tensorflow as tf

from model import Model

class Piece(Model):
    def __init__(self, config):
        super(Piece, self).__init__(config)
        self.construct()
        self.init_saver()

    def construct():
        # Shape [batch, in_depth, in_height, in_width, in_channels]
        input_layer = tf.placeholder(int, [-1, 6, 8, 8, 1])

        conv1 = tf.layers.conv2d(
            input=input_layer,
            filter=96,
            kernel_size=[3],
            strides=1,
            padding="same",
            activation=tf.nn.relu,
        )

        conv2 = tf.layers.conv2d(
            input=conv1,
            filter=256,
            kernel_size=[3],
            strides=1,
            padding="same",
            activation=tf.nn.relu,
        )

        conv3 = tf.layers.conv2d(
            input=conv2,
            filter=384,
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

        softmax = tf.nn.softmax(
            affine,
            axis=1,
        )