from multiprocessing import Process
from time import sleep

def func(name):
    pass
    print(f"{name}开始···")
    sleep(2)
    print(f"{name}结束···")

if __name__ == '__main__':
    p1 = Process(target=func, args=("p1",))
    p1.start()
    p2 = Process(target=func, args=("p2",))
    p2.start()