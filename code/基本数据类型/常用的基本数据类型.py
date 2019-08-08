"""
一：数字（int）
v = int（）       #转化为数字类型
二：字符串（str）
replace(替换):不加参数默认全部修改，加了参数，参数是几改几个
find:从左到右查找第一个指定字符对应的位置
join：a.join(b)————》把a拼接到b的每一个空袭中
strip：删除两边的空格；\t\n;去除指定字符不可以和空格\t\n连用，否则无效
split：从左到右以指定字符进行分割，不显示指定字符，可加参数指定多少个指定字符分割，参数为0时表示不分割,
splitlines：换行分割，True显示\n False不显示
startswith：判断是否以什么指定字符开头，可加参数规定该范围是否以该指定字符开头
endswith：判断是否以什么指定字符结尾，可加参数规定范围是否以该指定字符结尾
lower：字符串全部小写
upper：字符串全部大写
三：列表（list）
append：添加元素到列表,只可以添加一个元素，该元素可以是任一形式，进入列表只算一个元素
extend：扩赞列表，只可以添加一个元素，该元素不可以是整数，布尔值；在按该元素中包含到元素一一添加到列表中
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
删除
for循环
"""

"""
整数
"""
#int化为整型
test = '123'
a = int(test)
print(a)
"""
字符串
"""
#replace:替换
test = '洪吉昌好丑丑死了丑丑的'
v = test.replace('丑','帅',1)
print(v)
#find查找
v = test.find('丑',0,-1)
print(v)
#join,拼接
v = '_'.join(test)
print(v)
#strip;去除空格；\t\n；去除指定字符只可以单独使用
test = '洪吉昌洪'
v = test.strip('洪')
print(v)
v = test.lstrip('洪')
print(v)
v = test.rstrip('洪')
print(v)
#split:指定字符分割，不显示指定字符,可加参数指定多少个指定字符分割，参数为0时表示不分割
test = 'hongjijichang'
v = test.split('j')
print(v)
v = test.rsplit('j',2)
print(v)
#换行分割splitlines，True显示换行符号
test = 'hong\nji\nchang\nshuai'
v = test.splitlines(True)
print(v)
#判断是否以指定字符开头，可加参数规定范围判断
test = 'hongjichang'
v = test.startswith('g',3,6)
print(v)
#判断是否以指定字符结尾，可加参数规定范围判断
v = test.endswith('c',3,7)
print(v)
#所有字母小写lower
test = 'hongJIchang'
v = test.lower()
print(v)
v = test.casefold()
print(v)
v = test.islower()
print(v)
#所有字母大写upper
v = test.upper()
print(v)
v = test.isupper()
print(v)
"""
列表
"""
#添加元素到列表,只可以添加一个元素，该元素可以是任一形式，进入列表只算一个元素
li = [1,'洪吉昌',False,('hjc',123,['帅',True,123])]
li.append([11,'洪吉昌',(True,'无敌')])
print(li)
#扩赞列表，只可以添加一个元素，该元素不可以是整数，布尔值；在按该元素中包含到元素一一添加到列表中
li = [1,'洪吉昌',False,('hjc',123,['帅',False,123])]
li.extend('洪吉昌')
print(li)       #[1, '洪吉昌', False, ('hjc', 123, ['帅', False, 123]), '洪', '吉', '昌']
#在指定位置插入元素
li = [1,'洪吉昌',False,('hjc',123,['帅',False,123])]
li.insert(0,'无敌')
print(li)
#索引取值
li = [1,'洪吉昌',False,('hjc',123,['帅',False,123])]
v = li[3][2][0]     #列表有序
print(v)
#切片取值
v = li[0:4]
print(v)
#索引删除，切片删除
del li[3][2][0]
print(li)
del li[0:4]
print(li)
#for循环：子迭代对象
li = [1,'洪吉昌',False,('hjc',123,['帅',False,123])]
for item in li:
    print(item)
#while循环
count = 0
l = len(li)
while count < l:
    v = li[count]
    print(v)
    count += 1
"""
元祖
"""
#索引取值
tu = (1,'洪吉昌',[True,2,('无敌',123,'k1')],'结束')
v = tu[2][2][0]         #元祖是有序到
print(v)
#切片取值
tu = (1,'洪吉昌',[True,2,('无敌',123,'k1')],'结束')
v = tu[0:4]
print(v)
#for循环
tu = (1,'洪吉昌',[True,2,('无敌',123,'k1')],'结束')
for item in tu:
    print(item)
#while循环
tu = (1,'洪吉昌',[True,2,('无敌',123,'k1')],'结束')
count = 0
l = len(tu)
while count < l:
    v = tu[count]
    print(v)
    count += 1
#元祖的一级元素不可被删除
tu = (1,'洪吉昌',[True,2,('无敌',123,'k1')],'结束')
del tu[2][1]        #嵌套的元祖一级标题也是一样
print(tu)
"""
字典
"""
#索引取值       无序，通过key索引
dic = {1:'hjc',False:'洪吉昌',(1,'无敌'):(2,'无敌',{'k11':123,'谁':True,2:[]}),'k5':123}
v = dic[(1,'无敌')][2][2]
print(v)                #[]
#删除
dic = {1:'hjc',False:'洪吉昌',(1,'无敌'):(2,'无敌',{'k11':123,'谁':True,2:[]}),'k5':123}
del dic[(1,'无敌')]
print(dic)
#for循环
dic = {1:'hjc',False:'洪吉昌',(1,'无敌'):(2,'无敌',{'k11':123,'谁':True,2:[]}),'k5':123}
#默认输出key
for item in dic:
    print(item)
for item in dic.keys():
    print(item)
#输出value
for item in dic.values():
    print(item)
#输出key和value
for item in dic:
    print(item,dic[item])      #1 hjc————》key value
for item in dic.items():
    print(item)                #(1, 'hjc')————》(key，'value')
#输出所有的keys
dic = {1:'hjc',False:'洪吉昌',(1,'无敌'):(2,'无敌',{'k11':123,'谁':True,2:[]}),'k5':123}
v = dic.keys()
print(v)            #dict_keys([1, False, (1, '无敌'), 'k5'])
#输出所有的values
dic = {1:'hjc',False:'洪吉昌',(1,'无敌'):(2,'无敌',{'k11':123,'谁':True,2:[]}),'k5':123}
v = dic.values()
print(v)            #dict_values(['hjc', '洪吉昌', (2, '无敌', {'k11': 123, '谁': True, 2: []}), 123])
#输出所有的keys和values
dic = {1:'hjc',False:'洪吉昌',(1,'无敌'):(2,'无敌',{'k11':123,'谁':True,2:[]}),'k5':123}
v = dic.items()
print(v)        #dict_items([(1, 'hjc'), (False, '洪吉昌'), ((1, '无敌'), (2, '无敌', {'k11': 123, '谁': True, 2: []})), ('k5', 123)])


#get:根据key取值key不存在时，可通过参数指定值替代默认值（None）给不存在的key，但是不显示在词典中；key存在时，取它对应的value值
dic = {1:'hjc',False:'洪吉昌',(1,'无敌'):(2,'无敌',{'k11':123,'谁':True,2:[]}),'k5':123}
v = dic.get('k6','赋值')
print(dic,v)
#update：更新信息，key存在覆盖，不存在添加
dic = {1:'hjc',False:'洪吉昌',(1,'无敌'):(2,'无敌',{'k11':123,'谁':True,2:[]}),'k5':123}
dic.update({'k6':'洪吉昌',1:'洪吉昌'})
print(dic)

#根据列表，创建字典
v = dict.fromkeys([1,'洪吉昌',False],123)
print(v)