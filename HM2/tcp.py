import socket

s=socket.socket()
host=socket.gethostbyname('www.google.com')
port=80

s.connect((host,port))
s.sendall(bytes("GET /\r\n", "utf-8"))

response = s.recv(10000)

val = response.split(bytes("\r\n\r\n", "utf-8"))

print(response)
