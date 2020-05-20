from threading import Thread
from time import sleep


class MyThread(Thread):
    def __init__(self,name):
        Thread.__init__(self)
        self.name=name

    def run(self):
        print(f"Threading{self.name} strat ")
        sleep(3)


if __name__ == '__main__':
    t1 = MyThread("T1")
    t2 = MyThread("T2")
    t1.start()
    t2.start()