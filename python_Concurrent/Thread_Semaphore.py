from threading import Thread
from time import sleep
from threading import BoundedSemaphore

def  security_check(n):
    lock.acquire()
    print(f'第{n}个人完成安检')
    sleep(2)
    lock.release()


if __name__ == '__main__':

    lock = BoundedSemaphore(3)
    for i in range(10):
        t= Thread(target=security_check ,args=(f"{i+1}",))
        t.start()

