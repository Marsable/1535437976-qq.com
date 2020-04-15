def test(n):
    print("test",n)
    if n == 0:
        print("over")
    else:
        test(n-1)
print(test(4))