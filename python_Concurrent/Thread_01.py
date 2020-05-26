#coding=utf-8
from threading import *
from time import sleep,time

def func(name):
    print(f"Threading:{name} start")
    sleep(3)

if __name__ == '__main__':
    t1 = Thread(target=func, args=("t1",))
    t2 = Thread(target=func, args=("t2",))
    # 开始线程
    t1.start()

    t2.start()
    # 串行运行
    # func("t1")
    # func("t2")
