"""
装饰器：
    本质就是函数，功能是为其他函数添加附加功能
原则：
    1：不修改被修饰函数的源代码
    2：不修改被修饰函数的调用方式
装饰器的只是储备：
    装饰器 = 高阶函数 + 函数嵌套 + 闭包
"""

# 一：高阶函数：
"""
定义：
a：函数接收的参数是一个函数名————》为修饰函数增加功能，不改变其源代码
"""
# import time
#
#
# def foo(func):
#     start_time = time.time()
#     func()
#     stop_time = time.time()
#     res = stop_time - start_time
#     print('函数运行时间是：%s' %(stop_time - start_time))
#     return res
#
#
# def too():
#     time.sleep(1)
#     print('来自too')
#
#
# print(foo(too))
"""
b：函数的返回值是一个函数名—————》不改变被修饰函数的调用方式
"""
#
#
# def foo(func):
#
#     return func
#
#
# def too():
#
#     print('来自too')
#
#
# too = foo(too)
#
# too()     # 先运行 foo 函数，在运行 too 函数
"""
c：满足上述条件的任一一个，都可以叫做高阶函数
"""
# 多运行一次函数，不合格
# import time
#
#
# def foo(func):
#     start_time = time.time()
#     func()
#     stop_time = time.time()
#     print('函数运行时间是：%s' %(stop_time - start_time))
#     return func
#
#
# def too():
#
#     print('来自too')
#
#
# too = foo(too)
# too()

# 二：函数嵌套（内有闭包的概念）————》联系作用域
"""
函数内在定义函数，并在当前执行内部定义函数
以下面代码为例，闭包的概念就是：
有三个包：
    最内层的包内什么都没有封装
    第二个包封装了 yesterday 函数
    最外层的包内封装了 today 函数和传进来的 thing 变量；
函数即变量，包也只封装变量，包内没有变量，要使用时去外一层依次寻找，知道找到停止
"""


def tomorrow(thing):
    print('明天我要去做%s' % thing)

    def today():
        print('今天我也要去干%s' % thing)

        def yesterday():
            print('昨天我也要去干%s' % thing)

        yesterday()

    today()


tomorrow('学python')
