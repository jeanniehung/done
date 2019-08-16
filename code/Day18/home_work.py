"""
1:自定义模拟range(1,7,2)
"""


def my_r(start, stop, step=1):
    while start < stop:
        yield start
        start = start + step


obj = my_r(1, 7, 2)        # 先得让函数运行得到不同的yield
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())
# print(obj.__next__())      # StopIteration

# 应用于for循环
for i in my_r(1, 7, 2):
    print(i)


"""
2:模拟管道，实现功能:tail -f access.log | grep '404'
"""
