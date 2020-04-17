with open("a.txt","r") as f:
    print("文件名：{0}".format(f.name))
    print(f.tell())
    print("读取内容:{0}".format(f.readline()))
    print(f.tell())
    f.seek(0)
    print("读取内容:{0}".format(f.readline()))