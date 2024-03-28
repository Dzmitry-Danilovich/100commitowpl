import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def study(array, answer):

    np.set_printoptions(threshold=np.inf)
    np.set_printoptions(suppress=True)
    W1 = np.random.uniform(-1, 1, [128, 156816])
    W2 = np.random.uniform(-1, 1, [10, 128])

    sum1 = np.dot(W1, array)
    out1 = np.array([sigmoid(i) for i in sum1])

    sum2 = np.dot(W2, out1)
    out2 = np.array([sigmoid(i) for i in sum2])

    print(out2)
