import numpy as np
import random as rand
import matplotlib.pyplot as plt

def generate_dataset_norm(centers,var,num):
    retData = np.zeros((num,centers.shape[1]))
    retLabel = np.zeros((num))
    print(retData.shape)
    for ii in range(0,num):
        cls = rand.randint(0,centers.shape[0]-1)
        retData[ii,:] =  np.random.normal(centers[cls,:],var)
        retLabel[ii] = cls
    retLabel[retLabel == 1] = -1
    retLabel[retLabel == 0] = 1
    return retData.transpose(),retLabel.transpose()

def generate_dataset_static():
    data = np.array([[3,3],[4,4],[1,1]],float).transpose()
    label = np.array([1,1,-1],float)
    return data,label

def plot_data(w,b,data,label):
    eps = 0.000001
    x = np.linspace(np.min(data[0,:])-1,np.max(data[1,:])+1,100)
    y = -(b+w[0]*x)/(w[1] + eps)
    plt.plot(x,y)
    plt.plot(data[0,label==-1],data[1,label==-1],'r*')
    plt.plot(data[0,label==1],data[1,label==1],'g*')
    plt.show()
    return