import pickle
def savePickle(obj, filepath):
    with open(filepath, 'wb') as handle:
        pickle.dump(obj, handle, protocol=pickle.HIGHEST_PROTOCOL)
def loadPickle(filepath):
    with open(filepath, 'rb') as handle:
        return pickle.load(handle)
