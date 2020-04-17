
import os
# os.system("notepad.exe")
# os.system("ping www.baidu.com")
# os.system("cmd")

# os.startfile("")
#文件和文件夹相关信息
print(os.name)
print(os.sep)#分隔符
print(repr(os.linesep))#repr() 函数将对象转化为供解释器读取的形式。
print(os.stat("test02.py"))
#关于工作目录的操作
# print(os.getcwd())
# os.chdir()#改变路径为当前目录
# os.mkdir("test")
#创建目录、多级目录、删除目录
# os.mkdir("")
# os.rmdir()当前工作目录下改名
# os.makedirs("test0/test1/test2")
# os.removedirs("test0/test1/test2")#只能删除空目录
# os.makedirs("../python_model")#../指的是上一级目录
# os.rename("test","test01")
dir = os.listdir("test01")
print(dir)