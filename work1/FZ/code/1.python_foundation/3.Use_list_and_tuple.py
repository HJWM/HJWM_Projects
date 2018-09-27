# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#list and tuple  有序集合

#list 列表
classmate = [['frala','zhanglu'],'huasheng','xiakui']
print (classmate)
print (len(classmate))    #3
print (classmate[0])      #索引定位 从0开始
print (classmate[0][1])   #看成二维
print (classmate[-1])     #索引-1直接获取最后一个元素
print (classmate[-2])     #获取倒数第二个

classmate.append('liuyouze') #列表末尾追加元素
print (classmate)

classmate.insert(2,'liuhao') #固定位置插入特定元素
print (classmate)

classmate.pop(2)      #删除特定元素 不加索引号表示删除末尾元素
print (classmate)

classmate[3]='yangshun'  #替换元素则直接赋值
print (classmate)

L0=['fz',123,456.789]    #list中元素可以不同
print (L0)


#tuple  不可变的有序列表 元组 
classmate0 = ('frala','wangyaduo','baimaduoji')  #对元祖不能赋值
print (classmate0)

T = (1,)      #加逗号消除歧义
print (T)

t0 = ('123','456',['789','abc'])  #"可变"的元组
print (t0)
t0[2].append('def') #可变指列表可变 但元组指向不变
print (t0)

#exercise
L = [['Apple','Google','Microsoft'],['Java','Python','Ruby','PHP'],['Adam','Bart','Lisa']]
print (L[0][0])
print (L[1][1])
print (L[2][2])

#小结： list 和 tuple 是python内置的有序集合 一个可变 一个不可变
