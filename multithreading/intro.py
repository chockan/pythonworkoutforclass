"""

What is a Thread?
A thread is a unit of execution on concurrent programming. Multithreading is a technique which allows a CPU to execute many tasks of one process at the same time. These threads can execute individually while sharing their process resources.
#########################################
What is a Process?
A process is basically the program in execution. When you start an application in your computer (like a browser or text editor), the operating system creates a process.
############################################
What is Multithreading in Python?
Multithreading in Python programming is a well-known technique in which multiple threads in a process share their data space with the main thread which makes information sharing and communication within threads easy and efficient. Threads are lighter than processes. Multi threads may execute individually while sharing their process resources. The purpose of multithreading is to run multiple tasks and function cells at the same time.
#############################################
What is Multiprocessing?
Multiprocessing allows you to run multiple unrelated processes simultaneously. These processes do not share their resources and communicate through IPC.
######################################################
Python Multithreading vs Multiprocessing
To understand processes and threads, consider this scenario: An .exe file on your computer is a program. When you open it, the OS loads it into memory, and the CPU executes it. The instance of the program which is now running is called the process.

Every process will have 2 fundamental components:

The Code
The Data
Now, a process can contain one or more sub-parts called threads. This depends on the OS architecture,.You can think about a thread as a section of the process which can be executed separately by the operating system.

In other words, it is a stream of instructions which can be run independently by the OS. Threads within a single process share the data of that process and are designed to work together for facilitating parallelism.
#####################################################
Why use Multithreading?
Multithreading allows you to break down an application into multiple sub-tasks and run these tasks simultaneously. If you use multithreading properly, your application speed, performance, and rendering can all be improved.
###################################################
Python MultiThreading
Python supports constructs for both multiprocessing as well as multithreading. In this tutorial, you will primarily be focusing on implementing multithreaded applications with python. There are two main modules which can be used to handle threads in Python:

The thread module, and
The threading module
However, in python, there is also something called a global interpreter lock (GIL). It doesn’t allow for much performance gain and may even reduce the performance of some multithreaded applications. You will learn all about it in the upcoming sections of this tutorial.
###############################################
The Thread and Threading modules
The two modules that you will learn about in this tutorial are the thread module and the threading module.

However, the thread module has long been deprecated. Starting with Python 3, it has been designated as obsolete and is only accessible as __thread for backward compatibility.

You should use the higher-level threading module for applications which you intend to deploy. The thread module has only been covered here for educational purposes.




"""