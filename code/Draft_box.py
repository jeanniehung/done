# from functools import reduce
# reduce()


# def test(x, *args):
#     print(x, args, args[2])
#
#
# test(1, 1, 2, 3, 4, '洪吉昌')

#
# i = input('请输入姓名')
# j = input('年龄：')
# new = '我是{}年纪{}'.format(i, j)
# print(new)
#

#
# name = ['洪吉昌', '魏宽怀']
#
#
# def change_name():
#     name = '洪吉昌'
#     global name
#     print(name)
#
#
# change_name()

# name = '洪吉昌'
#
#
# def user():
#     name = '洪淑芳'
#
#     def add():
#         # nonlocal name
#         global name
#         name = '帅比'
#     add()
#     print(name)
#
#
# print(name)     # 洪吉昌
# user()          # 帅比
# print(name)     # 洪吉昌

# 简单递归代码
# import time
#
#
# def calc(n):
#     print('-'*20, n, sep='\n')
#     if int(n/2) == 0:
#         return n
#     time.sleep(1)
#     return calc(int(n/2))
#
#
# res = calc(10)
# print('*'*20, res, sep='\n')

# 模拟列表人员问路情况
# li = ['魏宽怀', '洪省昌', '洪淑芳', '无敌帅王']        # 问路列表名单
# # li_food = ['sb', 'asb', 'nab', '洪吉昌']
# #
# # import time
# #
# #
# # def ask_way(array):
# #     print('*'*20)
# #     if len(array) == 1:
# #         if array[0] != '洪吉昌':
# #             return '%s说,我也不知道' % array[0]
# #
# #     person = array.pop(0)
# #
# #     if person == '洪吉昌':
# #         return '%s说：直走，拐个弯就到' % person
# #
# #     print('%s说：我不知道，我帮你去问问%s' % (person, array[0]))
# #     time.sleep(1)
# #     good = ask_way(array)
# #     print('#'*20, '%s问的结果是：%s' % (person, good), sep='\n')
# #     return good
# #
# #
# # res = ask_way(li)
# # print('_'*20, res, sep='\n')


# shopping_list = [
#                     ['电脑', 1000],
#                     ['充电器', 100],
#                     ['数码相机', 500],
#                     ['phone', 300]
#                  ]
# my_list = []
# for i in shopping_list:
#     my_list.append(i)
# print(my_list)
#
# import time
#
#
# def shop(x):
#     print('*'*20)
#     if len(x) == 0:
#         return '我不想买了，谢谢'
#     good = x.pop(0)
#     if good[0] == 'phone':
#         return '我要买%s，给你%s元' % (good[0], good[1])
#     print('%s我不喜欢,可以拿一下%s给我看一下吗' % (good[0], x[0][0]))
#     time.sleep(1)
#     new = shop(x)
#     return new
#
#
# res = shop(my_list)
# print(res)


# num_list = [1, 2, 3, 4, 9]
#
#
# def hjc_func(func, array):
#     new_list = []
#     for i in array:
#         good = func(i)
#         new_list.append(good)
#     return new_list
#
#
# def add_one(x):
#     return x+1
#
#
# res = hjc_func(add_one, num_list)
# print(res)
# res = list(map(lambda x: x+1, num_list))
# print(res)
# res = list(map(add_one, num_list))
# print(res)

# msg = 'red',
# new_msg = list(map(lambda x: x.upper(), msg))
# print(new_msg)

# movie_people = ['a_sb', 'b_sb', 'c_sb', '洪吉昌']
# filter(lambda x: x.endswith('sb'), movie_people)
# print(list(filter(lambda x: not x.endswith('sb'), movie_people)))


# from functools import reduce
# person = ['洪吉昌', '帅比', '魏宽怀', 'sb']
# r = reduce(lambda x, y: x + y, person, '牛')
# print(r)


"""
内置函数
"""
# print(abs(-111))
# print(all([1, 2]))
# print(any([1, 2, 0]))
# print(ascii('洪吉昌'))
# print(bin(10))
# print(oct(10))
# print(hex(10))
# print(callable(tuple))
# print(chr(97))
# print(ord('a'))
# # print(copyright())      # 用于打印许可证文本的交互式提示对象,列表贡献者和版权声明。
# # print(credits())        # 用于打印许可证文本的交互式提示对象,列表贡献者和版权声明。
# print(dir())
# print(divmod(10, 3))
# d = {'hjc': 'hjc'}
# print(eval(str(d)))
# print(eval('2-1'))
# print(exit())
# print(hash(None))
# print(isinstance(1, int))
# print(isinstance('12', str))
# print(pow(2, 3))
# print(round(3.5))
# num = [1, 2, 3, 4, 10]
# s = slice(0, 4, 2)
# print(num[s])
# num = [1, 2, 3, 4, 10]
# print(list(reversed(num)))
# print(max(num))
# print(min(num))

"""
1. 文件a.txt内容：每一行内容分别为商品名字，价钱，个数，求出本次购物花费的总钱数
apple 10 3
tesla 100000 1
mac 3000 2
lenovo 30000 3
chicken 10 3

# 1:先创建一个a.txt文件
from functools import reduce
file = open('a.txt', 'w')
file.write('apple 10 3\n''tesla 100000 1\n''mac 3000 2\n''lenovo 30000 3\n''chicken 10 3\n')
file.close()
# 2:提取文件内容
read_f = open('a.txt', 'r')
data = read_f.readlines()
read_f.close()
# 3：去除字符串中的\n 和 空格
b = []
for i in data:
    data1 = i.replace('\n', '')
    data2 = data1.strip('')
# 4：只提取字符串里的数字到一个列表   （如果商品名称里有数字怎么办？）
    a = []
    for j in data2:
        if j.isnumeric():
            e = eval(str(j))
            a.append(e)
# 5：把字符串类型的数字转为数字类型，同时把最后一位和其他位数作为两个元素添加到一个新列表
# 如果所有商品的购买数量不全是个位数怎么办？
    d = []
    s = a[0:-1]
    c = ''
    for z in s:
        c += str(z)
    c = int(c)
    d.append(c)
    e = int(a[-1])
    d.append(e)
# 6：计算每一次的乘积
    r = reduce(lambda c, e: c*e, d)
    b.append(r)
# 7：总和相加
print(sum(b))

2. 修改文件内容，把文件中的alex都替换成SB
# 先创建一个文件
file = open('home_work', 'w')
file.write('alex你好帅\n')
file.write('alex你好帅\n')
file.write('alex你好帅\n')
file.write('alex你好帅\n')
file.close()

read_f = open('home_work', 'r')
data = read_f.read()
read_f.close()
write_f = open('home_work', 'w')
write_f.write(data.replace('alex', 'SB'))
write_f.close()
"""









