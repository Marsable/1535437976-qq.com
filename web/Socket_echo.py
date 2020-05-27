from socket import *

udpSock = socket(AF_INET, SOCK_DGRAM)
udpSock.bind(("", 8181))
while True:
    recvData = udpSock.recvfrom(1024)
    print(recvData[0].decode())
    Data = input("请输入：")
    udpSock.sendto(Data.encode(), recvData[1])

udpSock.close()