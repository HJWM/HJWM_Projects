# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 09:53:02 2018

@author: FZ
"""

# =============================================================================
#filter 
# =============================================================================


#keep odd
def is_odd(x):
    return x % 2 == 0

print (list(filter(is_odd,range(1,10))))

#去掉序列中空字符串
def not_empty(s):
    return s and s.strip()


L1 = ['frala',False,None,'C','F']


print (list(filter(not_empty,L1)))


#用filter求素数

#先构造以3为始的奇数无限序列 生成器
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

#define filter_function
def _not_divisible(n):
    return lambda x: x % n > 0

#define prime
def primes():
    yield 2
    it = _odd_iter()  #初始序列
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n),it)

for x in primes():
    if x < 100:
        print (x)
    else:
        break

# =============================================================================
# excise
# =============================================================================
#求回数
        
#法一 利用倒序切片
def is_palindrome2(n):
    L = list(str(n))
    L1 = list(str(n))
    L1.reverse()
    return L == L1


#法二 利用
def is_palindrome(n):
    s = (str(n))
    if len(str(n))//2==0:
        return n
    for i in range(len(str(n))//2):
        if s[i] == s[-(i+1)]:
            return n
        
print (list(filter(is_palindrome,range(1,200))))
print (list(filter(is_palindrome2,range(1,200))))   


