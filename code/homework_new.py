#一、元素分类
#有如下值集合 [11,22,33,44,55,66,77,88,99,90...]，将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中。
#即： {'k1': 大于66的所有值, 'k2': 小于66的所有值}
dic = {}
l = []
L = []
li = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
for i in range(len(li)):
    if li[i] > 66:
        v = li[i]
        l.append(v)
    elif li[i] < 66:
        v1 = li[i]
        L.append(v1)
    else:
        pass
dic.update({'k1': l, 'k2': L})
print(dic)



#四、购物车
"""
功能要求：
要求用户输入总资产，例如：2000
显示商品列表，让用户根据序号选择商品，加入购物车
购买，如果商品总额大于总资产，提示账户余额不足，否则，购买成功。
附加：可充值、某商品移除购物车
"""
iphone = [
    ["iphone 5s", 200],
    ["iphone 6", 300],
    ["iphone 8", 400],
    ["iphone Xr", 500]
]
iphone_list = []
count = 0
# 要求用户输入总资产，例如：2000
s = input('请输入总资产：')
# 显示商品列表，
for item in iphone:
    print("{}: {}".format(item[0], item[1]))
while True:

    i = input("需要选择的商品0, 1, 2, 3:")
    if i == 'q' or i == 'Q':
        break
    i = int(i)
    iphone_lis = iphone[i] # 0: iphone5s 1: iphone5, 2: iphone8, 3: iphoneXr
    iphone_list.append(iphone_lis[0])
    count = count + iphone_lis[1]
    if count > 2000:
        print("余额不足......")
        count = count - iphone_lis[1]
        break

print(count, "购买成功!!!")