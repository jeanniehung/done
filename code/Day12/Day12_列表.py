""""
列表：list（类）;有序的，元素可以被修改
列表的基本格式：li = [1,12,'age',['洪吉昌'],10]:中的元素是通过类创建的对象
特征:
a:中括号括起来；
b:,分割每个元素有n个，既有n+1个元素
c：列表中可以是数字，字符串，列表，布尔值，所有的都可以放进去
d：列表可以无限嵌套li=['age',[1,2,[True],'洪吉昌'],18]————》有3个元素
列表中的元素可以被修改
"""
li = [1,12,'age',['洪吉昌'],10]
#1：列表的修改，删除
#a：索引修改，删除
li[1] = '我'              #索引修改改成''该位置会有''这样的元素显示
print(li)
li[2] = [11,22,33,'无敌']
print(li)
del li[2]
print(li)
#b:切片修改，删除
li[1:2] = ''            #求片修改改成''该位置没有元素，等于删除该切片位置下的元素
print(li)
del li[1:2]
print(li)
#2：in 操作
v = 1 in li
print(v)

li = ['age',[1,2,[True,2,3],'洪吉昌'],18]
#3：索引取值————》取值类型不唯一
v = li[2]
print(v)
#列表有序
v = li[1][2][0]         #取到的元素是True，索引取值也支持嵌套
print(v)
#4：切片取值————》取值类型是列表
v = li[0:-1]
print(v)
#5：for循环
for item in li:
    print(item)
#6：while循环
count = 0
l = len(li)
while count < l:
    v = li[count]
    print(v)
    count += 1
#7：字符串转列表，内部使用了for循环
s = 'red'
v = list(s)
print(v)           #['r', 'e', 'd']
#8：列表转字符串
li = ['age',[1,2,[True],'洪吉昌'],18]
v = str(li)
print(v)           #'['age', [1, 2, [True], '洪吉昌'], 18]'
#a：列表中既有数字又有字符串，需要写for循环直接一个一个拼接
li = ['age',True,18]
s = ''
for item in li :
    s = s + str(item)
print(s)          #'ageTrue18'
#b:列表中只有字符串，直接使用join拼接
li = ['age','洪吉昌']
v = ''.join(li)
print(v)          #age洪吉昌

#list类中提供的方法

#1:原来值追加
li = [11,22,3,4]
li.append(['洪吉昌',666])      #[11, 22, 3, 4, ['洪吉昌', 666]]
print(li)
#2:扩展原列表，参数是可迭代对象
li = [11,22,3,4]
li.extend(['洪吉昌',666])      #[11, 22, 3, 4, '洪吉昌', 666]
print(li)
#3:清空列表
li = [11,22,3,4]
li.clear()
print(li)
#4:浅拷贝
li = [11,22,3,4]
v = li.copy()
print(v)
#5:计算元素出现的次数
li = [11,22,3,4]
v = li.count(22)
print(v)
#6：根据目标寻找第一个索引位置（从左往右）；可加参数规定寻找范围,找不到直接报错
li = [11,22,3,4]
v = li.index(22,0,3)
print(v)
#7：在指定位置插入元素，第一个参数插入位置，第二个位置插入元素的值
li = [11,22,3,4]
li.insert(0,'洪吉昌')
print(li)
#8:删除某个值，并获得该值，不加参数默认最后一个，添加参数（索引位置）规定位置，删除确定的值
li = [11,22,3,4]
v = li.pop(2)
print(li,v)
#9:删除指定的一个值，左边优先
li = [11,22,33,4,33]
li.remove(33)
print(li)
#10:将当前列表元素进行翻转
li = [11,22,3,4]
li.reverse()
print(li)
#11:列表的排序
li = ['洪吉昌','好帅','是']
li.sort(reverse=False)          #True，False
print(li)