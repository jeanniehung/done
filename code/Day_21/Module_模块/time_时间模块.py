import time


# 推迟运行时间
"""
time.sleep(n)   推迟n秒运行
"""
# 时间差
"""
time.clock()
"""
# 一：（timestamp）时间戳，用于计算时间长度
start_time = time.time()
"""
中间写上一些代码
"""
stop_time = time.time()
print(stop_time - start_time)   # 用于计算代码运算时长
print(time.time())  # 打印当前从1970到当前时间经过了多少秒
# 二：（stuck_time)结果化时间————》当地时间
print(time.localtime())
t_l = time.localtime()
print(t_l.tm_wday)  # 显示星期几，0是星期一
print(t_l.tm_yday)  # 显示一年的第几天
print(t_l.tm_year)  # 显示那一年
print(t_l.tm_mon)   # 显示那个月
print(t_l.tm_mday)  # 显示几号
print(t_l.tm_hour)  # 显示几点
print(t_l.tm_min)   # 显示第几分钟
print(t_l.tm_sec)   # 显示第几秒
# （stuck_time)结果化时间————》UTC时间，中国在东八区
print(time.gmtime())
# # 三：（format string）字符串标准时间
# """
# import datetime
# print(datetime.datetime.now) # 格式更适合我们
# """
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
%Y：年
%y：年份的后两位，00-99
%m：月
%d：日
%a：星期几的简写
%A：星期几的全称
%u：星期几，1-7
%b：月份的简写
%B：月份的全称
%H：小时，0-23
%l：小时，01-12
%M：分钟，01-59
%S：秒，0-60
%p：am或pm
%x：当前格式的日期，08/20/19————》2019年8月20号
%X：当前格式的时间，17:38:15
"""
