#定义一个函数，将输入的参数拆成列表元素，通过sort()逆序排列后再输出。如：输入3245，输出5432
#不创建新的列表的方法func
def func1():

    a = eval(input("请输入元素用','分隔"))
    print(a)
    b = list(a)
    print(b)
    b.sort(reverse=True)
    print(b)

#通过循环append添加进列表，再通过sort倒序
def func2():
    #循环输入数字
    num = []
    for i in range(4):
        num1 = input("请输入数字")
        num.append(num1)
    # num.sort(reverse=True)
    num = sorted(num,reverse=True)
    #通过sorted函数建立新列表来倒序
    print(num)
# func1()
func2()