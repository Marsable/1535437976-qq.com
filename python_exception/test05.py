class AgeError(Exception):
    def __init__(self,errorInfo):
        Exception.__init__(self)
        self.errorInfo = errorInfo
    def __str__(self):
        return self.errorInfo+"年龄错误！"

if __name__ =="__main__":
    age = int(input("请输入一个年龄："))
    if age<1 or age>120:
        raise AgeError(age)
    else:
        print("正常年龄",age)