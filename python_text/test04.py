#coding = utf-8
with open(r"G:\a.txt","r") as f:
#操作系统默认GBK
#pycharm默认Unicode
    for a in f:
        print(a,end="")