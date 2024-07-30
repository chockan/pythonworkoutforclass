import mysql.connector  #pip install mysql-connector-python

from tabulate import tabulate  #pip install tabulate


a= mysql.connector.connect(
        host="localhost",
        user="root",
        password="Yogan",
        database="my4"
    )

if a:
    print("connected")


else:
    print("not connected")


def insert(Name,Gender,City):
    b=a.cursor()
    c="insert into user1 (Name,Gender,City) values (%s,%s,%s)"
    d=(Name,Gender,City)
    b.execute(c,d)
    a.commit()
    print("Data insert success")
    


def update(Name,Gender,City,id):
    b=a.cursor()
    c="update user1 set Name=%s,Gender=%s,City=%s where id=%s"
    d=(Name,Gender,City,id)
    b.execute(c,d)
    a.commit()
    print("Data update success")

def select():
    b=a.cursor()
    c="select Id,Name,Gender,City from user1"
    b.execute(c)
    #result=b.fetchone()
    #result=b.fetchmany(2)
    result=b.fetchall()
    #print(result)
    print(tabulate(result,headers=['Id','Name','Gender','City']))


def delete(id):
    b=a.cursor()
    c="delete from user1 where id=%s"
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
        Name=input("Enter the name")
        Gender=input("Enter the Gender")
        City=input("Enter the City")
        insert(Name,Gender,City)

    elif choice==2:
        id=input("enter the id")
        Name=input("Enter the name")
        Gender=input("Enter the Gender")
        City=input("Enter the City")
        update(Name,Gender,City,id)

    elif choice==3:
        select()

    elif choice==4:
        id=input("enter the id")
        delete(id)

    elif choice==5:
        quit()
    else:
        print("invalid selection")