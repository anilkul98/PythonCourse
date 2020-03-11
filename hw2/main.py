import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from regression import regression
from testInput import handleInput


def plot(x,y,beta,e):
    y_pred = lambda x: x*beta + e
    x_points_on_line = [i for i in range(int(np.min(x)), int(np.max(x)), 5000)]
    y_points_on_line = [y_pred(x) for x in x_points_on_line]
    plt.plot(x,y,'bo', color = 'b')
    plt.plot(x_points_on_line, y_points_on_line, color='black')
    plt.xlabel("GDP Per Capita ($)")
    plt.ylabel("Corruption Perception Index (CPI)")
    plt.title("2015 GDP Per Capita vs Corruption Perception Index")
    plt.show()


data = np.genfromtxt('data.csv', delimiter=",", skip_header=True)
data = handleInput(data)
x = data[:,0]
y = data[:,1]

beta, e, standard_error, low_bound, up_bound = regression(x,y)
plot(x, y, beta, e)
