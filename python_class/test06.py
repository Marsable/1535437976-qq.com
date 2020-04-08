class Person:
    def __init__(self,naem,age):
        self.name = naem
        self.__age = age #私有

    def say_age(self):
        print("年龄")
    def __str__(self):
        return "名字是：{0}".format(self.name)
class Student(Person):
    def __init__(self,name,age,score):
        Person.__init__(self,name,age) #第一种 必须显示区调用
        self.score = score
    def say_age(self):
        print("我的年龄")#方法的重写

print(Student.mro())#生成类继承结构
s = Student("mys",20,100)
s.say_age()
# print(s.age)#无法直接调用
print(dir(s))#查看所有属性
print(s._Person__age)
print(s)
print(Student.mro())
