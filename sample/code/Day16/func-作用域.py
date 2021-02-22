"""
作用域
"""
# name = '洪吉昌'
#
#
# def foo():
#     name = '洪淑芳'
#
#     def bar():
#         print(name)
#     return bar    # bar的内存地址
#
#
# a = foo()           #  执行foo会得到bar的内存地址,可以赋给以后哥变量a
# print(a)            #   打印bar的内存地址  # <function foo.<locals>.bar at 0x102fc6ae8>
# a()                 #   等于执行bar这个函数   # 洪淑芳
# print(a())          #   会显示bar函数运行的过程,bar这个函数没有返回值，所以显示None     # 洪淑芳  None
#
# # foo()()
"""
匿名函数
"""
# 1:格式：
# lambada 形参：return返回值
#
# def calc(x):
#     return x+1
# print(calc(10))
#  两者相等
# function = lambda x: x+1
# print(function(10))
#
# name = 'alex'
# age = '18'
# f = lambda x: x+'_sb'
# print(f(age))
# f = lambda x: (x+'_sb', x+'_nb')    # 返回多个值一个加括号组成元祖的形式
# print(f(name))                      # ('alex_sb', 'alex_nb')
"""
编程的方法论：
    ——面向过程编程
    
    ——函数式编程=编程语言定义的函数+数学意义的函数
    一：高阶函数
        1：函数接收的参数是一个函数名
            def foo(s):
                print(s)
            def bar(name):
                print('my name is %s' % name
            foo(bar('洪吉昌'))                     # my name is 洪吉昌
                                                  #  None   
        
        2：返回值包含函数,可以是任意函数,包括自己
            def foo(s):
                print(s)
            def bar(n):
                print('my name is %s' % n)
                return foo                      # my name is 洪吉昌
            bar('洪吉昌')('帅比')                 #  帅比

            #     return foo('帅比')
            # bar('洪吉昌')                # 等同于上两步骤操作                    
            
    ——面向对象编程
"""

# 求阶层


# def num(n):
#     if n == 1:
#         return 1
#     return n * num(n-1)
#
#
# print(num(6))


"""
# map函数:  
1：功能：处理序列中的每个元素，得到的结果是一个可迭代对象（列表），该可迭代对象元素个数及位置与原来一样
2：格式：
map(func，array） array可迭代对象
func（函数）可以是lambda x: x+1 的匿名函数
也可以是自己定义的函数 def function（）：
"""

# 下面是例子

"""
num_list = [1, 2, 3, 4, 9]


def hjc_func(func, array):
    new_list = []
    for i in array:
        good = func(i)
        new_list.append(good)
    return new_list


def add_one(x):
    return x+1


res = hjc_func(add_one, num_list)
print(res)

res = list(map(add_one, num_list))
print(res)

res = list(map(lambda x: x+1, num_list))
print(res) 

res = list_map(lambda x: x**2, num_list)
print(res)  
"""

msg = 'red'
new_msg = list(map(lambda x: x.upper(), msg))
print(new_msg)      # ['R', 'E', 'D']

msg = 'red',
new_msg = list(map(lambda x: x.upper(), msg))
print(new_msg)     # ['RED']

"""
# filter函数:过滤作用
1：功能：遍历序列的每个元素，判断每个元素得倒布尔值，如果是True则保留下来
2：格式：
filter（func，array）
"""
movie_people = ['a_sb', 'b_sb', 'c_sb', '洪吉昌']
filter(lambda x: x.endswith('sb'), movie_people)  # 一个列表的内存地址，该列表里面的元素是带'sb'的名字
print(list(filter(lambda x: not x.endswith('sb'), movie_people)))   # ['洪吉昌']
    

"""
reduce函数：
1：功能：处理一个序列，然后序列进行合并操作
2；格式：在python3的版本，要写下一行的代码调用reduce函数
from functools import reduce # 从functools中调用reduce函数
reduce（func，array，init）
func必须是两个参数
reduce()还可以接收第3个可选参数，作为计算的初始值（init=n 作为默认参数）
"""
from functools import reduce      # 调用函数写在文件开头，from不会出现黄线
num_l = [1, 2, 3, 4, 5]
r = reduce(lambda x, y: x+y, num_l, 100)
print(r)
