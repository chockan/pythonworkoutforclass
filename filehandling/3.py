import pickle

cars=["audi","benz","bmw"]

file4=open("d:/python/new10.txt","wb")
pickle.dump(cars,file4)

file4.close()

# file4=open("d:/python/new2.txt","rb")
# print(pickle.load(file4))


# file=open("d:/python/new3.txt","wb")
# name=input("enter the name")
# place=input("enter the place")

# pickle.dump(name,file)
# pickle.dump(place,file)

# file.close()

###################################
# file=open("d:/simpledev html css/html css workout/1.jpg","wb")
# name="chennnai"
# pickle.dump(name,file)
# file.close()
# #print(pickle.load(file))
# #print(pickle.load(file))

# #######################################################
# file=open("d:/simpledev html css/html css workout/1.jpg","rb")
# name="chennnai"
# print(pickle.load(file))
# file.close()


###############################################################

# import pickle

# file=open("d:/python/new3.txt","wb+")

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


############################################################################



file3=open("d:/python/new.txt","r",encoding="utf-8")

print(file3.read())
file3.close()

##################################################################




