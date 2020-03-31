for x in range (1,10):
    for y in range (1,x+1):
        S = x*y
        print(x,"*",y,"=",S,end="\t")
    print()
        #print("{0}*{1}={2}".format(x,y,(x*y)))
r1 = dict(name="高小一",age=20,salary=30000,city="北京")
r2 = dict(name="高小二",age=20,salary=20000,city="上海")
r3 = dict(name="高小五",age=20,salary=10000,city="深圳")

r=[r1,r2,r3]

for a in r:
    if a.get("salary")>15000:
        print(a)