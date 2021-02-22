# 解压序列
a, b, c = (1, 2, 3)
print(a)        # 1
print(b)        # 2
print(c)        # 3
"""
一一对应，多一个变量名不行，多一个值也不行
"""

# 取列表中的个别值
num_l = [10, 9, 2, 7, 7, 1, 8]
first, *middle, end = num_l
print(first)    # 10
print(middle)        # [9, 2, 7, 7, 1]
print(end)      # 8

# 变量值对换
value1 = 10
value2 = 20
value3 = 30
value1, value2, value3 = value3, value1, value2
print(value1)       # 30
print(value2)       # 10
print(value3)       # 20


# 函数传参数时的解压序列


def foo(name, age, gender):
    print(name, age, gender)


def too(*args, **kwargs):
    foo(*args, **kwargs)


too('洪吉昌', 18, 'male')
# 一一对应； name———》洪吉昌  age————》18   gender————》male
"""
too('魏宽怀', 10000, 'female', 'sb')
报错，foo 只需要三个参数，传了四个，最后一个没有形参接收
"""