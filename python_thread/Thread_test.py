#coding=utf-8

from threading import *
from time import sleep, time
import threading

def func(name):
    print(f"Threading:{name} start")
    sleep(3)
    print(f"Threading:{name} end")
    # print(threading.currentThread())


# 共开了三个线程
if __name__ == '__main__':# 主线程
    # print(threading.currentThread())
    # t1 = Thread(target=func, args=("t1",))
    # t2 = Thread(target=func, args=("t2",))
    # 记录开始时间
    start = time()

    # 开始线程，启动线程后不要立刻join
    # t1.start()
    # t2.start()
    # 等待t1,t2线程结束
    # t1.join()
    # t2.join()
    # 串行运行
    # func("t1")
    # func("t2")
    Thread_list = []
    for i in range(10):
        t = Thread(target=func, args=(f"t{i+1}",))
        t.start()
        Thread_list.append(t)
    for t in Thread_list:
        t.join()
    # 程序运行时间
    end = time()-start
    print(end)