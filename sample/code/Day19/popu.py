"""
@Time    : 2019-08-16 22:05
@Author  : Jeannie
"""


# 统计各省人口占中国人口的比例
def get_pop():
    with open('全国各省人口数', 'r+', encoding='utf-8') as file:
        for line in file:
            yield line


gene_pop = get_pop()
s_pop = []
count = 0
for item in gene_pop:
    s_pop.append(eval(item))  # 使用eval函数将字符串转换为字典，本来字符串的内容就先是字典的结构
                                # 并将字典写入一个列表

    """
    举个例子：
    a = "{'a': 'jim', 'b': 15}"
    b = eval(a)
    print(type(b))
    """

for item in s_pop:
    count += item['population']  # 计算全国人口总是


# 之后计算百分比
for item in s_pop:
    print('%s人口占全国人口总数的比例是：%f%%' % (item['name'], item['population']/count))