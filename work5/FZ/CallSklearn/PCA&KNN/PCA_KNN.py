import pandas as pd
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

def trainDataProcess(file1,file2):
    df = pd.read_csv(file1)
    df1 = pd.read_csv(file2)
    dataTest = np.array(df1)
    data = np.array(df)
    labels = data[:,0]
    dataTrain = data[:,1:]
    return dataTest,dataTrain,labels

test_x,train_x,train_y= trainDataProcess('train.csv','test.csv')

pca = PCA(n_components=0.8)
train_x = pca.fit_transform(train_x)
test_x = pca.transform(test_x)


neigh = KNeighborsClassifier(n_neighbors=4)
neigh.fit(train_x, train_y)

test_y = neigh.predict(test_x)
pd.DataFrame({"ImageId": range(1,len(test_y)+1), "Label": test_y}).to_csv('result_PCA_KNN.csv', index=False, header=True)