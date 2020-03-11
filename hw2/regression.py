import numpy as np
import math

def regression(x,y):
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    beta_numerator = float(np.transpose(x).dot(y)) - x.size*x_mean*y_mean
    beta_denumerator = np.transpose(x).dot(x) - x.size*x_mean*x_mean
    beta = beta_numerator/beta_denumerator
    e = y_mean - beta*x_mean

    y_pred = beta*x + e

    std_squared_error = np.sum(np.square(y_pred-y)) / ((x.size-2)*np.sum(np.square(x - x_mean)))
    standard_error = math.sqrt(std_squared_error)

    (low_bound,up_bound) = (beta - 1.96*standard_error, beta + 1.96*standard_error)

    return beta, e, standard_error, low_bound, up_bound




