
#server
import socket

x=socket.socket()
port,host=5000,'127.0.0.1'
x.bind((host,port))
x.listen(5)
con,addr=x.accept()
print("connected Address",(con,addr))
x.close()