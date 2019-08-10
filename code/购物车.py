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

    def test():
        for i in iphone_list:
            print(i)
        print(count, s)
    if count > s:
        print('余额不足，请选择移除商品或者充值购买')
        i = input('请选择：')
        if i == '移除商品':
            while True:
                test()
                i = input('请输入移除商品索引号码：')
                i = int(i)
                iphone_list.pop(i)
                count = count - iphone_list[i][1]
                if count > s:
                    continue
                else:
                    break
        else:
            while True:
                test()
                i = input('请输入充值金额：')
                i = int(i)
                s = s + i
                if count < s:
                    break
                else:
                    continue
test()

