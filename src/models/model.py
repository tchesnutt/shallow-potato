import tensorflow as tf


class Model:
    def __init__(self, config):
        self.config = config
        self.init_saver()
        
    def construct(self):
        raise NotImplementedError
    
    def save(self, session):
        print('Saving model...')
        self.saver.sav(session, self.config.path)
        

    def init_saver(self):
        self.saver = tf.train.Saver(max_to_keep=self.config.max_to_keep)

    