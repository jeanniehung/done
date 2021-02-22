"""
高级的 文件、文件夹、压缩包 处理模块
"""
# import shutil
# ————————————————————》拷贝
# # 将文件里的内容拷贝到另一个文件中
# shutil.copyfileobj(open('xml_data', 'r'), open('new_xml_data', 'w'))
# # 拷贝文件————》 目标文件无需存在
# shutil.copyfile('new_xml_data', 'a')
# # 仅拷贝权限，内容，组，用户均不变——————》 目标文件必须存在
# shutil.copymode('new_xml_data', 'a')
# # 仅拷贝状态信息，包括 mode bits atime mtime flags——————》目标文件必须存在
# shutil.copystat('new_xml_data', 'a')
# # 拷贝文件和权限-————》目标文件无需存在
# shutil.copy('a', 'b')
# # 拷贝文件和状态信息
# shutil.copy2('a', 'c')


# 重命名文件
# shutil.move('a', 'aa')

# ——————————————————》打包
"""
base_name:压缩包文件名，也可以是压缩包的路径，只是文件名时，则保存到当前目录，否则保存到指定路径
data_bak                       =>保存至当前路径
/tmp/data_bak                  =>保存到 /tmp 下
format:压缩包种类————》'zip', 'tar', 'bztar', 'gztar'
root_dir:要压缩到文件路径，默认是当前路径————》源文件路径
owner:用户，默认是当前用户
group:组，默认是当前组
logger:用于记录日子，通常是 logging.logger 对象
"""
# shutil.make_archive('/Users/jeannie/hjc', 'zip',
#                     '/Users/jeannie/PycharmProjects/learning_python/code/Day22_模块',)


