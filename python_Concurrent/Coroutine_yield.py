def func():
    for i in range(11):
        print(f"love you : {i}")
        yield

def func01():
    g = func()
    next(g)
    for i in range(10):
        print(f"love you too ：{i}")
        next(g)

if __name__ == '__main__':
    func01()