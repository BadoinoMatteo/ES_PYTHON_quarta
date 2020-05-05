import socket

localIP= "127.0.0.1"
localPort= 80

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((localIP, localPort))

s.listen()

conn, address = s.accept()

print(f"{address}")

while True:
    data = conn.recv(4096)

    data.decode()

    print(f"messaggio ricevuto:", data.decode())

    conn.sendall(data)

s.close()