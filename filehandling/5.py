

# file=open("d:/python/new3.txt","wb")

# file.write("hi")
# file.write("hello how are you \n")
# file.write("i am fine \n")
# file.write("hope you are fine\n")
# file .close()

# import pickle

# cars=["audi","benz","bmw"]

# file4=open("d:/python/new4.dat","wb")
# pickle.dump(cars,file4)

# file4.close()

# count=int(input("how many students"))
# fileout=open("d:/python/new5.dat","w")
# for i in range(count):
#     print("enter the details for student",(i+1),"below:")
#     rollno=int(input("Rollno:"))
#     name=input("name:")
#     marks=float(input("marks"))
#     rec=str(rollno)+","+name+","+str(marks)+'\n'
#     fileout.write(rec)
# fileout.close()



#file=open("d:/python course/new4.txt","x")

# file=open("d:/python course/new4.txt","w")
# file.write("hi hello \n")
# file.write("how are you \n")
# file.write("I am fine \n")
# file.write("Hope you are fine ")
# file.close()

# file=open("d:/python course/new4.txt","r")

# ab=file.read()
# print(ab)
# file.close()
# print(ab)

# file=open("d:/python course/new4.txt","w")
# file.write("hi chennai \n")
# file.write("how are you \n")
# file.write("I am fine \n")
# file.write("Hope you are fine ")
# file.close()

# file=open("d:/python course/new4.txt","a")
# file.write("\n hi mumbai \n")
# file.write("welcome \n")
# file.write("hope you are good \n")
# file.write("thank you ")
# file.close()


# file=open("d:/python course/new4.txt","r")
# print(file.readline())
# print(file.readline())
# print(file.readline())
# file.close()


# file=open("d:/python course/new4.txt","r")
# print(file.tell())
# file.seek(5)
# print(file.tell())
# file.close()

# file3=open("d:/python course/new4.txt","r")
# file4=open("d:/python course/new5.txt","x")

# for i in file3:
#     file4.write(i)

# file3.close()
# file4.close()


file=open("d:/python/new6.dat" ,"w")
file.write("hi")
file.write("hello how are you \n")
file.write("i am fine \n")
file.write("hope you are fine\n")
file .close()

#################################


# import pickle

# cars=["audi","benz","bmw"]

# b=open(open("d:/python course/new6.txt","wb"))
# pickle.dump(cars,b)

# b.close()

import pickle

# cars=["audi","benz","bmw"]

# file4=open("d:/python/new10.txt","wb")
# pickle.dump(cars,file4)

# file4.close()


# file4=open("d:/python/new10.txt","rb")
# print(pickle.load(file4))

# file=open("d:/python/new11.txt","wb")
# name=input("enter the name")
# place=input("enter the place")

# pickle.dump(name,file)
# pickle.dump(place,file)

# file.close()


# import pickle

# file=open("d:/python/new13.txt","wb+")

# while True:
#     name=input("enter the name")
#     place=input("enter the place")
#     pickle.dump(name,file)
#     pickle.dump(place,file)
#     op=input("want to continue press y/Y")
#     if op!="Y" and op!="y":
#         break
# file.seek(0)
# while True:
#     try:
#         name=pickle.load(file)
#         place=pickle.load(file)
#         print(name)
#         print(place)
#     except:
#         print("error raised")
#         break
# file.close()
