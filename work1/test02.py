# print("hello world")
# #本着节约的精神，出现了把Unicode编码转化为“可变长编码”的UTF-8编码
# python中的list是有序元素的集合，元素类型多样，表示方法【】，不固定长度
# python中的tuple是元组，也是有序元素的集合，只是长度固定，表示方法（）
#python中的dict相当于c语言中的map，即“键-值”对，可以高效的查询，是一种以空间换取时间的做法，表示方法为｛｝
#          作为键必须是不可变的，整数、字符串可以作为key，而list可变，则不可作为key
# python中的set和dict的唯一区别是dict是key-value对，而set中只有key，无论是set还是dict的key，都不能重复，而且唯一固定，因为要保证能够查到，所以不可变
# list中添加元素是append，set中添加元素的方法是add
# python中将函数理解为抽象底层代码，可以直接进行多次调用，而无需进行多次代码的编写
# Python的函数返回多值其实就是返回一个tuple
# 函数的参数设置有：位置参数、默认参数、可变参数、关键字参数，跟C++中的缺省参数的函数设置很类似
# 可变参数一般为list和tuple，不同的是tuple参数前面有*号
# ？？*nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
# 在函数调用的时候，Python解释器自动按照参数位置和参数名把对应的参数传进去。
# 解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数也是可以的。
# 尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。
# 在Python中，代码不是越多越好，而是越少越好。代码不是越复杂越好，而是越简单越好
# 介绍Python中非常有用的高级特性，1行代码能实现的功能，决不写5行代码。请始终牢记，代码越少，开发效率越高。
# 对于list和tuple、字符串都可以使用切片【：】，在很多编程语言中，针对字符串提供了很多各种截取函数（例如，substring），其实目的就是对字符串切片。Python没有针对字符串的截取函数，只需要切片一个操作就可以完成，非常简单
# 迭代
# 如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。
# 在Python中，迭代是通过for ... in来完成的
# python中可迭代的对象有list、tuple、dict以及字符串
# 在Python中，这种一边循环一边计算的机制，称为生成器：generator。
# 列表生成式即生成一个list【】，而生成器定义的两种方法有一是表示为（），二是含有关键字yield
# 凡是可作用于for循环的对象都是Iterable类型；
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
# 函数是Python内建支持的一种封装，我们通过把大段代码拆成函数，通过一层一层的函数调用，就可以把复杂任务分解成简单的任务，这种分解可以称之为面向过程的程序设计。函数就是面向过程的程序设计的基本单元。
# 函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！
# Python对函数式编程提供部分支持。由于Python允许使用变量，因此，Python不是纯函数式编程语言。
# 函数本身也可以赋值给变量，即：变量可以指向函数。
# 既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数
# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
# Python内建的filter()函数用于过滤序列。和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
# 排序算法：Python内置的sorted()函数就可以对list进行排序
# 默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面。
# ？？？返回函数中的闭包
# 关键字lambda表示匿名函数，冒号前面的x表示函数参数。
# 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
# 用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：
# 在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
# 当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。
# 模块是一组Python代码的集合，可以使用其他模块，也可以被其他模块使用。
# 作用域
# 在一个模块中，我们可能会定义很多函数和变量，但有的函数和变量我们希望给别人使用，有的函数和变量我们希望仅仅在模块内部使用。在Python中，是通过_前缀来实现的。
# 正常的函数和变量名是公开的（public），可以被直接引用，比如：abc，x123，PI等；
# 类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的__author__，__name__就是特殊变量，hello模块定义的文档注释也可以用特殊变量__doc__访问，我们自己的变量一般不要用这种变量名；
# 类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等；
# class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的，通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。
# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
# 当子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run()，在代码运行的时候，总是会调用子类的run()。这样，我们就获得了继承的另一个好处：多态。
# 当我们定义一个class的时候，我们实际上就定义了一种数据类型。我们定义的数据类型和Python自带的数据类型，比如str、list、dict没什么两样
# 我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象。
# num=[12,1,17]
# for i in num :
#     if(i%2 == 0):
#         print(i)

# age = 3
# if age >18:
#     print("your name is ",age)
#     print("adult")
# else:
#     print("your name is ",age)
#     print('teenager')
#

# age = 3
# if age >18:
#     print("your name is ",age)
#     print("adult")
# elif age>6:
#     print("your name is ",age)
#     print('teenager')
# else:
#     print("kid")


# s = input('birth: ')
# birth = int(s)
# if birth < 2000:
#     print("00前")
# else:
#     print("00后")



# birth = input('birth: ')
# if birth < str(2000):
#     print("00前")
# else:
#     print("00后")



# names = ['micheal','bob','trace']
# for i in names:
#     print(i)

# i = 0
# sum = 0
# while(i<10):
#     sum = sum + i
#     i = i + 1
# print(sum)


# sum = 0
# for i in range(101):
#     sum = sum + i
# print(sum)

#
# n = 1
# while n <=  101:
#     if n > 10:
#         break
#     print(n)
#     n = n + 1
# print("END")


# n = 0
# while n < 10:
#     n = n + 1
#     if n % 2 == 0:
#         continue
#     print(n)

# d = {'micheal':95,'bob':75,'tracy':85}
# print(d['micheal'])

# def my_abs(x):
#     if x > 0:
#         return x
#     else:
#         return -x
# print(my_abs(-99))

# def my_abs(x):
#     if not isinstance(x,(int,float)):
#         raise TypeError("bad operand type")
#     if x > 0:
#         return x
#     else:
#         return -x
# print(my_abs("a"))

# import math
#
# def move(x,y,step,angle=0):
#     nx = x + step * math.cos(angle)
#     ny = y - step * math.sin(angle)
#     return nx,ny
# x,y = move(100,100,60,math.pi/6)
# print(x,y)

# import math
#
# def quadratic(a,b,c):
#     delta = b * b - 4 * a * c
#     if delta < 0:
#         print("此方程无解")
#     elif delta == 0:
#         print("此方程有两个相等的实数根")
#         return -b/(2*a)
#     else:
#         print("此方程有两个不同的实数根")
#         x1 = (-b + math.sqrt(delta))/(2*a)
#         x2 = (-b - math.sqrt(delta)) / (2 * a)
#         return x1,x2
# print(quadratic(2,1,0))

# def power(x,n):
#     s = 1
#     while n > 0:
#         s = s * x
#         n = n -1
#     return s
# # print(power(5))
# # print(power(5,2))
# print(power(5,3))
#
# def power(x,n=2):
#     s = 1
#     while n > 0:
#         s = s * x
#         n = n -1
#     return s
#
# print(power(3))


# def enroll(name,gender):
#     print("name:",name)
#     print("gender:",gender)
#
# enroll('sarach','F')


# def enroll(name,gender,age=6,city='BeiJing'):
#     print("name:",name)
#     print("gender:",gender)
#     print("age:",age)
#     print("city:",city)
#
# enroll('sachea','F',8)

#
# def add_end(l=[]):
#     l.append('END')
#     return l
# print(add_end([1,2,3]))
# print(add_end())
# print(add_end())
# print(add_end())

# def add_end(l=None):
#     if l is None:
#         l =[]
#     l.append('END')
#     return l
# print(add_end())
# print(add_end())
# print(add_end())

# def calc(numbers):
#     sum = 0
#     for i in numbers:
#         sum = sum + i*i
#     return sum
# print(calc([1,2,3]))

# def person(name,age,**kw):
#     print('name:',name,'age:',age,'other:',kw)
# # print(person('micheal',6))
#
# print(person('adam',6,gender='M',job='engineer'))

# def f1(a,b,c=0,*arg,**kw):
#     print('a=',a,'b=',b,'c=',c,'arg=',arg,'kw=',kw)
# f1(1,2)
# f1(1,2,c=3)
# f1(1,2,3,'a','b')
# f1(1,2,3,'a','b',x=99)
# f1(1,2,3,x=99,s=88,t=00)

# # 递归函数
# def fact(n):
#     if n==1:
#         return 1
#     return n*fact(n-1)
# print(fact(5))
# print(fact(100))
# # print(fact(1000))


# python高级特性


# 切边
# l = ['micheal','bob','jack','lice','tice']
# r = []
# n=3
# for i in range(n):
#     r.append(l[i])
# print(r)
# 对这种经常取指定索引范围的操作，用循环十分繁琐，因此，Python提供了切片（Slice）操作符，能大大简化这种操作。
# print(l[0:3])
# print(l[1:3])
# print(l[-2:])
# print(l[-2:-1])

# l = list(range(100))
# print(l)
# print(l[:10])
# print(l[-10:])
# print(l[10:20])
# print(l[:10:2])
# print(l[::5])
# print(l[:])

# (0,1,2,3,4,5)[:3]

# python中将循环遍历称之为迭代
# d = {'a':1,"b":2,'c':3}
# for key in d:
#     print(key)
#
# for value in d.values():
#     print(value)
#
# for key,value in d.items():
#     print(key,value)

# for i in '123':
#     print(i)

# 如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
# for i,value in enumerate(['a','b','c']):
#     print(i,value)
# for i in enumerate(['asc','bs','cdef']):
#     print(i)
# for x,y in [(1,1),(2,2),(3,3)]:
#     print(x,y)

# l = ['Hello','BEEL','Shar']
# print([s.lower() for s in l])

# g = (x*x for x in range(10))
# for i in g:
#     print(i)

# def fib(max):
#     n,a,b = 0,0,1
#     while n <max:
#         print(b)
#         a,b = b, a+b
#         n = n +1
#     return 'done'
# print(fib(6))

# def fib(max):
#     n,a,b = 0,0,1
#     while n <max:
#         yield b
#         a,b = b, a+b
#         n = n +1
#     return 'done'
# for i in fib(6):
#     print(i)

# 其实可以将生成器理解为生成的数据暂放的区域，如果需要用的话再使用即可

# from collections import Iterable
# print(isinstance([],Iterable))
#
# from collections import Iterable
# print(isinstance(100,Iterable))
#
# from collections import Iterable
# print(isinstance((x for x in range(10)),Iterable))


# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数

# from collections import Iterator
# print(isinstance((x for x in range(10)),Iterator))
#
# from collections import Iterator
# print(isinstance([],Iterator))
#
# from collections import Iterator
# print(isinstance((iter(())),Iterator))
#
# from collections import Iterator
# print(isinstance((iter([])),Iterator))

# x = abs(-10)
# print(x)
# f = abs
# print(f(-10))

# def add(x,y,f):
#     return f(x) + f(y)
#
# print(add(-5,-9,abs))

# def f(x):
#     return x*x
# r = map(f,[1,2,3,4,5,6,7,8])
# # print(list(r))
# for i in r:
#     print(i)

# print(list(map(str,(1,2,3,4,5))))
# print(tuple(map(str,(1,2,3,4,5))))

# from functools import reduce
# def add(x,y):
#     return x+y
# print(reduce(add,[1,2,3,4,5]))

# 将字符串不使用int强制函数转化为数字
# from functools import reduce
# def f(x,y):
#     return x*10+y
#
# def char2num(s):
#     digits = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
#     return digits[s]
#
# print(reduce(f,map(char2num,'13579')))

# def is_odd(n):
#     return n %2 ==1
#
# print(list(filter(is_odd,[1,2,3,4,5,6,7,8,9])))

# print(list(map(lambda x:x*x,[1,2,3,4,5,6,7,8,9])))

# def log(func):
#     def wrapper(*args,**kw):
#         print('call %s():'% func.__name__)
#         return func(*args,**kw)
#     return wrapper
# @log
# def now():
#     print("2018-09014")
# now()
#
# def int2(x,base=2):
#     return int(x,base)
# print(int2('1000000'))

# import functools
# int2 = functools.partial(int,base=2)
# print(int2('10000000'))

# class Student(object):
#
#     def __init__(self,name,score):
#         self.name = name
#         self.score = score
# bart = Student("bart simpoer",59)
# print(bart.name,bart.score)

# class Student(object):
#
#     def __init__(self,name,score):
#         self.name = name
#         self.score = score
#
#     def print_score(self):
#         print("%s:%s"%(self.name,self.score))
#
# bart = Student("bart simpoer",59)
# print(bart.name,bart.score)
# bart.score =99
# print(bart.score)
# # print_score(bart)
# bart.print_score()

# class Animal(object):
#     def run(self):
#         print("animal is running.....")
#
# class Dog(Animal):
#     def run(self):
#         print("dog is running....")
#     def eat(self):
#         print("eating meat")
#
# class Cat(Animal):
#     pass
#
# dog = Dog()
# dog.run()
# dog.eat()
#
# def run_twice(animal):
#     animal.run()
#     animal.run()
#
# run_twice(Animal())
#
# def run_twice(Animal):
#     Animal.run()
#     Animal.run()
#
# run_twice(Animal())
# run_twice(Dog())
# run_twice(Cat())






