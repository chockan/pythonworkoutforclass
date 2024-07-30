import mysql.connector    # pip install mysql-connector-python
from tabulate import tabulate  #pip install tabulate

a= mysql.connector.connect(
        host="localhost",
        user="root",
        password="Yogan",
        database="mymy"
    )

if a:
    print("connected")


else:
    print("not connected")



def insert(name,age,place):
    b=a.cursor()
    c="insert into my1 (name,age,place) values (%s,%s,%s)"
    d=(name,age,place)
    b.execute(c,d)
    a.commit()
    print("Data update success")
    

def update():
    pass
def select():
    b=a.cursor()
    c="select Id,name,age,place from my1"
    b.execute(c)
    #result=b.fetchone()
    #result=b.fetchmany(2)
    result=b.fetchall()
    #print(result)
    print(tabulate(result,headers=['Id','Name','age','place']))
def delete():
    pass
def exit():
    pass

while True:
    print("1.insert data")
    print("2.update data")
    print("3.select data")
    print("4.delete data")
    print("5.exit data")
    choice=int(input("enter your choice:"))

    if choice==1:
        name=input("enter name:")
        age=int(input("enter age"))
        place=input("enter place")
        insert(name,age,place)
    elif choice==2:
        update()
    elif choice==3:
        select()
    elif choice==4:
        delete()
    elif choice==5:
        quit()
    else:
        print("give valid data")