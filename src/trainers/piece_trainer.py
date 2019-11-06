import tensorflow as tf
import numpy as np

from trainers.train import Train

class PieceTrainer(Train):
    def __init__(self, sess, model, config):
        super(PieceTrainer, self).__init__(model, config)
        self.sess = sess

    
    def train(self, data):
        x, train_y = data
        print("hi")
        x = np.array(x)
        print(type(x))
        print(x.shape)
        
        
        

        
        train_x = tf.data.Dataset.from_tensor_slices(x.ravel())
        print(type(train_x))
        print(train_x)


        itr = tf.compat.v1.data.make_initializable_iterator(train_x)
        el = itr.get_next()


        feed_dict = { self.model.x: train_x, self.model.y: train_y }
        _, loss, acc = self.sess.run(itr.initializer, [self.model.config.train_step, self.model.cross_entropy, self.model.accuracy])
        return loss, acc