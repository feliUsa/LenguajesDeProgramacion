import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def addMatrix(a, b):
    return np.add(a, b)

def multiplyMatrix(a, b):
    return np.dot(a, b)

def transposeMatrix(a):
    return np.transpose(a)

def inverseMatrix(a):
    return np.linalg.inv(a)

def plotLine(x, y):
    plt.plot(x, y)
    plt.show()

def plotBar(categories, values):
    plt.bar(categories, values)
    plt.show()

def plotHistogram(data):
    plt.hist(data)
    plt.show()

def plotScatter3D(x, y, z):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z)
    plt.show()
