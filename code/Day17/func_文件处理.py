"""
文件处理得找到文件路径，最好与处理文件的.py（模块）文件地址相同，其他的完也不会
文件处理可以处理任意形式的文件
"""

"""
处理 .py 文件
"""
# with open('new_hjc.py', 'w') as file:
#     file.write('li = []')


# 文件名后面是功能 ———— 读 r     默认模式，   文件必须存在，不存在则抛出异常
#                    写 w     不可读，     不存在则创建；存在则清空内容
#                  追加 a     不可读，      不存在则创建；存在则只追加内容
#                    写 x     不可读       文件存在则报错，不存在即创建
#                       +     表示可以同时读写某个文件


# file = open('new', 'a', encoding='utf-8')    # mac默认解码是utf8;windows默认解码是gbk
# file是一个句柄
# file.close()            # 关闭文件， 每次做文件操作时，操作完都要关闭文件

# with open('new', 'a') as file:        # 等于上面三步操作


"""
读的操作 r
file = open('new', 'r', encoding='utf-8') 
file.close()
"""
# data = file.read()        # 读文件,光标移动到文件末尾
# print(data)

# print(file.readable())    # 是否可读

# 前提是没有 file.read() # 一次读一行
# print('第一行:', file.readline(0), end='')    # 读取一行内容,光标移动到第二行首部
# print('第二行:', file.readline())
# print('第三行:', file.readline())
# print('第四行:', file.readline())
# print('第五行:', file.readline())            # 文件没有那么多行显示空行


# 前提是没有 file.read() ; file.readline() ；     把文件里字符串形式的所有的内容读取出来弄成一个列表形式
# print(file.readlines())                       # ['11111\n', '22222\n', '洪吉昌\n', '你真的好帅']

"""
写的操作 w
file = open('new', 'w', encoding='utf-8') 
file.close()
        ——文件存在，清空文件在做操作
        ——文件不存在新建文件
文件内容只能是字符串类型
"""
# file.write('1111')
# file.write('2222')                  # 直接追加到其后面
#
# file.write('1111\n')                    # 换行操作
# file.write('2222\n''洪吉昌\n''真帅\n')   # 出现一个 \n 换一行开始写
#
# file.writelines(['洪淑芳\n', '加油\n'])  # 把列表形式的内容转为字符串形式写到文件中
#
# print(file.writable())          # 是否可写

"""
open函数写的模式操作
引号内还有引号，外层引号用单引号，内层引号用双引号
"""
# with open('测试文件', 'w', encoding='utf-8') as file:
#     file.writelines(['{"user_name": "洪吉昌", "password": 123}\n'])
#     file.write('{"user_name": "洪吉昌"}\n')
#     file.write('{1: 1}\n')
#     file.write('{("洪吉昌"): 1}\n')
#     file.write('{(1, 2, ''): 1}\n')
#     file.write('{'': 1}\n')
#     file.writelines(['{"user_name": "洪淑芳", "password": 123}\n', ])


"""
追加操作 a
file = open('new', 'a', encoding='utf-8') 
file.close()
        ——文件存在，在文件最后进行操作,追加内容到文件最后
        ——文件不存在新建文件
文件内容只能是字符串类型
"""
# file.write('加油兄弟们\n')     # 把加油兄弟们追到到new文件的最后一行


"""
文件修改
"""
# read_f = open('new', 'r')
# data = read_f.readlines()
# read_f.close()
# write_f = open('new', 'w')
# write_f.writelines(data[0: 5])      # 保护原文件第一到第五行
# write_f.close()

"""
由于不可以对一个文件读完操作又修改，所以建了一个新文件（new_1)来接收原文件修改的内容
等于上面的修改文件，只是把修改的内容放到一个新的文件当中
"""
# import os
# with open('new', 'r') as read_f, \
#         open('new.swap', 'w') as write_f:       # \ 代表的是一行代码太长，分割到下一行
#     data = read_f.readlines()
#     write_f.writelines(data[:-1])
# os.remove('new')
# os.rename('new.swap', 'new')

"""
文件去重
"""
# import os
# with open('new', 'r', encoding='utf-8') as read_f,\
#         open('new.swap', 'w', encoding='utf-8') as write_f:
#     s = set()
#     for line in read_f:
#         if line not in s:
#             s.add(line)
#             write_f.write(line)
# os.remove('new')
# os.rename('new.swap', 'new')
"""
#了解
f.readable() #文件是否可读
f.writable() #文件是否可读
f.closed #文件是否关闭
f.encoding #如果文件打开模式为b,则没有该属性
f.flush() #立刻将文件内容从内存刷到硬盘
f.name
"""

# 课后作业
"""
1. 文件a.txt内容：每一行内容分别为商品名字，价钱，个数，求出本次购物花费的总钱数
apple 10 3
tesla 100000 1
mac 3000 2
lenovo 30000 3
chicken 10 3

# # 1:先创建一个a.txt文件
# from functools import reduce
# file = open('a.txt', 'w')
# file.write('apple 10 3\n''tesla 100000 1\n''mac 3000 2\n''lenovo 30000 3\n''chicken 10 3\n')
# file.close()
# # 2:提取文件内容
# read_f = open('a.txt', 'r')
# data = read_f.readlines()
# read_f.close()
# # 3：去除字符串中的\n 和 空格
# PC_list = []
# for i in data:
#     data1 = i.replace('\n', '')
#     data2 = data1.strip('')
# # 4：只提取字符串里的数字到一个列表   （如果商品名称里有数字怎么办？）
#     num_str = []
#     for j in data2:
#         if j.isnumeric():
#             e = eval(str(j))
#             num_str.append(e)
# # 5：把字符串类型的数字转为数字类型，同时把最后一位和其他位数作为两个元素添加到一个新列表
# # 如果所有商品的购买数量不全是个位数怎么办？
#     num = []
#     price_str = num_str[0:-1]
#     price = ''
#     for z in price_str:
#         price += str(z)
#     price = int(price)
#     num.append(price)
#     count = int(num_str[-1])
#     num.append(count)
# # 6：计算每一次的乘积
#     r = reduce(lambda price, count: price*count, num)
#     PC_list.append(r)
# # 7：总和相加
# print(sum(PC_list))

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




