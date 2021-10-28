import socket
import os.path

print("\nSeyed Hadi Ranjbar :)\n")

host = input("Enter your domain : ")
page = input("Enter target page : ")

s=socket.socket()
host=socket.gethostbyname(host)
port=80
request = "GET /hadi.php \r\n";
request = "GET /" + page + " HTTP/1.0\r\n\r\n"

s.connect((host,port))
s.sendall(request.encode())

response = s.recv(10000).decode()

val = response.split("\r\n")

###############################################################

if '200' in val[0] :

    print("HTTP Response Code : 200")
    file = input("input file name (for save) : ")
    path = os.path.dirname(__file__)
    file = open(os.path.join(path, "tcp/" + file + ".txt"),"w", encoding='utf-8')
    file.write(val[14])
    file.close()    

elif '404' in val[0] :
    print("HTTP Response Code : 404")
else :
    print(val[0])

