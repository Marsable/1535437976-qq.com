from greenlet import greenlet

def gf(name):
    print(f"{name}:我想你了")
    g2.switch('yxy')
    print(f"{name}:你快来")
    g2.switch()

def bf(name):
    print(f"{name}:我也想你了")
    g1.switch()
    print(f"{name}:我来了")


if __name__ == '__main__':
    g1 = greenlet(gf)
    g2 = greenlet(bf)
    # 切换任务
    g1.switch('mys')