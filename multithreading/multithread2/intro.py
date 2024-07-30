"""
import threading
from threading import thread
import time

ex:
def abc(n):
    print(n*n)
abc(5)
this is thread function



"""

import threading
from threading import Thread
import time
def abc(n):
    time.sleep(.3)
    print(n*n)
abc(5)

def abc1(n):
    print(n*n)
abc1(5)


def abc2(n):
    print(n*n)
abc2(5)

print(threading.active_count())

thrd=Thread(target=abc,args=(5,))
thrd.start()
thrd1=Thread(target=abc1,args=(5,))
thrd1.start()



print(threading.active_count())

thrd.join()
thrd1.join()

print("finished")
