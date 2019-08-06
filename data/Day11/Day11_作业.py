#str--->bool
b = 'i'
a = bool(b)
print(a,type(a))

#1:执行python脚本的两种方式
#1：终端里输入python编译器的路径 + 文件路径
#2：终端中直接输入python进入编译器，在输入文件路径
#Linux操作系统可以通过chmod更改文件权限，直接    ./+文件路径


#2:简述位与字节的关系
#1字节等于8位---》1byte=8bit
#存储是以位为单位；计算机处理时以字节为单位

#3：
#最开始的时候是ascii；接着出现unicode；中国是utf8（unicode的压缩版）


#4：
#utf8一个汉字是3个字节；gbk一个汉字是两个字节



#5：python的单行注释：#    python的多行注释：""" """


#6:变量的组成：字母，数字，下划线（hjc_123）；不能以关键字重复；不能以数字开头


#7：bit_length;n=5由多少个二进制字节组成
n = 5
v = n.bit_length()
print(v)


#8：布尔值：True False
#   空字符串--》》False    字符串有内容--》》True
#   0--》》False       其他数字--》》True


#10
name = 'aleX'
v = name.strip()
print(v)
v = name.startswith('al')
print(v)
v = name.endswith('X')
print(v)
v = name.replace('l','p')
print(v)
v = name.split('l')
print(v)
#f不会
v = name.upper()
print(v)
v = name.lower()
print(v)
v = name[2]
print(v)
v = name[3]
print(v)
v = name[1:-1]
print(v)
v = len('e')
print(v)
v = name[0:-1]
print(v)


#21:
#可迭代对象————》》可以被for进行循环获取


#22:拼接
li = 'aaaabbbji'
v = '_'.join(li)
print(v)
li = ['alex','eric','rain']
v = '_'.join(li)
print(v)


#23:
#python 2 range:立即创建 xrange:for循环是一个一个创建
#python 3 range:for循环时一个一个创建


#24:
# 简单的计算器
value = input('>>>')
if '+' in  value:
    v1,v2 = value.split('+')
    print(v1, type(v1), v2, type(v2))
    v1 = int(v1)
    v2 = int(v2)
    print(v1, type(v1), v2, type(v2))
    v = v1 + v2
elif '-' in value:
    v1,v2 = value.split('-')
    print(v1, type(v1), v2, type(v2))
    v1 = int(v1)
    v2 = int(v2)
    print(v1, type(v1), v2, type(v2))
    v = v1 - v2
elif '*' in value:
    v1,v2 = value.split('*')
    print(v1, type(v1), v2, type(v2))
    v1 = int(v1)
    v2 = int(v2)
    print(v1, type(v1), v2, type(v2))
    v = v1 * v2
elif '/' in value:
    v1,v2 = value.split('/')
    print(v1, type(v1), v2, type(v2))
    v1 = int(v1)
    v2 = int(v2)
    print(v1, type(v1), v2, type(v2))
    v = v1 / v2
elif '%' in value:
    v1,v2 = value.split('%')
    print(v1, type(v1), v2, type(v2))
    v1 = int(v1)
    v2 = int(v2)
    print(v1, type(v1), v2, type(v2))
    v = v1 % v2
elif '//' in value:         #会直接去找/而不会来执行//
    v1,v2 = value.split('//')
    print(v1, type(v1), v2, type(v2))
    v1 = int(v1)
    v2 = int(v2)
    print(v1, type(v1), v2, type(v2))
    v = v1 // v2
elif '**' in value:         #会直接去找*而不会来执行**
    v1,v2 = value.split('**')
    print(v1, type(v1), v2, type(v2))
    v1 = int(v1)
    v2 = int(v2)
    print(v1, type(v1), v2, type(v2))
    v = v1 ** v2
else:
    pass
print(v)


#25:
# 用户输入的内容中有多少个十进制小数，几个英文字母
count1 = 0
count2 = 0
v = input('陛下请题字：')
for item in v:
    if item.isdecimal() == True:
        count1 += 1
    elif item.isalpha() == True:
        count2 += 1
    else:
        pass
print(count1)
print(count2)


#26：
#int 和 9 是类和对象的关系
#str 和 'hongjicahng' 是类和对象的关系


#27：
# 制作趣味模版程序
v1 = input('名字：')
v2 = input('地点：')
v3 = input('爱好：')
test = '敬可爱的{0},最喜欢在{1},地方干{2}'
v = test.format(v1,v2,v3)
print(v)


#28：
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


#29：
#开发敏感词过滤程序，比如'苍老师'改成'***','你'改成'%'
v = input('>>>')
v1 = v.replace('苍老师','***')
v2 = v1.replace('你','%')
print(v2)


#30：制作表格，循环提示输入用户名，密码，邮箱，表格长度不超过20个字符，如果用户输入q或Q表示不在继续输入
s = ''
while True:
    v1 = input('用户名:')
    v2 = input('密码：')
    v3 = input('邮箱；')
    test = '{0}\t{1}\t{2}\n'
    v = test.format(v1,v2,v3)
    s = s + v
    temp = input('请输入指令：')
    temp1 = temp.upper()
    if temp1 == 'Q':
        break
    else:
        pass
print(s.expandtabs(20))
