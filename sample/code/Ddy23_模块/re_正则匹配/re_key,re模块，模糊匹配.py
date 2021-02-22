"""
给字符串进行模糊匹配
"""

# 正则
"""
正则就是用一些具有特殊含义的符号组合到一起（称为正则表达式）来描述字符或者字符串的方法。
或者说：正则就是用来描述一类事物的规则。（在Python中）它内嵌在Python中，并通过 re 模块实现。
正则表达式模式被编译成一系列的字节码，然后由用 C 编写的匹配引擎执行。
"""
# 元字符：
"""
            .       匹配任意字符，除了换行符，re.DOTALL 可以匹配任意字符(re.S)
            ^       匹配字符串的开头
            $       匹配字符串的结尾      
            *       重复匹配 0 个或无数个表达式 [0,+∞）
            +       重复匹配 1 个或无数个表达式 [1,+∞)
            ？      重复匹配 0 个或者 1 个
            
贪婪匹配     .*       什么都可以无限匹配
非贪婪匹配    .*?      不规定类型出现0-1次

            {n, m}  假设有 n+2 个可以匹配到的对象，只要 m >= n+2 就匹配 n+2个对象；若 m < n+2 就匹配 m 个对象           
            {n}     精确匹配 n 个表达式  {0, } = *  {1, } = +  {0, 1} = ?
            *？      精确匹配 0 个
            +？      精确匹配 1 个
            a|b      匹配 a 或者 b 都存在就都输出 
print(re.findall('hell(?:o|a)', 'hellohellahelc'))            
    
            ()      分组  
print(re.search('(?P<name>[a-z,A-Z]+)(?P<age>\d+)', 'alex23Ange20').group('name'))  # alex
print(re.search('(?P<name>[a-z,A-Z]+)(?P<age>\d+)', 'alex23Ange20').group('age'))   # 23
print(re.search('(?P<name>[a-z,A-Z]+)(?P<age>\d+)', 'alex23Ange20').group())        # alex23 

            (abc)     优先取出括号里的内容
            (?:abc)    取消优先级
findall的结果不是匹配的全部内容，而是组内的内容,?:可以让结果为匹配的全部内容
print(re.findall('href="(.*?)"','<a href="http://www.baidu.com">点击</a>'))
# 结果是：['http://www.baidu.com']
print(re.findall('href="(?:.*?)"','<a href="http://www.baidu.com">点击</a>'))
# 结果是：['href=http://www.baidu.com']
    
"""

# 字符集   []      []内的都为普通字符了
"""
            [abc]    匹配 'a','b','c' 中的任意一个
            [^abc]   匹配除了 'a','b','c' 之外的所有字符,一个一个放在列表中，非
            [a-zA-Z]    匹配 a-z 范围中的所有字符
            [\]      转义(r) \(  不是元字符是(     \) 不是元字符是)
            
    print(re.findall('[+*-/]', '1+2-3*4/5'))
    # 取出字符串里的 +  * / - 但是 - 不能紧挨着在 + 的后面
    
    print(re.findall('([^()]*)', '2+(2*2+(2-1)*2)'))
    # 取出不是括号的每个元素，括号用''代替     ['2+', '', '2*2+', '', '2-1', '', '*2', '', '']

    print(re.findall('\([^()]*\)', '2+(2*2+(2-1)*2)'))
    # 取出最内层的括号和里面的元素    ['(2-1)']
    
"""
# 让元字符变成普通字符，让普通字符变成有功能的字符      \  转义 python中(r)
# r代表告诉解释器使用rawstring，即原生字符串，把我们正则内的所有符号都当普通字符处理，不要转义
"""
让普通字符变成有功能的字符：
            \d      匹配0-9中的任意一个字符，  等价[0-9]       \D      匹配除了0-9的任意一个字符， 等价[^0-9]
            \s      匹配任意空白空白字符    [\n\t\r\f]        \S      匹配任意非空字符        
            \w      匹配数字字母及下划线,汉字                  \W      匹配非字母数字及下划线   
            \A      匹配字符串开始————》^
            \G      匹配最后完成匹配的位置
            \z      匹配字符串结束                            \Z  __》$  匹配字符串结束，如果存在换行，自匹配换行前的结束字符
            \n      匹配一个换行符,需要转义
            \t      匹配一个制表符
            \b      匹配一个特殊字符边界      空格 @ # & 等    
print(re.findall(r'\n', 'hello egon \n123'))    # ['\n']  \n,\t 在python中也有意义 r 进行转义
print(re.findall(r'\t', 'hello egon\t123'))     # ['\t']
print(re.findall(r'\b', 'q&'))                 # ['q']

"""


"""
# re下的方法
"""
import re
"""
findall finditer    找出所有符合的字符   得到的列表里的元素都是字符串
"""
# 返回所有满足匹配条件的结果,放在列表里       ['e', 'e', 'e']
print(re.findall('e', 'alex make love'))
# 返回所有满足匹配条件的结果,生成一个迭代器,如果字符串没有匹配，则返回None。
print(re.finditer('e', 'alex make love'))
print(re.finditer('e', 'alex make love').__next__().group())  # 一个一个取出来
"""
# search  match 找出一个符合的字符  得倒的字符串
# """
# 从左到右找到第一个匹配然后返回一个包含匹配信息的对象,
# 该对象可以通过调用group()方法得到匹配的字符串,如果字符串没有匹配，则返回None。
print(re.search('h', 'alex make love'))
print(re.search('e', 'alex make love').group())
print(re.search('e', 'alex make love').span())          # 查看匹配长度
print(re.search('(?P<name>[a-z,A-Z]+)(?P<age>\d+)', 'alex23Ange20').group('name'))  # alex
print(re.search('(?P<name>[a-z,A-Z]+)(?P<age>\d+)', 'alex23Ange20').group('age'))   # 23
print(re.search('(?P<name>[a-z,A-Z]+)(?P<age>\d+)', 'alex23Ange20').group())        # alex23
# 同search,不过在字符串开始处进行匹配,完全可以用search+^代替match
print(re.match('hel', 'hello hel').group())     # hel
"""
split 分割     得到的列表里的元素都是字符串
第一步:按 a 分得倒                                 'c' 'cba'
第二步:按第一步得到的'cba'里面按'b'分得到             'c'  'a'
第三步:按第二步得到的'a'分得到                       ''  ''
故结果是：
        ['c','c','','']
"""
# 先按'a'分割得到''和'bcd',再对''和'bcd'分别按'b'分割
print(re.split('[a,b]', 'cacba'))   # ['c', 'c', '', '']
"""
sub 替换     得到的是字符串
"""
# a 替换 A    不指定 n 默认替换所有
print(re.sub('a', 'A', 'alex make love'))       # Alex mAke love
# a 替换 A    指定替换 1 个  从左往右找
print(re.sub('a', 'A', 'alex make love', 1))    # Alex make love
print(re.subn('a', 'A', 'alex make lea'))       # ('Alex mAke leA', 3) 输出替换个数
# 替换位置
"""
第三个括号取到的元素和第一个括号取到的元素对调位置
"""
print(re.sub('(\d+)(\s)(\d+)', r'\3\2\1', 'hjc 123 456 zh'))         # hjc 456 123 zh
print(re.sub('(.*?)(\d+)(\s)(\d+)(.*)', r'\1\4\3\2\5', 'hjc 123 456 zh'))  # hjc 456 123 zh
"""
compile 事先写好规则, 用一次调一次
"""
obj = re.compile('\d{2}')
print(obj.findall('2122a123b2c432'))            # ['21', '22', '12', '43']
print(obj.search('2122a123b2c432').group())     # '21'

"""
re.compile('-?\d+\.?\d*')     # 匹配小数 整数（正 负）
print('hello'.find('pattern'))

"""

"""
补充
"""
# import re

# #  使用|，先匹配的先生效，|左边是匹配小数，而findall最终结果是查看分组，所有即使匹配成功小数也不会存入结果
# #  而不是小数时，就去匹配(-?\d+)，匹配到的自然就是，非小数的数，在此处即整数
#
# print(re.findall(r"-?\d+\.\d*|(-?\d+)","1-2*(60+(-40.35/5)-(-4*3))"))
# # 找出所有整数['1', '-2', '60', '', '5', '-4', '3']
#
# # 找到所有数字:
# print(re.findall('\D?(\-?\d+\.?\d*)', "1-2*(60+(-40.35/5)-(-4*3))"))
# # ['1','2','60','-40.35','5','-4','3']
# print(re.findall('(\-?\d+\.?\d*)', "1-2*(60+(-40.35/5)-(-4*3))"))
# print(re.findall('\D?(?:\-?\d+\.?\d*)', "1-2*(60+(-40.35/5)-(-4*3))"))

"""
#总结:尽量精简,详细的如下
    # 尽量使用泛匹配模式.*
    # 尽量使用非贪婪模式:.*?
    # 使用括号得到匹配目标:用group(n)去取得结果
    # 有换行符就用re.S:修改模式
content='''Hello 123456 World_This
is a Regex Demo

res=re.match('He.*?(\d+).*?Demo$',content,re.S) #re.S让.可以匹配换行符
print(res)
"""

# 贪婪匹配:.*代表匹配尽可能多的字符
# import re
# content = 'Hello 123 456 World_This is a Regex Demo'
#
# res = re.match('^He.*(\d+).*Demo$',content)
# print(res.group(1))                   # 只打印6,因为.*会尽可能多的匹配,然后后面跟至少一个数字


# #非贪婪匹配:?匹配尽可能少的字符
# import re
# content = 'Hello 123 456 World_This is a Regex Demo'
#
# res = re.match('^He.*?(\d+).*?Demo$',content)
# print(res.group(1))                   # 打印 123
