# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 16:44:29 2018

@author: FZ
"""

#字典与集合
#dictionary

d = {
     'frala': 95,
     'zhanglu':88,
     'huasheng':91
     } #list 越大查找越慢 而dict 速度不会变慢
print (d['frala'])   #通过键值即key 进行hash 寻找value

d['zhanglu'] = 77    #通过 key值放入 value值  !!!所以dict中key不能变
print (d)

#key值不存在时会报错

#要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：
#二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：

#'frala' in d
#Out[63]: True

#利用pop删除key与其对应的value

d.pop('huasheng')
print (d)

#请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。
#
#和list比较，dict有以下几个特点：
#
#1.查找和插入的速度极快，不会随着key的增加而变慢；
#2.需要占用大量的内存，内存浪费多。
#
#而list相反：
#
#1.查找和插入的时间随着元素的增加而增加；
#2.占用空间小，浪费内存很少。
#所以，dict是用空间来换取时间的一种方法。


# =============================================================================
# set 无序不重复
#set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
s = set ([1,1,2,2,3])
print (s)
s.add(5)  #通过add添加key
print (s)
s.remove(2)
print (s)

#两个set的运算
s1 = set ([1,2,3])
s2 = set ([3,'frala','zhanglu'])
print (s1 & s2)  #交
print (s1 | s2)  #并

s3 = [4,5,5,6]
s1 = s3
print (s1)

#注 str 是不可变量 而list 是可变量
# =============================================================================


#小结
#
#使用key-value存储结构的dict在Python中非常有用，选择不可变对象作为key很重要，最常用的key是字符串。
#tuple虽然是不变对象，但试试把(1, 2, 3)和(1, [2, 3])放入dict或set中，并解释结果。

t1 =  (1,2,3)
t2 =  (1,[2,3])

d1 = set (t1)
#d2 = set (t2)
print (d1)





