import mysql.connector  #pip install mysql-connector-python

a= mysql.connector.connect(
        host="localhost",
        user="root",
        password="Yogan",
        database="my1"
    )

if a:
    print("connected")


else:
    print("not connected")

def insert(name,age,phonenumber):
    b=a.cursor()
    c="insert into users (name,age,phonenumber) values (%s,%s,%s)"
    d=(name,age,phonenumber)
    b.execute(c,d)
    a.commit()
    print("Data insert success")

    
def update():
    pass
def select():
    pass
def delete():
    pass
def exit():
    quit()

c=True
while c:
    print("1.insert data")
    print("2.update data")
    print("3.select data")
    print("4.delete data")
    print("5.exit data")
    choice=int(input("enter your choice"))

    if choice==1:

        name=input("Enter the name")
        age=int(input("Enter the age"))
        phonenumber=int(input("Enter the phonenumber"))
        insert(name,age,phonenumber)

    elif choice==2:                 
        update()
    elif choice==3:
        select()
    elif choice==4:
        delete()
    elif choice==5:
        c=False
        quit()
        
    else:
        print("give valid data")