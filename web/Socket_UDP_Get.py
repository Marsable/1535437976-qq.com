from socket import *

# s = socket(AF_INET, SOCK_STREAM)  # IPV4 tcp协议
# IPV4 UDP协议
s = socket(AF_INET, SOCK_DGRAM)
s.bind(("", 8788))
s.sendto(b"abc", ("192.168.0.103", 8181))
redata = s.recvfrom(1024)
print(redata[0].decode("GB2312"))
