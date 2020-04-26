import socket
import time
localIP= "127.0.0.1"
localPort= 80
message='3594'
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    s.sendto(message.encode(), (localIP, localPort))
    data, addres = s.recvfrom(1024)
    print(f"messaggio ricevuto:", {data.decode()})
    time.sleep(1);
s.close()

