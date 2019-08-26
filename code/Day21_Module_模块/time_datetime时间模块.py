"""
time
datetime 可以进行时间的加减操作
"""
import time,datetime

# 推迟运行时间
"""
time.sleep(n)   推迟n秒运行
"""
# 时间差
"""
time.clock()
"""
# 一：（timestamp）时间戳，用于计算时间长度,时间戳表示的是从1970年1月1日00:00:00开始按秒计算的偏移量。
# 我们运行“type(time.time())”，返回的是float类型。
start_time = time.time()
"""
中间写上一些代码
"""
stop_time = time.time()
print(stop_time - start_time)   # 用于计算代码运算时长
print(time.time())              # 打印当前从1970到当前时间经过了多少秒
# 二：（stuck_time)结果化时间————》当地时间, struck_time元组共有9个元素共九个元素:
# (年，月，日，时，分，秒，一年中第几周，一年中第几天，夏令时)
print(time.localtime())
t_l = time.localtime()
print(t_l.tm_wday)          # 显示星期几，0是星期一
print(t_l.tm_yday)          # 显示一年的第几天
print(t_l.tm_year)          # 显示那一年
print(t_l.tm_mon)           # 显示那个月
print(t_l.tm_mday)          # 显示几号
print(t_l.tm_hour)          # 显示几点
print(t_l.tm_min)           # 显示第几分钟
print(t_l.tm_sec)           # 显示第几秒
# （stuck_time)结果化时间————》UTC时间，中国在东八区
print(time.gmtime())
# # 三：（format string）字符串格式化时间

"""
标准时间的格式：
%a %b %d %H:%H:%S %Y
星期几的缩写 月份的缩写 多少号 时：分：秒 年
"""
print(time.asctime())   # 把结构化时间转化为固定的字符串标准时间
print(time.ctime())     # 把时间戳转化为固定的字符串标准时间
"""
时间类型的相互转化
"""
# stuck_time标准化时间转为timestamp时间戳
print(time.mktime(time.localtime()))    # 当前时间
# timestamp时间戳转为stuck_time标准化时间
print(time.localtime())                 # 可不加参数，默认当前时间
print(time.gmtime())                    # 可不加参数，默认当前时间
# stuck_time标准化时间转为 format string 字符串时间
print(time.strftime('%Y_%m_%d_%H_%M_%S'))
# stuck_time标准化时间转为 format string 字符串时间
print(time.strptime('2018/08/23 20:23:23', '%Y/%m/%d %H:%M:%S'))
"""
%a：星期几的简写
%A：星期几的全称
%b：月份的简写
%B：月份的全称
%c: 星期几的简写 月份的简写 日 时:分:秒 年  Sat Aug 24 15:50:54 2019
%d：日
%H：小时，0-23
%l：小时，01-12
%j：一年的第几天
%m：月
%M：分钟，01-59
%p：am或pm
%S：秒，0-60
%u：星期几，1-7
%U：第几周
%w：星期几，1-7
%W：第几周
%x：当前格式的日期，08/20/19————》2019年8月20号
%X：当前格式的时间，17:38:15
%y：年份的后两位，00-99
%Y：年
"""

# ————————————》 datetime 模块：
"""       
print(datetime.datetime.now)                            # 2019-08-24 16:11:30.152527
print(datetime.date.fromtimestamp(time.time()))         # 2019-08-24
时间的加减：
print(datetime.datetime.now() + datetime.timedelta(3))      # 2019-08-27 16:14:26.766939
print(datetime.datetime.now() + datetime.timedelta(-3))         # 当前时间 减 3 天
print(datetime.datetime.now() + datetime.timedelta(hours=4))    # 当前时间 加 4 个小时 
print(datetime.datetime.now() + datetime.timedelta(minutes=2))  # 当前时间 加 2 分钟
时间的替换:
c_time = datetime.datetime.now()
print(c_time.replace(hour=2, minute=10, day=22, month=7, year=2018, second=10, microsecond=10))
# 2018-07-22 02:10:10.000010
"""


# 动态显示进度条


def progress(self=20):
    import time
    print('执行开始了'.center(self // 2, '-'))        # center 不认识浮点型
    start = time.time()                             # time.perf_counter() 相等的意思
    for i in range(self+1):
        time.sleep(0.2)
        a = '*' * i
        b = '.' * (self-i)
        c = (i / self) * 100
        dur = time.time() - start
        print('\r\033[30m{:^3.0f}%\033[0m\033[31m[{}->{}]\033[0m'   # ^ 左对齐 3 宽度
              '\033[32m{:.2f}s\033[0m'.format(c, a, b, dur), end='')
        # print('\r{:^3.0f}% {}{} {:.2f}s'.format(percentage, left, right, run_time), end='')
        # print('\r%-3.0f%% %s%s %.2fs' % (percentage, left, right, run_time), end='')
    print('\n' + '执行结束了'.center(self // 2, '-'))


if __name__ == '__main__':
    progress(40)

