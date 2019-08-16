"""
# 一: 什么是迭代器协议
    1：迭代器协议是指：对象必须提供一个 next 方法，执行该方法要么返回下一项，要么就引起一个StopIteration异常
       以终止迭代（只能往后走，不能前进）
    2：可迭代对象：实现了迭代器协议的对象，（如何实现；对象内部定义一个——iter——（方法）
        num_l = [1, 2, 3]
        num = num_l.__iter__()  # num就是一个可迭代对象
        print(num.__next__())       # 1
        print(next(num))              # 1   next()函数就是pycharm定义好的next方法，和上式效果相同
    3：协议是一种规定，可迭代对象实现了迭代器协议，pycharm的内部工具（for，sum， max， map等）
       都是使用迭代器来访问对象

     # example
    s_l = ['a', 'b', 'c']
    for i in s_l:
        print(i)
    # 下面四步骤等同于for操作
    iter_s = s_l.__iter__()    # iter_s 是一个可迭代对象
    print(iter_s.__next__())
    print(iter_s.__next__())
    print(iter_s.__next__())
    # print(iter_s.__next__())      # 由于只有三个元素，所以报错StopIteration，for操作就会不输出这步骤内容


# 二：for循环的工作原理
    1：执行in后的对象._iter_()操作，得倒一个迭代器对象
    2：执行next(迭代器对象)，将得到的值一一打印出来，循环下去
    3：直到出现StopIteration，停止操作

# for语句的原始代码
    s_l = ['a', 'b', 'c']
    iter_s = s_l.__iter__()
    while True:
        try:
            print(iter_s.__next__())
        except StopIteration:
            break


# 三：迭代器的优缺点
    优点：
  — 提供一种统一的、不依赖于索引的迭代方式
  - 惰性计算、节省空间
    缺点：
  - 无法获取长度（只有在next完毕才知道有几个值）
  - 一次性的，只能往后走

    # 索引取值的迭代方式
    s_l = ['a', 'b', 'c']
    count = 0
    while count < len(s_l):
        print(s_l[count])
        count += 1
"""


# 处理文件
with open('日志文件', 'r+') as f:
    i_f = f.__iter__()
    print(i_f.__next__())


# 索引取值的迭代方式
s_l = ['a', 'b', 'c']
count = 0
while count < len(s_l):
    print(s_l[count])
    count += 1


# for语句的原始代码
s_l = ['a', 'b', 'c']
iter_s = s_l.__iter__()
while True:
    try:
        print(iter_s.__next__())
    except StopIteration:
        break


# example
s_l = ['a', 'b', 'c']
for i in s_l:
    print(i)
# 下面四步骤等同于for操作
iter_s = s_l.__iter__()    # iter_s 是一个可迭代对象
print(iter_s.__next__())
print(iter_s.__next__())
print(iter_s.__next__())
# print(iter_s.__next__())      # 由于只有三个元素，所以报错StopIteration，for操作就会不输出这步骤内容
