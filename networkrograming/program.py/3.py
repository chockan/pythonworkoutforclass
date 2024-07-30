#server
import socket
from pickle import *

x=socket.socket()
port,host=5000,'127.0.0.1'
x.bind((host,port))
x.listen(5)
c,addr=x.accept()
print("connected Address",(c,addr))
data=c.recv(1024)
# print(data)
g=loads(data)
print(g)
x.close()