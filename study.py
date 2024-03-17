import numpy as np

def study(array, answer):

    W1 = np.random.rand(len(array), len(array[0])) * 2 - 1
    W1_rounded = np.round(W1, 4)

    print(W1_rounded)
