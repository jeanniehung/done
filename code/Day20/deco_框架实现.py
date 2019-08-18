"""
装饰器框架
"""

# def decorator(func):
#     def wrapper():      # wrapper:包装器
#         res = func()          # 闭包的概念，当前没有变量 func 去上一级找，找到 func 运行
#         pass            # 包装器内写上要实现的功能
#         return res
#     return wrapper      # 返回wrapper函数的内存地址
#
#
# decorator()     # 括号里加上要装饰的函数名就ok
"""
实现一个计算函数运行时间的装饰器
"""
import time


def d_t(func):

    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)     # 直接从 wrapper 函数接收变量
        stop_time = time.time()
        print('函数运行时间：%s' % (stop_time - start_time))
        return res
    return wrapper


@d_t                # @d_t = 'foo = d_t(foo)'
def foo(x, y):
    time.sleep(1)
    print('来自foo', x, y)
    return '这是 foo 的返回值'


# foo = d_t(foo)    # 得到wrapper的内存地址赋值给foo
"""
语法糖：@
@d_t = 'foo = d_t(foo)'
"""
res1 = foo(1, 2)        # 函数定义几个参数传几个————执行 wrapper() 函数
print(res1)              # 打印 wrapper() 函数的返回值
"""
虽然形式是执行foo()函数，但实际上在这执行的是装饰器内定义 wrapper() 函数
wrapper()函数运行的时候会有 foo() 函数运行的代码
"""