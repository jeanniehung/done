"""
1：设计计算器的思路：
    —— 递归找到表达式中只含有 数字和运算符 的表达式，并计算结果
    —— 由于整数计算会忽略小数，所有的数字都认为是浮点型操作，以此来保留小数
2：使用技术：
    —— 正则表达式
    —— 递归
————————》
正则匹配时， 有 1 个或者以上最好写 +
           有 0 个或者以上最好写 *
           [\+\-\*\/] = [+\-*/] 加减乘除 选择其中之一

——————》 集体步骤：
    ——1：从左到右找到第一个最内层到括号
"""

import re


def compute_mul_div(self):
    """
    计算乘除
    :param self:
    :return:
    """
    # 拿到表达式
    expression = self[0]
    # 设置好正则匹配规则
    obj = re.compile('\d+\.?\d*[*/][+\-]?\d+\.?\d*')
    # 如果不符合规则就退出函数
    if not obj.search(expression):
        return
    # 从左到右得到第一个  符合规则的 表达式
    content = obj.search(expression).group()
    # 判断如果是 * 进行计算
    if len(content.split('*')) > 1:
        n1, n2 = content.split('*')
        value = float(n1) * float(n2)
    # 如果是 / 进行计算
    else:
        n1, n2 = content.split('/')
        value = float(n1) / float(n2)
    # 把表达式按 拿出的第一个表达式 左右分割 分别赋给变量
    before, after = re.split('\d+\.?\d*[*/][+\-]?\d+\.?\d*', expression, 1)
    # 把 得倒的结果 和 之前赋值好的变量 左右拼接
    self[0] = '%s%s%s' % (before, value, after)
    # 递归处理 乘除 运算
    compute_mul_div(self)


def compute_add_sub(self):
    """
    计算加减
    :param self:
    :return:
    """
    # 循环处理 + - 符号
    while True:
        if self[0].__contains__('++') or self[0].__contains__('+-')\
                or self[0].__contains__('-+')or self[0].__contains__('--'):
            # 符号相反是 -       符号相同是 +
            self[0] = self[0].replace('++', '+')
            self[0] = self[0].replace('+-', '-')
            self[0] = self[0].replace('-+', '-')
            self[0] = self[0].replace('--', '+')
        # 直到没有上述类型 退出循环
        else:
            break
    # 判断如果是 - 开头 提出 - ； 所有符号取反 ； 状态 0 加 1
    if self[0].startswith('-'):
        self[1] += 1
        # 不可以是 .  小数点  会影响 计算结果  ——————————————————————》 我操
        self[0] = self[0].replace('-', '。')
        self[0] = self[0].replace('+', '-')
        self[0] = self[0].replace('。', '+')
        self[0] = self[0][1:]
    # 拿到表达式
    expression = self[0]
    # 设置好正则匹配规则
    obj = re.compile('\d+\.?\d*[+\-]\d+\.?\d*')
    # 如果不符合规则，退出函数
    if not obj.search(expression):
        return
    # 从左到右拿到 第一个 符合规则的表达式
    content = obj.search(expression).group()
    # 判断如果是 + 进行运算
    if len(content.split('+')) > 1:
        n1, n2 = content.split('+')
        value = float(n1) + float(n2)
    # 如果是 - 进行运算
    else:
        n1, n2 = content.split('-')
        value = float(n1) - float(n2)
    # 把表达式 以拿出的第一个符合规则的表达式 左右分割 并赋值给变量
    before, after = re.split('\d+\.?\d*[+\-]\d+\.?\d*', expression, 1)
    # 以得到 的值 和 之前定义好的变量 左右拼接
    self[0] = '%s%s%s' % (before, value, after)
    # 递归处理 加减 运算
    compute_add_sub(self)


def compute(self):
    """
    计算加减乘除
    :param self:
    :return:
    """
    # 把 表达式 和 一个状态量 0 拼接成 两个元素的列表
    ex_list = [self, 0]
    # 先进行 乘除 运算
    compute_mul_div(ex_list)
    # 在进行 加减 运算
    compute_add_sub(ex_list)
    # 判断 状态量 和 2 的 余数 ； 如果是 1 ————》提出了 符号 得到的值 * -1 是需要的结果
    if divmod(ex_list[1], 2)[1] == 1:
        result = float(ex_list[0]) * -1
    # 如果不是 得倒的值 就是需要的结果
    else:
        result = float(ex_list[0])
    # 返回得倒的结果
    return result


def exec_bracket(expression):
    """
    递归处理括号
    :param expression:
    :return:
    """
    # 定义好 处理 （） 的 规则        这里的 加减乘除 后面要用 *
    obj = re.compile('\(([+\-*/]*\d+\.?\d*){2,}\)')
    # 如果不符合 规则； 直接调运算函数 进行运算
    if not obj.search(expression):
        value = compute(expression)
        return value
    # 从左到右 得倒第一个符合规则的表达式
    content = obj.search(expression).group()
    # 原表达式 以得到的第一个表达式为中心 分割成   三部分
    before, nothing, after = re.split('\(([+\-*/]*\d+\.?\d*){2,}\)', expression, 1)
    # 得倒的表达式去除 （） ；只要 （） 里面的数字和运算符号
    content = content[1: len(content)-1]
    # 把表达式传入 计算函数计算 并接收返回的结果
    new_content = compute(content)
    # 用之前分割得倒的 左右变量 和 返回的结果 拼接成新的表达式
    expression = '%s%s%s' % (before, new_content, after)
    # 递归处理 （） 问题
    return exec_bracket(expression)


if __name__ == '__main__':
    while True:
        # inp = "1-5*980.0"
        # inp = "1-2*-30/-12*(-20+200*-3/-200*-300-100)"
        # inp = '1 - 2 * ( (60-30 +(-40.0/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) ) '
        inp = input('请输入表达式:').strip()
        if inp.upper() == 'Q':
            break
        # 表达式中的 任意非空白字符 用 '' 替换 ——————》 表达式里没有空格
        inp = re.sub('\s*', '', inp)
        # 把表达式传入 执行支架 函数里进行处理，并且接收返回结果
        e_b = exec_bracket(inp)
        # 打印返回结果
        print('\033[33m结果是\033[0m', '\033[31m%s\033[0m' % e_b)


# def compute_mul_div(self):
#     # 取出表达式
#     vag = self[0]
#     # 乘除的格式
#     muh = re.search('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*', vag)
#     if not muh:
#         return
#     # 取出第一个符合格式的算式
#     content = re.search('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*', vag).group()
#     # 计算算式 （浮点型）
#     if len(content.split('*')) > 1:
#         n1, n2 = content.split('*')
#         value = float(n1) * float(n2)
#     else:
#         n1, n2 = content.split('/')
#         value = float(n1) / float(n2)
#     before, after = re.split('\d+\.*\d*[\*\/]+[+\-]?\d+\.*\d*', vag, 1)
#     new_str = '%s%s%s' % (before, value, after)
#     self[0] = new_str
#     compute_mul_div(self)
#
#
# def compute_add_sub(arg):
#     # 加减操作之前 进行 符号 转换
#     while True:
#         if arg[0].__contains__('+-') or arg[0].__contains__("++") or arg[0].__contains__('-+') or arg[0].__contains__(
#                 "--"):
#             arg[0] = arg[0].replace('+-', '-')
#             arg[0] = arg[0].replace('++', '+')
#             arg[0] = arg[0].replace('-+', '-')
#             arg[0] = arg[0].replace('--', '+')
#         else:
#             break
#     # 是以 - 号开头 标记一个状态， + 换成- ， - 换成 +
#     if arg[0].startswith('-'):
#         arg[1] += 1
#         arg[0] = arg[0].replace('-', '&')
#         arg[0] = arg[0].replace('+', '-')
#         arg[0] = arg[0].replace('&', '+')
#         # 表达式 是 除去 - 的 式子
#         arg[0] = arg[0][1:]
#     val = arg[0]
#     mch = re.search('\d+\.?\d*[\+\-]{1}\d+\.?\d*', val)
#     if not mch:
#         return
#     content = re.search('\d+\.?\d*[\+\-]{1}\d+\.?\d*', val).group()
#     if len(content.split('+')) > 1:
#         n1, n2 = content.split('+')
#         value = float(n1) + float(n2)
#     else:
#         n1, n2 = content.split('-')
#         value = float(n1) - float(n2)
#
#     before, after = re.split('\d+\.?\d*[\+\-]{1}\d+\.?\d*', val, 1)
#     new_str = "%s%s%s" % (before, value, after)
#     arg[0] = new_str
#     compute_add_sub(arg)
#
#
# def compute(self):
#     # 把表达式 放在列表的第 0 个位子, 第 1 个位置元素是为了标识状态 0 或者 1
#     inp = [self, 0]
#     # 先处理乘除
#     compute_mul_div(inp)
#     # 在处理加减
#     compute_add_sub(inp)
#     # inp[1]的值是 0 或者 1， 和 2 进行求商取余, 拿到余数进行判断
#     if divmod(inp[1], 2)[1] == 1:
#         result = float(inp[0])
#         # 取出 - 号 全变号得到的结果 * -1 才是原值
#         result = result * -1
#     else:
#         result = float(inp[0])
#     return result
#
#
# def deal_parentheses(self):
#     # 没有括号
#     if not re.search('\(([\+\*\-\/]*\d+\.?\d*){2,}\)', self):
#         value = compute(self)
#         return value
#     else:
#         # 获取 第一个 只含有 数字/小数 和 操作符 的括号
#         content = re.search('\(([\+\-\*\/]*\d+\.*\d*){2,}\)', self).group()
#         # 以取出的括号分割表达式，分割成三部分
#         before, nothing, after = re.split('\(([\+\-\*\/]*\d+\.*\d*){2,}\)', self, 1)
#         print('before:', self)
#         # 去掉 （） 取出的表达式
#         content = content[1:len(content)-1]
#         # 把没有 （）的表达式交给 compute 函数计算，并且得到返回值
#         ret = compute(content)
#         # 返回值 取代 去掉 （） 取出的表达式 并且打印出来
#         print('%s=%s' % (content, ret))
#         # 把得倒 新的表达式 拼接出来
#         data = "%s%s%s" % (before, ret, after)
#         # 把 新的表达式 打印出来
#         print('after:', data)
#         print('上一次计算结束'.center(20, '.'))
#         # 递归处理 括号
#         return deal_parentheses(data)
#
#
# if __name__ == '__main__':
#     # 原始表达式
#     # expression = "1-2*-30/-12*(-20+200*-3/-200*-300-100)"
#     # expression = "1-5*2.0"
#     expression = '1 - 2 * ( (60-30 +(-40.0/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) ) '
#     # 表达式的 任意非空白字符 替换成 ''
#     expression = re.sub('\s*', '', expression)
#     # 表达式 传入 计算 得到 返回结果
#     d_p = deal_parentheses(expression)
#     # 打印结果
#     print(d_p)
