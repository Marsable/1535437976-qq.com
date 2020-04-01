def f1(*a,b,c):
    print(a,b,c)

# f1(10,20,30,40)
f1(10,b=20,c=30)
#强制命名参数
def f2(a,b,**c):
    print(a,b,c)

f2(10,20,name="mys",age=18)

def f3(a,*b,**c):
    print(a,b,c)

f3(10,20,30,name="mys",age=18)