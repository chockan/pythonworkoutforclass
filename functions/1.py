# def wish(*names):

#     for name in names:
#         print("Hello",name)
# wish("MRCET","CSE","SIR","MADAM")




def result(a):
    if a>40:
        return "pass"
    else:
        return "fail"
a=int(input("Enter one subject marks"))
print(result(a))