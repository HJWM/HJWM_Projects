# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 09:49:02 2018

@author: FZ
"""

# =============================================================================
#函数的参数



#1.位置参数
def power(x):   #x的平方
    return x*x

print (power(5))

def power(x,n):   #x的n次方
    sum = x
    while n>1:  
        sum = sum * x
        n = n - 1
    return sum

print (power(9,3))
#print (power(5))    会抛出错误



#2.默认参数
#必选参数在前，默认参数在后（必须）
#当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
def power(x,n=2):   #x的平方 默认为2 与n次平方一致
    return x*x

print (power(5))

def add_end(L=[]):
    L.append('end')
    return L

print (add_end([1,2,3]))
#默认参数必须指向不变对象#  不变对象str None
#如果可以设计一个不变对象，那就尽量设计成不变对象

def add_end(L=None): #直接将参数设计为 L = [] 会产生问题
    if L is None:
        L = []
    L.append('end')
    return L



#3.可变参数
def calc(numbers):   #不可变 tuple 或者 list
    sum = 0
    for x in numbers:
        sum = sum + x * x
    return sum

def calc1(*numbers):   #可变参数 可以为空参数
    sum = 0
    for x in numbers:
        sum = sum + x * x
    return sum   

T = (1,2,3)
print (calc1(1,2,3)) 
print (calc(T))
print (calc1(*T))    #Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：



#4.关键字参数
#它可以扩展函数的功能
def person (name,age,**kw):
    print ('name:',name,'age:',age,'other:',kw)
    
person('frala',22)
person('frala',22,city='Xian')

#也可以先组装一个dict
extra = {'city':'Xian','gender':'M'}
person ('frala',22,**extra)
#**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。
person('frala',22,gender='M',job='AI Engineer')
#试想你正在做一个用户注册的功能，除了用户名和年龄是必填项外，其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求。



#5.命名关键字参数
#对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查。
def person1(name,age,**kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print ('name:',name,'age:',age,'other:',kw)

person1('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)

def person2(name, age, *, city='Xian', job):                 #只接收job 与 city 可缺省 关键字 否则报错 
                                                            # 缺少 *，city和job被视为位置参数
    print(name, age, city, job)

person2('Jack',24,job='engineer')

def person(name, age, *args, city, job):
    print(name, age, args, city, job)



#6.参数组合
#5种参数都可以组合使用，除了可变参数无法和命名关键字参数混合
#参数定义的顺序必须是：必选参数、默认参数、可变参数/命名关键字参数和关键字参数
def f1(a,b,c=0,*args,**kw):
    print ('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)
def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1,2)
f1(1,2,3)
f1(1,2,3,'a','b')
L = ('a','b')
f1(1,2,3,*L)
f1(1,2,3,*L,x=99)

f2(1,2,d='comment kw argu',name ='frala')

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args,**kw)
       
args = (1, 2, 3)
f2(*args,**kw)
#所以，对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。

#小结
#Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。
#默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！
#要注意定义可变参数和关键字参数的语法：
#*args是可变参数，args接收的是一个tuple；
#**kw是关键字参数，kw接收的是一个dict。
#以及调用函数时如何传入可变参数和关键字参数的语法：
#可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
#关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
#使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
#命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。
#定义命名的关键字参数不要忘了写分隔符*，否则定义的将是位置参数。
# =============================================================================