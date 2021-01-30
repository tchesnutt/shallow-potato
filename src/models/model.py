class Model:
    __slots__ = ["config", "model"]

    def __init__(self, config):
        self.config = config

    def construct(self):
        raise NotImplementedError

    def init_saver(self):
        raise NotImplementedError

    def save(self):
        raise NotImplementedError
