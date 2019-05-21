import tensorflow as tf


model_key = {
    'pawn': 'piece',
    'knight': 'piece',
    'bishop': 'piece',
    'rook': 'piece',
    'queen': 'piece.',
    'king': 'piece',
    'picker': 'file_name'
}

config = {

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
        trainer = getattr(module, v + "_trainer")
        trainers[k] = trainer
    return trainers



if __name__ == "__main__":
    models = initModels(model_key)
    trainers = initTrainers(model_key)

    data = {}

    for model_name, model_instance in models:
        # Read in data for model

        # init model and trainer
        sess = tf.Session()
        model = model_instance(config)
        trainer = trainers[model_name](model, data, config)
        
        trainer.train()
        model.save()