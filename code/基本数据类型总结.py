"""
一：数字（int）
v = int（）       #转化为数字类型
二：字符串（str）
replace(替换)
find:从左到右查找第一个指定字符对应的位置
join：a.join(b)————》把a拼接到b的每一个空袭中
strip：删除两边的空格；\t\n;指定字符
split：从左到右以指定字符进行分割，不显示指定字符， splitlines：换行分割，True显示\n False不显示
startswith：判断是否以什么指定字符开头，可加参数规定该范围是否以该指定字符开头
endswith：判断是否以什么指定字符结尾，可加参数规定范围是否以该指定字符结尾
lower：字符串全部小写
upper：字符串全部大写
三：列表（list）
append：添加元素到列表，添加元素是一个列表，只算一个元素
extend：列表扩展，添加元素是一个列表，内有几个元素就添加几个元素
insert：在指定位置插入元素，第一个参数确定位置，第二个参数为添加的元素
索引：li [a]
切片:li [a:b]
循环:for 循环；while循环
四：元祖（tuple）
索引；tu [a]
切片:tu [a:b]
循环:for 循环；while循环
一级元素不能修改，有序
五：字典（dict）
get:根据key取值，key不存在时，可通过参数指定值替代默认值（None）给不存在的key，但是不显示在词典中
格式：v = dic.get(key,value)
update：更新,原有信息覆盖，新信息添加————》格式：dic.update({key:value})
keys:输出字典中所有的key              #dict_keys(['k1', 2, 'k3'])
values：输出字典中所有的value          #dict_values([18, '洪吉昌', 'True'])
items：输出字典中所有的key和value     #dict_items([('k1', 18), (2, '洪吉昌'), ('k3', 'True')])
索引：无序，dic [key]...
for循环
"""
#基本数据类型
#一：整数型（int）
#1：化为整型
a = '123'
b = int (a)
print(a)
#2:用二进制表示需要多少位
age = 9
v = age.bit_length()
print(v)
#二：布尔值:bool（True：1，False：0）
v = bool(None)  #0,'',(),{},[]
print(v)
#三：字符串（str):字符串一旦创建，就不可被修改；一旦修改或者拼接，就会生成新的字符串
test = 'hongJIchang'
#只有首字母大写
v = test.capitalize()
print(v)
#全部小写
v = test.casefold()
print(v)
v = test.lower()
print(v)
#判断是否都是小写
v = test.islower()
print(v)
#全部大写
v = test.upper()
print(v)
#判断是否都是大写
v = test.isupper()
print(v)
#大小写相互转化
v = test.swapcase()
print(v)
#是否全是数字
test = '8888'
v = test.isdecimal()
print(v)
v = test.isdigit()
print(v)
v = test.isnumeric()
print(v)
#是否是数字和字母
test = 'hjc666'
v = test.isalnum()
print(v)
#是否是字母和汉字
test = '洪吉昌sb'
v = test.isalpha()
print(v)
#是否是标识符（变量）
test = 'hjc_123'
v = test.isidentifier()
print(v)
#查找子序列出现的次数
test = 'hongjijichang'
v = test.count('j',0,-1)
print(v)
#以什么开头，以什么结尾
v = test.startswith('g',3,7)
print(v)
v = test.endswith('c',2,9)
print(v)
#从左往右找，找到第一个规定参数显示其位置，可加参数规定其寻找范围，找不到输出-1
v = test.find('j',8,9)
print(v)
#找不到直接报错
v = test.index('j',1,9)
print(v)
#判断是为不可显示字符
test = '\n'
v = test.isprintable()
print(v)
#判断是否为标题
test = 'hong ji chang 帅'
v = test.title()        #转为标题
print(v)
v = test.istitle()
print(v)
#判断是否为空格
test = '    '
v = test.isspace()
print(v)
#插空拼接
test = '洪吉昌好帅'
temp = '——'
v = temp.join(test)
print(v)
#设置长度，并将内容显示在左边，右边，中间
test = '洪吉昌'
v = test.center(20,'帅')
print(v)
v = test.ljust(20,'@')
print(v)
v = test.rjust(20,'%')
print(v)
v = test.zfill(20)
print(v)
#断句，制表
test = 'name\tage\ttel\n洪吉昌\t19\t111\n洪吉昌\t19\t111\n洪吉昌\t19\t111\n'
v = test.expandtabs(20)
print(v)
#去除空白；\t\n;指定字符
test = ' 洪吉昌 '
v = test.strip()
print(v)
v = test.lstrip()
print(v)
v = test.rstrip()
print(v)
#制作模版，格式化
test = '{0}{1}'
v = test.format('洪吉昌','帅')
print(v)
test = '{name},{a}'
v = test.format(name='洪吉昌',a=19)
print(v)
v = test.format_map({'name':'洪吉昌','a':19})
print(v)
#替换
test = '洪吉昌'
v = test.replace('洪','帅')
print(v)
test = '洪吉昌'
temp = '无敌帅'
m = str.maketrans(test,temp)
item = '洪吉昌洪吉昌'
v = item.translate(m)
print(v)
#分割
test = 'hongjijichang'
v = test.partition('j')
print(v)
v = test.rpartition('j')
print(v)
v = test.split('j')
print(v)
v = test.rsplit('j',2)
print(v)
#换行分割
test = 'hong\ntest\nhahha\n111'
v = test.splitlines(True)
print(v)
#索引
test = 'hong'
v = test[2]
print(v)
#切片
v = test[0:-1]
print(v)
#显示字符串长度
v = len(test)
print(v)
#for循环
for item in test:
    print(item,type(item))
count = 0
l = len(test)
while count < l:
    v = test[count]
    print(v)
    count += 1
#创建连续，不连续的数字
v = range(0,10,2)
for item in v:
    print(item)
#将字符串对应的索引打印出来
# test = input('陛下请题字：')
# l = len(test)
# r = range(0,l)
# for item in r:
#     print(item,test[item])
#四：列表（list）：列表中的元素可以被修改
#列表的修改，删除
#a:索引修改，删除
li = [1,2,3,4,'洪吉昌','_']
li [1] = '帅比'
print(li)
li [3] = [22,33,4,66]
print(li)
del li[3]
print(li)
#b：切片修改，删除
li [1:2] = ''
print(li)
li [1:2] = ['洪吉昌真78帅']
print(li)
del li [0:3]
print(li)
#in 操作
li = [1,2,3,4,'洪吉昌','_']
v = 2 in li
print(v)
#索引取值
v = li[2]
print(v)
#列表有序
li = [1,2,3,4,[0,1,2,('帅',1,2)],'洪吉昌','_']
v = li[4][3][0]
print(v)
#切片取值
li = [1,2,3,4,'洪吉昌','_']
v = li[0:2]
print(v)
#for循环
for item in li :
    print(item)
#数据类型的相互转化
#————》整数型   int（）
#————》布尔值   bool（）
#————》列表     list()
#————》元祖     tuple()
#————》字典      dict（）
#转化为字符串是有两种情况：
#a：既有数字又有字符串
s = ''
li = [1,2,3,4,'洪吉昌','_']
for item in li :
    s = s + str(item)
print(s)
#b:全是字符串
li = ['洪吉昌','zhen爽']
v = ''.join(li)
print(v)          #age洪吉昌
#原来值追加
li = [1,2,3,4,'洪吉昌','_']
li.append(['帅',666])
print(li)
#扩展原列表
li = [1,2,3,4,'洪吉昌','_']
li.extend(['帅',666])
print(li)
#清空列表
li.clear()
print(li)
#浅复制
li.copy()
print(li)
#计算元素出现的次数
li = [1,2,3,4,'洪吉昌','_',2,2,3,4,3,4,2]
v = li.count(2)
print(v)
#寻找目标元素从左到右的第一个位置，可添加参数规定寻找范围
li = [1,2,3,4,'洪吉昌','_',2,2,3,4,3,4,2]
v = li.index(2,0,9)
print(v)
#删除某个值，并或得该值，不加参数默认最后一个，添加参数规定删除那个位置的元素
li = [1,2,3,4,'洪吉昌']
v = li.pop(0)
print(li,v)
#删除指定的一个元素，左边优先
li = [1,2,3,4,'洪吉昌',2]
li.remove(2)
print(li)
#从指定位置插入元素，第一个参数规定位置，第二个参数规定元素
li = [1,2,3,4,'洪吉昌']
li.insert(1,'帅')
print(li)
#当前元素列表进行翻转
li = [1,2,3,4,'洪吉昌']
li.reverse()
print(li)
#列表的排序，只能是字符串
li = ['hahah1','好帅呀','洪吉昌']
li.sort(reverse=False)
print(li)
#五：元祖（tuple）
#1：索引取值
tu = (1,'洪吉昌',[11,22,33,('hjc',1)],)
v = tu [2]
print(v)
#2:切片取值
tu = (1,'洪吉昌',[11,22,33,('hjc',1)],)
v = tu[0:3]
print(v)
#for 循环
for item in tu:
    print(item)
#while 循环
count = 0
l = len(tu)
while count < l:
    v = tu[count]
    print(v)
    count += 1
#4:数据类型的相互转化————》上同

#5：元祖，有序
tu = (1,'洪吉昌',[11,22,33,('hjc',1)],)
v = tu [2][3][0]
print(v)
#6;元祖的一级元素不可被增删改查
tu = (1,'洪吉昌',[11,22,33,('hjc',1)],)
tu[2][3]= '洪吉昌'
print(tu)
del tu[2][3]
print(tu)
#7:获取元祖中指定元素出现的次数
tu = (1,'洪吉昌',[11,22,33,('hjc',1)],1,44,1,)
v = tu.count(1)
print(v)
#8:寻找指定元素的位置，从左到右,找不到直接报错，可加参数规定寻找范围
tu = (1,'洪吉昌',[11,22,33,('hjc',1)],1,44,1,)
v = tu.index(1,0,9)
print(v)
#六：字典（dict）
#基本格式：{key:value,keay1:value1}  key 不可是字典，列表；value可以是任意的
dic = {1:'洪吉昌','k2':2222}
print(dic)
#1：字典是无序的

#2:索引取值————》由于字典无序，所以用key索引
dic = {1:'洪吉昌','k1':123,False:[],123:['kk1',123,(),{'kk1':123,1:'hjc'}]}
v = dic[123][3]['kk1']
print(v)
#3：字典的删除
del dic[123][2]
print(dic)
#4：for 循环
for item in dic:            #默认输出keys
    print(item)
for item in dic.keys():     #输出keys
    print(item)
for item in dic.values():   #输出values
    print(item)
for item in dic:            #输出key value
    print(item,dic[item])
for item in dic.items():   #输出（key，value）
    print(item)
#5：字典清理
dic = {1:'洪吉昌','k1':123,False:[],123:['kk1',123,(),{'kk1':123,1:'hjc'}]}
dic.clear()
print(dic)
#6:浅拷贝
dic.copy()
print(dic)
#7:根据序列，创建字典，并指定kkey value
v = dict.fromkeys([123,'k1',True],'洪吉昌')
print(v)
#8：根据key取值，key不存在时，输出None，可通过参数改变None，key存在时,输出key对应的value值
dic = {'k1':18,2:'洪吉昌','k3':'True'}
v = dic.get('1','帅气')
print(v)
#9：根居字典的key value 还有kay和value配对
dic = {'k1':18,2:'洪吉昌','k3':'True'}
v = dic.keys()
print(v)
v = dic.values()
print(v)
v = dic.items()
print(v)
#10:更新，原有数据覆盖，新信息添加
dic.update({'k1':111,'k4':'滚'})
print(dic)
#11:删除并获取key对应的value值，当key不存在时，添加参数输出参数，不加参数，报错；当key存在时,返回key对应当value值
v = dic.pop('k11',2)
print(dic,v)
v = dic.pop('k1')
print(v,dic)
#随机删除
k,v = dic.popitem()
print(k,v)
#12:设置值，如果key已存在，输出对应当value值，字典内容不变;
# 若key不存在，添加新key到字典中，不输入value参数，其对应到值为None
dic = {'k1':18,2:'洪吉昌','k3':'True'}
v = dic.setdefault('k2',1)
print(v,dic)
#13：判断是否在key里，value里
dic = {'k1':18,2:'洪吉昌','k3':'True'}
v = 'k1' in dic
print(v)
v = 18 in dic.values()
print(v)