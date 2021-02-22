# 统计各省人口占中国人口的比例
def get_pop():
    with open('全国各省人口数', 'r+', encoding='utf-8') as file:
        for line in file:
            yield eval(line)


def get_bili():
    gene_pop = get_pop()
    pop_list = []
    count = 0
    for i in gene_pop:
        pop_list.append(i)
    for i in pop_list:
        count += i['population']
    for i in pop_list:
        print('%s人口占全国总人口的比例是:%f%%' % (i['name'], i['population']/count))

# all_pop = sum(int(eval(i)['population']) for i in gene_pop)
#  文件中全国人口数22023453330
# s_pop = []
# for i in gene_pop:
#     pop_num = int(eval(i)['population'])
#     pop_province = eval(i)['name']
#     print('%s人口占全国人口总数的比例是：%f%%' % (pop_province, pop_num / 22023453330))
#     s_pop.append(pop_num)
# all_pop = sum(s_pop)
# print('全国总人口：', all_pop)
# print('%s人口占全国人口的比例是：%s %%' % ('pop_province', pop_num/all_pop))


# 上五步和下面相同，占内存
# all_pop = sum([int(eval(i)['population']) for i in gene_pop])


"""
1. 文件a.txt内容：每一行内容分别为商品名字，价钱，个数，求出本次购物花费的总钱数
apple 10 3
tesla 100000 1
mac 3000 2
lenovo 30000 3
chicken 10 3
"""
all_price = []


def count_price():
    with open('购物清单', 'r+', encoding='utf-8') as file:
        for line in file:
            yield line


gene_cp = count_price()
# for i in gene_cp:
#     i1 = int(eval(i)['价格'])
#     i2 = int(eval(i)['个数'])
#     p_c = i1 * i2
#     all_price.append(p_c)
# print(sum(all_price))
print(sum(eval(i)['价格']*eval(i)['个数'] for i in gene_cp))



