import numpy as np
from sklearn import datasets
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, Activation


def binary_step_function(x):
    if x >= 0:
        return 1
    else:
        return 0


def ffnn(X):
    hide3 = wh1 * input[0][0] + wh2 * input[1][0]
    hide4 = wh4 * input[0][0] + wh3 * input[1][0]
    hide3 = binary_step_function(hide3)
    hide4 = binary_step_function(hide4)
    output5 = wh1 * input[0][0] + wh2 * input[1][0]
    output5 = wh5 * hide3 + wh6 * hide4
    output6 = wh7 * hide3 + wh8 * hide4
    output5 = binary_step_function(output5)
    output6 = binary_step_function(output6)
    print(output5)
    print(output6)


def relu(x):
    return x * (x > 0)


def ffnn_relu(X):
    hide3 = wh1 * input[0][0] + wh2 * input[1][0]
    hide4 = wh4 * input[0][0] + wh3 * input[1][0]
    hide3 = relu(hide3)
    hide4 = relu(hide4)
    output5 = wh1 * input[0][0] + wh2 * input[1][0]
    output5 = wh5 * hide3 + wh6 * hide4
    output6 = wh7 * hide3 + wh8 * hide4
    output5 = relu(output5)
    output6 = relu(output6)

    print(output5)
    print(output6)


def ffnn2(X):
    hide3 = wh1 * input[0][0] + wh2 * input[1][0]
    hide4 = wh4 * input[0][0] + wh3 * input[1][0]
    hide3 = binary_step_function(hide3)
    hide4 = binary_step_function(hide4)
    output5 = wh1 * input[0][0] + wh2 * input[1][0]
    output5 = wh5 * hide3 + wh6 * hide4
    output6 = wh7 * hide3 + wh8 * hide4
    output5 = binary_step_function(output5)
    output6 = binary_step_function(output6)

    output7 = wh9 * output5 + wh10 * output6
    output8 = wh11 * output5 + wh12 * output6
    output7 = binary_step_function(output7)
    output8 = binary_step_function(output8)
    print(output7)
    print(output8)


if __name__ == '__main__':
    x = np.array([[0, 0], [1, 0], [0, 1], [1, 1]])

    input = np.array([[0], [1]])

    wh1 = -2
    wh2 = 3
    wh3 = 4
    wh4 = -1
    wh5 = 1
    wh6 = -1
    wh7 = -1
    wh8 = 1

    input = np.array([[0], [1]])

    wh1 = -2
    wh2 = 3
    wh3 = 4
    wh4 = -1
    wh5 = 1
    wh6 = -1
    wh7 = -1
    wh8 = 1

    print("Output(5,6) -> Binary step function:")
    ffnn(input)

    input = np.array([[0], [1]])

    wh1 = -2
    wh2 = 3
    wh3 = 4
    wh4 = -1
    wh5 = 1
    wh6 = -1
    wh7 = -1
    wh8 = 1
    wh9 = 1
    wh10 = -1
    wh11 = 1
    wh12 = -1

    print("Output(7,8) -> (Addition of a hidden layer):")
    ffnn2(input)

    input = np.array([[0], [1]])

    wh1 = -2
    wh2 = 3
    wh3 = 4
    wh4 = -1
    wh5 = 1
    wh6 = -1
    wh7 = -1
    wh8 = 1

    print("Output(5,6) -> (Relu function):")
    ffnn_relu(input)
