# iphone = [
#     ["iphone 5s", 200],
#     ["iphone 6", 300],
#     ["iphone 8", 400],
#     ["iphone Xr", 500]
# ]
# iphone_list = []
# count = 0
# # 要求用户输入总资产，例如：2000
# s = input('请输入总资产：')
# s = int(s)
# for i in iphone:
#     print(i, sep='\n')
# while True:
#     i = input('请输入商品序号0，1，2，3：')
#     if i.upper() == 'Q':
#         break
#     i = int(i)
#     iphone_lis = iphone[i]  # 购买的商品
#     iphone_list.append(iphone_lis)  # 购买的商品列表
#     count += iphone_lis[1]  # iphone_lis[0]: 商品名称, iphone_lis[1]: 商品价格
#     if count > s:
#         print('余额不足, 总计', count, '请选择移除商品或者充值购买')
#         i = input('请选择(1.移除商品， 2.充值购买)：')
#         if i == '1':
#             while True:
#                 print(iphone_list, count)
#                 i = input('请输入移除商品索引号码：')
#                 if i == 'q' or i == 'Q':
#                     print('你可以继续选择商品啦。。。')
#                     break
#                 i = int(i)
#                 if i >= len(iphone_list):
#                     print("商品索引有限，商品总计：", len(iphone_list))
#                     continue
#                 count = count - iphone_list[i][1]
#                 iphone_list.pop(i)
#         elif i == '2':
#             while True:
#                 print(iphone_list, count)
#                 i = input('请输入充值金额：')
#                 i = int(i)
#                 s = s + i
#                 print('你可以继续选择商品啦。。。, 目前账户总资产：', s)
#                 if s > count:
#                     break
#                 else:
#                     continue
#         else:
#             print("输入错误。。。。。")
#     else:
#         print(iphone_list, count, '可以购买')
#
# print('购买的商品', iphone_list, '\n商品总价', count, '\n账户总额', s)


# 猜字游戏
# 要求：
#    允许用户最多尝试3次，3次都没猜对的话，就直接退出，如果猜对了，打印恭喜信息并退出
# num = 10
# count = 0
# while True:
#     inp_num = int(input('请猜：'))
#     if inp_num == num:
#         print('恭喜')
#         break
#     if count == 2:
#         break
#     else:
#         count += 1
#         continue

# 猜年龄游戏升级版
"""
要求：
    允许用户最多尝试3次
    每尝试3次后，如果还没猜对，就问用户是否还想继续玩，如果回答Y或y, 
        就继续让其猜3次，以此往复，如果回答N或n，就退出程序
    如何猜对了，就直接退出 
"""
# num = 10
# count = 0
# while True:
#     if count == 3:
#         choice = input('请选择Y，y还是N，n')
#         if choice.upper() == 'Y':
#             count = 0
#         else:
#             break
#     guss_num = int(input('请猜测:'))
#     if guss_num == num:
#         print('恭喜')
#         break
#     count += 1

"""
# 简单购物车,要求如下：
# 实现打印商品详细信息，用户输入商品名和购买个数，
# 则将商品名，价格，购买个数加入购物列表，如果输入为空或其他非法输入则要求用户重新输入　　
"""
# msg_dic = {
#         'apple': 10,
#         'tesla': 100000,
#         'mac': 3000,
#         'lenovo': 30000,
#         'chicken': 10,
# }
# shop_l = []
# while 1:
#     for key, item in msg_dic.items():
#         print('name:{name} price:{p}'.format_map({'name': key, 'p': item}))
#     choice = input('请选择商品：').strip()
#     if choice.upper() == 'Q':
#         break
#     if not choice or choice not in msg_dic:
#         continue
#     count = input('购买个数；').strip()
#     if not count.isdigit():
#         continue
#     shop_l.append((choice, msg_dic[choice], count))
#     print(shop_l)
#


# 统计s='hello alex alex say hello sb sb'中每个单词的个数
s = 'hello alex alex say hello sb sb'
# s_l = s.split()     # 利用空格分割，把元素分到一一列表内
# dic = {}
# for i in s_l:
#     if i in dic:
#         dic[i] += 1
#     else:
#         dic[i] = 1
# print(dic)
# dic = {}
# s_l = s.split()
# for i in s_l:
#     dic[i] = s.count(i)
# print(dic)
"""
setdefault的功能————》赋值功能
1：key存在，则不赋值，key不存在则设置默认值
2：key存在，返回的是key对应的已有的值，key不存在，返回的则是要设置的默认值
"""
# dic = {}
# s_l = s.split()
# for i in s_l:
#     dic.setdefault(i, s.count(i))
# print(dic)

# 集合去重，减少循环次数
# dic = {}
# l_set = set(s.split())
# for i in l_set:
#     dic[i] = s.count(i)
# print(dic)