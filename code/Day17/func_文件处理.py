"""
文件处理得找到文件路径，最好与处理文件的.py（模块）文件地址相同，其他的完也不会
文件处理可以处理任意形式的文件
"""

# 文件名后面是功能 ———— 读 r 写 w 追加 a
# file = open('new', 'a', encoding='utf-8')    # mac默认解码是utf8;windows默认解码是gbk
# file是一个句柄
# file.close()            # 关闭文件， 每次做文件操作时，操作完都要关闭文件

# with open('new', 'a') as file:        # 等于上面三步操作

"""
处理 .py 文件
"""
# with open('new_hjc.py', 'w') as file:
#     file.write('li = []')

"""
读的操作
file = open('new', 'r', encoding='utf-8') 
"""
# data = file.read()        # 读文件
# print(data)

# print(file.readable())    # 是否可读

# 前提是没有 file.read() # 一次读一行
# print('第一行:', file.readline(0), end='')     # 第一行: 第二行: 11111
# print('第二行:', file.readline())
# print('第三行:', file.readline())
# print('第四行:', file.readline())     # 没有那么多行显示
# print('第五行:', file.readline())


# 前提是没有 file.read() ; file.readline() ； 把文件里字符串形式的所有的内容读取出来弄成一个列表形式
# print(file.readlines())         # ['11111\n', '22222\n', '洪吉昌\n', '你真的好帅']

"""
写的操作
file = open('new', 'w', encoding='utf-8') 
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
追加操作
file = open('new', 'a', encoding='utf-8') 
追加内容到文件最后
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
# with open('new', 'r') as read_f, \
#         open('new_1', 'w') as write_f:       # \ 代表的是一行代码太长，分割到下一行
#     data = read_f.readlines()
#     write_f.writelines(data[0: 5])
