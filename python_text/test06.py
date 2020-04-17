with open("a.jpg","rb") as f:
    with open("b.jpg","wb") as w:
        for line in f.readlines():
            w.write(line)
print("拷贝完成")