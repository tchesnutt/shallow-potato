import tensorflow as tf


class Model:
    def __init__(self, config):
        self.config = config
        self.init_saver()
        
    def construct(self):
        raise NotImplementedError
    
    def save(self, sess):
        print('Saving model...')
        self.saver.sav(sess, self.config.path)
        

    def init_saver(self):
        self.saver = tf.train.Saver(max_to_keep=self.config.max_to_keep)

    