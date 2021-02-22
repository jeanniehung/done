# ***********七个必须掌握的魔法************（
# （split）分割
"""
s = 'shhsahsakd'
v1 = s.partition('h')    #从左边开始找，找到第一个h开始分割，将原来字符串分割成三份
v2 = s.rpartition('h')   #从右边开始找，找到第一个h开始分割，将原来字符串分割成三份
#v3 = s.split('h',a)      #从左边开始找，找到h开始分割，a规定找几个h，分割成几份，但是看不看h
#v4 = s.rsplit('h',a)     #从右边开始找，找到h开始分割，a规定找几个h，分割成几份，但是看不看h
print(v1,v2,v3,v4)
"""
# 只能根据换行分割
"""
s = 'sjsjs\nssjssssa\naaaaddd'
v = s.splitlines(False)     #参数True显示\n,False不显示\n
print(v)
"""
# （strip）去除空白；出去\t \n;去除指定字符，有限最多匹配移除；最先去除空白
"""
s = ' \n hjc'
v1 = s.lstrip('h')      #去除左边空白
v2 = s.rstrip()         #去除左边空白
v3 = s.strip()          #去除左边空白
print(v1,v2,v3)
"""
# （join）将字符串中的每一个元素按照分隔符进行拼接，在其他数据类型可能也会用到
"""
s = '洪吉昌超级帅'
print(s)
t = '帅到爆炸'
v = t.join(s)
print(v)
"""
# （find）从开始往后找，找到第一个目标后，获取其位置(字符串(0-7)第一个位置是0);从第a位置开始到第b个位置结束去找
# -1表示没有找到
"""
v = test.find('x',a,b)
print(v)
#找不到直接报错
v = test.index('x',a,b)
print(v)
"""
# （lower）判断是否都是小写
"""
s = 'Hjc'
s1 = s.lower()      #s内的内容全部改为小写
print(s1)
v = s1.islower()
print(v)
"""
# （upper）判断是否全部大写
"""
s = 'Hjc'
s1 = s.upper()      #s内的内容全部改为大写
print(s1)
v = s1.isupper()
print(v)
"""
# 替换
"""
s = 'abcabcabc'
v = s.replace('b','洪',2)    #前两个b替换为洪
print(v)
"""
# ***********灰魔法************（其他数据类型也可以使用）
# 索引，下标，获取字符串中的某一字符
"""
s = 'hjcnb'
v = s [2]
print(v)
#切片
v = s[2:-1] #2=< [] <(-1)其中0是h，-1是b
print(v)
"""
# 获取当前字符串由几个字符组成（python3才可以使用)
"""
s = 'code'
v = len(s)
print(v)
li = [11,22,33,44,55,'aaahjc']      #列表长度
v = len(li)
print(v)
"""
# for循环
# 格式：
# for 变量名 in 字符串
# print(变量名)
"""
s = '爽爽有种冲我来'
for hjc in s:
    print(hjc)
s = '爽爽有种和我一起玩'
count =0
while   count < len(s):
    v = s [count]
    print(v)
    count+=1
"""
# 帮助创建连续的数字,通过步长（5）创建不连续的数字
"""
v = range(0,10,5)
for n in v:
   print(n)
"""
# 将文字对应的索引打印出来
"""
s = input('>>>')
n = len(s)
r = range(0,n)
for hjc in r:
    print(hjc, s[hjc])

s = input('麻溜的:')
for t in range(0,len(s)):
    print(t,s[t])
"""
# 生成随机验证码2
"""
def check_code():
    import random
    checkcode = ''
    for i in range(4):
        current = random.randrange(0,4)
        if current != i:
            temp = chr(random.randint(65,90))
        else:
            temp =random.randint(0,9)
        checkcode += str(temp)
    return checkcode
code = check_code()
print(code)
code = input('>>>')
"""