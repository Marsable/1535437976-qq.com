#coding=utf-8
#测试递归

num = 1
def a1():
    global num
    num +=1
    print("a1")
    if num <10 :
        a1()


def a2():
    print("a2")


a1()
