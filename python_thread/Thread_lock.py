from threading import Thread
from threading import Lock

def func01(self):
    global count
    # lock.acquire()
    with lock:
        for i in range(1000000):
            count += 1
    # lock.release()


if __name__ == '__main__':
    count = 0
    t_list = []
    lock = Lock()
    for i in range(10):
        t = Thread(target=func01,args=(f't{i}',))
        t.start()
        t_list.append(t)
    for t in t_list:
        t.join()
    print(count)