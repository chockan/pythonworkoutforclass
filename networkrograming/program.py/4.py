import socket
from pickle import *
x=socket.socket()
port,host=5000,'127.0.0.1'
x.connect((host,port))

#x.sendall(b'this is client data')
data=dumps("this is client side")
# data=dumps([x for x in "Hello World"])

x.sendall(data)