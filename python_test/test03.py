class Employee:
    id = 1000
    def __init__(self,name,salary):
        self.name = name
        self.__salary = salary
        Employee.id += 1
    def __add__(self, other):
        if isinstance(other,Employee):
            return "薪水和{0}".format(self.__salary + other.__salary)
        else:
            return "不是同类，不能相加"
    # def get_salary(self):
    @property
    def salary(self):
        return "薪水{0}".format(self.__salary)
    @salary.setter#针对salary的方法
    def salary(self,salary):
        if 1000<salary<5000:
            self.__salary = salary
        else:
            print("输入薪水错误")


E1 = Employee("mys",1000)
print(E1.salary)
print(E1.id)
E2 = Employee("茅尧舜",2000)
print(E2.salary)
print(E2.id)
E2.salary= -3000
print(E2.salary)
print(E1+E2)
print(E1.id)

# E1.salary = 2000
# print(E1.salary)