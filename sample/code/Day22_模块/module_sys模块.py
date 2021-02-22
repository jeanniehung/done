# import sys
"""
动态进度条的制作 print（）中 file = sys.stdout
该模块提供对解释器使用或维护的一些变量的访问，以及与解释器强烈交互的函数。它始终可用
"""
# print(sys.path)         # 返回模块的搜索路径
# print(sys.platform)     # 返回操作系统的平台名称 darwin————》该台设备
# print(sys.version)      # 或得 python 解释器版本信息
# print(sys.maxsize)      # 文件最大存储字节量
# print(sys.argv)         # 命令行参数列表,第一个元素是程序本身的路径
# sys.exit()的用法————》退出程序，只有0是正常退出
"""
def foo(self):
    import sys
    if self == '1':
        print(1)
        # print('\033[31m洪吉昌\033[0m')
        sys.exit('洪吉昌')
        print(4)
    else:
        print('2')
foo('1')
只要括号里的内容是有长度的数据类型len，都会退出程序，
以 print('\033[31m len\033[0m') 的方式输出括号里的内容
只有 sys.exit(0)  是正常退出
"""

# sys.argv的用法————》命令行参数列表,第一个元素是程序本身的路径
"""
sys.argv[]是用来获取命令行输入的参数(参数和参数之间空格区分),
sys.argv[0]表示代码本身文件路径,所以从参数1开始,表示获取的参数了
    在终端操作：
        cd /Users/jeannie/PycharmProjects/learning_python/code/Day22_模块
        python sss.py "post" "111"  "get"
        得到的结果  ————》['/Users/jeannie/PycharmProjects/learning_python/code/Day22_模块/sss.py',
                            'post', '111', 'get']
    sss.py 的内容:
        import sys
        
        
        print(sys.argv)         # 终端看的到结果
        com = sys.argv[1]
        pa = sys.argv[2]
        if com == "post":       # 成立可以直接调用程序
            pass
        elif pa == "get":
            pass

"""

# sys.stdout.write('#')   # 等同于print,输出的内容都在同一行

"""
进度条的原理
"""
# import sys,time
# for i in range(100):
#     sys.stdout.write('#')      # 内容都储存在内存中,等所有内容都完成了在打印出来
#     time.sleep(0.2)
#     sys.stdout.flush()          # 刷新内存上的数据到屏幕
"""
实现打印文件传输的进度条
"""
# import sys, time
#
#
# def progress(self, width=50):
#     start_time = time.time()
#     if self > 1:
#         self = 1
#     time.sleep(0.8)
#     left = ('%%-%ds' % width) % (int(self * width) * '.')
#     run_time = time.time() - start_time
#     print('\r%-3.0f%% %s %.2fs' % (self * 100, left, run_time), file=sys.stdout, flush=True, end='')
#
#
# if __name__ == '__main__':
#     data_size = 1024
#     receive_size = 0
#     while receive_size < data_size:
#         time.sleep(0.2)                         # 模拟数据传输延迟
#         receive_size += 10                     # 每次接收10
#         percent = receive_size/data_size       # 接收的比例
#         progress(percent, width=30)


"""
模拟文件传输
"""
# import time
# import sys
#
#
# def progress(percentage, width=50):
#     if percentage >= 1:
#         percentage = 1
#     start_time = time.perf_counter()
#     for i in range(width+1):
#         # left_str = ('%%-%ds' % width) % (int(percentage * width) * '-')
#         left_str = i * '-'
#         # right_str = ('%%-%ds' % width) % ((width - i) * '.')
#         right_str = (width - i) * '.'
#         time.sleep(0.1)
#         run_time = time.perf_counter() - start_time
#         # print('\r  %.0f%% [%s->%s] %.2fs' % (percentage*100, left_str, right_str, run_time),
#         #       file=sys.stdout, flush=True, end='')
#         # print(' \r %.0f%% %s' % (percentage*100, left_str),
#         #       file=sys.stdout, flush=True, end='')
#         print('\r\033[30m{:^3.0f}%  \033[0m\033[31m{}\033[0m->\033[32m{}\033[0m  '
#               '\033[34m{:.2f}s\033[0m'.format(percentage*100, left_str, right_str, run_time),
#               file=sys.stdout, flush=True, end='')
#
#
# if __name__ == '__main__':
#     data_size = 1024
#     receive_size = 0
#     while receive_size < data_size:
#         time.sleep(0.2)
#         receive_size += 10
#         per = receive_size / data_size
#         progress(per, 40)

"""
字符串拼接：
    -      左边
    +      右边
    数字    长度
    %%      %
"""
"""
文件传输进度条
"""
# import sys, time, random
#
#
# def progress(self, width=50):
#
#     start_time = time.time()
#     if self > 1:
#         self = 1
#     for i in range(width):
#         time.sleep(0.1)
#         left = i * '.'
#         right = (width - i) * '#'
#         run_time = time.time() - start_time
#         print('\r%.0f%% %s%s %.2fs' % (self * 100, left, right, run_time),
#               file=sys.stdout, flush=True, end='')
#
#
# if __name__ == '__main__':
#     date_size = 1024
#     receive_size = 0
#     while receive_size < date_size:
#         time.sleep(0.2)
#         receive_size += random.randint(40, 60)
#         percentage = receive_size / date_size
#         progress(percentage, 40)





