import time


def d_t(func):

    def wrapper():
        start_time = time.time()
        func()
        stop_time = time.time()
        print('函数运行时间：%s' % (stop_time - start_time))

    return wrapper


@d_t
def foo():
    time.sleep(1)
    print('来自foo')


foo()           # 执行 wrapper 函数

# 加上返回值


def d_t(func):

    def wrapper():
        start_time = time.time()
        res = func()
        stop_time = time.time()
        print('函数运行时间：%s' % (stop_time - start_time))
        return res
    return wrapper


@d_t
def foo():
    time.sleep(1)
    print('来自foo')
    return '这是 foo 的返回值'


foo()           # 执行 wrapper 函数
print(foo())    # 加上返回值

# 加上参数


def d_t(func):

    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        stop_time = time.time()
        print('函数运行时间：%s' % (stop_time - start_time))
        return res
    return wrapper


@d_t
def foo(name, age):                 # 函数定义几个参数传几个
    time.sleep(1)
    print('来自foo,姓名是【%s】,年龄是【%s】' % (name, age))
    return '这是 foo 的返回值'


foo('洪吉昌', 18)           # 执行 wrapper 函数,加上参数，可以是任意长度
# print(foo('洪吉昌', 18))    # 函数执行结果加上返回值


@d_t
def too(name, age, gender):         # 函数定义几个参数传几个
    time.sleep(1)
    print('来自foo,姓名是【%s】,年龄是【%s】,性别是【%s】' % (name, age, gender))
    return '这是 too 的返回值'


print(too('洪吉昌', 18, 'male'))       # female：女；参数长度可以是任意的


