import tensorflow as tf
import numpy as np

from trainers.train import Train
from utils import coord_to_prob_dist



class PieceTrainer(Train):
    def __init__(self, sess, model, config):
        super(PieceTrainer, self).__init__(model, config)
        self.sess = sess
        self.layer = 0

    
    def prep_train(self):
        print(self.model.model)
        self.model.model.compile(loss='mean_squared_error', optimizer='sgd')


    def train(self, data):
        x, y_coord = data
        
        x = np.array(x)
        x = np.expand_dims(x, axis=1)

        y = []
        for i in y_coord:
            y.append(coord_to_prob_dist(i, self.layer))
        y = np.array(y)
        
        train_dataset = tf.data.Dataset.from_tensor_slices((x, y))

        self.model.model.fit(train_dataset)


    def train_step(self, data):
        
        return