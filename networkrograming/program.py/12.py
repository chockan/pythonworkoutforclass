import socket
import sys
import time

print('\nWelcome to chat Room')
print("initializing....................")

a=input("enter your name")
x=socket.socket()
port,host=5000,'127.0.0.1'
x.connect((host,port))
print("connected")
x.send(a.encode())
b=x.recv(1024)
c=b.decode()
print(c,"has joined")

while True:
    f=x.recv(1024)
    g=f.decode()
    print(c,":",g)
    k=input("Me:")
    x.send(k.encode())