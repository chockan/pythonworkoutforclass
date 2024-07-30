import pickle

# cars=["audi","benz","bmw"]

# file4=open("d:/python/new13.txt","wb")
# pickle.dump(cars,file4)

# file4.close()


file4=open("d:/python/new13.txt","rb")
print(pickle.load(file4))

file4.close()


# file=open("d:/python/new11.txt","wb")
# name=input("enter the name")
# place=input("enter the place")

# pickle.dump(name,file)
# pickle.dump(place,file)

# file.close()

# file4=open("d:/python/new11.txt","rb")
# print(pickle.load(file4))
# print(pickle.load(file4))

# file4.close()

# import pickle

# file=open("d:/python/new12.txt","wb+")

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