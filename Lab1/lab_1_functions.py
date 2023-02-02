import numpy as np

def f(x):
    '''
    :param x: (array-like) function inputs

    :return value: (float) function evaluation at x
    '''
    return np.exp(-.65987596/2*x)*np.cos(x*np.sqrt(1-np.power(.65987596*.5, 2)))




def g(x):
    '''
    :param x: (array-like) function inputs

    :return value: (float) function evaluation at x
    '''
    return 20*np.sin(x)+np.power(x, 2)


def h(x):
    '''
    :param x: (array-like) function inputs

    :return value: (float) function evaluation at x
    '''
    return np.sin(x)
