import socket

host=socket.gethostbyname('www.google.com')
port=80

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))

while True:
 s.send('net.tcp://[server ip address]:41012/Lapis.Btouch/ServerInfo')
 response = s.recv(1024)
 print(response)

s.close()