from threading import Thread
from time import sleep


class MyThread(Thread):
    def __init__(self,name):
        Thread.__init__(self)
        self.name=name

    def run(self):
        print(f"Threading{self.name} strat ")
        sleep(3)
        print(f"Threading{self.name} end ")


if __name__ == '__main__':
    for i in range(10):
        t = MyThread(f"t{i}")
        t.setDaemon(True)  # 主线程结束，子线程也跟着结束，即为守护进程
        t.start()

    print("主进程结束！")