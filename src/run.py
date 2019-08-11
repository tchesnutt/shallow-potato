import os
import pickle
import tensorflow as tf

from utils import *


model_key = {
    'P': 'piece',
    # 'N': 'piece',
    # 'B': 'piece',
    # 'R': 'piece',
    # 'Q': 'piece.',
    # 'K': 'piece',
    # 'picker': 'file_name'
}


def initModels(model_key):
    models = {}
    for k, v in model_key.items():
        module = __import__('models.'+ v + '_model', fromlist=[v + '_model'])
        model = getattr(module, v.capitalize())
        models[k] = model
    return models

def initTrainers(model_key):
    trainers = {}
    for k, v in model_key.items(): 
        module = __import__('trainers.' + v + '_trainer', fromlist=[v + '_trainer'])
        trainer = getattr(module, v.capitalize() + "Trainer")
        trainers[k] = trainer
    return trainers

def getDataFile(model_name):
    files = []
    for file_name in os.listdir("./data/parsed/"):
        if file_name.startswith(model_name):
            files.append("./data/parsed/" + file_name)
    return files

def loadDataFile(file_name):
    file = open(file_name, 'rb')
    return pickle.load(file)

def parse_fileobjs(filenames):
    parsed_files = []
    for filename in filenames:
        model, something, series = filename.split('_')
        parsed_files.append({
            "filename": filename,
            "series": series,
            "type": something,
        })
    return parsed_files

    
def sort_files(fileobj):
    return (fileobj["series"], fileobj["type"])


if __name__ == "__main__":
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

    models = initModels(model_key)
    trainers = initTrainers(model_key)

    for model_name, model_instance in models.items():
        config_file = "./src/configs/" + model_key[model_name] + ".json"
        config = process_config(config_file)
    
        files = getDataFile(model_name)

        sess = tf.Session()
        model = model_instance(config)
        trainer = trainers[model_name](sess, model, config)

        parsed_fileobjs = parse_fileobjs(files)
        sorted_files = sorted(parsed_fileobjs, key=sort_files)
        sorted_files = [file["filename"] for file in sorted_files]
        
        file_pairs = zip(sorted_files[::2], sorted_files[1::2])

        for pair in file_pairs:
            data = (loadDataFile(pair[0]), loadDataFile(pair[1]))
            trainer.train(data)
            
        model.save(sess)