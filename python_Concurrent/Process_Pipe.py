from multiprocessing import Process,Pipe
import os


def func(name,con1):
    print("进程ID{0}：{1}".format(os.getpid(), con1.recv()))
    con1.send("yxy")


if __name__ == '__main__':
    print("进程ID{0}".format(os.getpid()))
    con1,con2 = Pipe()
    p1 = Process(target=func,args=("p1",con1))
    p1.start()
    con2.send("mys")
    print(con2.recv())
