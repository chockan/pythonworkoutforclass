

# file=open("d:/python/new1.txt","x")
# file.close()

# file2=open("d:/python/new1.txt","w")
# file2.write("hello")
# file2.write("how r u")
# file2.write("i am fine")
# file2.write("how about you")
# file2.write("where are you")
# file2.close()


# file3=open("d:/python/new1.txt","r")
# a=file3.read()
# b=file3.tell()
# print(b)
# d=file3.seek(5)
# f=file3.tell()
# print(f)

# file3.close()


file3=open("d:/python/new1.txt","r")
file4=open("d:/python/new2.txt","x")


for i in file3:
    file4.write(i)

file3.close()
file4.close()


########################
file=open("d:/python/new6.dat" ,"w")
file.write("hi")
file.write("hello how are you \n")
file.write("i am fine \n")
file.write("hope you are fine\n")
file .close()

##############################
