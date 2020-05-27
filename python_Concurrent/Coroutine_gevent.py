from gevent import monkey
monkey.patch_all()
import gevent
from time import time,sleep


def gf(name):
    print(f"{name}:我想你了")
    # gevent.sleep(1)
    sleep(1)
    print(f"{name}:你快来")


def bf(name):
    print(f"{name}:我也想你了")
    # gevent.sleep(1)
    sleep(1)
    print(f"{name}:我来了")


if __name__ == '__main__':
    start = time()
    g1 = gevent.spawn(gf, "yxy")
    g2 = gevent.spawn(bf, "mys")
    g1.join()
    g2.join()
    end = time()
    print(end-start)