# 导入方式一
# import module01 

# module01.func()

# 使用as取别名解决冲突
# import module01 as m01
# m01.func()

# 导入方式二
# 将指定成员导入到当前模块作用域中
# from module01 import Myclass
# from module01 import func
# 程序自上而下执行，谁离得近执行谁，小心导入进来的成员，不要和当前模块成员名称相同
# def func():
#     print("module的方法")
# func()
# my01 = Myclass()

# 导入方式三
# 将指定模块的所有成员导入到当前模块作用域中
# 导入进来的成员和其他模块成员冲突
from module01 import *

func()