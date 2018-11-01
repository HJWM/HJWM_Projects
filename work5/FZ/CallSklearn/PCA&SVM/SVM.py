from sklearn.decomposition import PCA
from sklearn import svm

import numpy as np
import pandas as pd


def trainDataProcess(file1,file2):
    df = pd.read_csv(file1)
    df1 = pd.read_csv(file2)
    dataTest = np.array(df1)
    data = np.array(df)
    labels = data[:,0]
    dataTrain = data[:,1:]
    return dataTest,dataTrain,labels

test,train,target= trainDataProcess('train.csv','test.csv')

pca_model = PCA(n_components=35, copy=False, whiten=True)
train = pca_model.fit_transform(train)
test = pca_model.transform(test)

svm_model = svm.SVC()
svm_model.fit(train, target)

prediction = svm_model.predict(test)
np.savetxt('result_PCA&SVM.csv', np.c_[range(1, len(test) + 1), prediction], delimiter=',', comments = '', header = 'ImageId,Label', fmt='%d')

#Time For Run HandwritingRecognizationWithPCA&SVM:56.6s