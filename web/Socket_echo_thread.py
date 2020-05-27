from socket import *
from threading import Thread


def ReceiveData():
    r = socket(AF_INET, SOCK_DGRAM)
    r.bind(("127.0.0.1", 8585))
    while True:
        ReceiveData = r.recvfrom(1024)
        print(ReceiveData[0].decode(),)
    r.close()

def SendData():
    s = socket(AF_INET, SOCK_DGRAM)
    while True:
        Data = input("请输入：")
        s.sendto(Data.encode(), ("127.0.0.1",8585))
    s.close()


if __name__ == '__main__':
    t1 = Thread(target=ReceiveData)
    t2 = Thread(target=SendData)
    t1.start()
    t2.start()