from threading import Thread
from time import sleep
from threading import Event


def car():
    # global count
    num = 1
    while True:
        if event.is_set():
            print("车已到站")
            sleep(1)
            # count+=1
            num += 1
            if num %5 == 0:
                event.clear()
        else:
            print("车已开走")
            sleep(6)
            # count=1
            event.set()


def person():
    while True:
        if event.is_set():
            print("上车")
            sleep(1)
        else:
            print("等待上车")
            # sleep(1)
            event.wait()


if __name__ == '__main__':
    # count = 1
    event = Event()
    t1 = Thread(target=car)
    t2 = Thread(target=person)
    t1.start()
    t2.start()