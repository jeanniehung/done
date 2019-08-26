import os
import logging.config
"""
定义两种 log 格式
"""
standard_format = '%(asctime)s-[%(threadName)s--%(thread)s]-[task_id:%(name)s]-%(module)s' \
                  '-%(lineno)s-%(levelname)s  %(message)s'

simple_format = '%(asctime)s-%(levelname)s-%(module)s-%(lineno)s  %(message)s'

"""
创建 log 文件的路径名
"""

logfile_dir = os.path.dirname(os.path.abspath(__file__))        # log 文件的目录
logfile_name = 'config.log'                                     # log 文件的文件名

if not os.path.isdir(logfile_dir):
    os.mkdir(logfile_dir)                                       # 如果不存在目录，就创建一下

logfile_path = os.path.join(logfile_dir, logfile_name)             # 拼接 log 文件的全路径

"""
配置 log 字典
"""
logging_dic = {
    'version': 1,
    'disable_existing_loggers': False,
    'filter': {},
    'Formatter': {'standard': standard_format, 'simple': simple_format},
    'handlers': {
        'console': {'level': 'DEBUG', 'class': 'logging.StreamHandler', 'Formatter': 'simple'},
        # 打印到屏幕到格式
        'default_file': {'level': 'DEBUG',
                         'class': 'logging.handlers.RotatingFileHandler',
                         # 将日志发送到文件,并支持日志文件大小分割
                         'maxBytes': 1024*1024*5,           # 日志大小 5m
                         'filename': logfile_path,
                         'Formatter': 'standard',
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
    logger = logging.getLogger(__name__)
    logger.debug('d你好')
    logger.info('i你好')


if __name__ == '__main__':
    load_my_logging_config()
