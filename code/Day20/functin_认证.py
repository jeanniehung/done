"""
装饰器无参数
"""
# user_dict = [
#     {'username': '洪吉昌', 'password': '123'},
#     {'username': '宋梦娜', 'password': '123'},
#     {'username': '洪淑芳', 'password': '123'},
#     {'username': '洪省昌', 'password': '123'},
#     {'username': '魏宽怀', 'password': '123'}
# ]
# current_user = {'username': None, 'login': False}
# """
# current ————》 当前的
# 定义一个登录状态，开始给'username' 用户名 和 'login' 登录状态都赋bool值为假的值，
# 只要登录一次成功，把 username 传给 current_dict 的 username ；login 改为 True
# 在写一个 if 判断，如果 username 和 login 都不是假，就直接执行下面的功能，无需再次认证certification
# """
#
#
# def certification(func):
#     def wrapper(*args, **kwargs):
#         if current_user['username'] and current_user['login']:
#             res = func(*args, **kwargs)
#             return res
#         username = input('用户名：').strip()
#         password = input('密码：').strip()
#         for i in user_dict:
#             if username == i['username'] and password == i['password']:
#                 current_user['username'] = username
#                 current_user['login'] = True
#                 res = func(*args, **kwargs)
#                 return res
#         else:
#             print('用户名或密码错误')
#     return wrapper
#
#
# @certification
# def interface(name):
#     print('%s欢迎来到京东' % name)
#
#
# @certification
# def home(name):
#     print('%s欢迎回家' % name)
#
#
# @certification
# def shopping_cart(name):
#     print('%s你的购物车里有%s，%s，%s' % (name, '手机', '蓝牙耳机', '奶茶妹妹'))
#
#
# print('之前的登录状态:', current_user)
# interface('洪吉昌')
# print('之后的登录状态:', current_user)
# home('洪吉昌')
# shopping_cart('洪吉昌')

"""
装饰器有参数————》闭包概念完成，在最外层传入参数，内部每一层都可以使用
"""
# 选择以什么类型认证
"""
默认以file（文件）模式处理数据
"""


def cer(cer_type='file'):
    def certification(func):
        def wrapper(*args, **kwargs):
            print('认证类型是:', cer_type)
            if cer_type == 'file':
                if current_user['username'] and current_user['login']:
                    res = func(*args, **kwargs)
                    return res
                username = input('用户名：').strip()
                password = input('密码：').strip()
                for i in user_dict:
                    if username == i['username'] and password == i['password']:
                        current_user['username'] = username
                        current_user['login'] = True
                        res = func(*args, **kwargs)
                        return res
                else:
                    print('用户名或密码错误')
            elif cer_type == 'ldap':
                print('我不会玩')
                res = func(*args, **kwargs)
                return res
            else:
                print('这是什么鬼认证类型')
                res = func(*args, **kwargs)
                return res
        return wrapper
    return certification


user_dict = [
    {'username': '洪吉昌', 'password': '123'},
    {'username': '宋梦娜', 'password': '123'},
    {'username': '洪淑芳', 'password': '123'},
    {'username': '洪省昌', 'password': '123'},
    {'username': '魏宽怀', 'password': '123'}
]
current_user = {'username': None, 'login': False}
"""
current ————》 当前的
定义一个登录状态，开始给'username' 用户名 和 'login' 登录状态都赋bool值为假的值，
只要登录一次成功，把 username 传给 current_dict 的 username ；login 改为 True
在写一个 if 判断，如果 username 和 login 都不是假，就直接执行下面的功能，无需再次认证certification
"""

"""
@cer()，括号里需要传入参数，如果，什么都不传，就是默认的file模式；
想更改模式就传入对应的模式名字就OK了————》er_type='模式名'
"""


@cer()    # @cer =  'certification = cer(cer_type='file')'————》@certification
def interface(name):
    print('%s欢迎来到京东' % name)


@cer(cer_type='ldap')       # 专门做认证的 ldap 集中账号管理
def home(name):
    print('%s欢迎回家' % name)


@cer(cer_type='sss')
def shopping_cart(name):
    print('%s你的购物车里有%s，%s，%s' % (name, '手机', '蓝牙耳机', '奶茶妹妹'))


print('之前的登录状态:', current_user)
interface('洪吉昌')
print('之后的登录状态:', current_user)
home('洪吉昌')
shopping_cart('洪吉昌')
