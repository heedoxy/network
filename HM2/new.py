import socket
# Create a client socket

host=socket.gethostbyname('www.google.com')
port=80

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

# Connect to the server

clientSocket.connect((host,port));
# Send data to server

data = "GET /";

clientSocket.send(data.encode());
# Receive data from server

dataFromServer = clientSocket.recv(1024);
# Print to the console

print(dataFromServer.decode());