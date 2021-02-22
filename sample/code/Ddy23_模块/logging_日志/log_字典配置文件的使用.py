import time
import logging
import logging_配置


logger = logging.getLogger('黄')


def demo():
    logging.debug('start range...time:{}'.format(time.strftime('%Y-%m-%d', time.localtime())))
    logger.info('开始测试')
    for i in range(10):
        logger.debug('i:{}'.format(i))
        time.sleep(0.2)
    else:
        logger.debug('over range...time:{}'.format(time.strftime('%Y-%m-%d', time.localtime())))
    logger.info('测试结束')


if __name__ == '__main__':
    logging_配置.load_my_logging_config()
    demo()