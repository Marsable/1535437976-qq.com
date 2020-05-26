from multiprocessing import Process,current_process
import os
from multiprocessing import Manager


def func(name,m_list,m_dict):
    print("子进程ID{}:{}".format(os.getpid(), m_list))
    print("子进程ID{}:{}".format(os.getpid(), m_dict))


if __name__ == '__main__':
    print("主进程ID:{}".format(current_process().pid))
    with Manager() as mgr:
        m_list = mgr.list()
        m_dict = mgr.dict()
        m_list.append("Hello!")
        p1 = Process(target=func,args=("p1", m_list, m_dict))
        p1.start()
        p1.join()
