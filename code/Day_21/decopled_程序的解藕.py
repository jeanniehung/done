import os


def file_handle(array, func_type, res=None):
    if func_type == query:
        with open('文件.conf', 'r', encoding='utf-8') as read_f:
            tag = False
            res = []
            for item in read_f:
                # 文件里字符串左右两边有什么空格，\n,\t符号要除掉在比较
                if item.strip() == 'backend %s' % array:  # 文件在backend 和后面的内容直接有空格
                    tag = True
                    continue
                if tag and item.startswith('backend'):
                    break
                if tag:
                    print('\033[35m%s\033[0m' % item, end='')
                res.append(item)
            return res
    if func_type == change:
        with open('文件.conf', 'r') as read_f, \
                open('new_文件.conf', 'w') as write_f:
            tag = False
            tag1 = True
            for item in read_f:
                if item.strip() == array:  # 找到文件  backend www.hjc1.org 这一行
                    tag = True  # 改变tag的状态
                    continue  # 继续读下一行

                if tag:  # 修改的数据在 backend www.hjc1.org 的下一行可以开始操作
                    if tag1:
                        res.insert(0, '%s\n' % array)  # res里面没有 backend www.hjc1.org ，自己加上去，
                        for record in res:  # 循环已经改好的 backend www.hjc1.org，一行一行读取
                            write_f.write(record)  # 一行写入一个新文件中
                        tag1 = False

                if tag and item.startswith('backend'):
                    tag = False
                if not tag:  # 没有找到 backend www.hjc1.org 就把文件的内容一行一行写到新文件中
                    write_f.write(item)
        os.remove('文件.conf')  # 删除原文件
        os.rename('new_文件.conf', '文件.conf')  # 修改的文件名改成原文件名
        return res


def add():
    print('\033[34;4m 欢迎进入查询功能\033[0m')
    pass


def delete():
    print('\033[33;4m 欢迎进入查询功能\033[0m')
    pass


def change(array):
    print('\033[32;4m 欢迎进入修改功能\033[0m')
    backend = array[0]['backend']   # 得倒www.hjc1。org
    backend_data = 'backend %s' % backend   # 得到 backend www.hjc1.org
    old_record = '%sserver %s %s weight %s max %s\n' % (    # 单词写错,悔恨终身
                        ' ' * 4,
                        array[0]['record']['server'],
                        array[0]['record']['server'],
                        array[0]['record']['weight'],
                        array[0]['record']['max'],
    )
    new_record = '%sserver %s %s weight %s max %s\n' % (
        ' ' * 4,
        array[1]['record']['server'],
        array[1]['record']['server'],
        array[1]['record']['weight'],
        array[1]['record']['max'],
    )
    res = query(backend)        # 得到query函数的返回值，并且赋值给res
    if not res or old_record not in res:    # 如果查询返回的值是空的或者你要改的记录不在赶回值里面
        print('想要修改的值不在文件里')
    else:
        count = res.index(old_record)       # 超着要改的记录在返回的列表中的索引位置
        res[count] = new_record             # 把改好的值赋给返回列表中对应的要改的值

    return file_handle(backend_data, func_type=change, res=res)


def query(array):
    print('\033[31;4m 欢迎进入查询功能\033[0m')

    return file_handle(array, func_type=query)


if __name__ == '__main__':
    msg = """ 有以下功能:
        1: "增加",
        2: '删除',
        3: '修改',
        4: '查询',
        ('q', 'Q'): '退出'
    """
    msg_func = {
        '1': add,
        '2': delete,
        '3': change,
        '4': query,
    }
    # 下面是需要修改的数据和改好的数据
    my = [{'backend': 'www.hjc1.org', 'record': {'server': '10.10.70', 'weight': 20, 'max': 30}},
          {'backend': 'www.hjc1.org', 'record': {'server': '1.1.7', 'weight': 2, 'max': 3}}]
    while True:
        print(msg, sep='\n')
        choice = input('请选择你想要的功能:').strip()
        if not choice:
            continue
        if choice.upper() == 'Q':
            break
        data = input('请输入你想操作的数据:').strip()
        if choice != '4':
            data = eval(data)
        ret = msg_func[choice](data)
        print('\033[45m这是返回值\033[0m:', ret)

