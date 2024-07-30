
# def name(n):
#     print("hello",n)

# def place(a):
#     print("welcome to",a)


# name("sachin")
# place("chennai")
###############################################
# #ex=1
import time
def name(n):
    time.sleep(1)
    print("hello",n)

def place(a):
    time.sleep(1)
    print("welcome to",a)

s=time.time()
name("sachin")
place("chennai")
e=time.time()
print(e-s)

#################################################
import threading
import time

def name(n):
    time.sleep(1)
    print("hello",n)

def place(a):
    time.sleep(1)
    print("welcome to",a)


x=time.time()
t1=threading.Thread(target=name,args=("sachin",))
t2=threading.Thread(target=place,args=("mumbai",))
t1.start()
# t1.join()
t2.start()
# t2.join()
e=time.time()
print("time taken",e-x)



###################################################

# import threading
# import time

# def name(n):
#     time.sleep(1)
#     print("hello",n)

# def place(a):
#     time.sleep(1)
#     print("welcome to",a)


# x=time.time()
# t1=threading.Thread(target=name,args=("sachin",))
# t2=threading.Thread(target=place,args=("mumbai",))
# t1.start()
# t2.start()

# # # t1.join()
# # # t2.join()
# print("time taken",time.time()-x)

#####################################################

# import threading
# import time

# def name(n):
#     time.sleep(1)
#     print("hello",n)

# def place(a):
#     time.sleep(1)
#     print("welcome to",a)


# x=time.time()
# t1=threading.Thread(target=name,args=("sachin",))
# t2=threading.Thread(target=place,args=("mumbai",))
# t1.start()
# t1.join()
# t2.start()

# # t1.join()
# t2.join()
# print("time taken",time.time()-x)


###################################################
# import threading  
# def print_hello(n):  
#     print("Hello, how old are you? ", n)  
# T1 = threading.Thread( target = print_hello, args = (20, ))  
# T1.start()  
# # T1.join()  
# print("Thank you") 


###############################################
# import multiprocessing as mp
# import time
# import math


# a1=[]
# a2=[]
# a3=[]

# def ggg1(numbers):
#     for i in numbers:
#         a1.append(math.sqrt(i**2))
#     print(a1)



# def ggg2(numbers):
#     for i in numbers:
#         a2.append(math.sqrt(i**2))
#     print(a2)



# def ggg3(numbers):
#     for i in numbers:
#         a3.append(math.sqrt(i**2))
#     print(a3)


# if __name__=="__main__":

#     number_list=list(range(5)) 

#     p1=mp.Process(target=ggg1,args=(number_list,))
#     p2=mp.Process(target=ggg2,args=(number_list,))
#     p3=mp.Process(target=ggg3,args=(number_list,))

#     start=time.time()
#     p1.start()
#     p2.start()
#     p3.start()
#     end=time.time()
#     print("multiproceesing  method time:",end-start)

#     s=time.time()
#     ggg1(number_list)
#     ggg2(number_list)
#     ggg3(number_list)
#     e=time.time()


#     print("normal method time:",e-s)
###########################################################################
# from concurrent.futures import ThreadPoolExecutor
# import time
# def fun(n):
#     print(f"calculating the result of {n}")
#     time.sleep(1)
#     print(f"{n} value is {n**2}")

# pool=ThreadPoolExecutor(2)
# work1=pool.submit(fun,3)
# work2=pool.submit(fun,4)
# work3=pool.submit(fun,5)
# work4=pool.submit(fun,6)
# work5=pool.submit(fun,7)

# print("hello")


# print("work1 running function",work1.running())
# #print("work1",work1.cancel())
# time.sleep(3)
# print("work1 done function",work1.done())
# pool.shutdown()



##############################################################
# from concurrent.futures import ThreadPoolExecutor
# from time import sleep
# def square(numbers):
#    for val in numbers:
#       ret = val*val
#       sleep(1)
#       print("Number:{} Square:{}".format(val, ret))
# def cube(numbers):
#    for val in numbers:
#       ret = val*val*val
#       sleep(1)
#       print("Number:{} Cube:{}".format(val, ret))

# numbers = [1,2,3,4,5]
# executor = ThreadPoolExecutor(4)
# thread1 = executor.submit(square, (numbers))
# thread2 = executor.submit(cube, (numbers))
# print("Thread 1 executed ? :",thread1.done())
# print("Thread 2 executed ? :",thread2.done())
# sleep(2)
# print("Thread 1 executed ? :",thread1.done())
# print("Thread 2 executed ? :",thread2.done())

##########################################################

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

# from threading import *
# import time

# l=Lock()
# def watchtv(name):
#     l.acquire()#Thread acquires here Lock
#     print("hi",end=" ")
#     time.sleep(1)
#     print(name)
#     l.release()#Thread releases here Lock

# a='sachin'
# b="dhoni"
# t=Thread(target=watchtv,args=(a,))
# t2=Thread(target=watchtv,args=(b,))
# t.start()
# t2.start()

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