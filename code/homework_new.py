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