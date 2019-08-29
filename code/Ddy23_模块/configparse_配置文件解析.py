import configparser
"""
DEFAULT 这个块只可以有一个
不区分大小写
配置文件的格式：
    [section]
        k1 = k2 
        k3 : k4
配置文件相当于字典嵌套，section 相当于大字典的key;k1,k3相当于小字典的key
"""
# ————————》创建一个配置文件
import configparser
config = configparser.ConfigParser()      # 相当于一个空字典
config['DEFAULT'] = {
    'name': '洪吉昌',
    'age': 18,
    'gender': 'male'
}
config['宋梦娜'] = {}
config['宋梦娜']['name'] = '宋梦娜'

config['魏宽怀'] = {}
con = config['魏宽怀']
con['name'] = '魏宽怀'
con['age'] = '180'              # 必须是字符串
con['gender'] = 'male'

config['洪淑芳'] = {
    'name': '洪淑芳',
    'age': 18,
    'gender': 'female'
}

with open('example.ini', 'w') as f:
    config.write(f)


# ————————————》对配置文件的增删改查
config = configparser.ConfigParser()        # 得倒的是一个迭代对象
config.read('example.ini')
# ————————————》查
for i in config:                # 将所有的标题一个一个打印出来
    print(i)
for i in config['洪淑芳']:       # 遍历标题下的 key 会加上 DEFAULT 下的所有key
    print(i)                    # 标题的key 和 DEFAULT 的key相同是就不显示
# 查看所有的标题
print('宋梦娜' in config)              # True
print(config.sections())              # ['宋梦娜', '魏宽怀', '洪淑芳'] DEFAULT 不显示
# 查看标题下的所有的 key
print(config.options('洪淑芳'))        # ['name', 'age', 'gender', 'name1', 'age1', 'gender1']
# 查看标题下的所有的 （key， value）
print(config.items('洪淑芳'))
# 查看标题下 key 对应的 value   也可以取默认标题下的 key
print(config.get('洪淑芳', 'name1',))              # 取字符串
print(config.getint('洪淑芳', 'age',))             # 取整型
print(config.getfloat('洪淑芳', 'age',))           # 取浮点型
print(config.getboolean('魏宽怀', 'is_admin'))     # 取bool类型的值
# 判断是否存在某个标题,返回布尔值
print(config.has_section('洪淑芳'))
# 判断标题下的 key 是否存在
print(config.has_option('洪淑芳', 'age'))

# ————————————》改写

# 添加一个标题
config.add_section('alex')
config.add_section('nb')

# 添加标题下的 key, value
config.set('alex', 'name', 'alex')
config.set('alex', 'age', '18')                 # 必须是字符串

# 删除标题下的 key
config.remove_option('alex', 'age')
config.remove_option('alex', 'name')

# 删除一个标题
config.remove_section('alex')


# 将修改的内容写入文件,修改完一定要有的操作，这种操作不要自己关闭文件
config.write(open('example.ini', 'w'))      # 可以是原文件也可以新文件

