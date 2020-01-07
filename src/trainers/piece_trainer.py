import tensorflow as tf
import numpy as np

from trainers.train import Train
from utils import flatten_coord



class PieceTrainer(Train):
    def __init__(self, sess, model, config):
        super(PieceTrainer, self).__init__(model, config)
        self.sess = sess
        self.train_data = None
        self.validation_data = None

    
    def prep_train(self):
        self.model.model.compile(loss='mean_squared_error', optimizer='sgd')


    def train(self):
        x, y = self.train_data
        
        x = np.array(x)
        x = np.expand_dims(x, axis=1)

        y = np.array(y)
        
        train_dataset = tf.data.Dataset.from_tensor_slices((x, y))

        # add validation_data arg in here
        self.model.model.fit(train_dataset)


    def train_step(self, data):
        
        return