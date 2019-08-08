#一、元素分类
#有如下值集合 [11,22,33,44,55,66,77,88,99,90...]，将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中。
#即： {'k1': 大于66的所有值, 'k2': 小于66的所有值}
dic = {}
l = []
L = []
li = [11,22,33,44,55,66,77,88,99,90]
for i in range(len(li)):
    if li[i] > 66:
        v = li[i]
        l.append(v)
    elif li[i] < 66:
        v1 = li[i]
        L.append(v1)
    else:
        pass
dic.update({'k1':l,'k2':L})
print(dic)


#二、查找
#查找列表中元素，移除每个元素的空格，并查找以 a或A开头 并且以 c 结尾的所有元素。
li = ["alec", " aric", "Alex", "Tony", "rain"]
tu = ("alec", " aric", "Alex", "Tony", "rain")
dic = {'k1': "alex", 'k2': ' aric',  "k3": "Alex", "k4": "Tony"}
for i in li:
#元祖把li换成tu，字典把li换成dic.values()，其他不变
   v = i.strip()
   v1 = v.startswith('a')
   v2 = v.startswith('A')
   v3 = v.endswith('c')
   if v1 == True or v2 == True and v3 == True:
       print(v)
   else:
       pass



#三、输出商品列表，用户输入序号，显示用户选中的商品
li = ["手机", "电脑", '鼠标垫', '游艇']
for i,j in enumerate(li,0):
    print(i,j)
s = input('输入序号：')
v = int(s) % 4
print(li[v])

#四、购物车
"""
功能要求：
要求用户输入总资产，例如：2000
显示商品列表，让用户根据序号选择商品，加入购物车
购买，如果商品总额大于总资产，提示账户余额不足，否则，购买成功。
附加：可充值、某商品移除购物车
"""
# s = input('请输入总资产：')
# test = '{name}price{a}'
# v = test.format(name='电脑'a=3000)
# v1 = test.format(name='手机'a=1000)
# v2 = test.format_map({'name':'鼠标垫''a':40})
# v3 = test.format(name='游艇'a=10000)
# print(v,v1,v2,v3)


#五：九九乘法表
s = ''
for i in range(1,10):
    for j in range(1,i+1):
        s += str(i)+'*'+str(j)+"="+str(i*j)+'\t'
    print(s)
    s = ''


#六:用下划线将列表的每一个元素拼接
li = ['alex','eric',123]
li[2]=str(li[2])
print('_'.join(li))


#七:写代码，如下元祖，按要求实现每一个功能
tu = ('alex','eric','ranin')
#a:计算元祖长度并输出
print(len(tu))
#b:获取元祖的第2个元素并输出
print(tu[2])
#c:获取元祖的第1—2个元素，并输出
print(tu[1:90])
#d:请使用for输出元祖的元素
for i in tu:
    print(i)
#e:请使用for，len，range输出元祖的索引
for j in range(0,len(tu)):
    print(j)
#f:请使用enumerate输出元祖元素和序号（序号从10开始）
for i,j in enumerate(tu,10):
    print(i,j)



#八:有如下变量，请实现要求的功能
tu = ('alex',[11,22,{'k1':'v1','k2':['age','name'],'k3':(11,22,33)}],44)
#a：讲述元祖的特性
"""
1；有序性
2：一级元素不可被修改，删除
"""
#b：请问tu变量中的第一个元素'alex'是否可以被修改————》不可以
#c：k️2对应的值是列表，可以，
tu[1][2]['k2'].append('seven')
print(tu)
#d:k3对应的是元祖，不可以



#九:字典
dic = {'k1':'v1','k2':'v2','k3':[11,22,33]}
#请循环输出所有的key
for i in dic:
    print(i)
for i in dic.keys():
    print(i)
#输出所有的value
for i in dic.values():
    print(i)
#输出所有的key和value
for i in dic.items():
    print(i)
for i in dic:
    print(i,dic[i])
#添加'k4':'v4'在词典最后
dic.update({'k4':'v4'})
print(dic)
#修改k1对应的值为alex
dic.update({'k1':'alex'})
print(dic)
#在k3后追加一个元素44
dic['k3'].append(44)
print(dic)
#在k3对应的值的第 1 个位置插入个元素18
dic['k3'].insert(1,18)
print(dic)




# 十:转换
# a:将字符串s='alex'转换成列表
s = 'alex'
v = list(s)
print(v)
#b:将字符串s='alex'转换成元祖
s = 'alex'
v = tuple(s)
print(v)




# 十一:列举布尔值是False的所有值
# 一共有七个 {} () [] None 0 '' False




# 十二：分页显示内容
# a：通过for循环创建301条数据，数据类型不限制
# b：分页，每页显示十条内容
"""
不会
"""
# test = ''
# for i in range(1,302):
#     s = 'alex'+'_'+str(i)+'\t''alex@live.com'+'_'+str(i)+'\t''pwd' + '_' + str(i)
#     test = s
#     print(test.expandtabs(10))
#     v = input('请输入页码：')
#     v1 = int(v)
#     v2 = v1 % 10 + 1
#     v3 = v1 % 10 + 9
#     v4 = str[v2:v3]
#     for i in v4:
#         print(test[i])



#十三:有1，2，3，4，5，6，7，8个数字，能组成多少个互不相同的两位数
count = 0
for i in range(1,9):
    for j in range(1,9):
        if i != j:
          count += 1
print(count)




#十四：又一个列表，求出相加为9对应的元素
nums = [2,7,11,15,1,8,7]
for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i]+nums[j] == 9 and i != j:
            print(i,j)



# 十五:公鸡5文钱一只，母鸡3文钱一只，小鸡3只1文钱；用100文钱买100只鸡的组合
for i in range(1,100//5):
    for j in range(1,100//3):
        for z in range(1,99):
            if i+j+z == 100 and 5*i+3*j+z/3 == 100:
                print(i,j,z)
