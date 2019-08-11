import tensorflow as tf

from trainers.train import Train

class PieceTrainer(Train):
    def __init__(self, sess, model, config):
        super(PieceTrainer, self).__init__(model, config)
        self.sess = sess

    
    def train(self, data):
        train_x, train_y = data
        feed_dict = {self.model.x: train_x, self.model.y: train_y}
        _, loss, acc = self.sess.run([self.model.config.train_step, self.model.cross_entropy, self.model.accuracy], 
                                      feed_dict=feed_dict)
        return loss, acc