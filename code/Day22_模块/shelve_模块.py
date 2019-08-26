"""
shelve: shelve模块比pickle模块简单，只有一个open函数，返回类似字典的对象，
        可读可写;key必须为字符串，而值可以是python所支持的数据类型
相当于 python 里的字典类型
建的文件看不懂
"""
import shelve
f = shelve.open(r'shelve文件')        # 文件可以不存在
f['stu1_info'] = 1        # 等号前面是 key 后面是 value
f['stu2_info'] = {'name': '洪吉昌', 'age': 18}     # value 是python的字典类型还可以继续 key 取值
f['school_info'] = {'website': 'http://www.pypy.org', 'city': 'beijing'}

print(f['school_info']['city'])     # 文件得是开启状态才可以查看打印

f.close()


with shelve.open(r'a') as f:
    f['level'] = 1
    print(f['level'])
