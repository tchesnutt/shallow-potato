import tensorflow as tf
import numpy as np

from trainers.train import Train

class PieceTrainer(Train):
    def __init__(self, sess, model, config):
        super(PieceTrainer, self).__init__(model, config)
        self.sess = sess

    
    def prep_train(self):
        print(self.model.model)
        self.model.model.compile(loss='mean_squared_error', optimizer='sgd')


    def train(self, data):
        x, y = data
        x = np.array(x)
        x = np.expand_dims(x, axis=1)
        y = np.array(y)
        
        train_dataset = tf.data.Dataset.from_tensor_slices((x, y))

        self.model.model.fit(train_dataset)


    def train_step(self, data):
        
        return