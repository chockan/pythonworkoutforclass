#############################################
# import time
# def abc():
#     for i in range(5):
#         time.sleep(1)
#         print("hello")
# abc()

######################################

# import time
# def abc():
#     for i in range(5):
#         time.sleep(1)
#         print("hello")
# abc()

# def abc1():
#     for i in range(5):
#         time.sleep(1)
#         print("hi")
# abc1()

############################################
# import time
# def abc():
#     for i in range(5):
#         time.sleep(1)
#         print("hello")

# def abc1():
#     for i in range(5):
#         time.sleep(1)
#         print("hi")

# a=time.time()
# abc()
# abc1()
# b=time.time()
# print("time is:",b-a)

################################################
from threading import *
import time
def abc():
    for i in range(5):
        time.sleep(1)
        print("hello")

def abc1():
    for i in range(5):
        time.sleep(1)
        print("hi")

a=time.time()
t=Thread(target=abc)
t1=Thread(target=abc1)
t.start()
t.join()
t1.start()
t1.join()
# t.join()
# t1.join()
b=time.time()
print("time is:",b-a)

######################################################

# from threading import *
# import time
# def abc(values):
#     for i in values:
#         time.sleep(1)
#         print("hello",i)

# def abc1(values):
#     for i in values:
#         time.sleep(1)
#         print("hi",i)
# ab=[1,2,3,4,5]
# a=time.time()
# t=Thread(target=abc,args=(ab,))
# t1=Thread(target=abc1,args=(ab,))
# t.start()
# t1.start()
# t.join()
# t1.join()
# b=time.time()
# print("time is:",b-a)

#############################################

# from threading import *
# import time
# def abc(values):
#     for i in values:
#         time.sleep(1)
#         print("hello",i)

# def abc1(values):
#     for i in values:
#         time.sleep(1)
#         print("hi",i)
# ab=[1,2,3,4,5]

# t=Thread(target=abc,args=(ab,))
# t.start()
# t.join()

# for i in range(5):
#     print("outer code",i)

# t1=Thread(target=abc1,args=(ab,))
# t1.start()
# t1.join()
###################################################

# from threading import *
# import time
# def abc(values):
#     for i in values:
#         time.sleep(1)
#         print("hello",i)

# def abc1(values):
#     for i in values:
#         time.sleep(1)
#         print("hi",i)
# ab=[1,2,3,4,5]

# t=Thread(target=abc,args=(ab,))
# t1=Thread(target=abc1,args=(ab,))
# t.start()
# t1.start()
# t.join()
# t1.join()

# for i in range(5):
#     print("outer code",i)




