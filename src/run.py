import os
import pickle
import tensorflow as tf


model_key = {
    'P': 'piece',
    'N': 'piece',
    'B': 'piece',
    'R': 'piece',
    'Q': 'piece.',
    'K': 'piece',
    'picker': 'file_name'
}

config = {
    path: "_"
}

def initModels(model_key):
    models = {}
    for k, v in model_key:
        module = __import__(v + ".py")
        model = getattr(module, v)
        models[k] = model
    return models

def initTrainers(model_key):
    trainers = {}
    for k, v in model_key: 
        module = __import__(v + "_trainer.py")
        trainer = getattr(module, v + "Trainer")
        trainers[k] = trainer
    return trainers

def getDataFile(model_name):
    files = []
    for file_name in os.listdir("./data/parsed"):
        if file_name.startswith(model_name):
            files.append("./data/parsed" + file_name)
    return files

def loadDataFile(file_name):
    file = open(file_name)
    return pickle.load(file)


if __name__ == "__main__":
    models = initModels(model_key)
    trainers = initTrainers(model_key)

    for model_name, model_instance in models:
        files = getDataFile(model_name)

        # init model and trainer
        sess = tf.Session()
        model = model_instance(config)
        trainer = trainers[model_name](model, config)

        for file in files:
            trainer.data = loadDataFile(file)
            trainer.train()
            
        model.save()