#sub class
#thread class

from threading import *

class abcThread(Thread):
    def run(self):
        for i in range(5):
            print("hello")

a=abcThread()
a.start()
for k in range(5):
    print("hi")

"""
inheritance are happened here, base class is thread , child class
act as abcThread.
"""

######################################################
#using class in thread

from threading import *
class ABCD:
    def display(self):
        for i  in range(5):
            print("helllo")

a=ABCD()
t=Thread(target=a.display)
t.start()

for i in range(5):
    print("Hi")

