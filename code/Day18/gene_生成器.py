"""
# 一：什么是生成器
    生成器相当于一种数据类型，它自动完成了迭代器协议（别的数据类型需要._iter_()才能完成迭代器协议）
    所以生成器是一种可迭代对象
# 二：生成器分类及在python的表现形式（两种）：
    1：生成器函数：
        常规函数定义，但是使用yield返回值而不是return
——yield用法总结：
    1：把函数做成迭代器
    2：对比return，可以返回多个值，可以 挂起/保存 函数的运行状态


def func():

    yield [1, 2]
    yield '好成绩'
    yield (1, 'a')
    yield 1


g = func()
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
# print(g.__next__())     # StopIteration


    2：生成器表达式：
        类似列表指导，但是，生成器返回按需求产生结果，而不是一次构建一个结果列表

        # 三元表达式
            name = '洪吉昌'
            res = '帅哥' if name == '洪吉昌' else 'sb'
            print(res)      # 帅哥
        # 列表解析
            age_list = []
            for i in range(10):
                age_list.append('鸡蛋%s' % i)

            # 列表里可以是三元或三元以下的表达式，但不可以超过三元

            age_list = ['鸡蛋%s' % i for i in range(10)]

    生成器表达式就是把列表解析的[]换成()
        g = ('鸡蛋%s' %i for i in range(10))
        print(g.__next__())                     # 鸡蛋0
        print(g.__next__())                     # 鸡蛋1
        print(g.__next__())                     # 鸡蛋2
        print(g.__next__())                     # 鸡蛋3
总结：
1：列表解析把[]换成()就是生成器表达式
2：列表解析和生成器表达式都是便利的编程方式，生成器表达式更节省内存

# example
    num_l = [5, 6, 7, 8, 9]
    print(sum(num_l))

    # 列表解析生成了列表在内存里，如果列表超级大，会卡死
    print(sum([i for i in range(10) if i > 4]))

    # 生成器表达式只是在使用是一个一个调用，节省内存
    print(sum(i for i in range(10) if i > 4))

# 三：使用生成器的优点：
        对延时操作提供了支持，
        延时操作：需要时产生结果，而不是立即产生


"""

# 生成器函数


def func():

    yield [1, 2]
    yield '好成绩'
    yield (1, 'a')
    yield 1


g = func()
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
# print(g.__next__())     # StopIteration


# 三元表达式
name = '洪吉昌'
res = '帅哥' if name == '洪吉昌' else 'sb'
print(res)  # 帅哥


# 列表解析
age_list = []
for i in range(10):
    age_list.append('鸡蛋%s' % i)
# 列表里可以是三元或三元以下的表达式，但不可以超过三元
age_list = ['鸡蛋%s' % i for i in range(10)]


# 生成器表达式
g = ('鸡蛋%s' % i for i in range(10))
print(g.__next__())  # 鸡蛋0
print(g.__next__())  # 鸡蛋1
print(g.__next__())  # 鸡蛋2
print(g.__next__())  # 鸡蛋3


# example
num_l = [5, 6, 7, 8, 9]
print(sum(num_l))

# 列表解析生成了列表在内存里，如果列表超级大，会卡死
print(sum([i for i in range(10) if i > 4]))

# 生成器表达式只是在使用是一个一个调用，节省内存
print(sum(i for i in range(10) if i > 4))