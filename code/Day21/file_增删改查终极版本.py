import os


def file_handle(filename, backend_data, record_list=None, type='query'):
    filename_swap = filename + '_swap'
    bak_file = filename + '_bak'
    # type query change append
    if type == 'query':
        r_list = []
        with open(filename, 'r') as read_f:
            tag = False
            for line in read_f:
                if line.strip() == backend_data:
                    tag = True
                    continue
                if tag and line.startswith('backend'):
                    tag = False
                if tag and line:
                    r_list.append(line.strip())     # 每条数据开头都没有了空格
            for item in r_list:
                print(item)
        return r_list
    elif type == 'append':
        with open(filename, 'r') as read_f,\
                open(filename_swap, 'w') as write_f:
            for line in read_f:
                write_f.write(line)
            for new_line in record_list:
                if new_line.startswith('backend'):
                    write_f.write(new_line + '\n')
                else:
                    write_f.write('%s%s\n' % (' ' * 4, new_line))
        os.rename(filename, bak_file)
        os.rename(filename_swap, filename)
        os.remove(bak_file)
        return record_list
    elif type == 'change':
        with open(filename, 'r') as read_f,\
                open(filename_swap, 'w') as write_f:
            tag = False
            has_write = False
            for line in read_f:
                if line.strip() == backend_data:
                    tag = True
                    continue
                if tag and line.startswith('backend'):
                    tag = False
                if not tag:
                    write_f.write(line)
                if tag:
                    if not has_write:
                        for new_line in record_list:
                            if new_line.startswith('backend'):
                                write_f.write(new_line + '\n')  # 一行写一次循环的new_line
                            else:
                                write_f.write('%s%s\n' % (' '*4, new_line))
                        has_write = True
        os.rename(filename, bak_file)
        os.rename(filename_swap, filename)
        os.remove(bak_file)
        return record_list


def query(self):
    backend_data = 'backend %s' % self
    return file_handle('测试.conf', backend_data, type='query')


def change(self):
    backend = self[0]['backend']
    record_list = query(backend)
    backend_data = 'backend %s' % backend
    old_record = 'server %s %s weight %s max %s' % (
                        self[0]['record']['server'],
                        self[0]['record']['server'],
                        self[0]['record']['weight'],
                        self[0]['record']['max'],)
    new_record = 'server %s %s weight %s max %s' % (
        self[1]['record']['server'],
        self[1]['record']['server'],
        self[1]['record']['weight'],
        self[1]['record']['max'],)
    if not record_list or old_record not in record_list:
        print('\033[33m无此数据\033[0m')
    else:
        record_list.insert(0, backend_data)
        count = record_list.index(old_record)
        record_list[count] = new_record
        return file_handle('测试.conf', backend_data, record_list, 'change')


def add(self):
    backend = self['backend']
    record_list = query(backend)
    backend_data = 'backend %s' % backend
    current_record = 'server %s %s weight %s max %s' % (
                        self['record']['server'],
                        self['record']['server'],
                        self['record']['weight'],
                        self['record']['max'],)
    if not record_list:
        record_list.append(backend_data)
        record_list.append(current_record)
        file_handle('测试.conf', backend_data, record_list, 'append')
    else:
        record_list.insert(0, backend_data)
        if current_record not in record_list:
            record_list.append(current_record)
        file_handle('测试.conf', backend_data, record_list, 'change')


def delete(self):
    backend = self['backend']
    record_list = query(backend)
    backend_data = 'backend %s' % backend
    current_record = 'server %s %s weight %s max %s' % (
        self['record']['server'],
        self['record']['server'],
        self['record']['weight'],
        self['record']['max'],)
    if not record_list or current_record not in record_list:
        print('\033[34m无此数据\033[0m')
        return record_list
    else:
        record_list.insert(0, backend_data)
        record_list.remove(current_record)
        file_handle('测试.conf', backend_data, record_list, 'change')


if __name__ == '__main__':
    msg = """有以下功能：
        1：查询
        2：修改
        3：添加
        4：删除
        q，Q：退出
    """
    msg_func = {
        '1': query,
        '2': change,
        '3': add,
        '4': delete,
        'q': exit,
        'Q': exit,
    }
    my = {'backend': 'www.hjc1.org',
          'record': {'server': '2.2.2.3', 'weight': 20, 'max': 3000}}

    while True:

        print(msg)
        choice = input('请输入对应的功能:').strip()
        if not choice or choice not in msg_func.keys():
            continue
        if choice.upper() == 'Q':
            break
        data = input('>>数据:') .strip()
        if choice != '1':
            data = eval(data)
        que = msg_func[choice](data)
        print(que)

