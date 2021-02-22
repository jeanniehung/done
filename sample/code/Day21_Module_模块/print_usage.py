# print(self, *args, sep=' ',end='\n', file=None)
"""
还可以和 字符串的拼接 联合使用
默认格式是：
    import sys
    print(self, *args, sep=' ',end='\n', file=sys.stdout, flush=False)

1：*args:要打印的值，表示任何多个无名参数, 各个值之间用‘,’(逗号隔开)，打印出来各个值之间用空格隔开
2：sep=' ':表示输入多个打印的值时，各个值之间的分割方式，默认是空格
3：end='\n':控制print中传入值输出完后结束符号，默认换行

4：file=sys.stdout:设置输出设备以及print的值打印到什么地方，默认输出到终端（Terminal）
可以设置————》file=文件句柄，就可以把内容存到文件中
    with open('测试.conf', 'w') as write_f:
        print('write_f就是文件句柄', file=write_f)

5：flush=False:刷新内存缓冲区的数据立即写入文件，默认是False，不刷新；flush=True 时表示刷新

——————》 转义字符
6: \r 是光标重新回到头部,覆盖之前的字符
    print(('\r%s %d%%') % (show_str, int(100*percent)),

"""




