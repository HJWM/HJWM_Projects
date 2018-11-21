# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 09:07:58 2018

@author: zhe

E-mail: 1194585271@qq.com
"""

import numpy as np
import pandas as pd
import time 
import matplotlib.pyplot as plt

def trainDataProcess(file1,file2):
    df = pd.read_csv(file1)
    df1 = pd.read_csv(file2)
    dataTest = np.array(df1)
    data = np.array(df)
    labels = data[:,0]
    dataTrain = data[:,1:]
    return dataTest,dataTrain,labels


def trainNB0(trainMatrix,trainCategory):
    
    numTrainDocs = len(trainMatrix) 
    numWords = len(trainMatrix[0]) 
    
    px = []
    pxVector = []
    cNum = []
    
    for i in range(10):
        px.append(0)
        cNum.append(1) #laplace smoothing                     
        pxVector.append(np.ones(numWords))  #laplace smoothing
    
    for i in range(numTrainDocs):    
        if trainCategory[i] == 0:
            cNum[0] += 1
            pxVector[0] += trainMatrix[i]
        elif trainCategory[i] == 1:
            cNum[1] += 1
            pxVector[1] += trainMatrix[i]    
        elif trainCategory[i] == 2:
            cNum[2] += 1
            pxVector[2] += trainMatrix[i]              
        elif trainCategory[i] == 3:
            cNum[3] += 1
            pxVector[3] += trainMatrix[i]              
        elif trainCategory[i] == 4:
            cNum[4] += 1
            pxVector[4] += trainMatrix[i]              
        elif trainCategory[i] == 5:
            cNum[5] += 1
            pxVector[5] += trainMatrix[i]              
        elif trainCategory[i] == 6:
            cNum[6] += 1
            pxVector[6] += trainMatrix[i]              
        elif trainCategory[i] == 7:
            cNum[7] += 1
            pxVector[7] += trainMatrix[i]              
        elif trainCategory[i] == 8:
            cNum[8] += 1
            pxVector[8] += trainMatrix[i]  
        else:
            cNum[9] += 1
            pxVector[9] += trainMatrix[i]  
            
    for i in range(10):
        px[i] = cNum[i]/(numTrainDocs+10)
        pxVector[i] = np.log(pxVector[i]/cNum[i])
        
    return px,pxVector

def trainNB_bag(trainMatrix,trainCategory):
    
    numTrainDocs = len(trainMatrix) 
    numWords = len(trainMatrix[0]) 
    
    px = []
    pxVector = []
    cNum = []
    
    pDeom = []
    
    for i in range(10):
        px.append(0)
        pDeom.append(0)
        cNum.append(1) #laplace smoothing                     
        pxVector.append(np.ones(numWords))  #laplace smoothing
    
    for i in range(numTrainDocs):    
        if trainCategory[i] == 0:
            pDeom[0]=sum(trainMatrix[i])
            cNum[0] += 1
            pxVector[0] += trainMatrix[i]
        elif trainCategory[i] == 1:
            pDeom[1]=sum(trainMatrix[i])
            cNum[1] += 1
            pxVector[1] += trainMatrix[i]    
        elif trainCategory[i] == 2:
            pDeom[2]=sum(trainMatrix[i])
            cNum[2] += 1
            pxVector[2] += trainMatrix[i]              
        elif trainCategory[i] == 3:
            pDeom[3]=sum(trainMatrix[i])
            cNum[3] += 1
            pxVector[3] += trainMatrix[i]              
        elif trainCategory[i] == 4:
            pDeom[4]=sum(trainMatrix[i])
            cNum[4] += 1
            pxVector[4] += trainMatrix[i]              
        elif trainCategory[i] == 5:
            pDeom[5]=sum(trainMatrix[i])
            cNum[5] += 1
            pxVector[5] += trainMatrix[i]              
        elif trainCategory[i] == 6:
            pDeom[6]=sum(trainMatrix[i])
            cNum[6] += 1
            pxVector[6] += trainMatrix[i]              
        elif trainCategory[i] == 7:
            pDeom[7]=sum(trainMatrix[i])
            cNum[7] += 1
            pxVector[7] += trainMatrix[i]              
        elif trainCategory[i] == 8:
            pDeom[8]=sum(trainMatrix[i])
            cNum[8] += 1
            pxVector[8] += trainMatrix[i]  
        else:
            pDeom[9]=sum(trainMatrix[i])
            cNum[9] += 1
            pxVector[9] += trainMatrix[i]  
            
    for i in range(10):
        px[i] = cNum[i]/(numTrainDocs+10)
        pxVector[i] = np.log(pxVector[i]/pDeom[i])
        
    return px,pxVector
    

def classifyNB(vec2Classify, pxVector, px):
    resultP = [0 for i in range(10)]
    
    for i in range(10):
        resultP[i] = sum(vec2Classify*pxVector[i]) + np.log(px[i])     
        
    result =  np.array(resultP)
    return result.argmax()


if __name__=="__main__":
    start=time.clock()
    dataTest,trainMatrix,trainCategory= trainDataProcess('train.csv','test.csv')
    
    px,pxVector =  trainNB0(trainMatrix,trainCategory)
    
    print (classifyNB(dataTest[0], pxVector, px))
        
    row = 0
    plt.imshow(dataTest[row].reshape(28, 28))
    plt.show()  
    
    result = []
    for i in range(len(dataTest)):
        print(i,"/",len(dataTest))
        result.append(classifyNB(dataTest[i],pxVector,px))
        
    end=time.clock()
    total_time=end-start
    
    df = pd.DataFrame(result)
    df.columns = ['Label']
    df['ImageId']=[i+1 for i in range(len(df))]
    df = df[['ImageId','Label']]
    df.to_csv('result_NB.csv',index=False)
    print("Time For Run HandwritingRecognizationWithNB:"+str(total_time))

#Time For Run HandwritingRecognizationWithNB:48.89396409425353
#Time For Run HandwritingRecognizationWithNB_Bag:51.662562077722214