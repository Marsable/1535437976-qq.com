from multiprocessing import Pool
import os
from time import sleep


def func(name):
    print(f"当前进程ID：{os.getpid()},{name}")
    sleep(2)
    return name


def func1(args):
    print(args)


if __name__ == '__main__':
    pool = Pool(5)
    pool.apply_async(func, args=("mys1",), callback=func1)
    pool.apply_async(func, args=("mys2",))
    pool.apply_async(func, args=("mys3",))
    pool.apply_async(func, args=("mys4",))
    pool.apply_async(func, args=("mys5",))
    pool.apply_async(func, args=("mys6",))
    pool.apply_async(func, args=("mys7",))
    pool.apply_async(func, args=("mys8",))
    # apply_async是并发执行，单纯的apply是串行执行
    pool.close()
    # 先关后join
    pool.join()

