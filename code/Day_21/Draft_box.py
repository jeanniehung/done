# import os
#
#
# def file_handle(array, func_type, res=None):
#     if func_type == query:
#         with open('数据', 'r') as read_f:
#             tag = False
#             res = []
#             for file_line in read_f:
#                 if file_line.strip() == 'backend %s' % array:
#                     tag = True
#                     continue
#                 if tag and file_line.startswith('backend'):
#                     tag = False
#                 if tag:
#                     print('\033[35m%s\033[0m' % file_line, end='')
#                     res.append(file_line)  # 查询到的数据加载到列表中
#         return res
#     if func_type == change:
#         with open('数据', 'r') as read_f, \
#                 open('数据.swap', 'w') as write_f:
#             tag = False
#             has_write = True
#             for file_line in read_f:
#                 if file_line.strip() == array:
#                     tag = True
#                     continue
#                 if tag and file_line.startswith('backend'):
#                     tag = False
#                 if not tag:  # 放在第一个位置，文件修改内容在第一个目录下，第一个目录名会多一个；
#                     # 放在当前第一和第二个if判断的中间，第二个目录名会消失；
#                     # 只能放在当前文字
#                     write_f.write(file_line)
#                 if tag:
#                     if has_write:
#                         res.insert(0, '%s\n' % array)
#                         for recode in res:
#                             write_f.write(recode)
#                         has_write = False
#
#         os.remove('数据')
#         os.rename('数据.swap', '数据')
#         return res
#
#
# def add():
#     pass
#
#
# def delete():
#     pass
#
#
# def change(array):
#     print('\033[32;4m欢迎进入修改功能\033[0m')
#     backend = array[0]['backend']
#     backend_data = 'backend %s' % backend
#     old_record = '%sserver %s %s weight %s max %s\n' % (
#                 ' ' * 4,
#                 array[0]['record']['server'],
#                 array[0]['record']['server'],
#                 array[0]['record']['weight'],
#                 array[0]['record']['max'],
#     )
#     new_record = '%sserver %s %s weight %s max %s\n' % (
#         ' ' * 4,
#         array[1]['record']['server'],
#         array[1]['record']['server'],
#         array[1]['record']['weight'],
#         array[1]['record']['max'],
#     )
#     res = query(backend)
#     if not res or old_record not in res:
#         print('文件中不存在改数据需要被修改')
#     else:
#         count = res.index(old_record)
#         res[count] = new_record
#
#     return file_handle(backend_data, func_type=change, res=res)
#
#
# def query(array):
#     print('\033[31;4m欢迎进入查询功能\033[0m')
#     return file_handle(array, func_type=query)
#
#
# if __name__ == '__main__':
#     msg = """有以下功能：
#     1：增添
#     2：删除
#     3：修改
#     4：查询
#     (q,Q)：退出
#     """
#     msg_func = {
#         '1': add,
#         '2': delete,
#         '3': change,
#         '4': query
#     }
#     my = [{'backend': 'www.hjc1.org', 'record': {'server': '10.10.70', 'weight': 20, 'max': 30}},
#           {'backend': 'www.hjc1.org', 'record': {'server': '1.1.7', 'weight': 2, 'max': 3}}]
#
#     while True:
#         print(msg)
#         choice = input('请选择你需要的功能:').strip()
#         if not choice or choice not in msg:
#             continue
#         if choice.upper() == 'Q':
#             break
#         data = input('请输入你要操作的数据:').strip()
#         if choice != '4':
#             data = eval(data)
#         ret = msg_func[choice](data)
#         print(ret)
# import os
#
#
# def file_handle(array, func_type, res=None):
#     if func_type == query:
#         with open('数据', 'r') as read_f:
#             tag = False
#             res = []
#             for file_line in read_f:
#                 if file_line.strip() == 'backend %s' % array:
#                     tag = True
#                     continue
#                 if tag and file_line.startswith('backend'):
#                     tag = False
#                 if tag:
#                     print('\033[35m%s\033[0m' % file_line)
#                     res.append(file_line)
#         return res
#     if func_type == change:
#         with open('数据', 'r') as read_f,\
#                 open('数据.swap', 'w') as write_f:
#             tag = False
#             has_write = True
#             for file_line in read_f:
#                 if file_line.strip() == array:
#                     tag = True
#                     continue
#                 if tag and file_line.startswith('backend'):
#                     tag = False
#                 if not tag:
#                     write_f.write(file_line)
#                 if tag:
#                     if has_write:
#                         res.insert(0, '%s\n' % array)
#                         for record in res:
#                             write_f.write(record)
#                         has_write = False
#         os.remove('数据')
#         os.rename('数据.swap', '数据')
#         return res
#
#
# def change(array):
#     print('\033[32;4m这是修改功能\033[0m')
#     back_data = 'backend %s' % array[0]['backend']
#     old_record = '%sserver %s %s weight %s max %s\n' % (
#         ' ' * 4,
#         array[0]['record']['server'],
#         array[0]['record']['server'],
#         array[0]['record']['weight'],
#         array[0]['record']['max'],
#     )
#     new_record = '%sserver %s %s weight %s max %s\n' % (
#         ' ' * 4,
#         array[1]['record']['server'],
#         array[1]['record']['server'],
#         array[1]['record']['weight'],
#         array[1]['record']['max'],
#     )
#     res = query(array[0]['backend'])
#     if not res or old_record not in res:
#         print('要修改内容不在文件中')
#     else:
#         count = res.index(old_record)
#         res[count] = new_record
#     return file_handle(back_data, func_type=change, res=res)
#
#
# def query(array):
#     print('\033[31;4m这是查找功能\033[0m')
#     return file_handle(array, func_type=query)
#
#
# if __name__ == '__main__':
#     msg = """有以下功能:
#         1:修改
#         2:查找
#         (q,Q):退出
#     """
#     msg_func = {
#         '1': change,
#         '2': query
#     }
#     my = [{'backend': 'www.hjc1.org', 'record': {'server': '10.10.70', 'weight': 20, 'max': 30}},
#           {'backend': 'www.hjc1.org', 'record': {'server': '1.1.7', 'weight': 2, 'max': 3}}]
#
#     while True:
#         print(msg)
#         choice = input('请输入你想使用的功能:').strip()
#         if not choice:
#             continue
#         elif choice.upper() == 'Q':
#             break
#         data = input('请输入操作的数据').strip()
#         if choice != '2':
#             data = eval(data)
#         res = msg_func[choice](data)
#         print(res)
