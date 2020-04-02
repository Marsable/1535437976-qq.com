def function():
    x1, y1 = eval(input("请输入第一个点的坐标(x1,y1)"))
    x2, y2 = eval(input("请输入第二个点的坐标(x2,y2)"))
    x3, y3 = eval(input("请输入第二个点的坐标(x3,y3)"))
    #输入点坐标
    S = x1*y2+x2*y3+x3*y1-x1*y3-x2*y3-x3*y1
    if S>0:

        print(S)

    else:
        print("无法构成三角形")

function()