from threading import Thread
from time import sleep
from threading import Event
from random import randint


def door():
    global state
    while True:
        if event.is_set():
            print("门开着，可以通行")
            # sleep(1)
        else:
            state = 0
            print("门关上了！请刷卡！")
            event.wait() # 门是被动的，需要找人开启所以需要等待
        sleep(1)
        state += 1
        if state>3:
            print("超过3s自动关闭")
            event.clear()


def person():
    global state
    num = 1
    while True:
        if event.is_set():
            print(f"门开着，第{num}个人进去")
        else:
            print(f"门关着,第{num}号人刷卡进入")
            event.set()
            state = 0
        num += 1
        sleep(randint(1,10))


if __name__ == '__main__':
    # count = 1
    state = 0
    event = Event()
    t1 = Thread(target=door)
    t2 = Thread(target=person)
    t1.start()
    t2.start()