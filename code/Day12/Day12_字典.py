"""
字典（dict）
基本格式：dic = {key:value}
        dic = {'k1':18,'k2':'洪吉昌','k3':'True','k4':[],'k5':(),'k6':{}}
        字典的value可以是任意形式
        列表，字典不可以作为字典的key，key相同时只显示一个（True：1，False：0）
特征：
a：大中括号{}括起来
b：,分割每个元素
"""
#1:字典是无序的
dic = {'k1':18,2:'洪吉昌','k3':'True','k4':[{1:'hjc','kk2':'vv1','kk3':(11,22)}],'k5':(),'k6':{}}
print(dic)
#2:索引取值————》由于字典是无序的，所以索引其key
dic = {'k1':18,2:'洪吉昌','k3':'True','k4':[{1:'hjc','kk2':'vv1','kk3':(11,22)}],'k5':(),'k6':{}}
v = dic['k4'][0]['kk3'][0]
print(v)        #输出11
#3：字典的删除
dic = {'k1':18,2:'洪吉昌','k3':'True','k4':[{1:'hjc','kk2':'vv1','kk3':(11,22)}],'k5':(),'k6':{}}
del dic['k4'][0]['kk2']
print(dic)
#4：for循环
dic = {'k1':18,2:'洪吉昌','k3':'True'}
for item in dic:                   #默认输出keys
    print(item)
for item in dic.keys():
    print(item)
for item in dic.values():          #显示values
    print(item)
for item in dic:                   #输出key：value
    print(item,dic[item])
for k,v in dic.items():            #输出key：value
    print(k,v)
#5:清空字典
dic = {'k1':18,2:'洪吉昌','k3':'True'}
dic.clear()
print(dic)
#6:浅拷贝
dic = {'k1':18,2:'洪吉昌','k3':'True'}
v = dic.copy()
print(v)
"""重点使用
#7:(重点）根据序列，创建字典，并指定key，value
v = dict.fromkeys(['k1',2,'洪吉昌'],123)
print(v)        #{'k1': 123, 2: 123, '洪吉昌': 123}
#8:根据key取值，key不存在时，可通过参数指定默认值（None）给不存在的key，但是不显示在词典中
dic = {'k1':18,2:'洪吉昌','k3':'True'}
v = dic.get('1','帅气')
#9：输出字典的key，value还有kay和value配对
dic = {'k1':18,2:'洪吉昌','k3':'True'}
print(v)
v = dic.values()
print(v)
v = dic.keys()
print(v)
v = dic.items()
print(v)
#10：更新,原有信息覆盖，新信息添加
dic = {'k1':18,2:'洪吉昌','k3':'True'}
dic.update({'k1':111,'k4':'滚'})
print(dic)          #{'k1': 111, 2: '洪吉昌', 'k3': 'True', 'k4': '滚'}
dic.update(k1=123,k4='滚')
print(dic)          #{'k1': 123, 2: '洪吉昌', 'k3': 'True', 'k4': '滚'}
"""
#11：删除并获取删除key对应的value值；当key不存在时，后可加参数，会返回参数；当key存在时，加不加参数没影响
dic = {'k1':18,2:'洪吉昌','k3':'True'}
v = dic.pop('k1',2)
print(dic,v)        #{2: '洪吉昌', 'k3': 'True'} 18
v = dic.pop('k4',2)
print(dic,v)        #{'k1': 18, 2: '洪吉昌', 'k3': 'True'} 2
#随机删除
dic = {'k1':18,2:'洪吉昌','k3':'True'}
k,v = dic.popitem()
print(k,v)          #k3 True
#12：设置新值，若key存在，获取当前key的值;若value值已存在，不改变；若不存在,设置，获取当前key值
dic = {'k1':18,2:'洪吉昌','k3':'True'}
v = dic.setdefault('k1',1)
print(dic,v)        #{'k1': 18, 2: '洪吉昌', 'k3': 'True'} 18
v = dic.setdefault('k11',18)
print(dic,v)        #{'k1': 18, 2: '洪吉昌', 'k3': 'True', 'k11': 18} 18
#13：更新,原有信息覆盖，新信息添加
dic = {'k1':18,2:'洪吉昌','k3':'True'}
dic.update({'k1':111,'k4':'滚'})
print(dic)          #{'k1': 111, 2: '洪吉昌', 'k3': 'True', 'k4': '滚'}
dic.update(k1=123,k4='滚')
print(dic)          #{'k1': 123, 2: '洪吉昌', 'k3': 'True', 'k4': '滚'}
#14:判断是否在key里面，value里
dic = {'k1':18,2:'洪吉昌','k3':'True'}
v = 'k1' in dic
print(v)
v = '洪吉昌' in dic.values()
print(v)

