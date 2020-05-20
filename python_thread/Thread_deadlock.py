from threading import Lock
from threading import RLock

def func01():
    lock.acquire()
    print("func01拿到锁")
    func02()
    lock.release()
    print("func01释放锁")
def func02():
    lock.acquire()
    print("func02拿到锁")
    lock.release()
    print("func02释放锁")
def func03():
    func01()
    func02()


if __name__ == '__main__':
    # lock = Lock()
    lock = RLock()
    func03()