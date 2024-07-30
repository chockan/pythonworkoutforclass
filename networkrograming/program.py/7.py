import socket
from pickle import *
from threading import *

def abc():
    global c,a
    while(a):
        data=c.recv(1024)
        print("connected data",loads(data))
       
    

x=socket.socket()
port,host=5000,'127.0.0.1'
x.bind((host,port))
x.listen(5)
c,addr=x.accept()
a=True
# abc()
# print("connected datas:",(c,addr))
# data=c.recv(1024)
# #print(data)
# g=loads(data)
# print(g)
t=Thread(target=abc)
t.start()

print("good morning")
x.close()