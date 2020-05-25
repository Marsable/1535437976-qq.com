from multiprocessing import Process,current_process,Queue
# from queue import Queue
import os


def func(name,mq):
    print("进程ID{0}：{1}".format(os.getpid(), mq.get()))
    mq.put("yxy")

if __name__ == '__main__':
    print("进程ID:{}".format(current_process().pid))
    print("进程ID:{}".format(os.getpid()))
    mq = Queue()
    mq.put("mys")
    p1 = Process(target=func, args=("p1",mq))
    p1.start()
    p1.join()
    print(mq.get())