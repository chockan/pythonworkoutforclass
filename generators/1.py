##########################################
list = [1,2,3,4,5,6]  
  
z = (x**3 for x in list)  
  
print(next(z))  
  
print(next(z))  
  
print(next(z))  
  
print(next(z))  

#######################################

def table(n):  
    for i in range(1,11):  
        yield n*i 

        i = i+1  
  
for i in table(15):  
    print(i)  


#################################
def simple():  
    for i in range(10):  
        if(i%2==0):  
            yield i  
  
#Successive Function call using for loop  
for i in simple():  
    print(i)  

###################################
    
def mygenerator():
    print('First item')
    yield 10

    print('Second item')
    yield 20

    print('Last item')
    yield 30


gen = mygenerator() 
val = next(gen) #First item
print(val) #10

val = next(gen) #Second item
print(val) #20

val = next(gen) #Last item
print(val) #30

val = next(gen) #error  

##############################
def get_sequence_upto(x):
    for i in range(x):
        yield i

seq = get_sequence_upto(5) 
print(next(seq)) #0
print(next(seq)) #1
print(next(seq)) #2
print(next(seq)) #3
print(next(seq)) #4
print(next(seq)) #error
#################################
list = [1,2,3,4,5,6,7]  
  
# List Comprehension  
z = [x**3 for x in list]  
  
# Generator expression  
a = (x**3 for x in list)  
  
print(a)  
print(z)  