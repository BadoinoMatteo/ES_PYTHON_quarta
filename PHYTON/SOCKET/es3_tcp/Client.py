import socket
import time

ip= "127.0.0.1"
porta = 80
message= ""

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((ip, porta))

while True:

    message= input("inserisci messaggio da mandare")

    s.sendall(message.encode())

    data=s.recv(1024)

    print("messaggio ricevuto: ", data.decode())

    time.sleep(1)

s.close()
