import logging
"""
默认（DEFAULT）：
    ——默认打印到终端
    ——默认级别是 warning 及其以上
    ——默认格式是： '%(levelname)s:%(name)s:%(message)s'

日志级别：不区分大小写
    critical = fatal    ————》50
    error               ————》40
    warning  = warn     ————》30
    info                ————》20
    debug               ————》10
    notset              ————》0 不设置
"""

# ——————————————————————》 为logging模块指定全局配置
"""
可在logging.basicConfig()函数中可通过具体参数来更改logging模块默认行为
filename：用指定的文件名创建，默认是终端
filemode：文件打开方式，在指定了filename时使用这个参数，默认值为“a”还可指定为“w”。
format：指定handler使用的日志显示格式。
datefmt：指定日期时间格式。
level：设置rootlogger（后边会讲解具体概念）的日志级别，默认是warning
stream：用指定的stream创建StreamHandler。可以指定输出到sys.stderr,sys.stdout或者文件，
默认为sys.stderr。若同时列出了filename和stream两个参数，则stream参数会被忽略。

format参数中可能用到的格式化串：
%(name)s            Logger的名字,并非用户名，默认是root
%(levelno)s         数字形式的日志级别
%(levelname)s       文本形式的日志级别
%(pathname)s        执行文件的完整路径名，可能没有
%(filename)s        调用日志输出函数的模块的文件名 cal.py
%(module)s          调用日志输出函数的模块名      cal
%(funcName)s        调用日志输出函数的函数名
%(lineno)d          调用日志输出函数的语句所在的代码行
%(created)f         当前时间，用UNIX标准的表示时间的浮 点数表示
%(relativeCreated)d 输出日志信息时的，自Logger创建以 来的毫秒数
%(asctime)s         字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
%(thread)d          线程ID。可能没有
%(threadName)s      线程名。可能没有
%(process)d         进程ID。可能没有
%(message)s         用户输出的消息
"""
logging.basicConfig(
    filename='日志文件',
    filemode='w',
    format='[%(lineno)s] %(asctime)s-%(levelname)s-%(filename)s-%(name)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %p',
    level=10
)
logging.debug('你好')
logging.info('是的')
logging.warning('好的')
logging.error('错的 ')
logging.critical('帅的')
# ——————————————————————》 生成logger对象
"""
logger：产生日志的对象

Filter：过滤日志的对象 ——————————》 还没学

Handler：接收日志然后控制打印到不同的地方，FileHandler用来打印到文件中，StreamHandler用来打印到终端

Formatter对象：可以定制不同的日志格式对象，
然后绑定给不同的Handler对象使用，以此来控制不同的Handler的日志格式
"""

#  ——————————————————————》 设置logger
logger = logging.getLogger('洪吉昌')       # root下的子用户，同名是一个用户
logger.setLevel('INFO')             # 日志级别默认是10
# logger.setLevel(logging.INFO)
h = logging.FileHandler('hah', 'w')     # 设置文件模式，默认是 'a'
s = logging.StreamHandler()
f = logging.Formatter(              # 设置格式
    '%(asctime)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %p'
)
h.setFormatter(f)
s.setFormatter(f)
logger.addHandler(h)
logger.addHandler(s)


#  ——————————————————————》 操作日志

logger.debug('你好')
logger.info('你好')
logger.warning('你好')
logger.error('你好')
logger.critical('你好')


# ————-——————————————》logger的继承
"""
设置了 handler 的级别以 handler 的级别为主
getlogger()  括号里有字符串就是 root 的子 下一级 特别级别用 . 链接 root.洪吉昌
"""

logger = logging.getLogger()
logger1 = logging.getLogger('洪吉昌')
logger2 = logging.getLogger('洪吉昌.son')
logger.setLevel(10)         # 本来五条，在第一层，打印五条
logger1.setLevel(20)        # 本来四条，在第二层，打印8条
logger2.setLevel(40)        # 本来两条，在第三层，打印6条
# 解决办法，让上一级不工作，就可以不打印上一级的内容
f = logging.FileHandler('哈哈', 'w')
s = logging.StreamHandler()
m = logging.Formatter(
    '%(name)s-%(asctime)s-%(lineno)d-%(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %p',

)
f.setFormatter(m)
s.setFormatter(m)
logger.addHandler(f)
logger1.addHandler(f)
logger2.addHandler(f)
logger.addHandler(s)
logger1.addHandler(s)
logger2.addHandler(s)

logger.debug('d你好')
logger1.debug('d你好')
logger2.debug('d你好')
logger.info('i你好')
logger1.info('i你好')
logger2.info('i你好')
logger.warning('w你好')
logger1.warning('w你好')
logger2.warning('w你好')
logger.error('e你好')
logger1.error('e你好')
logger2.error('e你好')
logger.critical('c你好')
logger1.critical('c你好')
logger2.critical('c你好')

"""
logging.debug(), logging.info()等方法的定义中，除了msg和args参数外，
还有一个**kwargs参数。它们支持3个关键字参数: exc_info, stack_info, extra，
下面对这几个关键字参数作个说明。
关于exc_info, stack_info, extra关键词参数的说明:
exc_info： 其值为布尔值，如果该参数的值设置为True，则会将异常异常信息添加到日志消息中。如果没有异常信息则添加None到日志信息中。
stack_info： 其值也为布尔值，默认值为False。如果该参数的值设置为True，栈信息将会被添加到日志信息中。
extra： 这是一个字典（dict）参数，它可以用来自定义消息格式中所包含的字段，但是它的key不能与logging模块定义的字段冲突。
"""
