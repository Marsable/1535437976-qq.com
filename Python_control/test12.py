x = int(input("请输入X轴的值："))
y = int(input("请输入y轴的值："))

if x>0:
    if y >0:
        print("该点在第一象限")
    else:
        print("该点在第四象限")
else:
    if y>0:
        print("该点在第二象限")
    else:
        print("该点在第三象限")