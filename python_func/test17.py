a = 100

def outer():
    b = 10
    def inter():
        nonlocal b
        #外部函数的局部变量

        print("outer:",b)
        b = 20
        global  a
        #全局变量
        a = 200
        print("a:",a)
    inter()
    print("b:",b)
outer()

print("a:",a)