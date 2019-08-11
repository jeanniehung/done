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
for i in iphone:
    print(i, sep='\n')
while True:
    i = input('请输入商品序号0，1，2，3：')
    if i.upper() == 'Q':
        break
    i = int(i)
    iphone_lis = iphone[i]  # 购买的商品
    iphone_list.append(iphone_lis)  # 购买的商品列表
    count += iphone_lis[1]  # iphone_lis[0]: 商品名称, iphone_lis[1]: 商品价格
    if count > s:
        print('余额不足, 总计', count, '请选择移除商品或者充值购买')
        i = input('请选择(1.移除商品， 2.充值购买)：')
        if i == '1':
            while True:
                print(iphone_list, count)
                i = input('请输入移除商品索引号码：')
                if i == 'q' or i == 'Q':
                    print('你可以继续选择商品啦。。。')
                    break
                i = int(i)
                if i >= len(iphone_list):
                    print("商品索引有限，商品总计：", len(iphone_list))
                    continue
                count = count - iphone_list[i][1]
                iphone_list.pop(i)
        elif i == '2':
            while True:
                print(iphone_list, count)
                i = input('请输入充值金额：')
                i = int(i)
                s = s + i
                print('你可以继续选择商品啦。。。, 目前账户总资产：', s)
                if s > count:
                    break
                else:
                    continue
        else:
            print("输入错误。。。。。")
    else:
        print(iphone_list, count, '可以购买')

print('购买的商品', iphone_list, '\n商品总价', count, '\n账户总额', s)