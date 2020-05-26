from multiprocessing import Process
from time import sleep
import os


class MyProcess(Process):
    def __init__(self,name):
        Process.__init__(self)
        self.name = name

    def run(self):
        print("当前进程号{}".format(os.getpid()))
        print("父进程号{}".format(os.getppid()))
        print(f"{self.name}开始")
        sleep(2)
        print(f"{self.name}结束")


if __name__ == '__main__':
    print("父进程号{}".format(os.getppid()))
    print("当前进程号{}".format(os.getpid()))
    p1 = MyProcess("P1")
    p2 = MyProcess("P2")
    p1.start()
    p2.start()