class ComputerFactory:

    __obj = None
    __init_flag = True
    def __init__(self):
        if ComputerFactory.__init_flag:#只初始化一次
            print("电脑品牌")
            ComputerFactory.__init_flag = False
    def __new__(cls, *args, **kwargs):
        if cls.__obj == None:
            cls.__obj = object.__new__(cls)
            __init_flag = False
        return cls.__obj
    def CreateComputer(self,brand):
        if brand == "联想":
            return Lenovo
        elif brand == "华硕":
            return ASUS
        elif brand == "神舟":
            return Hasee
        else:
            return "不是该三种品牌"
class Computer:
    def __init__(self,name):
        self.name = name
    def calculate(self):
        print("品牌".format(self.name))
class Lenovo(Computer):  #显示区调用
    def __init__(self,name,type):
        Computer.__init__(self,name)
        self.type = type
    def calculate(self):
        print("联想")
class ASUS(Computer):
    def calculate(self):
        print("华硕")
class Hasee(Computer):
    def calculate(self):
        print("神州")
s=ASUS("华硕")
s.calculate()#调用重写的caculate方法

cp1 = ComputerFactory()
cp2 = ComputerFactory()
C1 = cp1.CreateComputer("联想")
print(C1)
C2 = cp2.CreateComputer("华为")
print(C2)