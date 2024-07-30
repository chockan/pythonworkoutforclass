import time
import threading

class threadtester (threading.Thread):
    def __init__(self, id, name, i):
       threading.Thread.__init__(self)
       self.id = id
       self.name = name
       self.i = i
       
    def run(self):
       thread_test(self.name, self.i, 5)
       print ("%s has finished execution " %self.name)

def thread_test(name, wait, i):

    while i:
       time.sleep(wait)
       print ("Running %s \n" %name)
       i = i - 1

if __name__=="__main__":
    thread1 = threadtester(1, "First Thread", 1)
    thread2 = threadtester(2, "Second Thread", 2)
    thread3 = threadtester(3, "Third Thread", 3)

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()



"""

This part is the same as our previous example. Here, you import the time and thread module which are used to handle the execution and delays of the Python threads.
In this bit, you are creating a class called threadtester, which inherits or extends the Thread class of the threading module. This is one of the most common ways of creating threads in python. However, you should only override the constructor and the run() method in your app. As you can see in the above code sample, the __init__ method (constructor) has been overridden. Similarly, you have also overridden the run() method. It contains the code that you want to execute inside a thread. In this example, you have called the thread_test() function.
This is the thread_test() method which takes the value of i as an argument, decreases it by 1 at each iteration and loops through the rest of the code until i becomes 0. In each iteration, it prints the name of the currently executing thread and sleeps for wait seconds (which is also taken as an argument).
thread1 = threadtester(1, “First Thread”, 1) Here, we are creating a thread and passing the three parameters that we declared in __init__. The first parameter is the id of the thread, the second parameter is the thread’s name, and the third parameter is the counter, which determines how many times the while loop should run.
thread2.start()T he start method is used to start the execution of a thread. Internally, the start() function calls the run() method of your class.
thread3.join() The join() method blocks the execution of other code and waits until the thread on which it was called finishes.

"""