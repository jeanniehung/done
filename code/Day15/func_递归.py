# 五：全局变量与局部变量
"""
全局变量变量名大写
局部变量变量名小写

函数中无global关键词：
    ——有局部变量，读取局部变量
        name = ['洪吉昌', '魏宽怀']
        def change_name():
            name = '帅比'
            print(name)
        change_name()               # 帅比
    ——无局部变量，读取全局变量，但不可以对其修改，若全局变量是不可变类型，可对其追加，删除操作
        name = ['洪吉昌', '魏宽怀']
        def change_name():
            name.append('自己')
            print(name)
        change_name()               # ['洪吉昌', '魏宽怀', '自己']
函数中有global关键词：
    ——有局部变量，会直接报错
        name = ['洪吉昌', '魏宽怀']
        def change_name():
            name = '洪吉昌'
            global name
            print(name)
        change_name()               # 直接报错
    ——无局部变量，读取全局变量，可以直接更改，若更改后对变量是不可变类型，可对其追加，删除操作
        name = ['洪吉昌', '魏宽怀']
        def change_name():
            global name
            name = ['洪吉昌']          # 可以直接对全局变量进行更改
            name.append('自己')       # 因为更改会的变量是列表，可以对其进行列表的操作
            print(name)
        change_name()                 # ['洪吉昌', '自己']
"""
# global只能指定全局变量
# nonlocal只能指定上一级变量,上一级是全局变量会报错
"""
name = '洪吉昌'
def user():
    name = '洪淑芳'
    def add():
        nonlocal name
        # global name
        name = '帅比'
    add()
    print(name)
print(name)     # 洪吉昌
user()          # 帅比        
print(name)     # 洪吉昌
"""
# 风湿理论：函数即变量
# 先执行最外层代码，依次进入执行


#   递归
"""
递归特性：
1：必须有一个明确的结束（return）判断（if）
2：每次进入更深一层递归时，问题规模相比上一次递归都一个减少
3：递归效率不高，递归用的次数过多，会导致栈的溢出
"""
# 简单递归代码
# import time
#
#
# def calc(n):
#     print('-'*20, n, sep='\n')
#     if int(n/2) == 0:
#         return n
#     time.sleep(1)
#     return calc(int(n/2))
#
#
# res = calc(10)
# print('*'*20, res, sep='\n')
"""
写一个问路代码
要求：1：只有洪吉昌知道怎么走
     2：安照列表顺序一个问一个
     3：问路名单只可以是列表
     3：使询问过程更贴近生活————》使用 import time函数增加时间
        ——函数合适
            import time
            time。sleep（停止时间长度）
"""
# li = ['魏宽怀', '洪省昌', '洪淑芳', '无敌帅王']
# li_food = ['sb', 'asb', 'nab', '洪吉昌']
#
# import time
#
#
# def ask_way(array):
#     print('*'*20)
#     if len(array) == 1:
#         if array[0] != '洪吉昌':
#             return '%s说,不好意思,我不清楚' % array[0]
#
#     person = array.pop(0)
#
#     if person == '洪吉昌':
#         return '%s说：直走，拐个弯就到' % person
#
#     print('%s说：我不知道，我帮你去问问%s' % (person, array[0]))
#     time.sleep(1)
#     good = ask_way(array)
#     print('#'*20, '%s问的结果是：%s' % (person, good), sep='\n')
#     return good
#
#
# res = ask_way(li)                 # 传入问路列表
# print('_'*20, res, sep='\n')
"""
拓展：写一个购物列表
要求：
1：只想买phone
2：和售货员按着列表清单一个接着一个买
3：更贴切生活，加上时间函数
"""
# shopping_list = [
#                     ['电脑', 1000],
#                     ['充电器', 100],
#                     ['数码相机', 500],
#                     ['phone', 300]
#                  ]
# my_list = []
# for i in shopping_list:
#     my_list.append(i)
# print(my_list)
#
# import time
#
#
# def shop(x):
#     print('*'*20)
#     if len(x) == 0:
#         return '%x[0][1]太贵了，我不想买了，谢谢'
#     good = x.pop(0)
#     if good[0] == 'phone':
#         return '我要买%s，给你%s元' % (good[0], good[1])
#     print('%s我不喜欢,可以拿一下%s给我看一下吗' % (good[0], x[0][0]))
#     time.sleep(1)
#     new = shop(x)
#     return new
#
#
# res = shop(my_list)
# print(res)
