def test01():
    print("test01")
    test02()
def test02():
    print("test02")

# test01()

#递归做阶乘
def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)


result = factorial(5)
print(result)