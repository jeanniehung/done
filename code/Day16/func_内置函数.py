"""
1：abs()—————》取绝对值
2：all()————》序列的每一个元素做bool运算,全为真才是True，如果可迭代对象为空，也返回True
3：any()—————》序列的每一个元素做bool运算,有一个真是True
4：bin()————》十进制转为二进制
  hex()—————》十进制转为十六进制
  oct()————》十进制转为八进制
5：bool()————》转为布尔类型
   dict()
   enumerate()
6：bytes('你好'，encoding='utf8'，decode='utf8')————》编码，解码
bytes('你好'，encoding='gbk'，decode='gbk'  —————》decode默认用utf8，ascii码不能解码中文
7：chr()————》ascii码对应
8: dir()
9:divmod()————》取商，取余，用于分页
10：eval()————》1：把字符串里的数据结构给提取出来
               2：把字符串的表达式进行运算
11：hash()————》可hash的数据类型是不可变数据类型，不可hash的数据类型是可变数据类型
12：isinstance(1，int)————》判断数据类型
13：globals()————》全局变量
13：locals()————》局部变量
14：max()————》取最大值
    min()————》取最小值
"""
print(abs(-1))
print(all([1, 0, 1]))
print(divmod(10, 3))
