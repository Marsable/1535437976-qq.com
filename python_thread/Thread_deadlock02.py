from threading import Lock
from threading import RLock
from threading import Thread
from time import sleep

def func01(): # 第一个人先菜刀后锅
    lock01.acquire()
    print("func01拿到菜刀")
    sleep(3)# 由于休眠了3s所以线程2抢占了线程1，这个时候就出现了死锁
    lock02.acquire()
    print("func01拿到锅")
    lock01.release()
    print("func01释放菜刀")
    lock02.release()
    print("func01放下锅")
def func02(): #第二个人先锅后菜刀
    lock02.acquire()
    print("func02拿到锅")
    lock01.acquire()
    print("func02拿到菜刀")
    lock02.release()
    print("func02释放锅")
    lock01.release()
    print("func02放下菜刀")


if __name__ == '__main__':
    # lock = Lock()Thread_deadlock.py
    lock01 = Lock()  # 菜刀
    lock02 = Lock()  # 锅
    t1 = Thread(target=func01)
    t2 = Thread(target=func02)
    t1.start()
    t2.start()