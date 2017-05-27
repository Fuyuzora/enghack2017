# Created by Yuchen on 5/27/17.
import numpy as np
from matplotlib import pyplot as plt
import math


def softmax(w, t=1.0):
    e = np.exp(np.array(w) / t)
    dist = e / np.sum(e)
    return dist

def inverse_log(x):
    x = np.array(x)
    return 1/np.log(x)

def plot(x,y):
    plt.plot(x,y)
    plt.show()

def arctan(x):
    return np.arctan(x)

def score_func(x):
    x = np.array(x)
    return 2*np.arctan(x / 6.652146493630526)/math.pi

if __name__ == '__main__':
    print(softmax([-1,1,2,3,-5]))
    x = list(range(-100,100))
    # plot(x, inverse_log(x))
    plot(x, score_func(x))
    print(0.5*score_func(-32))
