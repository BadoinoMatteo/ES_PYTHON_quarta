import socket
import time

localIP= "127.0.0.1"
localPort= 80
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((localIP, localPort))

while True:
    data, addres = s.recvfrom(1024)
    print(f"messaggio ricevuto:", {data.decode()})
    s.sendto(data, (addres))
    time.sleep(1);

s.close()

