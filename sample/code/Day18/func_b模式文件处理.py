"""
windows系统需要使用b模式查看图片，视频这类文件
linux系统不需要
# 字符串——————》编码 encode——————》bytes
# bytes——————》解码 decode——————》字符串
"""
# # 写
# file = open('new', 'wb')   # b方式 不能指定编码
# file.write('洪吉昌'.encode('utf-8'))
# # file.write(bytes('洪吉昌', encoding='utf-8'))
# file.close()
# # 读
# file = open('new', 'rb')
# data = file.read()
# print(data)
# print(data.decode('utf-8'))
# file.close()
# # 追加
# file = open('new', 'ab')
# file.write('\n'.encode('utf8'))
# file.write('牛逼'.encode('utf8'))
# file.close()
"""
文件操作的其他方法
"""
# open('new', 'r', encoding='utf-8', newline='')  # 读取真正的换行符
# file.flush()  # 将文件从内存刷新到硬盘
# file.tell()   # 光标的位置
# file.seek(2)    # 光标移动到第二个字节的位置，第二个位置不加参数(0)默认光标从开头开始移动
# file.seek(2, 1)   # 相对上一次的位置seek,必须是b模式打开文件的前提下
# file.seek(-2,2)  # 光标从末尾倒者移动两个字节的位置，b模式下
# file.truncate(10)   # 从头开始算，截取10个字节，在r+,a+的前提下
"""
一: read(3)：
　　1. 文件打开方式为文本模式时，代表读取3个字符
　　2. 文件打开方式为b模式时，代表读取3个字节
二: 其余的文件内光标移动都是以字节为单位如seek，tell，truncate
注意：
　　1. seek有三种移动方式0，1，2，其中1和2必须在b模式下进行，但无论哪种模式，都是以bytes为单位移动的
　　2. truncate是截断文件，所以文件的打开方式必须可写，但是不能用w或w+等方式打开，
       因为那样直接清空文件了，所以truncate要在r+或a或a+等模式下测试效果
"""


"""
查看大文件的最后几行内容
"""
inp = int(input('请选择需要后几行内容:'))
with open('日志文件', 'rb') as file:
    for i in file:          # 循环文件的推荐方式
        off = -10
        while True:
            file.seek(off, 2)
            data = file.readlines()
            if len(data) > inp:
                count = 1
                while True:
                    print('文件的最后第%s一行的内容是：%s' % (count, data[-count].decode('utf-8')))
                    if count == inp:
                        break
                    count += 1
                break
            off *= 2
