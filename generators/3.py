# def table():  
#     for i in range(1,5):  
#         yield i 

         
  
# for i in table():  
#     print(i)  

####################################################

# def table1():
#     return "hi"



# print(table1())

# #########################################

# def table():
#     yield "hi"


# a=table()
# print(table())
# for i in a:
#     print(i)


#########################################
# def table(n):  
#     for i in range(1,3):  
#         yield n*i 
 
  
# for i in table(5):  
#     print(i) 

################################################
def get_sequence_upto(x):
    for i in range(x):
        yield i

a= get_sequence_upto(5) 
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
# print(next(a))







