# @Time    : 2018/10/22 5:25 PM
# @Author  : 林晓民
# @Site    : 
# @File    : perceptron.py
# @Software: PyCharm


import sys

sys.path.append('.')
import numpy as np
import random as rand
import matplotlib.pyplot as plt


def generate_dataset_norm(centers, var, num):
    retData = np.zeros((num, centers.shape[1]))
    retLabel = np.zeros((num))
    print(retData.shape)
    for ii in range(0, num):
        cls = rand.randint(0, centers.shape[0] - 1)
        retData[ii, :] = np.random.normal(centers[cls, :], var)
        retLabel[ii] = cls
    retLabel[retLabel == 1] = -1
    retLabel[retLabel == 0] = 1
    return retData.transpose(), retLabel.transpose()


def generate_dataset_static():
    data = np.array([[3, 3], [4, 4], [1, 1]], float).transpose()
    label = np.array([1, 1, -1], float)
    return data, label


def train(trainData, trainLabel):
    # w 数据维数行，1列
    w = np.array([0, 0], float).transpose()
    b = 0
    lrate = 1
    # --------------------------------------------
    # algorithm start here
    wrong_point = len(trainData[0])
    j = 0
    while wrong_point > 0:
        i = j % len(trainData[0])
        x_1 = trainData[0][i]
        x_2 = trainData[1][i]
        y = trainLabel[i]
        if y * (w[0] * x_1 + w[1] * x_2 + b) <= 0:
            w[0] = w[0] + y * x_1
            w[1] = w[1] + y * x_2
            b = b + y
            wrong_point = len(trainData[0])
        else:
            wrong_point = wrong_point - 1
        j = j + 1
    return w, b


def plot_data(w, b, data, label):
    eps = 0.000001
    x = np.linspace(np.min(data[0, :]) - 1, np.max(data[1, :]) + 1, 100)
    y = -(b + w[0] * x) / (w[1] + eps)
    plt.plot(x, y)
    plt.plot(data[0, label == -1], data[1, label == -1], 'r*')
    plt.plot(data[0, label == 1], data[1, label == 1], 'g*')
    plt.show()
    return


if __name__ == "__main__":
    trainData, trainLabel = generate_dataset_norm(np.array([[0,0],[1,-1]]),[0.1],50)
    # train data: 数据维度行，样本个数列
    # trainData, trainLabel = generate_dataset_static()
    w, b = train(trainData, trainLabel)
    plot_data(w, b, trainData, trainLabel)
