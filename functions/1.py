# def wish(*names):

#     for name in names:
#         print("Hello",name)
# wish("MRCET","CSE","SIR","MADAM")





# def result(a):
#     if a>40:
#         return "pass"
#     else:
#         return "fail"
# a=int(input("Enter one subject marks"))
# print(result(a))


########################################
# import pdb

# def some_function():
#     x = 5
#     y = 10
#     pdb.set_trace()  # Set a breakpoint
#     z = x + y
#     return z

# def main():
#     result = some_function()
#     print("Result:", result)

# main()

##################################################
import pdb

def some_function():
    x = 5
    y = 10
    pdb.set_trace()  # Set a breakpoint
    z = x + y
    return z

def main():
    result = some_function()
    print("Result:", result)

if __name__ == "__main__":
    main()


