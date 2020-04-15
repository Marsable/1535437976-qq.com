# s = "我爱你中国\n"
with open(r"a.txt","r",encoding="utf-8") as f:
#操作系统默认GBK
#pycharm默认Unicode
    s = f.read()
    print(s)