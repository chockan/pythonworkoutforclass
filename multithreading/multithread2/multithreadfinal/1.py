# def abc():
#     for i in range(5):
#         print(i)
# abc()

# # # #############################################
# from threading import *

# def abc():
#     for i in range(5):
#         print(i)
# t=Thread(target=abc)
# t.start() #starting thread objects

###############################################

# from threading import *

# def abc():
#     for i in range(5):
#         print("function",i)
# t=Thread(target=abc)
# t.start() #starting thread objects
# # abc()
# for j in range(6,12):
#      print("for loop",j)

#############################################
# from threading import *

# def abc():
#     for i in range(5):
#         print("function",i)
# t=Thread(target=abc)
# t.start() #starting thread objects
# for j in range(6,12):
#     print("for loop",j)

################################################

# from threading import *

# def base():
#     for i in range(5):
#         print("base",i)
# t=Thread(target=base)
# t.start() #starting thread objects

# def child():
#     for k in range(5):
#         print("child",k)
# t1=Thread(target=child)
# t1.start()

# for j in range(6,12):
#     print("normal",j)

########################################
# from threading import *
# def base():
#     for i in range(5):
#         print("base",i)
# base()

# def child():
#     for k in range(5):
#         print("child",k)
# t1=Thread(target=child)
# t1.start()

# for j in range(6,12):
#     print("normal",j)

# print(current_thread().getName())
# current_thread().setName("ABC")
# print(current_thread().getName())

#########################################
# from threading import *

# def base():
#     for i in range(5):
#         print("base",i)

# def child():
#     for k in range(5):
#         print("child",k)
# t1=Thread(target=child)
# t=Thread(target=base)
# t.start()
# t.join() #starting thread objects
# t1.start()

# t1.join()

# for j in range(6,12):
#     print("normal",j)

##############################################
from threading import *

def base():
    for i in range(5):
        print("base",i)

def child():
    for k in range(5):
        print("child",k)
t1=Thread(target=child)
t=Thread(target=base)
t.start() #starting thread objects
t1.start()
t.join()
t1.join()

for j in range(6,12):
    print("normal",j)