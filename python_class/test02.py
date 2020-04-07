class Student:
    company = "SXT"  # 类属性

    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age
    #
    # @classmethod
    # def printCompany(cls):
    #     print(cls.company)
    #     # print(self.name) 类对象的方法无法调用实例对象和实例变量
    #
    # @staticmethod
    # def add(a, b):
    #     print("{0}+{1}={2}".format(a, b, (a + b)))
    #     # return a+b
    #
    # def __del__(self):
    #     print("销毁对象")

    def __call__(self, salary):
        print("算工资啦")
        yearSalary = salary * 12
        return  salary

# Student.printCompany()
# Student.add(20,30)
S = Student()
print(S(300))