import mysql.connector  #pip install mysql-connector-python

from tabulate import tabulate  #pip install tabulate
a= mysql.connector.connect(
        host="localhost",
        user="root",
        password="Yogan",
        database="db2"
    )

if a:
    print("connected")


else:
    print("not connected")



def insert(Name,age,city):
    b=a.cursor()
    c="insert into user2 (Name,age,city) values (%s,%s,%s)"
    d=(Name,age,city)
    b.execute(c,d)
    a.commit()
    print("Data insert success")

def update(Name,age,city,id):
    b=a.cursor()
    c="update user2 set Name=%s,age=%s,city=%s where id=%s"
    d=(Name,age,city,id)
    b.execute(c,d)
    a.commit()
    print("Data update success")

    

def select():
    b=a.cursor()
    c="select Id,Name,age,city from user2"
    
    b.execute(c)
    #result=b.fetchone()
    #result=b.fetchmany(2)
    result=b.fetchall()
    #print(result)
    print(tabulate(result,headers=['Id','Name','age','City']))


def delete():
    b=a.cursor()
    c="delete from user1 where id=%s"
    d=(id,)
    b.execute(c,d)
    a.commit()
    print("Data delete success")
    pass


while True:
    print("1.insert data")
    print("2.update data")
    print("3.select data")
    print("4.delete data")
    print("5.exit data")

    choice=int(input("enter your choice"))

    if choice==1:
        Name=input("Enter the name:")
        age=int(input("Enter the age:"))
        city=input("Enter the City:")

        insert(Name,age,city)
    elif(choice==2):
        id=input("enter the id")
        Name=input("Enter the name")
        age=int(input("Enter the age"))
        city=input("Enter the City")
        update(Name,age,city,id)
    elif(choice==3):
        select()
    elif(choice==4):
        delete()
    elif(choice==5):
        quit()
    else:
        print("give valid input")
    
