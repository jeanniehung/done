#用户登陆
"""
n1=input('请输入用户名:')
n2=input('请输入密码:')
print(n1)
print(n2)
"""
#变量
"""
n1="hjc_123"
n2="好省昌"
print(n1)
print(n2)
"""
#条件语句
#如果1等于1，那么就输出 欢迎进入第一会所，否则就输出 欢迎进入一本道
"""
if 1==1:
    print('欢迎进入第一会所')
    print('欢迎进入第一会所1')
else:
    print('欢迎进入一本道')
print('开启嘿嘿嘿模式')
"""
#if else嵌套
"""
if 1==1:
    if 2==2:
        print('欢迎进入第一会所')
        print('欢迎进入第一会所1')
    else:
        print('欢迎进入东京热')
else:
    print('欢迎进入一本道')
"""
#if elif
"""
inp = input('请输入会员级别:')
if inp == "高级会员":
    print('美女')
elif inp =="白金会员":
    print('超模')
elif inp =="铂金会员":
    print('一线小明星')
else:
    print('黄劢')
print('开启嘿嘿嘿模式')
"""
#输入一整数判断其是偶数还是奇数
"""
a = input('请输入整数:')
temp = int(a) % 2  #把字符串a化为整数类型
if temp ==0:
    print('整数')
else:
    print('奇数')
"""
#死循环
"""
while 1==1:
    print('洪吉昌')
"""
#作业
#1:使用while循环输入1 2 3 4 5 6   8 9 10
"""
count= 1
while count< 11:
    if count==7:
       pass
    else:
        print(count)
count= count+1
"""
"""
count=1
while count <11:
    if count ==7:
        count=count+1
        continue#count=7时不输出，直接回到从8开始循环
    else:
        print(count)
    count=count+1
"""
#2:求1-100所有数的和
"""
n=1
s=0
while n<101:
    s=s+n
    n=n+1
print(s)
"""
#3:输出1-100内所有的奇数
"""
n=1
while n<101:
    a=n%2
    if a==0:
        pass
    else:
        print(n)
    n=n+1
"""
#4:输出1-100内所有的偶数
"""
n=1
while n<101:
    a=n%2
    if a==0:
        print(n)
    else:
        pass
    n=n+1
"""
#5:求1-2+3-4+5-...+99所有数的和
"""
n=1
s=0
while n<100:
    a=n%2
    if a==0:
        s=s-n
    else:
        s=s+n
    n=n+1
print(s)
"""
#6:用户登陆（三次机会重试）
"""
n=1
while n<4:
    n=n+1
    a1=input('请输入用户名:')
    a2=input('请输入密码:')
    if a1 == '洪吉昌' and a2 == '123':
        print('登陆成功')
        break
    else:
       print('用户名或密码错误')
"""
"""
n=1
while n<4:
    user = input('>>>')
    pwd = input('>>>')
    if user == 'alex' and pwd =='123':
        print('登陆成功')
        break
    else:
        print('用户名或密码错误')
    n=n+1
"""
# 判断某个东西是否在某个东西里包含
"""
name='洪吉昌'
if '洪昌' in name:    #not in :不在
    print('ok')
else:
    print('error')
"""
#将字符串转换成数字
"""
a = '777'
print(type(a),a)    #print(type()):输出括号内的数据类型
b = int(a,base=8)
print(type(b),b)
"""
#当前数字的二进制，至少n为来表示
"""
age = 4
r = age.bit_length()
print(r)
"""
"""
name = '洪吉昌'
if '洪吉' in name:
      print('你好帅')
else:
      print('你好丑陋')

name='洪吉昌'
if '洪昌' not in name:    #not in :不在
     print('ok')
else:
     print('error')

a = 'e'
b = int(a,base=16)
# print(type(b),b)

age = 10
v = age.bit_length()
print(v)
"""