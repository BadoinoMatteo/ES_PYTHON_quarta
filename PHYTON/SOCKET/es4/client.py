import socket
import time
localIP= "127.0.0.1"
localPort= 80
comando=""
variabie=""
stinga=""
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    comando=input("inserisci il comando")
    variabie=(input("inserisci la variabile"))
    stringa=comando + "_" + variabie
    s.sendto(stringa.encode(), (localIP, localPort))

s.close()