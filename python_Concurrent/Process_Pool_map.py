from multiprocessing import Pool
import os
from time import sleep


def func(name):
    print(f"当前进程ID：{os.getpid()},{name}")
    sleep(2)
    return name


if __name__ == '__main__':
    with Pool(5) as pool:
        args = pool.map(func, ("mys1","mys2","mys3","mys4","mys5","mys6","mys7"), )
        for i in args:
            print(i)
