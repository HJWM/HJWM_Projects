# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 14:56:18 2018

@author: zhe

E-mail：1194585271@qq.com
"""
import numpy as np
import matplotlib.pyplot as plt

def loadDataSet(fileName):
    dataMat = []; labelMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr = line.strip().split('\t')     #delete ' ',\n  split with '\t'
        dataMat.append([float(lineArr[0]), float(lineArr[1])])
        labelMat.append(float(lineArr[2]))
    return dataMat,labelMat

"""
训练模型
b:bias
eta:learning rate
"""
def trainModel(dataMatIn,labelMatIn,eta):
    dataMat = np.mat(dataMatIn); labelMat = np.mat(labelMatIn).transpose()
    b = 0; m,n = np.shape(dataMat)
    alpha = np.mat(np.zeros((m,1)))
    flag = True
    while flag:
        for i in range(m):
            if  labelMatIn[i]*(float(np.multiply(alpha,labelMat).T*(dataMat*dataMat[i,:].T)) + b)<= 0:
                alpha[i] = alpha[i] + eta 
                b = b + eta * labelMat[i]
                w = np.multiply(labelMat,alpha).T*dataMat
                print (i,alpha[i],w,b)
                flag = True
                break
            else:
                flag = False
    w = (np.multiply(labelMat,alpha).T*dataMat).T
    return w,b
    
# 可视化展示分类结果
def drawing(dataArr,labelArr,weight,b):
    n = np.shape(labelArr)[0] 
    xcord1 = []; ycord1 = []   
    xcord2 = []; ycord2 = []
    for i in range(n):
        if int(labelArr[i])== 1:
            xcord1.append(dataArr[i][0])
            ycord1.append(dataArr[i][1])
        else:
            xcord2.append(dataArr[i][0])
            ycord2.append(dataArr[i][1]) 
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1, ycord1, s=40, c='yellow', marker='s',label='class 1')
    ax.scatter(xcord2, ycord2, s=40, c='green',label='class -1')	

    ax.legend(loc='best')

#    x = np.arange(0, 3, 0.5)      #例2_1
    x = np.arange(4.5, 5.25, 0.1)
    y = ((-weight[0]/weight[1])*x-b/weight[1]).T
    
    ax.plot(x, y,'-')
    plt.xlabel('X1'); plt.ylabel('X2');
    plt.savefig('PerceptronDuality.eps',dpi=2000)
    plt.show()
    
    
if __name__ == "__main__":
    dataMatIn, labelMatIn = loadDataSet('testSet.txt')
    weight,bias = trainModel(dataMatIn,labelMatIn,1)
    drawing(dataMatIn, labelMatIn, weight, bias)