"""
python中，一个包含一组功能的.py文件就是一个模块

在python中，模块的使用方式都是一样的，但其实细说的话，模块可以分为四个通用类别：　
    1：在python中编写的.py文件
    2：已被编译为共享库或DLL的C或C++扩展
    3：把一系列模块组织到一起的文件夹（文件夹下有以下__init__.py文件，该文件夹称为包）
    4：使用 c 编写并链接到 python 解释器到内置模块 re json logging
我们可以从sys.module中找到当前已经加载的模块，sys.module是一个字典，内部包含模块名与模块对象的映射，
该字典决定了导入模块时是否需要重新导入。

为模块起别名：
    import time as my
    my.sleep(0.1)

导入多个模块：
    import re,sys,os,time
"""

# 执行文件的路径问题
"""

当前执行文件的文件名字————》bin.py

查看所有执行文件的路径：
    import sys
    print(sys.path)
临时添加一个执行文件的路径：
    import sys
    sys.path.append('/Users/jeannie/Desktop')
    
"""

# import 的用法
"""
import的用法：

1：执行一遍模块文件(有import就会执行一遍模块文件）
2：引入模块文件里的变量 （函数即变量）

一：执行文件和调用模块在同一个目录下：
    A：调用模块所有变量
    
        a：调用单个模块
            import 模块名字：
                import mod_func         
                print(mod_func.add(1, 2))
                
        b：调用多个模块
            import 模块1,模块2：同时调用模块1，模块2到当前模块
            import mod_func1,mod_func
    B：调用模块特定变量
    
        from 模块 import 变量名
            from mod_func import add
            print(add(1, 2))
            
        ————》调用模块里的所有变量
        from 模块 import *                    # 不推荐使用
            from mod_func import *
            print(add(1, 2), sub(2, 1), sep='\n)
    好处：使用起来方便了
    坏处：容易与当前执行文件中的名字冲突,当前文件定义的函数和模块里的函数一样，当前文件的函数会被覆盖
二：执行文件和调用模块不在同一目录下：（调用特定变量和调用所有变量方式和第一步相同）

第一步：
    import sys
    print(sys.path)         # 查看执行文件的目录，以列表的形式打印出来
                    ['/Users/jeannie/PycharmProjects/learning_python/code/Day21/Day21_Module_模块',
                    '/Users/jeannie/PycharmProjects', ...等还有很多]
  
    A：在执行文件的子目录下
    
    ————》假设调用模块（cal）在 Day21_Module_模块 下 web1/web2 这个包里
            from 包名1.包名2 import cal
            form web1.web2 import cal 
             
    B:执行文件的上级 
    ————》假设调用模块（cal）在 PycharmProjects 下的 learning_python/code 里
            from learning_python.code import cal 

三：调用文件在系统的任意位置  
————》假设调用模块的路径为 /Users/jeannie/Desktop/l.py

第一步：
    import sys
    sys.path.append('/Users/jeannie/Desktop'） # 临时添加执行文件路径
    from l import func
    print(func(1, 2))
或者
    import l
    print(l.func(1, 2))

但这种会生成一个 __pycache__ 文件夹 里面有个调用模块的 .pyc 文件
                           
"""

# __name__的用法
"""
__name__ 的用法：
    1：在当前执行文件时，         __name__ = '__main__'
    2: 在调用文件里，被调用的     __name__  是调用文件的相对执行文件的相对路径  __name__ ！= '__main__' 
    
if __name__ == '__main__':   
    测试代码 
故可以使用，做代码的调试，就算文件被import调用，测试代码也不会执行         
"""

# __file__的用法
"""
print(__file__):查看当前文件的绝对路径————》pycharm 自己做的，本来只是 module_概念.py 文件名

import os
print(os.path.abspath(__file__))
查看当前文件的相对路径，在终端里调用也是可行的

import os
print(os.path.dirname(__file__)):查看当前文件上一级的绝对路径

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)
在哪里都被认可是当前文件的上一级目录的绝对路径

"""
# import os
# print(os.path.abspath(__file__))