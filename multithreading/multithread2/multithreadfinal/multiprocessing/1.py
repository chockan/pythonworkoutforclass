import multiprocessing as mp
import time
import math


a1=[]
a2=[]
a3=[]

def ggg1(numbers):
    for i in numbers:
        a1.append(math.sqrt(i**2))
    print(a1)



def ggg2(numbers):
    for i in numbers:
        a2.append(math.sqrt(i**2))
    print(a2)



def ggg3(numbers):
    for i in numbers:
        a3.append(math.sqrt(i**2))
    print(a3)


if __name__=="__main__":
    number_list=list(range(5)) 

    p1=mp.Process(target=ggg1,args=(number_list,))
    p2=mp.Process(target=ggg2,args=(number_list,))
    p3=mp.Process(target=ggg3,args=(number_list,))

    start=time.time()
    p1.start()
    p2.start()
    p3.start()
    end=time.time()
    print("multiproceesing  method time:",end-start)

    # ad=time.time()
    # ggg1(number_list)
    # ggg2(number_list)
    # ggg3(number_list)
    # de=time.time()


    # print("normal method time:",de-ad)
