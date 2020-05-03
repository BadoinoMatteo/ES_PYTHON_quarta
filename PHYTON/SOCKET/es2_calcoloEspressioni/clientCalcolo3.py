import socket
import time

ipServer= "127.0.0.1"
portaServer= 80
message=""
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    message=input("inserisci l' espressione da risolvere")
    s.sendto(message.encode(), (ipServer, portaServer))
    data, addres= s.recvfrom(4096)
    print(f"risultato espressione {message} = {data.decode()} ")
    time.sleep(1)

s.close()