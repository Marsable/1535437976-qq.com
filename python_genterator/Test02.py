g = (x for x in range(10))
# print((next(g)))
# print(g.__next__())
# for i in g:
#     print(i)
# print(g.send(None))
# print(g.send(2))


def text():
    for x in range(5):
        yield x  # 变成生成器


t = text()
print(type(t))
print(next(t))