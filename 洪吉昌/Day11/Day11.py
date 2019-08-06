#字母大小写的改动与判断
test = 'hongJIchang'
#字符串首字母大写
v = test.capitalize()
print(v)
#字符串所有字母小写
v = test.casefold()
print(v)
v = test.lower()
print(v)
#判断字符串所有字母是否都是小写
v = test.islower()
print(v)
#字符串所有字母大写
v = test.upper()
print(v)
#判断字符串所有字母是否都是大写
v = test.isupper()
print(v)
#字符串所以字母大写改小写，小写改大写
v = test.swapcase()
print(v)
#寻找字符串的子序列的位置与字符串判断
test = 'hongjijichang'
#字符串中子序列出现的次数，可加参数规定其寻找的范围，字符串的第一个位置为0
v =test.count('j',1,9)
print(v)
#判断字符串以什么开头
v = test.startswith('h',0,13)
print(v)
#判断字符串以什么结尾
v = test.endswith('g',0,13)
print(v)
#字符串中从左往右找，找到第一个子序列，显示出其位置，可加参数规定其寻找范围,
#找不到输出-1
v = test.find('j',1,9)
print(v)
#找不到直接报错
v = test.index('j',1,9)
print(v)
#判断数字，字母，汉字，变量
#判断是否含有数字，字母，或二者之一，有则显示True，无则显示False
test = 'hjc666'
v = test.isalnum()
print(v)
#判断是否只含有数字
test = '88888'
v1 = test.isdecimal()   #十进制数字
v2 = test.isdigit()     #十进制数字+特殊字符数字
v3 = test.isnumeric()   #十进制数字+特殊字符数字+中文数字
print(v1,v2,v3)
#判断是否含有字母，汉字，或者二者之一，
test = 'hjc好帅'
v = test.isalpha()
print(v)
#判断是否含有字母，数字，下划线（变量不能以数字开头），或者三者其中，
test = 'hjc_123'
v = test.isidentifier()
print(v)
#判断是否存在不可显示的字符
test = '\t'
v = test.isprintable()
print(v)
#判断是否全是空格
test = '  '
v = test.isspace()
print(v)
#判断是否为标题
test = 'Abc hong ji chang'
v = test.title()    #将test改为标题（标题每个单词首字母必须大写）
print(v)
v = test.istitle()
print(v)
#将字符串中的每一个元素按照分隔符进行拼接，插入空档中
test = '吉昌'
temp = '洪宋魏'
v1 = test.join(temp)    #洪吉昌宋吉昌魏
print(v1)
s = '无敌'
v = s.join(v1)          #洪无敌吉无敌昌无敌宋无敌吉无敌昌无敌魏
print(v)
#设置长度，并将内容居中（最左边，最右边）
test = '洪吉昌'
v1 = test.center(20,'!')
print(v1)
v2 = test.ljust(20,'!')
print(v2)
v3 = test.rjust(20,'!')
print(v3)
v4 = test.zfill(20)         #填充内容默认为0,内容在最右边
print(v4)
#断句，\t为制表符，\n为分行符
test = 'name\tage\tschool\n洪吉昌\t19\t青海民族大学\n黄劢\t22\t青海民族大学\n吕嘉行\t20\t青海民族大学\n'
v = test.expandtabs(20)
print(v)
#去除空白,去除\t,\n；去除指定字符
test = '\t hjc \t'
v = test.strip()
print(v)
v = test.lstrip()
print(v)
v = test.rstrip()
print(v)
#格式化，将一个字符串的占位符替换成指定的量
test = 'i an {name},age {a}'
print(test)
v = test.format_map({'name':'洪吉昌','a':19})
print(v)
v = test.format(name='洪吉昌',a=19)
print(v)
test = 'i am {0},age {1}'
v = test.format('洪吉昌',19)
#替换
test = '洪吉昌'
test1 = '大帅b'
m = str.maketrans(test,test1)
v = '洪吉昌你好'
v1 = v.translate(m)
print(v1)
#替换
test = 'abcabcabc'
v = test.replace('b','洪',2)
print(v)
#分割（split，rsplit，partition，rpartition）
test = 'abcdabcdabcd'
v = test.partition('b')
print(v)
v = test.rpartition('b')
print(v)
v = test.split('b',2)
print(v)
v = test.rsplit('b',2)
print(v)
#换行分割,
test = 'abcd\nabcd\nabcd\nabcd'
v = test.splitlines(False)
print(v)
#索引
test = 'abcdabcd'
v = test[3]
print(v)
#切片
test = 'abcdabcd'
v = test [1:-1]
print(v)
#获取字符串是有几个字符组成
test = '111111hjc!_['
v = len(test)
print(v)
list = [11,22,33,'44','hjc','洪吉昌','_','!']
v = len(list)
print(v)
#for循环
test = '小帅哥快来玩啊'
count = 0
while count < len(test):
    v = test[count]
    print(v)
    count += 1
for r in test:
    print(r)
#创建连续的数字,第三位数是步长，在这个范围的步长的所有公倍数
v = range(0,10,2)
for r in v:
    print(r)
#将文字对应的索引打印出来
test = input('麻溜的:')
l = len(test)
r = range(0,l)
for n in r:
    print(test[n],n)

test = input('麻溜的：')
for n in range(0,len(test)):
    print(test[n],n)
#制作随机验证码，不区分大小写,可无限次输入,直到输入正确为止
while  True:
    def check_code():
        import random
        checkcode = ''
        for i in range(4):
            current = random.randrange(0,4)
            if current != i:
                temp = chr(random.randint(65,90))
            else:
                temp = random.randint(0,9)
            checkcode += str(temp)
        return checkcode
    code1 = check_code()
    print(code1)
    code2 = input('请输入验证码：')
    c1 = code1.upper()
    c2 = code2.upper()
    if c1 == c2:
        print('登陆成功')
    else:
        print('验证妈输入输入有误，请重新输入')

