f = open(r"G:\a.txt","a")
#操作系统默认GBK
#pycharm默认Unicode
s = "我爱你中国\n"
f.write(s)
f.close()