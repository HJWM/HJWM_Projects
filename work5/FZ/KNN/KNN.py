# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 11:07:20 2018

@author: zhe

E-mail: 1194585271@qq.com
"""

import numpy as np
import operator
import pandas as pd
import time 
import matplotlib.pyplot as plt



def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]   #training sample
    diffMat = np.tile(inX, (dataSetSize,1)) - dataSet   #difference
    sqDiffMat = diffMat**2   #square
    sqDistances = sqDiffMat.sum(axis=1)   #axis=1 row; 0 column
    distances = sqDistances**0.5   #root
    sortedDistIndicies = distances.argsort()   #sort to get index       
    classCount={}          
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1  # value default 0
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True) #iterator,Specified sort field,Descending order
    return sortedClassCount[0][0]

def trainDataProcess(file1,file2):
    df = pd.read_csv(file1)
    df1 = pd.read_csv(file2)
    dataTest = np.array(df1)
    data = np.array(df)
    labels = data[:,0]
    dataTrain = data[:,1:]
    return dataTest,dataTrain,labels

if __name__=="__main__":
    start=time.clock()
    dataTest,dataTrain,labels= trainDataProcess('train.csv','test.csv')
    
    
    row = 7
    print (dataTest[row])
    plt.imshow(dataTest[row].reshape(28, 28))
    plt.show()
    
    result = []
    for i in range(len(dataTest)):
        print(i,"/",len(dataTest))
        result.append(classify0(dataTest[i],dataTrain,labels,6))
        
    end=time.clock()
    total_time=end-start
    
    df = pd.DataFrame(result)
    df.columns = ['Label']
    df['ImageId']=[i+1 for i in range(len(df))]
    df = df[['ImageId','Label']]
    df.to_csv('result_k=6.csv',index=False)
    print("Time For Run HandwritingRecognizationWithKNN_k=6:"+str(total_time))
#    
#Time For Run HandwritingRecognizationWithKNN_k=2:12488.27681482169 FZ_201
#Time For Run HandwritingRecognizationWithKNN_k=3:11999.86497525453 FZ_201     
#Time For Run HandwritingRecognizationWithKNN_k=4:17755.39816159673 FZ
#Time For Run HandwritingRecognizationWithKNN_k=5:12192.99400288247 FZ_201
#Time For Run HandwritingRecognizationWithKNN_k=6:16501.60844552612 FZ
#Time For Run HandwritingRecognizationWithKNN_k=8:12505.81551002438 FZ_201