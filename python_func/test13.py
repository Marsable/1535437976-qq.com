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

sum_sequence()
