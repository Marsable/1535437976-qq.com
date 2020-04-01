f = lambda a,b,c,d:a*b*c*d

def test01(a,b,c,d):
    print("####")
    return a*b*c*d

print(f(2,3,4,5))

h = [test01,test01]
print(h[0](3,4,5,6))