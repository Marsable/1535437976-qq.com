#编写一个函数，计算数列n/(n+1)的sum
#通过循环计算n/(n+1)
def sum_sequence():
    Sum = 0
    i =1
    n = int(input("请输入n:"))

    while i <n+1:
        Sum = i/(i+1)

        i += 1

    print(Sum)

# sum_sequence()
#递归计算n/n+1

n = int(input("请输入n："))
def sum_sequence01(n):
    if n == 1:
        return 1/2
    else:
        return n/(n+1)+sum_sequence01(n-1)

result = sum_sequence01(n)
print(result)
