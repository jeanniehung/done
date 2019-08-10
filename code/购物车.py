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
s = int(s)
# 显示商品列表
for i in iphone:
    print(i, sep='\n')
while True:
    i = input('请输入商品序号0，1，2，3：')
    if i.upper() == 'Q':
        break
    i = int(i)
    iphone_lis = iphone[i]
    iphone_list.append(iphone_lis)
    count += iphone_lis[1]
    if count > 2000:
        print('余额不足，请选择移除商品或者充值购买')
        i = input('请选择：')
        if i == '移除商品':
            while True:
                print(iphone_list, count)
                i = input('请输入移除商品索引号码：')
                i = int(i)
                iphone_list.pop(i)
                count = count - iphone_list[i][1]
                if count > 2000:
                    continue
                else:
                    break
        else:
            while True:
                print(iphone_list, count)
                i = input('请输入充值金额：')
                i = int(i)
                blance = s + i - count
                if blance >= 0:
                    break
                else:
                    continue

print(iphone_list, count, blance)
