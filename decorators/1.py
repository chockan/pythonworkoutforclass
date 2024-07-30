
#decorators


# def new_func():
#     print("this is an user defined function")


# def main_func(f):
#     def sub_func():
#         print("welcome to Happy students")
#         f()
#         print("this a learning side")
#     return sub_func()


main_func(new_func)

#####################################

def main_func(func):
    def sub_func():
        print("welcome to Happy students")
        func()
        print("this a learning side")
    return sub_func()

@main_func
def new_func():
    print("this is an user defined function")



