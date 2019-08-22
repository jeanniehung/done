"""
os模块是与操作系统交叉的一个接口:对文件，目录的操作
"""
import os
"""
等同于终端操作
"""
print(os.getcwd())  # 当前执行文件的目录
os.chdir('..')        # 相当与cd，括号里加 cd 后面的内容
os.curdir             # 返回当前目录：（'.'）
os.pardir             # 获取当前目录的父目录字符串名：('..')
print(os.sep)           # 输出指定系统的分隔符
print(os.linesep)       # 输出当前平台使用的行终止符
print(os.pathsep)       # 输出系统用于分割文件路径的字符串
print(os.name)          # 输出字符串指示当前平台
print(os.environ)       # 输出系统环境变量
os.system('pwd')      # 相当于终端，括号里直接输入命令
os.mkdir('Day21')     # 建单级目录，相对执行文件同一级
os.rmdir('Day21')     # 建单级目录，相对执行文件同一级
print(os.listdir('path'))   # 列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
os.makedirs('a/b')    # 建递归目录，相对执行文件同一级
os.removedirs('b')    # 若目录为空，则删除,依此类推,故要先进入a目录在执行该操作
os.remove('path')     # 括号里是文件路径，删除文件
os.rename('old_name', 'new_name')   # 重命名文件，目录
"""
文件绝对路径问题
"""
print(os.path.abspath('sss'))    # 返回 sss 规范化的绝对路径
print(os.path.split('绝对路径'))
# 用一个元祖装 sss 分割 ('/Users/jeannie/PycharmProjects/learning_python/code/Day22_模块', 'sss.py')
print(os.path.dirname('sss.py'))    # 元祖的一个元素
print(os.path.basename('sss.py'))   # 元祖的第二个元素，如何path以／或\结尾，那么就会返回空值
print(os.path.join('/Users/jeannie', 'PycharmProjects'))        # 路径拼接
print(os.path.exists('sss.py'))     # 如果path存在，返回True；如果path不存在，返回False
print(os.path.isabs('sss'))      # 如果path是绝对路径，返回True
print(os.path.isfile('sss'))     # 如果path是一个存在的文件，返回True。否则返回False
print(os.path.isdir('sss'))     # 如果path是一个存在的目录，则返回True。否则返回False

"""
print(os.stat('sss.py'))
# 查看文件，目录的信息
# st_size=7, 文件大小,有多少个字节
# st_atime=1566308131：文件上一次操作时间
# st_mtime=1566308029：文件上一次修改时间
# st_ctime=1566308130：文件创建时间————》时间戳形式
"""
os.path.getatime('path')  # 返回path所指向的文件或者目录的最后存取时间
os.path.getmtime('path')  # 返回path所指向的文件或者目录的最后修改时间
os.path.getsize('path')   # 返回path的大小
