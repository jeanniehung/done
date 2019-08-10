#变量：
#可变类型：变量中元素改变，变量对应的id号不变（id（变量名））：列表，字典
#不可变类型：变量中元素改变，变量对应的id号改变：字符串，数字，元祖
"""
集合：
1：不同元素组成
2：无序
3：集合的元素是不可变类型：字符串，数字，元祖
基本格式：set = {}
"""
#不同元素组成
set = {1, 1, 2, 3, 'hello', (1, 'world')}
print(set,type(set))
#元素的添加,只能添加1个元素
set = {1, 1, 2, 3, 'hello', (1, 'world')}
set.add('洪吉昌')
print(set)
#集合的清除
set = {1, 1, 2, 3, 'hello', (1, 'world')}
set.clear()
print(set)
#集合的复制
set = {1, 1, 2, 3, 'hello', (1, 'world')}
s1 = set.copy()
print(s1)
#集合元素的删除
set = {1, 1, 2, 3, 'hello', (1, 'world')}
set.pop()               #随机删除
print(set)
set.remove('hello')     #指定元素删除，元素不存在集合时，报错
print(set)
set.discard('1')        #指定元素删除，元素不存在集合时，不会报错
print(set)


#两集合求交集
s1 = {1, 2, 'hello'}
s2 = {1, ('hjc', 1)}
s = s1.intersection(s2)         #   s = s1 & s2
print(s)
#两集合求并集
s = s1.union(s2)                #   s = s1 | s2
print(s)
#两集合求差集
s = s1.difference(s2)           #   s = s1 - s2
print(s)
s1.difference_update(s2)
print(s1)
#两集合求交叉补集
s = s1.symmetric_difference(s2)      # {2, ('hjc', 1), 'hello'}      s = s2 ^ s1
print(s)


#是否有交集，有显示False，没有显示True
s1 = {1, 2}
s2 = {2, 3}
s = s1.isdisjoint(s2)
print(s)
#判断是s1是不是s2的子集合
s1 = {1, 2}
s2 = {1, 2, 3}
s = s1.issubset(s2)     # s = s1 < s2
print(s)
#判断是s1是不是s2的父集合
s1 = {1, 2, 3}
s2 = {1, 3, 'hello'}
print(s)
s = s1.issuperset(s2)   # s = s1 > s2
print(s)
#更新信息,更新多个值,可迭代对象都可以传
s1 = {1, 2, 3}
s1.update('洪吉昌', '帅')
print(s1)           #{1, 2, 3, '吉', '帅', '洪', '昌'}
s1 = {1, 2, 'hello'}
s1.update([1,2,'洪吉昌'])
print(s1)
#不可变集合
s = frozenset('hello')
print(s)
#可变集合
# s = set('hello')
# print(s)
#不考虑顺序，简单去重
# tu = (1,2,3,1,'洪吉昌','洪吉昌')
# tu = tuple(set(tu))
# print(tu)           #(1, 2, 3, '洪吉昌')