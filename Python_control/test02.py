score = int(input("请输入分数"))

degree = "ABCDE"

if score>100 or score<0:
    print("输入错误，请重新输入")
else:
    num = score//10
    if num<6:
        num=5
    print("分数是{0},等级是{1}".format(score,degree[9-num]))
