import socket
import time
import turtle

localIP= "127.0.0.1"
localPort= 80
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
lista=[]
s.bind((localIP, localPort))
listaComandi=['forward', 'backward', 'left', 'right']


while True:
    ricevuto, addres = s.recvfrom(1024)
    lista.append(addres)
    lista.append(turtle.Turtle())
    stringa=ricevuto.decode().split('_')
    if(addres in lista):
        while True:
            variabile = (int)(stringa[1])
            if (listaComandi[0] == stringa[0]):
                lista[lista.index(addres)+1].forward(variabile)
                break
            if (listaComandi[1] == stringa[0]):
                lista[lista.index(addres)+1].backward(variabile)
                break
            if (listaComandi[2] == stringa[0]):
                lista[lista.index(addres)+1].left(variabile)
                break
            if (listaComandi[3] == stringa[0]):
                lista[lista.index(addres)+1].right(variabile)
                break
    else:
        print("non presente")


s.close()