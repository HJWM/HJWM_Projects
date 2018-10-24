import sys
sys.path.append('.')
import numpy as np
import random as rand
import matplotlib.pyplot as plt
#################输出正太分布数据-不可分###################
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
##########################可分数据###################################
def generate_dataset_static():
    data = np.array([[3,3],[4,3],[1,1]],float).transpose()
    label = np.array([1,1,-1],float)
    print(data)
    print(label)
    return data,label


#################感知机 原始形式####################
def train_origin(trainData,trainLabel):
    #w 数据维数行，1列
    w = np.array([0,0],float).transpose()
    b = 0
    lrate = 1
    #--------------------------------------------
    #algorithm start herecount
    count = 1
    while :
         count = 0
         for i in range(trainData.shape[1]):
            if trainLabel[i]*(np.inner(w,trainData[:,i]) + b ) <= 0:
                w = w + lrate*trainLabel[i]*trainData[:,i]
                b = b + lrate*trainLabel[i]
                count += 1
                print("tarinLabel[%s] = "%i,trainLabel[i])
                print("w = ",w)
                print("b = ",b)

    return w,b



################感知机 对偶形式#################
##########计算Gram矩阵############
def G_matrix(trainData):
    global G
    G = np.zeros((trainData.shape[1],trainData.shape[1]))
    for i in range(trainData.shape[1]):
        for j in range(trainData.shape[1]):
            G[i][j]=np.dot(trainData[:,i],trainData[:,j])
    print(G)
    return G

##############迭代###############
def train_dual(trainData,trainLabel):
    a = np.zeros((trainData.shape[1]))
    b = 0
    w = np.zeros((trainData.shape[0])).transpose()
    lrate = 1
    global G
    G = G_matrix(trainData)
    count = 1
    while count:
        count = 0
        for i in range(trainData.shape[1]):
               tmp = 0
               for j in range (trainData.shape[1]):
                   tmp += a[j]*trainLabel[j]*G[i][j]
               tmp1 = trainLabel[i]*(tmp+b)
               if tmp1<=0:
                   a[i] += lrate
                   b += trainLabel[i]*lrate
                   count = 1
    for i in range(trainData.shape[1]):
       w += a[i]*trainData[:,i]*trainLabel[i]
    return w,b
#######对于不可分数据的感知机口袋算法###########
##得到错误值##
def Get_Err_Num(trainData,trainLabel,w,b):
    sum = 0
    for i in range (trainData.shape[1]):
        if trainLabel[i] * (np.inner(w, trainData[:, i]) + b) <= 0:
            sum += 1
    return sum
#####迭代
def pocket_alg(trainData,trainLabel,iterateMax):
    b_p = 0
    w_p = np.zeros((trainData.shape[0])).transpose()
    ErrNum_p = Get_Err_Num(trainData, trainLabel, w_p, b_p)

    b= 0
    w= np.zeros((trainData.shape[0])).transpose()
    ErrNum = 0

    lrate = 1
    iterate = 0
    dataIdx = 0

    while iterate<iterateMax:
        dataIdx = rand.randint(0,trainData.shape[1]-1)
        if trainLabel[dataIdx] * (np.inner(w, trainData[:, dataIdx]) + b) <= 0:
            iterate+=1
            w = w + lrate * trainLabel[dataIdx] * trainData[:, dataIdx]
            b = b + lrate * trainLabel[dataIdx]
            ErrNum = Get_Err_Num(trainData,trainLabel,w,b)
            if ErrNum<ErrNum_p:
                w_p = w
                b_p = b
                ErrNum_p = ErrNum
    return w_p,b_p









###########画出图像###############
def plot_data(w,b,data,label):
    eps = 0.000001
    x = np.linspace(np.min(data[0,:])-1,np.max(data[1,:])+1,100)
    y = -(b+w[0]*x)/(w[1] + eps)
    plt.plot(x,y)
    plt.plot(data[0,label==-1],data[1,label==-1],'r*')
    plt.plot(data[0,label==1],data[1,label==1],'g*')
    plt.show()
    return
##动态显示
if __name__ == "__main__":
    ##正态分布数据
    trainData, trainLabel = generate_dataset_norm(np.array([[0,0],[1,-1]]),[0.5],50)
   # train data: 数据维度行，样本个数列
    ##书上样例
   # trainData, trainLabel = generate_dataset_static()

    ##感知机 原始形式
   # w,b = train_origin(trainData, trainLabel)

    ##感知机 对偶形式
   # w,b = train_dual(trainData,trainLabel)

    ###口袋算法
    w, b = pocket_alg(trainData, trainLabel,100)
    print("w = ",w)
    print("b = ",b)
    ##画出图像
    plot_data(w,b,trainData,trainLabel)

