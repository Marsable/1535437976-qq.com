num = 0
Sum = 0
Sum_odd = 0
Sum_even = 0
for num in range(1,101):

    Sum = num + Sum
    if num%2==0:Sum_even = Sum_even + num
    else:
        Sum_odd += num
print(Sum)
print(Sum_even)
print(Sum_odd)