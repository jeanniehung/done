# 1:列举布尔值为False的值
"""
None, 0, False, '', (), [], {}
"""
# 2:写函数，
"""
根据范围获取其中 3 和 7 整除所有数的和，并返回调用者；
符合条件的数字个数以及符合条件的数字的总和：如
def func（start， end）：
"""
# example (1,21)
count = 0
sum_count = 0
start = 1
end = 21
while True:
    if start % 3 == 0 and start % 7 == 0:
        print(start)
        count += 1
        sum_count += start
    if start == end:
        break
    start += 1
print('符合条件数字个数：', count)
print('符合条件数字总和：', sum_count)


# 求一集合内两数的公倍数个数


def com_mul(start1, end1, num1, num2, count=0):
    if start1 % num1 == 0 and start1 % num2 == 0:
        print(start)
        count += 1

    if start == end1:
        return count

    return com_mul(start + 1, end, num1, num2, count)


count1 = com_mul(1, 21, 3, 7)
print('符合条件数字个数：', count)

# 3:函数的默认返回值是什么？
"""
None
"""
# 4:简述break/continue/return的区别
"""
break：结束当前循环
continue：结束本次循环，进入下一次
return：结束函数，并返回值，默认是None
"""
# 5:函数传递参数时，是引用还是复制值？并证明
"""
执行函数是调用变量而不是复制————》引用
"""
name = '洪吉昌'


def func():
    print(id(name))  # 4472744912


func()
print(id(name))  # 4472744912

# 6:简述三元运算及其书写格式
"""
变量名 = 值1 if判断 else 值2
name = '洪吉昌'
three = 帅 if name == '洪吉昌' else 丑
拓展：
列表解析：       li_think = [三元运算]    可以是三元或三元以下
生成器表达式：     gene = (三元运算)
"""
# 7:简述lambda表达式书写格式及其运用场景
"""
函数名 = lambda 形参: 功能  也可以不写函数名，lambda函数就是匿名函数
将简单的函数书写成lambda匿名函数，减少代码，减少占空间
运用场景：
max(比较对象, key=lambda 形参: 功能)
"""
# 8:使用set集合获取两个列表l1 = [11, 22, 33],l2 = [22, 33, 44]中的相同元素
l1 = [11, 22, 33]
l2 = [22, 33, 44]
print(set(l1) & set(l2))  # 不考虑顺序获取相同元素
print(set(l1).intersection(set(l2)))
print(set(l1) | set(l2))  # 求并集合
print(set(l1).union(set(l2)))
print(set(l1) - set(l2))  # 求差集
print(set(l1).difference(set(l2)))
# set(l1).difference_update(set(l2))
# print(set(l1))    # {33, 11, 22}
print(set(l1) ^ set(l2))  # 求交叉补集
print(set(l1).symmetric_difference(set(l2)))

# 9:定义一个函数统计一个字符串中大写字母，小写字母，数字的个数，并以字典为结果返回给调用者
dic = {'大写字母': 0, '小写字母': 0, '数字': 0}


def str_count(array):
    for i in array:
        if i.isupper():
            dic['大写字母'] += 1
        if i.islower():
            dic['小写字母'] += 1
        if i.isdigit():
            dic['数字'] += 1
    return dic


print(str_count('hjCcS111洪吉昌'))

# 10:简述函数的 位置参数 关键字参数 默认参数 可变长参数 的特点及其注意事项
"""
位置参数：按形参的位置传入，一一对应，多一个少一个都不行
关键字参数：传入实参指定形参的值，一一对应，多一个不行，少一个也不行
    —— 两者混合使用，位置参数必须都在关键字参数的左边
默认参数：在定义形参的时候就给其赋于特定的值
可变长参数：*args ：只接收位置参数，或者列表，元祖,字典,和*[]格式
          **kwargs ：只接收关键字参数，和**{}格式
"""

# 11:简述Python3中的range函数和Python2.7中的range函数有什么区别
"""
Python3中使用range函数得到的是一个可迭代对象
Python2.7中使用range函数得到的是一个列表对象，要想得倒可迭代对象应该使用xrange
python3————》range(10)=xrange(10)————》Python2.7
"""
# 12:简述对象和类的关系
"""
类是具有相同数据结构（属性）和相同操作功能（行为）对象的集合
对象是符合某种类所产生的一个实例
str（类）————》'洪吉昌'（对象）
"""
# 13:内置函数 all 和 any 的区别
"""
all()：括号里的每一个元素做bool运算，全为真才显示True，元素是'' [] () {} 中的任一一个也显示True
any()：括号里的每一个元素做bool运算，一个为真就显示True，元素是'' [] () {} 中的任一一个显示False
"""
# 14:将字符串'洪吉昌'转换成 UTF-8 编码的字节类型
name = '洪吉昌'
print(bytes(name, encoding='utf-8'))
print(name.encode('utf-8'))

# 15:简述 globals（）和 locals（）作用
"""
globals():获取所有的全局变量
locals():获取所有的局部变量
"""
# 16:利用内置函数 zip(),获取字符串 s='alex_is_good_guy'
l1 = ['alex', 11, 22, 33, 44]
l2 = ['is', 11, 22, 33, 44]
l3 = ['good', 11, 22, 33, 44]
l4 = ['guy', 11, 22, 33, 44]
s = '_'.join(list(zip(l1, l2, l3, l4))[0])


# 17:利用递归实现 1*2*3*...*7=5040


def class_num(n):
    if n == 1:
        return 1
    return n * class_num(n - 1)


print(class_num(7))

from functools import reduce

print(reduce(lambda x, y: x * y, (i for i in range(1, 8))))

# 18:写函数
# 有以下两个列表
# 第一个列表中的数字无序不重复排列，第二个为空列表
l1 = [1, 11, 111, 22, 33, 444, 1112]
l2 = []
"""
取出第一个列表的最小值，放到第二个列表的首位置
取出第一个列表的最小值(仅小于上一次的最小值），放到第二个列表的首位置
取出第一个列表的最小值(仅小于上一次的最小值），放到第二个列表的首位置
取出第一个列表的最小值(仅小于上一次的最小值），放到第二个列表的首位置
...
以此类推，得倒一个有序的列表l2，并返回给函数调用者
"""

# l2 = list(reversed(sorted(l1)))
# print(l2)


def func_sort(wait_l, args):
    for i in range(len(wait_l)):
        m = min(wait_l)
        args.insert(0, m)
        wait_l.remove(m)
    return args


print(func_sort(l1, l2))

# 19:猴子吃桃，
"""
第一摘了好多桃子，吃了一半，没过瘾，又吃了一个，以后每天都吃剩下的一半加一个，
到了第十天只有一个桃子。
问第一天摘了多少个桃子？
"""
p = 1
print('第十天吃之前还剩%s个桃子' % p)
for i in range(9, 1, -1):
    p = (p+1)*2
    print('#'*20, '第%s天吃之前，还剩%s个桃子' % (i, p), sep='\n')
print('_'*20, '第一天一共摘了%s个桃子' % p, sep='\n')


# 20:写程序

# a.利用filter、自定义函数获取 l1 中元素大于 33 的所有元素l1 = [11, 22, 33, 44, 55]
l1 = [11, 22, 33, 44, 55]


def num_33(args):

        if args > 33:       # filter函数会遍历出列表中的每一个元素进行判断
            return True


print(list(filter(num_33, l1)))   # 实参是一个列表，所以用args

print(list(filter(lambda x: x > 33, l1)))

# b.利用filter、lambda 表达式获取 l1 中元素小于 33 的所有元素l1 = [11, 22, 33, 44, 55]
l1 = [11, 22, 33, 44, 55]
print(list(filter(lambda x: x < 33, l1)))

# c.利用map、自定义函数将所有是奇数的元素加 100
l1 = [11, 22, 33, 44, 55]


def odd_add(args):
    if args % 2 != 0:
        args += 100
    return args


print(list(map(odd_add, l1)))

print(list(map(lambda x: x if x % 2 == 0 else x+100, l1)))
# d.利用map、lambda 表达式将所有是偶数的元素加 100
l1 = [11, 22, 33, 44, 55]

print(list(map(lambda x: x+100 if x % 2 == 0 else x, l1)))

# 21、写程序
"""
a.文件操作时 with 的作用？
with 打开文件执行完毕后自动关闭
"""
# b.写程序：利用 with 实现同时打开两个文件（一读，一写，并将读取的内容写入到写入模式的文件中）

import os
with open('测试文件', 'r', encoding='utf-8') as read_f,\
        open('测试文件.swap', 'w', encoding='utf-8') as write_f:
    write_f.writelines(read_f.readlines()[:-1])

os.remove('测试文件')
os.rename('测试文件.swap', '测试文件')
