# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 10:50:52 2018

@author: zhe

E-mail: 1194585271@qq.com
"""

import pandas as pd

df = pd.read_csv('train.csv')
df1 = pd.read_csv('test.csv')

df[:len(df)//10].to_csv('subTrain.csv',index=False)
df1[:len(df1)//10].to_csv('subTest.csv',index=False)