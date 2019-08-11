# 变量：
# 可变类型：变量中元素改变，变量对应的id号不变（id（变量名））：列表，字典
# 不可变类型：变量中元素改变，变量对应的id号改变：字符串，数字，元祖

"""
集合：
1：不同元素组成
2：无序
3：集合的元素是不可变类型：字符串，数字，元祖
基本格式：set = {}
集合的作用：
    不考虑顺序，简单去重
    tu = (1,2,3,1,'洪吉昌','洪吉昌')
    tu = tuple(set(tu))
    print(tu)           # (1, 2, 3, '洪吉昌')
"""
# 不同元素组成
s = {1, 1, 2, 3, 'hello', (1, 'world')}
print(set, type(set))
# 元素的添加,只能添加1个元素
s = {1, 1, 2, 3, 'hello', (1, 'world')}
s.add('洪吉昌')
print(set)
# 集合的清除
s = {1, 1, 2, 3, 'hello', (1, 'world')}
s.clear()
print(set)
# 集合的复制
s = {1, 1, 2, 3, 'hello', (1, 'world')}
s1 = s.copy()
print(s1)
# 集合元素的删除
s = {1, 1, 2, 3, 'hello', (1, 'world')}
s.pop()               # 随机删除
print(s)
s.remove('hello')     # 指定一个元素删除，元素不存在集合时，报错
print(s)
s.discard('1')        # 指定一个元素删除，元素不存在集合时，不会报错
print(s)


# 两集合求交集
s1 = {1, 2, 'hello'}
s2 = {1, ('hjc', 1)}
s = s1.intersection(s2)         #   s = s1 & s2
print(s)
# 两集合求并集
s = s1.union(s2)                #   s = s1 | s2
print(s)
# 两集合求差集
s = s1.difference(s2)           #   s = s1 - s2
print(s)
s1.difference_update(s2)
print(s1)
# 两集合求交叉补集
s = s1.symmetric_difference(s2)      # {2, ('hjc', 1), 'hello'}      s = s2 ^ s1
print(s)


# 判断是否有交集,有交集输出False，无交集输出True
s1 = {1, 2}
s2 = {4, 3}
s = s1.isdisjoint(s2)
print(s)
# 判断s1是不是被s2包含，是他的子集合
s1 = {1, 2}
s2 = {1, 2, 3}
s = s1.issubset(s2)     # s = s1 < s2
print(s)
# 判断s1是不是包含s2，是他的父集合
s1 = {1, 2, 3}
s2 = {1, 3, 'hello'}
s = s1.issuperset(s2)   # s = s1 > s2
print(s)
# 更新信息,更新多个值,值必须是可迭代对象，还可以是集合
s1 = {1, 2, 3}
s1.update('洪吉昌')
print(s1)           # {1, 2, 3, '吉', '昌', '洪'}
s1 = {1, 2, 3}
s1.update(['洪吉昌'])
print(s1)           # {1, 2, 3, '洪吉昌'}
s1.update('洪吉昌14')
print(s1)           # {1, 2, 3, '洪', '4', '1', '吉', '昌'}    下同
s1.update('洪吉昌', '1', '4')
print(s1)
s1.update('洪吉昌', ['1', '4'])
print(s1)
s1.update('洪', ('吉', '昌'), ['1', '4'])
print(s1)
s1.update({'洪', '吉', '昌', '1', '4'})
print(s1)           # {1, 2, 3, '1', '洪', '吉', '4', '昌'}
# 不可变集合
s = frozenset('hello')
print(s)        # frozenset({'o', 'e', 'h', 'l'})
# 可变集合
s = set('hello')
print(s)       # {'o', 'e', 'h', 'l'}

