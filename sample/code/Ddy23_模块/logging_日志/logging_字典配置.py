"""
1、有了上述方式我们的好处是：所有与logging模块有关的配置都写到字典中就可以了，更加清晰，方便管理
2、我们需要解决的问题是：
    1、从字典加载配置：logging.config.dictConfig(settings.LOGGING_DIC)
    2、拿到logger对象来产生日志
        logger对象都是配置到字典的loggers 键对应的子字典中的
        按照我们对logging模块的理解，要想获取某个东西都是通过名字，也就是key来获取的
        于是我们要获取不同的logger对象就是
        logger=logging.getLogger('loggers子字典的key名')
但问题是：如果我们想要不同logger名的logger对象都共用一段配置，那么肯定不能在loggers子字典中定义n个key
    我们的解决方式是，定义一个空的key
这样我们再取logger对象时
logging.getLogger(__name__)，不同的文件__name__不同，这保证了打印日志时标识信息不同，
但是拿着该名字去loggers里找key名时却发现找不到，于是默认使用  key=''  的配置
"""


"""
yml 文件配置日志文建
原理还是 字典配置
yaml 可以把 yml 文件解析成一个字典
yaml        logging.config
"""
# import logging.config
# import yaml
#
#
# with open('yanl_字典配置日志文件.yml', 'r') as read_f:
#     logging_dict = yaml.load(read_f)
# logging.config.dictConfig(logging_dict)
# logger = logging.getLogger('洪吉昌')
# logger.debug('d')                   # name ————————》 洪吉昌
# logger.error('de')
# logger.critical('c')
# logging.debug('d你好')              # name ——————————》 root
# logging.info('i你好')
# logging.warning('w你好')
# logging.error('e你好')
# logging.critical('c你好')

"""
手动操作写 log 配置字典
os      logging.config
"""
import os
import logging.config
# """
# 定义两种 log 格式
# """
standard_format = '%(asctime)s-[%(threadName)s--%(thread)s]-[task_id:%(name)s]-%(module)s' \
                  '-%(lineno)s-%(levelname)s  %(message)s'

simple_format = '%(asctime)s-%(levelname)s-%(module)s-%(lineno)s  %(message)s'

"""
创建 log 文件的路径名 ——————》 为了字典里 filename
"""

logfile_dir = os.path.dirname(os.path.abspath(__file__))        # log 文件的目录
logfile_name = 'config.log'                                     # log 文件的文件名
# logfile_name = input('请输入文件名:').strip()
if not os.path.isdir(logfile_dir):
    os.mkdir(logfile_dir)                                       # 如果不存在目录，就创建一下

logfile_path = os.path.join(logfile_dir, logfile_name)             # 拼接 log 文件的全路径

"""
配置 log 字典
"""
logging_dic = {
    'version': 1,
    'disable_existing_loggers': False,          # 禁用现有 logger
    'filter': {},
    'formatters': {'standard': {'format': standard_format, 'datefmt': '%Y -- %m'},
                   'simple': {'format': simple_format, 'datefmt': '%Y -- %m %p'}},
    # datefmt 配置时间格式
    'handlers': {
        'console': {'level': 'DEBUG', 'class': 'logging.StreamHandler', 'formatter': 'simple'},
        # 打印到屏幕到格式
        'default_file': {'level': 'DEBUG',
                         'class': 'logging.handlers.RotatingFileHandler',
                         # 将日志发送到文件,并支持日志文件大小分割
                         'maxBytes': 1024*1024*5,           # 日志大小 5m
                         'filename': logfile_path,
                         'formatter': 'standard',
                         'backupCount': 5,                  # 备份数
                         'encoding': 'utf8'
                         }
    },
    'loggers': {
        # logging.getlogger(__name__) 拿到的 logger 配置 前面的引号内容
        '': {'handlers': ['console', 'default_file'],   # 把上面定义的 handlers 都加上
             'level': 'DEBUG',
             'propagate': True      # 可以向更高的级别的 logger 传递
             }
    }
}


def load_my_logging_config():
    logging.config.dictConfig(logging_dic)
    logger = logging.getLogger('洪吉昌')
    logger.debug('d你好')         # name——————》 洪吉昌
    logger.info('i你好')
    logging.debug('dd你好')       # name——————》 root
    logging.info('ii你好')


if __name__ == '__main__':
    load_my_logging_config()
