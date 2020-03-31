#不可变对象的可变子对象
# a = 10
a = (10,20,[50,60])
#
print(id(a))

def test1 (m):
    print(id(m))
    # m[2] = 20
    #元组的值不可以更改
    m[2][0]=20
    #不过元组中局部的列表可以改变
    print(m)
    print(id(m))

test1(a)
print(a)