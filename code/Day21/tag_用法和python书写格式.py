"""
存在函数时：

函数就顶头写
if __name__ == '__main__':  # main
    下面是你要写的代码

"""
# def file_handle(array, func_type, res=None):
# def add():
# def delete():
# def change():
# def query():
# if __name__ == '__main__':
#     print("\033[1;45m洪吉昌真的好帅呀\033[0m")
#     print('\033[34m洪吉昌\033[0m')


"""
tag用法,执行一次退出，不管在第几层，直接全部退出循环
用于模拟两种状态，一种状态干什么，另一种状态干什么
"""
tag = True
while tag:
    print('第一层')
    choice = input('这是level1输入的内容:').strip()
    if choice == 'q':
        break
    if choice.upper() == 'Q':
        tag = False
    while tag:
        print('第二层')
        choice = input('这是level2输入的内容:').strip()
        if choice == 'q':
            break
        if choice.upper() == 'Q':
            tag = False
        while tag:
            print('第三层')
            choice = input('这是level3输入的内容:').strip()
            if choice == 'q':
                break           # 退出当前层到上一层
            if choice.upper() == 'Q':
                tag = False     # 不管在哪里，退出所有层
