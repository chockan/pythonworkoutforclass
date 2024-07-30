"""
multithreading is a threading technique in python programming to run multiple threads concurrently
by rapidly switching between threads with a CPU help.
multithread arms to perform multiple tasks simultaneously, which increases performance speed.
it is very useful technique for time saving, improving the performance.
mutlithreading allows the programmer to divide application into subtasks and simultaneously run them in a program.
it allows to communicate and share resources such as files ,data,memory to sameprocessor
there are two amin modules
(i)thread module
(ii)threading module

thread module

a thread is an entity(individual) within a process that can be sheduled for execution.also it is smallest
unit of processing that can be performed in an operating system.
in simple words a thread is a sequence of instructions within a program that can be executed independently
of the other class
python 3========== import_thread====syntax:_thread.start_new_thread(function_name,(args))
python 2========== import thread


Threading Modules
methods
threading.activeCount()=======Returns the number of thread objects that are active
threading.currentThread()======Returns the number of thread objects in the callers threadcontrol
threading.enumerate()=======Returns a list of all thread objects that are  currently active

thread class methods
run()===is entry point for a thread
start()=== starts a thread by calling the run method
join()===waits for thread to terminate
isAlive()===checks whether a thread is still executing
getName()===returns the name of a thread
setName()===sets the name of a thread

objects types
Thread====object that represents a single thread of execution
RLock====RLock or Re-entrant lock object provides ability for a single thread to (re)acquire an already
held lock.
condition===condition variable object causes one thread to wait untill certain "condition"
has been satisfied by anotherthread.(such as change in state or some data value)
Event====its a  kore general version of condition variables, where by a nuber of threads can be made to wait to 
for some event to occur and all the threads  waiting will only waken when the event happens
Semaphore====provides  a "counter" of finite resources shared between threads block when none are available
BoundedSemaphore====Similar to a Semaphore but  ensures that it never exceeds
Timer===Similar to thread , except that it waits for a specified period of time before running


"""

#ex=1
# def name(n):
#     print("hello",n)

# def place(a):
#     print("welcome to",a)

# name("sachin")
# place("chennai")

##########################################

import _thread
import time

def name(n):
    time.sleep(0.5)
    print("hello",n)

def place(a):
    time.sleep(0.5)
    print("welcome to",a)


x=time.time()
_thread.start_new_thread(name,("sachin",))
_thread.start_new_thread(place,("mumbai",))
print("time taken",time.time()-x)

##############################################

# import threading
# import time

# def name(n):
#     time.sleep(0.5)
#     print("hello",n)

# def place(a):
#     time.sleep(0.5)
#     print("welcome to",a)


# x=time.time()
# t1=threading.Thread(target=name,args=("sachin",))
# t2=threading.Thread(target=place,args=("mumbai"))
# t1.start()
# t2.start()

# t1.join()
# t2.join()
# print("time taken",time.time()-x)

############################################