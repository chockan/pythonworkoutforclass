# use / 
#file=open("d:/python/new.txt","x")


# file2=open("d:/python/new.txt","w")
# file2.write("hi hello \n")
# file2.write("how are you \n")
# file2.write("I am fine \n")
# file2.write("Hope you are fine ")
# file2.close()

# file3=open("d:/python/new.txt","r")
# s=file3.read()
# e=file3.tell()
# d=file3.seek(5)
# f=file3.tell()
# print(f)
# file3.close()

#xb====create binary
#wb=====
#ab=====
# built in functions


#copy
# file3=open("d:/python/new.txt","r",encoding="utf-8")
# file4=open("d:/python/new1.txt","x")
# for i in file3:
#     file4.write(i)

# file3.close()
# file4.close()


# #read
# file4=open("d:/python/new1.txt","r")
# print(file4.read())
# file4.close()

# #split
# file4=open("d:/python/new1.txt","r")
# print(file4.read().split())
# file4.close()

# #truncate
# file4=open("d:/python/new1.txt","r")
# print(file4.truncate(5))
# file4.close()

#flush
# file4=open("d:/python/new1.txt","r")
# file4.write("hi good morning")
# file4.flush()
# file4.write("hi good evening")
# file4.close()
"""
open()

read()
readline()
readlines()
====================to read text

write()
close()

seek()  #hello
tell()  


#data persistence

it is the concept of storing datain a persistent form.It means data should be
 permanently stored on disk for further manipulation

 picklr module==== the process of converts any kind of python objects into byte streams is called picking or serialization.

 we can convert the byte stream back into python objectsnby a process called as unpickling or deserializing.

 both are allow to easily transer data from one server/sytem to another and the store it in a file or db.

 python pickle module is used to serialize and deserializeing python object.

 pickle.dump()=============is used to pickle objects
 pickle.load()=============is used to un pickle objects

 syntax
 import pickle

"""


#pickle
# import pickle
# a=["abc",777,"ball"]
# b=open(open("d:/python/new1.txt","r"))
# pickle.dump()
