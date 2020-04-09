class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __add__(self, EX1):
        if isinstance(EX1,Person):
            return self.name+EX1.name
        else:
            return "不能添加"

p1 = Person("mys",30)
p2 = Person("MYS",25)

print(p1+p2)