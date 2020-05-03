import socket
import time

localIP= "127.0.0.1"
localPort= 80
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((localIP, localPort))
while True:
    data, addres = s.recvfrom(4096)
    x=eval(data.decode())
    s.sendto(str(x).encode(), addres)
s.close()