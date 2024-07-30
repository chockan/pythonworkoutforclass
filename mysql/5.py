import mysql.connector   #pip install mysql-connector-python

a= mysql.connector.connect(
        host="localhost",
        user="root",
        password="Yogan",
        database="myaa"
    )
if a:
    print("connected")


else:
    print("not connected")



def insert(Name,Gender,City):
    b=a.cursor()
    c="insert into user1 (Name,Gender,City) values (%s,%s,%s)"
    d=(Name,Gender,City,id)
    b.execute(c,d)
    a.commit()
    print("Data update success")

def update():
    pass

def select():
    pass

def delete():
    pass

while True:
    print("1.insert data")
    print("2.update data")
    print("3.select data")
    print("4.delete data")
    print("5.exit data")
    choice=int(input("enter your choice:"))


    if choice==1:
        Name=input("Enter the name")
        Gender=input("Enter the Gender")
        City=input("Enter the City")
        insert(Name,Gender,City)
    elif choice==2:
        update()
    elif choice==3:
        select()
    elif choice==4:
        delete()
    elif choice==5:
        quit()
    else:
        print("give valid input")

