import socket


print('\nWelcome to chat Room')
print("initializing....................")

a=socket.socket()
port,host=5000,'127.0.0.1'
a.bind((host,port))
x=input("Enter Your Name")
a.listen(1)
print("waiting for connection")
con,addr=a.accept()
print("Received connection from addr",addr[0],addr[1])
b=con.recv(1024)
c=b.decode()
print(c,"has connected to chat room")
con.send(x.encode())

while True:
    message=input("Me:")
    con.send(message.encode())
    r=con.recv(1024)
    t=r.decode()
    print(c,":",t)
