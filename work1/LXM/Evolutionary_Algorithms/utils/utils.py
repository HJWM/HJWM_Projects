import math

'''
获取编码长度，使用编码公式，函数输入为一个dirt，函数输出也为一个dirt
'''


def encodeLens(parameters, precision):
    len = {}
    for key, range in parameters.items():
        len[key] = calcRange(range, precision)
    return len


def calcRange(range, precision):
    a = range[0]
    b = range[1]
    coe = precision
    base = (b - a) * math.pow(10, coe) + 1
    m = math.log(base, 2)
    return math.ceil(m)


def decode(x, range, m):
    a = range[0]
    b = range[1]
    y = a + (b - a) * x / (math.pow(2, m) - 1)
    return y


def encodeTotalLen(parameters):
    count = 0
    for key, value in parameters.items():
        count += value
    return count


def __init__():
    parameters = {'x1': [-3.0, 12.1], 'x2': [4.1, 5.8]}
    preceision = 4
    print(encodeLens(parameters, preceision))
    print(encodeTotalLen(encodeLens(parameters,preceision)))


__init__()
