from socket import *

# s = socket(AF_INET, SOCK_STREAM)  # IPV4 tcp协议
# IPV4 UDP协议
s = socket(AF_INET, SOCK_DGRAM)
addr = ("192.168.0.103", 8080)
data = input("请输入：")
s.sendto(data.encode("GB2312"), addr)
redata = s.recvfrom(1024)
print(redata[0].decode("GB2312"))
s.close()
