try:
    f = open("G:\a.txt","a")
    #操作系统默认GBK
    #pycharm默认Unicode
    s = "我爱你中国\n"
    x = ["aa\n","bb\n"]
    f.write(s)
    f.writelines(x)
except BaseException as e:
    print(e)
finally:
    f.close()
    #必须close释放空间