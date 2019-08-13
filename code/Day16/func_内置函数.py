"""
1：abs()—————》取绝对值,只能放一个参数
2：all()————》一个序列的每一个元素做bool运算,全为真才是True，如果该序列为空，也返回True
3：any()—————》序列的每一个元素做bool运算,有一个真是True，如果该序列为空，也返回False
4：bin()————》十进制转为二进制        0b...
  hex()—————》十进制转为十六进制      0x...
  oct()————》十进制转为八进制         0o...
5：bool()————》转为布尔类型
   dict()
   enumerate()————》规定顺序从什么开始
   type()————》查看数据类型
   sum()————》求和
6：bytes('你好'，encoding='utf8'，decode='utf8')————》编码，解码
bytes('你好'，encoding='gbk'，decode='gbk'  —————》decode默认用utf8，ascii码不能解码中文
7：chr()————》ascii码对应的位置
   ord()————》位置对应的ascii吗
8: dir()————》如果没有参数调用，则返回当前作用域中的名称。
9: divmod()————》取商，取余，用于分页
10：eval()————》1：把字符串里的数据结构给提取出来
                d = {'hjc': 'hjc'}
                l = [1, 2, 3]
                print(eval(str(l))[1]) # 2

               2：把字符串的表达式进行运算
11：hash()————》可hash的数据类型是不可变数据类型，不可hash的数据类型是可变数据类型
12：isinstance(1，int)————》判断数据类型
13：globals()————》全局变量
    locals()————》局部变量
14：pwo(x,y,z)————》只有x和y：x**y ；有x,y,z： x**y%z
15:reversed()————》翻转
16：round()————》四舍五入
17：slice(0,2)————》[0:2]做切片
    l = 'hello'
    print(slice(0,4,2),start,stop,step)
18:vars()————》没有参数=locals()，有参数，显示成字典类型
19：import 导入模块，模块就是一个py文件 test
    模块是一个'test'字符串类型，t = _import_('test') ,t = test
20:file = open('new', 'a', encoding='utf-8')        new是文件名
   file.close()
20： sorted()————》相同数据类型排序
    max()————》取最大值
    min()————》取最小值
max和min的高级用法：
——比较元素是可迭代类型，相当于一个for循环取出元素一一进行比较
        ——不同数据类型之间不可进行比较
——从第一个元素第一个位置开始比（字典是无序的）,如果第一个位置分出结果，不需要在进行，依次进来 ，b>a,2>1;
"""
# zip函数
# 序列：列表，元祖，字符串
"""
格式：
zip(一个序列，一个序列)  
序列：列表，元祖，字符串
取其元素一一对应，左边多一个不显示，右边多一个不显示
"""
z = zip(('a', 'b', 'c'), (1, 2, 3))
print(list(z))      # [('a', 1), ('b', 2), ('c', 3)]

z = zip((1, 2, 4), ['a', 'b', 'c'])     # 得到的是一个内存地址，储存着信息
print(list(z))

age_dict = {'洪吉昌_age': 18, '魏宽怀_age': 200}
print(max(age_dict))                            # 比较的是keys
print(max(age_dict.values()))                   # 比较的是values
print(max(zip(age_dict.values(), age_dict)))    # 比较的是values，同时显现对应的key

age_list = [
    {'name': '洪吉昌', 'age': 18},
    {'name': '魏宽怀', 'age': 20},
    {'name': '洪淑芳', 'age': 28},
    {'name': '好省昌', 'age': 38}
]

m = max(age_list, key=lambda x: x.get('age'))
print(m)
m = max(age_list, key=lambda x: x['age'])
print(m)        # {'name': '好省昌', 'age': 38}

