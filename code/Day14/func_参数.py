# 一：函数的定义
# 1：有参数


def test(x):
    """

    :param x: 整数数字
    :return: 返回值
    """
    res = x**3
    return res


print(test)             # 函数内存地址<function test at 0x10827aea0>
print(test(3))
# 2： 没有参数


def test():
    """

    :return: 返回值
    """
    x = 2
    res = x**3
    return res


print(test())
# 二：使用函数的好处
"""
1：代码重复使用
2：保持一致性，易维性
3：可扩展性——————》直接更改函数就OK了
"""
# 三：函数和过程
'''
过程是没有返回值的函数
1：过程没有返回值，print（test（））是None
2：只有一个返回值，就是其本身
3：返回值有很多，都放人元祖中充当元素，生成一个元祖
'''
# 四：函数的参数
"""
1:形参变量：只有在调用时才分配内存单元，在调用结束时，即释放内存单元
2:实参变量：常量，变量，表达式，函数等，在调用函数时，它们必须有确定的值
"""


def test(x,y):           # x,y是形参
    res = x**y
    print(x, y)
    return res


t = test(3,3)           # 2，3是实参
print(t)
"""
3:位置参数：位置需要一一对应，多一个不行少一个也不行
4：关键字参数：位置不需要一一对应，多一个不行少一个也不行
5:混合使用，位置参数必须在关键字参数左边
"""
# 位置参数


def test(x, y, z):
    res = x+y+z
    return res


print(test(1, 2, 3))
# 关键字参数


def test(x, y, z):
    res = x+y+z
    return res


print(test(z=3, x=1, y=2))
# 位置参数和关键字参数混合使用，位置参数都要在最左边


def test(x, y, z):
    res = x+y+z
    return res


print(test(1, z=3, y=2))
"""
6:默认参数 init的默认值是'帅气'
"""


def handle(x, init='帅气'):
    print(x, init)       # 1 帅气


handle(1)
"""
7：参数组   *：列表:位置参数传数传的数据   **：字典:关键字参数传的数据
"""
# 列表的元素以位置参数的形式传输


def test(x, *args):
    print(x, args, args[2])     # 列表的与元素以元祖的形式打印出来


test(1, 1, 2, 3, 4, '洪吉昌')  # 1 (1, 2, 3, 4, '洪吉昌') 3
"""
test(1, [2, 4, 4])            #1 ([2, 4, 4],)   元祖中只有一个元素
test(1, *[2, 4, 4])           #1 (2, 4, 4)      元祖中有三个元素
"""
# 字典的元素以关键字参数形式传输  x=1————》{key:value} key='x'，value=1


def test(x, **kwargs):
    print(x, kwargs)


test(1, y=2, z=3)              # 1 {'y': 2, 'z': 3}
"""
test(1, **{'hello':1, 'hjc':2})     #1 {'hello': 1, 'hjc': 2}
test(1, hello=1, hjc=2)
"""


def test(x, *args, **kwargs):
    print(x, args, kwargs)


test(1, 1, 2, 3, 4, 5, 6, name='洪吉昌', age=18)
# 1 (1, 2, 3, 4, 5, 6) {'name': '洪吉昌', 'age': 18}




