# 字符串拼接
"""
*：列表
**：字典
"""
#   +号拼接
new = 'i am' + '洪吉昌' + 'my hobby is ' + '18'
print(new)

# 百分号方式

#  %s可以拼接任一数据类型
new = 'i am %s hobby is %s' % ('洪吉昌', ['paly', 'coding'])
print(new)
#  %d 只可以拼接数字类型
new = 'i am %s hobby is %d' % ('洪吉昌', 18)
print(new)
new = 'i am %(name)s hobby is %(hobby)d' % {'name': '洪吉昌', 'hobby': 18}
print(new)
#  %.nf打印小数点后n位浮点数
tp = 'percent   %.3f' % 99.9762344444
print(tp)
tp = 'percent   %(pp).3f' % {'pp': 99.9762344444}
print(tp)
# 打印百分比
tp = 'percent   %.3f%% ' % 99.9762344444
print(tp)
tp = 'percent   %.3f%s' % (99.9762344444, '%')
print(tp)


# format方式

# 列表索引一一对应，默认0，1，2。。。
tp = 'i am {} age {} {}'.format('洪吉昌', 18, 'handsome')
print(tp)
tp = 'i am {} age {} {}'.format(*['洪吉昌', 18, 'handsome'])   # *[1,2,3] 等于 1,2,3
print(tp)
# 字典索引一一对应，根据对应的key
tp = 'i am {name} age {a} {l}'.format(name='洪吉昌', a=18, l='handsome')
print(tp)
tp = 'i am {name} age {a} {l}'.format(**{'name': '洪吉昌', 'a': 18, 'l': 'handsome'})
print(tp)
tp = 'i am {name} age {a} {l}'.format_map({'name': '洪吉昌', 'a': 18, 'l': 'handsome'})
print(tp)
# 引索对应
tp = 'i am {1} age {0} {2}'.format(18, '洪吉昌', 'handsome')
print(tp)
tp = 'i am {0[0]} age {0[1]} {0[2]}'.format(['洪吉昌', 18, 'handsome'], [11, 22, 33])
print(tp)
# s对应字符串 d对应整数型  f对应小数点后六位浮点小树 一一对应
tp = 'i am {:s} age {:d} {:f}'.format('洪吉昌', 18, 77.7)
print(tp)
tp = 'i am {name:s} age {a:d} {b:f}'.format(name='洪吉昌', a=18, b=77.7)
print(tp)
# 更改数字类型，format后加数字可多不可少
tp = 'numbers: {:b},{:o},{:d},{:x},{:X},{:f},{:%}'.format(15, 15, 15, 15, 15, 15, 15, 2)
print(tp)
tp = "numbers: {0:b},{0:o},{0:d},{0:x},{0:X},{0:f} {0:%}".format(15)
print(tp)
tp = "numbers: {num:b},{num:o},{num:d},{num:x},{num:X},{num:f} {num:%}".format(num=15)
print(tp)
"""
b:二进制
o:八进制
d:十进制
x:十六进制，小写
X:十六进制，大写
f:六位浮点小数字
%:百分数，六位小数
"""
