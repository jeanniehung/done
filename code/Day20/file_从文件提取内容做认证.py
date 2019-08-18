"""
文件（file）模式处理认证装饰器
"""
current_user = {'user_name': None, 'login': False}


def cer(cer_type='file'):
    def certification(func):
        def wrapper(*args, **kwargs):
            print('当前处理模式:%s' % cer_type)
            if cer_type == 'file':
                if current_user['user_name'] and current_user['login']:
                    global user_name
# 把user_name 定义成全局变量，以闭包的思想所有的包都可以使用该变量
                    user_name = current_user['user_name']
                    res = func(user_name, *args, **kwargs)
                    return res
                user_name = input('请输入用户名:').strip()
                password = input('请输入密码:').strip()
                with open('用户信息', 'r', encoding='utf-8') as file:
                    for item in file:
                        item = eval(item)       # 文件里的内容都是字符串，要用eval提取出来
                        if item['user_name'] == user_name and item['password'] == password:
                            current_user['user_name'] = user_name
                            current_user['login'] = True
                            res = func(user_name, *args, **kwargs)
                            return res
                    else:
                        print('用户名或者密码错误')
            elif cer_type == 'ldap':
                print('我不会玩')
                res = func(user_name, *args, **kwargs)
                return res
            else:
                print('这是什么鬼认证类型')
                res = func(user_name, *args, **kwargs)
                return res
        return wrapper
    return certification


@cer()
def interface(user_name):
    print('%s欢迎来到主页面' % user_name)


@cer(cer_type='ldap')
def home(user_name, assets):
    print('%s你的总资产是%s ' % (user_name, assets))


@cer('sss')
def shopping_cart(user_name):
    print('%s的购物车里有%s,%s,%s' % (user_name, '手机', '蓝牙耳机', '奶茶'))


"""
user_name 是默认参数， wrapper 函数已经处理好了， 谁登录了谁就是 user_name
"""
print('before用户状态:%s' % current_user)
interface()
print('after用户状态:%s' % current_user)
home(1000)
shopping_cart()

