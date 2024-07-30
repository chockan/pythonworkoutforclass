# synchronization

# from threading import *
# import time

# def abc(name):
#     print("hi",end=" ")
#     time.sleep(1)
#     print(name)

# a='sachin'
# b="dhoni"
# t=Thread(target=abc,args=(a,))
# t2=Thread(target=abc,args=(b,))
# t.start()
# t2.start()

###############################################

from threading import *
import time

l=Lock()
def watchtv(name):
    l.acquire()#Thread acquires here Lock
    print("hi",end=" ")
    time.sleep(1)
    print(name)
    l.release()#Thread releases here Lock

a='sachin'
b="dhoni"
t=Thread(target=watchtv,args=(a,))
t2=Thread(target=watchtv,args=(b,))
t.start()
t2.start()

############################################
#deadlock
# from threading import *
# import time

# l=Lock()
# def watchtv(name):
#     l.acquire()#Thread acquires here Lock
#     print("hi",end=" ")
#     c=input("enter the your place")
#     time.sleep(1)
#     print(name,c)
#     l.release()#Thread releases here Lock

# a='sachin'
# b="dhoni"
# t=Thread(target=watchtv,args=(a,))
# t2=Thread(target=watchtv,args=(b,))
# t.start()
# t2.start()

#################################################

#RLock only used in recursion program
# from threading import *
# import time
# l=RLock
# def fact1(n):
#     l.acquire()
#     if (n==0):
#         result=1
#     else:
#         result=n*fact1(n-1)
#     l.release()
#     return result
# def call(no):
#     print("factorial number is:",fact1(no))
# call(3)
# t=Thread(target=call,args=(4,))
# t1=Thread(target=call,args=(5,))
# t.start()
# t1.start()

#####################################