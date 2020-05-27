from time import time,sleep


def consumer():
    # while True:
    #     n = yield
    for n in range(5):
        sleep(1)
        print(f"生产了{n}个产品")


def productor():
    consumer()
    # g = consumer()
    # next(g)
    for i in range(5):
        # g.send(i)
        print(f"消费了{i}个产品")


if __name__ == '__main__':
    start = time()
    productor()
    end = time()
    print(end-start)