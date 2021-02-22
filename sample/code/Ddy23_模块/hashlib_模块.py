"""
是一种摘要算法
1：什么是hash：hash是一种算法（3.x里代替了md5模块和sha模块，主要提供 SHA1, SHA224, SHA256(用这个), SHA384, SHA512 ，MD5 算法），
该算法接受传入的内容，经过运算得到一串hash值
2：hash 的特点：
    1：只要传入的内容一样，得倒的 hash 值必然一样=====>要用明文传输密码文件完整性校验
    2：不能由 hash 值返解成内容=======》把密码做成hash值，不应该在网络传输明文密码
    3：只要 hash 算法不变，无论校检的内容多大，得倒的 hash 值长度是固定的
    
加密：明文变成密文；密文变成明文
md5：明文变成密文, 32 位
sha256：明文变成密文, 65 位

注意：
    把一段很长的数据update多次，与一次update这段长数据，得到的结果一样
    但是update多次为校验大文件提供了可能。
加盐：
    以上加密算法虽然依然非常厉害，但时候存在缺陷，即：通过撞库可以反解。
    所以，有必要对加密算法中添加自定义key再来做加密。
    
python 还有一个 hmac 模块，它内部对我们创建 key 和 内容 进行进一步的处理然后再加密:
    1 import hmac
    2 h = hmac.new('alvin'.encode('utf8'))
    3 h.update('hello'.encode('utf8'))
    4 print (h.hexdigest())#320df9832eab4c038b6c1d7ed73a5940
要想保证hmac最终结果一致，必须保证：
    1:hmac.new括号内指定的初始key一样
    2:无论update多少次，校验的内容累加到一起是一样的内容
"""
# import hashlib
# obj = hashlib.md5('洪吉昌'.encode('utf8'))                 # 这里可以加盐 就没那么大的概率被破解
# obj.update('hello'.encode('utf8'))
# print(obj.hexdigest())
# # 5d41402abc4b2a76b9719d911017c592
# obj.update('hjc'.encode('utf8'))
# print(obj.hexdigest())
# # aee9c56bc7a0f99539170534b69f9c64          # 得倒的是 hellohjc 的 hash 值
# obj1 = hashlib.md5('洪吉昌'.encode('utf8'))
# obj1.update('hellohjc'.encode('utf8'))
# print(obj1.hexdigest())
# # aee9c56bc7a0f99539170534b69f9c64
#
#
# sha = hashlib.sha256('洪吉昌'.encode('utf8'))
# sha.update('hello'.encode('utf8'))
# print(sha.hexdigest())
# # 6cb17975840cc7cdaf7d7b61a54a74125669d04fbe3693a6a4b9ebf857dd7000
# sha.update('hjc'.encode('utf8'))
# print(sha.hexdigest())
# # 40ebfadf7e82e3f036e4469c2a5d16e89beeb0c57842b240c77993f9fc83685c      # 得倒的也是 hellohjc 的 hash 值
# sha1 = hashlib.sha256('洪吉昌'.encode('utf8'))
# sha1.update('hellohjc'.encode('utf8'))
# print(sha1.hexdigest())
# # 40ebfadf7e82e3f036e4469c2a5d16e89beeb0c57842b240c77993f9fc83685c


# ——————————————》 模拟装库破解密码 (不知的加盐参数，也没也加盐）
import hashlib

db_passwords = [
    'hjc1231',
    'hjc1232',
    'hjc1233',
    'hjc1234',
    'hjc1235',
    'hjc1236',
]


def make_password_dic(self):        # 把明文密码和 hash 之后的密码 对应成 key:value 生成一个字典
    password_dic = {}
    for i in self:
        obj = hashlib.md5()
        obj.update(i.encode('utf8'))
        password_dic[i] = obj.hexdigest()
    return password_dic


def crack_password(hash_password, password_dic):     # 传入得倒的 hash 密码 返回明文密码

    for k, v in password_dic.items():
        if v == hash_password:
            print('密码是————》\033[33m%s\033[0m' % k)
    return '\033[45m这个傻逼密码真是简单\033[0m'


if __name__ == '__main__':
    ha_p = '2f2362f19364e391c08df86a8f5e2e20'
    c_p = crack_password(ha_p, make_password_dic(db_passwords))
    print(c_p)      # 得倒 crack_password 函数的返回值

