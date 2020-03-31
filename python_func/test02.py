a = 100

def func(a):
    print("a",id(a))
    a += 200
    print("a",id(a))
    print(a)
func(a)
print("a",id(a))
