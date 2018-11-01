import pandas as pd
from sklearn.naive_bayes import MultinomialNB
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


model = MultinomialNB()
model.fit(train_x, train_y)
test_y = model.predict(test_x)

pd.DataFrame({"ImageId": range(1,len(test_y)+1), "Label": test_y}).to_csv('result_PCA_NB.csv', index=False, header=True)