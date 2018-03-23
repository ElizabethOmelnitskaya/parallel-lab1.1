import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 8887))
s.send(b'Hello, Elizabeth!')
data = s.recv(1024)
s.close()
print(data.decode())