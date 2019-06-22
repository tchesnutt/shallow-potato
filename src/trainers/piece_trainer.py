import tensorflow as tf

from trainers.train import Train

class PieceTrainer(Train):
    def __init__(self, model, config):
        super(PieceTrainer, self).__init__(model, config)
        self.data = None
    
    def train(self):
        pass
        # train_x, train_y = self.data
        # feed_dict = {self.model.x: train_x, self.model.y: train_y, self.model.is_training: True}
        # _, loss, acc = self.sess.run([self.model.train_step, self.model.cross_entropy, self.model.accuracy, feed_dict=feed_dict])