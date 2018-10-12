# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 16:00:45 2018

@author: FZ
"""

#循环
#两种循环 for...in循环 依次把list或tuple中的每个元素迭代出来
names = ['frala','zhanglu','huasheng']
for name in names:
    print ('hello,%s!'%name)


L = list(range(100))
sum = 0
for num in range(101):   #range 函数返回
   sum = sum + num
print (sum)


#while 循环
sum1 = 0
x = 100

while x >= 0:
    sum1 = sum1 + x
    x = x - 1
print (sum1)

#break 跳出循环
#continue 跳过循环

###小结
#循环是让计算机做重复任务的有效的方法。
#break语句可以在循环过程中直接退出循环，而continue语句可以提前结束本轮循环，并直接开始下一轮循环。
#这两个语句通常都必须配合if语句使用。
#要特别注意，不要滥用break和continue语句。break和continue会造成代码执行逻辑分叉过多，容易出错。
#大多数循环并不需要用到break和continue语句，上面的两个例子，都可以通过改写循环条件或者修改循环逻辑，去掉break和continue语句。
#有些时候，如果代码写得有问题，会让程序陷入“死循环”，也就是永远循环下去。
#这时可以用Ctrl+C退出程序，或者强制结束Python进程。
#请试写一个死循环程序。