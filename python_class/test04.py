class Employee:
    __company = "njust"
    def __init__(self,name,age):
        self.name = name
        self.__age = age #私有属性

    def __work(self): #私有方法
        print("好好工作")
        print("年龄：{0}".format(self.__age)) #类内直接调用

e = Employee("mys",25)
print(e.name)
print(e._Employee__age)
e._Employee__work()
print(dir(e))
print(Employee._Employee__company)