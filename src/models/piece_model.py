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
        model.add(tf.keras.layers.Conv2D(96, (3, 3), activation='relu', input_shape=(6, 8, 8), padding="same"))
        model.add(tf.keras.layers.Conv2D(256, (3, 3), activation='relu', input_shape=(6, 8, 8), padding="same"))
        model.add(tf.keras.layers.Conv2D(384, (3, 3), activation='relu', input_shape=(6, 8, 8), padding="same"))
        model.add(tf.keras.layers.Dense(32, activation=None))

        model.summary()

    def construct_old(self):
        # Shape [batch, in_depth, in_height, in_width, in_channels]
        self.x = tf.compat.v1.placeholder(tf.float16, [1, 6, 8, 8])
        self.y = tf.compat.v1.placeholder(tf.float16, [1, 6, 8, 64])

        conv1 = tf.compat.v1.layers.conv2d(
            inputs=self.x,
            filters=96,
            kernel_size=[3,3],
            strides=1,
            padding="same",
            activation=tf.nn.relu,
        )

        conv2 = tf.compat.v1.layers.conv2d(
            inputs=conv1,
            filters=256,
            kernel_size=[3,3],
            strides=1,
            padding="same",
            activation=tf.nn.relu,
        )

        conv3 = tf.compat.v1.layers.conv2d(
            inputs=conv2,
            filters=384,
            kernel_size=[3,3],
            strides=1,
            padding="same",
            activation=tf.nn.relu,
        )

        # TODO find replacement for this layer
        affine = tf.contrib.layers.fully_connected(
            inputs=conv3,
            num_outputs=64,
            activation_fn=None,
        )

        self.probs = tf.nn.softmax(
            affine,
            axis=1,
        )

        with tf.compat.v1.name_scope("loss"):
            self.cross_entropy = tf.reduce_mean(input_tensor=tf.nn.softmax_cross_entropy_with_logits(labels=tf.stop_gradient(self.y), logits = self.probs))
            correct_prediction = tf.equal(tf.argmax(input=self.probs,axis=1), tf.argmax(input=self.y, axis=1))
            self.accuracy = tf.reduce_mean(input_tensor=tf.cast(correct_prediction, tf.float16))


    def init_saver(self):
        self.saver = tf.compat.v1.train.Saver(max_to_keep=self.config.max_to_keep)

    def save(self, sess):
        # TODO: put model name in here
        print('Saving model...')
        self.saver.save(sess, self.config.path)
