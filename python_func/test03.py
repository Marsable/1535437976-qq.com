import copy
a = [10,20,[50,60]]
# b = copy.copy(a)
b = copy.deepcopy(a)
#深拷贝将赋值的部分全部复制一份一模一样的
# def testCopy():
print(a)
print(id(a))
print(b)
print(id(b))

b.append(30)
#在b中的30进行改变，a无法改变
b[2].append(7)
#在b中调用的对象里添加，a也调用了，所以对a也进行了改变，
print(a)
print(b)