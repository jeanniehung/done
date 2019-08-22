"""
用于磁盘传输和网络传输————》序列化，反序列化
"""
# json  调用方式————》import json
"""
如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML，
但更好的方法是序列化为JSON，因为JSON表示出来就是一个字符串，可以被所有语言读取，
也可以方便地存储到磁盘或者通过网络传输。JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。
"""

"""
一：json.dumps(数据类型):————》

    数据类型转成字符串类型
        1:数据类型有引号全部变成双引号
        2:数据类型外在加引号，变成字符串类型
        3:要使用两个引号，一定是内部双引号，外部单引号，
        4:中文会转化为 unicode 对应的编码              洪吉昌————》\u6d2a\u5409\u660c
    example:
    python——————————————————————————》json
    1                                   "1"
    'name'                          '"name"'
    [1, '2']                        '[1, "2"]'
    {'name': "洪吉昌"}               '{"name": "\u6d2a\u5409\u660c"}'
    (1, 2)                          "[1, 2]"
    True/False/None                  "true"/"false"/"null"
    
    注释：
        只需要使用一个引号时，用双引号 " "
        需要使用多个引号时，单引号在最外层 '"洪吉昌"，"真帅"'
    
二：json.loads():————》

    将 json 的数据类型解析出来：
     无论数据是怎样创建的，只要满足json格式，就可以json.loads出来,不一定非要dumps的数据才能loads    
        1：可以直接解析json类型汉字    data = json.loads('"洪吉昌"')————》"洪吉昌"
        2：unicode编码对应的汉字也一样解析   \u6d2a\u5409\u660c————》洪吉昌
        3：没有元祖类型；python 元祖类型()转成json类型是"[]";解析出来直接就是个列表
    注释：
        import json
        dct="{'1':111}"             # json 只认外单引号，内双引号
        dct=str({"1":111})          # 报错，str得倒的数据结构和上面是一样的："{'1': 111}"
        print(json.loads(dct))
        
特别注意：python 格式是一个单引号 '' ；多个引号共同使用内层是 '' 最外层是双引号 "" 
        str()————》也会把双引号转化为单引号
man = {"hello": '是的'}
print(str(man), type(str(man))  ——————》"{'hello': '是的'}" 字符串

"""


# 应用实例
"""
原始方案
"""
# dic = {"name": "洪吉昌"}
# with open("测试", "w") as write_f:
#     dic_str = '{"name": "洪吉昌"}'    # 转为这种格式才可以被写到文件中
#     write_f.write(dic_str)
# with open("测试", "r") as read_f:
#     data = read_f.read()
#     data = eval(data)               # 将字符串的数据类型提取出来
#     print(data, type(data))         # 这样才可以拿到一个字典
"""
json方案
"""
# import json
# dic = {"name": "洪吉昌"}
# with open("new_测试", "w") as write_f:
#     write_f.write(json.dumps(dic))    # 但是写入中文的时候，中文在文件里显示的unicode编码
#     # json.dump(dic, write_f)             # 仅限于文件操作，和上一步相等
# with open("new_测试", "r") as read_f:
#     data = json.loads(read_f.read())   # 把以 json 类型写的文件 解析出来，成为原来的数据类型
#     # data = json.load(read_f)          # 仅限于文件操作，和上一步相等
#     print(data, type(data))


"""
pickle：调用方式————》import pickle
    Pickle的问题和所有其他编程语言特有的序列化问题一样，
    就是它只能用于Python，并且可能不同版本的Python彼此都不兼容，
    因此，只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系。
pickle序列化之后是字节形式————》文件打开方式是 wb 模式，语法操作和 json 相同，但可以序列化 函数，类
json序列化之后是字符串形式
"""
# import pickle
# dic = {'name': 'alvin', 'age': 23, 'sex': 'male'}
# print(type(dic))  # <class 'dict'>
# j = pickle.dumps(dic)
# print(type(j))  # <class 'bytes'>
# f = open('序列化对象_pickle', 'wb')  # 注意是w是写入str,wb是写入bytes,j是'bytes'
# f.write(j)  # -------------------等价于pickle.dump(dic,f)
# f.close()
# # -------------------------反序列化
# f = open('序列化对象_pickle', 'rb')
# data = pickle.loads(f.read())  # 等价于data=pickle.load(f)
# print(data['age'])


