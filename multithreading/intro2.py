"""
The Threading Module
This module is the high-level implementation of threading in python and the de facto standard for managing multithreaded applications. It provides a wide range of features when compared to the thread module.

Structure of Threading module
Structure of Threading module
Here is a list of some useful functions defined in this module:

Function Name	Description
activeCount()	Returns the count of Thread objects which are still alive
currentThread()	Returns the current object of the Thread class.
enumerate()	Lists all active Thread objects.
isDaemon()	Returns true if the thread is a daemon.
isAlive()	Returns true if the thread is still alive.
Thread Class methods
start()	Starts the activity of a thread. It must be called only once for each thread because it will throw a runtime error if called multiple times.
run()	This method denotes the activity of a thread and can be overridden by a class that extends the Thread class.
join()	It blocks the execution of other code until the thread on which the join() method was called gets terminated.
Backstory: The Thread Class
Before you start coding multithreaded programs using the threading module, it is crucial to understand about the Thread class.The thread class is the primary class which defines the template and the operations of a thread in python.

The most common way to create a multithreaded python application is to declare a class which extends the Thread class and overrides it’s run() method.

The Thread class, in summary, signifies a code sequence that runs in a separate thread of control.

So, when writing a multithreaded app, you will do the following:

define a class which extends the Thread class
Override the __init__ constructor
Override the run() method
Once a thread object has been made, the start() method can be used to begin the execution of this activity and the join() method can be used to block all other code till the current activity finishes.
"""