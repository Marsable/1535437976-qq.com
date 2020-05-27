from threading import Thread
from queue import Queue
from time import sleep

def producer():
    num = 1
    while True:
        if mq.qsize() <10:
            mq.put(f"{num}个")
            print(f"生产了{num}个")
            num += 1
        sleep(1)


def consumer():
    while True:
        print("购买了{}".format(mq.get()))
        sleep(3)


if __name__ == '__main__':
    # 共享数据的容器
    mq = Queue()
    # 创建生产者线程
    t1 = Thread(target=producer)
    # 创建消费者线程
    t2 = Thread(target=consumer)
    t3 = Thread(target=consumer)
    t1.start()
    t2.start()
    t3.start()
