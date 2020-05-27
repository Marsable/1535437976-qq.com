from time import time, sleep
from greenlet import greenlet


def func1():
    num = 0
    for i in range(10000000):
        num += 1
        g2.switch()

def func2():
    num = 0
    for i in range(10000000):
        num += 1
        g1.switch()

if __name__ == '__main__':
    g1 = greenlet(func1)
    g2 = greenlet(func2)
    start = time()
    g1.switch()
    end = time()

    print(end-start)