import mysql.connector  #pip install mysql-connector-python
from tabulate import tabulate  #pip install tabulate
a=mysql.connector.connect(host="localhost",
        user="root",
        password="Yogan",
        database="my8")
if a:
    print("connected")
else:
    print("not connected")
    
    
def insert(name,age,phonenumber):
    b=a.cursor()
    c="insert into user8 (name,age,phonenumber) values (%s,%s,%s)"
    d=(name,age,phonenumber)
    b.execute(c,d)
    a.commit()
    print("Data insert success")

def update(name,age,phonenumber,id):
    b=a.cursor()
    c="update user8 set name=%s,age=%s,phonenumber=%s where id=%s"
    d=(name,age,phonenumber,id)
    b.execute(c,d)
    a.commit()
    print("Data update success")

def select():
    b=a.cursor()
    c="select id,name,age,phonenumber from user8"
    
    b.execute(c)
    #result=b.fetchone()
    #result=b.fetchmany(2)
    result=b.fetchall()
    print(result)
    print(tabulate(result,headers=['Id','Name','age','phonenumber']))


def delete(id):
    b=a.cursor()
    c="delete from user8 where id=%s"
    d=(id,)
    b.execute(c,d)
    a.commit()
    print("Data delete success")
    

while True:
    print("1.insert data")
    print("2.update data")
    print("3.select data")
    print("4.delete data")
    print("5.exit data")
    
    choice=int(input("enter your choice"))
    
    if choice==1:
        name=input("enter the name")
        age=int(input("enter the age"))
        phonenumber=int(input("enter the phonenumber"))
        insert(name,age,phonenumber)
        
    elif choice==2:
        id=input("enter the id")
        name=input("enter name")
        age=int(input("enter age"))
        phonenumber=int(input("enter the phone number"))
        update(name,age,phonenumber,id)
    
    elif choice==3:
        select()
    elif choice==4:
        id=int(input("enter the id"))
        delete(id)
    elif choice==5:
        quit()