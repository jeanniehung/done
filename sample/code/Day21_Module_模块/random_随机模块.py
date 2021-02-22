"""
获取随机数字,字母（字符串）
"""
import random

# 0-1...float 随机获取0-1范围的浮点数
ran = random.random()
print(ran)
# 规定范围，随机取浮点数
ran = random.uniform(0.1, 100)
print(ran)
# 规定范围 [ ]，随机取整形数
ran = random.randint(1, 5)
print(ran)
# 规定范围 [ )，随机取整型，没有尾
ran = random.randrange(1, 5)    # range(1, 5) = [1,5) 取不到5
print(ran)
# 规定范围，取可迭代对象，出现的概率相同，字符串，列表，元祖
ran = random.choice([11, 22, 33])
print(ran)
# 规定范围，取可迭代对象，出现的概率相同，可以取多个值,以列表的形式呈现出来
ran = random.sample([11, 22, 33, 44, 44], 3)
print(ran)
ran = random.sample((11, 22, 33, 44, 44), 3)
print(ran)      # [22, 44, 11]
"""
打乱顺序:
# ran = {1, 2, 3, 4, '好成绩', True}   # 集合类型不支持
# ran = (1, 2, 3, 4, '好成绩', True)   # 元祖类型不支持
# ran = False         # bool类型不支持   没有长度
# ran = 123           # 数字类型不支持    没有长度
# ran = '1233洪吉昌'   # 字符串类型不支持
ran = {1: '1', 4: '好成绩', (1, 2, 4): '1'} # 字典类型不支持
"""
ran = [1, 2, 3, 4, '好成绩', True]
random.shuffle(ran)
print(ran)


"""
获取随机的字母
"""
# chr() 内置函数        # 65————》A  122————》z
ch = chr(random.randint(65, 122))
print(ch)
# ascii码对应的数字
print(ord('-'))     # 45

"""
随机验证码的制作:
    1:只由数字和字母组成
    2:验证码（verification code）长度可以自己控制
    3:一直输入，知道正确打印欢迎光临，不区分大小写
    4:是在想退出输入Q 或者 q
"""


def verification_code(self):
    import random
    v_c = ''
    for i in range(1, self+1):
        num = random.randrange(1, 10)
        letter = chr(random.randint(65, 122))
        current = random.choice([num, letter])
        # current = random.sample([num, letter], 1)     # 显示出来一个一个的列表，不可行
        v_c = v_c + str(current)
    return v_c


if __name__ == '__main__':
    while True:
        length = int(input('请选择验证码长度:').strip())
        ver_code = verification_code(length)
        print('\033[33m%s\033[0m' % ver_code)
        my_code = input('请输入验证码:').strip()
        if ver_code.upper() == my_code.upper():
            print('\033[31m欢迎光临\033[0m')
            break
        if my_code.upper() == 'Q':
            break
        else:
            continue


