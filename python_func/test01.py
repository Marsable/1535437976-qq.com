b = [10,20]

def func(m):
    print("m",id(m))

    m.append(30)

    print("m", id(m))
func(b)
#调用func()
print("b",id(b))
#对象没有变过
print(b)