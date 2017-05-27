# Created by Yuchen on 5/27/17.
import numpy as np


def softmax(w, t=1.0):
    e = np.exp(np.array(w) / t)
    dist = e / np.sum(e)
    return dist

if __name__ == '__main__':
    print(softmax([-1,1,2,3,-5]))
