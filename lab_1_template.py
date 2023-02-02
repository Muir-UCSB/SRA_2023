import numpy as np
import pylab as pl
import matplotlib.ticker as ticker
from lab_1_functions import *
import os


def get_f_gradient(point, delta):
    '''
    Gets gradient of f at a point
    :param point: (float) point at which to calculate the gradient

    :return gradient:
    '''
    f_gradient = (f(point+delta)-f(point))/delta
    return f_gradient


if __name__ == "__main__":
    '''
    Initial parameters
    '''
    lower_bound = -6
    upper_bound = 6
    delta = .1
    alpha = .001
    num_iterations = 1000

    x0 = np.random.uniform(low = lower_bound, high = upper_bound) # NOTE: initial guess
    update = [x0] # NOTE:  holds updated values, including the initial guess

    '''
    Optimization loop
    '''
    for i in range(num_iterations):
        grad = get_f_gradient(update[i], delta) # NOTE: calculates gradient of f at point x_i
        new_guess = update[i]-alpha*grad # NOTE: calculates the update
        update.append(new_guess)




    print(np.min(f(t)))
