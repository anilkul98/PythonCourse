import numpy as np

def handleInput(data):
    data = data[~np.isnan(data).any(axis=1)]
    return data