from concurrent.futures import ThreadPoolExecutor
import time
def fun(n):
    print(f"calculating the result of {n}")
    time.sleep(1)
    print(f"{n} value is {n**2}")

p=ThreadPoolExecutor(2)
work1=p.submit(fun,3)
work2=p.submit(fun,4)
work3=p.submit(fun,5)
work4=p.submit(fun,6)
work5=p.submit(fun,7)

print("hello")


print("work1 running function",work1.running())
#print("work1",work1.cancel())
time.sleep(3)
print("work1 done function",work1.done())
p.shutdown()




##############################################################
from concurrent.futures import ThreadPoolExecutor
from time import sleep
def square(numbers):
   for val in numbers:
      ret = val*val
      sleep(1)
      print("Number:{} Square:{}".format(val, ret))
def cube(numbers):
   for val in numbers:
      ret = val*val*val
      sleep(1)
      print("Number:{} Cube:{}".format(val, ret))

numbers = [1,2,3,4,5]
executor = ThreadPoolExecutor(4)
thread1 = executor.submit(square, (numbers))
thread2 = executor.submit(cube, (numbers))
print("Thread 1 executed ? :",thread1.done())
print("Thread 2 executed ? :",thread2.done())
sleep(2)
print("Thread 1 executed ? :",thread1.done())
print("Thread 2 executed ? :",thread2.done())