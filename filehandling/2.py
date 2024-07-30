#file=open("d:/python course/abc.txt","x")

# file=open("d:/python course/abc.txt","w")
# file.write("hi \n")
# file.write("how are you \n")
# file.write("i am fine \n")
# file.write("hope you are fine \n")
# file.write("Thank you \n")
# file.close()

# file=open("d:/python course/abc.txt","r")
# print(file.readline())
# print(file.readline())
# print(file.readline())
# file.close()

# file=open("d:/python course/abc.txt","r")
# #print(file.tell())
# file.seek(5)
# print(file.tell())

# file.close()



# file3=open("d:/python course/abc.txt","r")
# file4=open("d:/python/new1.txt","x")

# for i in file3:
#     file4.write(i)

# file3.close()
# file4.close()

#split
# file4=open("d:/python/new1.txt","r")
# print(file4.read().split("you"))
# file4.close()

#truncate
# file4=open("d:/python/new1.txt","r")
# print(file4.truncate(5))
# file4.close()

# file4=open("d:/python/new1.txt","w")
# file4.write("hi ")
# # file4.flush()
# # file4.write("hi good evening")
# file4.close()

file4=open("d:/python/new1.txt","a")
file4.write("hope you are well ")
# file4.flush()
# file4.write("hi good evening")
file4.close()

