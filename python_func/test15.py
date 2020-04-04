# 使用海龟绘图。输入多个点，将这些点都两两相连。

import turtle


def link():
    a = []
    b = []
    n = int(input("请输入点的数量："))
    for i in range(n):
        x, y = eval(input("请输入点的坐标用,分隔"))
        a.append(x)
        b.append(y)
        i += 1
    print(a, b)
    t = turtle.Pen()


    for j in range(n):
        for k in range(j,n):
            t.penup()
            t.goto(a[j], b[j])
            t.pendown()
            t.goto(a[k],b[k])


    turtle.done()


link()
