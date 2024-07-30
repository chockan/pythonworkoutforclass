#write a program to find common letters between two letters

# def abc(a,b):
#     s1=set(a)
#     s2=set(b)
#     print(s1,s2)
#     l1=s1&s2
#     print(l1)

# a=input("enter the name1")
# b=input("enter the name1")
# abc(a,b)

###################################

#write a program to count the frequency of wordsaearing ina string
#ex.Sheena loves eating ale and mango.Her sister also loves eating apple and mango

# def abc(a):
#     b=a.split()
#     print(b)
#     d={}
#     for i in b:
#         if i not in d.keys():
#             d[i]=0
#         d[i]=d[i]+1
#     print(d)
# a=input("enter the sentence")
# abc(a)

############################################
#write a program to convert two lists into a dictionary
#ex.list1=[Naina,kimi,sheena]
#ex.list2=[858545,567845,691276]

# def abc(x,y):
#     a=zip(x,y)
#     print(a)
#     b=dict(a)
#     print(b)
   
# list1=["Naina","kimi","sheena"]
# list2=[858545,567845,691276]
# abc(list1,list2)

#####################################
#find missing number in an array(using summation and xor operation)
#12456
#sum of natural numbers n*(n+1)/2

# def abc(a):
#     n=a[-1]
#     sum1=0
#     t=n*(n+1)//2
#     print(t)
#     sum1=sum(a)
#     print(t-sum1)

# a=[1,2,4,5,6,7]
# abc(a)

#second method
# def abc1(a):
#     n=len(a)
#     b=a[0]
#     for i in range(1,n):
#         b=b^a[i]
#     print(b)
#     x2=0
#     for index in range(1,n+2):
#         x2=x2^index
#     print(b^x2)

# a=[1,2,4,5,6,7]
# abc1(a)

#####################################
#find out pairs with given s value of an array

# def abc(b,s):
#     left=0
#     right=len(b)-1
#     while(left<=right):
#         if(b[left]+b[right]>s):
#             right=right-1
#         elif(b[left]+b[right]<s):
#             left=left+1
#         elif(b[left]+b[right]==s):
#             print("value pair is",b[left],"&",b[right])
#             right=right-1
#             left=left+1


# a=[5,7,4,3,9,8,19,21]
# s=17
# b=sorted(a)
# print(b)
# abc(b,s)

##########################################
# Python 3 program to find 
# factorial of given number
# def factorial(n):
#     if(n==1 or n==0):
#         return 1
#     else:
#         return n*factorial(n-1)
    
#     # single line to find factorial
#     #return 1 if (n==1 or n==0) else n * factorial(n - 1) 

# # Driver Code
# num = 5
# print("Factorial of",num,"is",factorial(num))

# ##########################################
# # Python3 program to find simple interest
# # for given principal amount, time and
# # rate of interest.


# def simple_interest(p,t,r):
# 	print('The principal is', p)
# 	print('The time period is', t)
# 	print('The rate of interest is',r)
	
# 	si = (p * t * r)/100
	
# 	print('The Simple Interest is', si)
# 	return si
	
# # Driver code
# simple_interest(8, 6, 8)
##########################################
# Python 3 code to find sum
# of elements in given array

# input values to list
# arr = [12, 3, 4, 15]

# # sum() is an inbuilt function in python that adds
# # all the elements in list,set and tuples and returns
# # the value
# ans = sum(arr)

# # display sum
# print('Sum of the array is ', ans)
##########################################
# list1 = [12, 3, 4, 15]
# s=0
# for i,a in enumerate(list1): 
#     s+=a 
# print(s)

##################################
#Python Program to Find Sum of Array Using counter method.

# from collections import Counter

# arr = [12, 3, 4, 15]
# c = Counter(arr)
# print(c)
# sum = 0

# for key, value in c.items():
# 	sum += key * value

# print("Sum of the array is", sum)

######################################
#Python Program to Find Largest Element in an Array
# def abc(a):
# 	b=a[0]
# 	c=len(a)
# 	for i in range(1,c):
		
# 		if (b < a[i]):
			
# 			b=a[i]
# 	return b
			
# a= [10, 324, 45, 90, 9808]
# print(abc(a))

######################################
#sorting based on length
# my_list = ["apple", "banana", "cherry"]
# my_list.sort(key=len)
# print(my_list)  # Output: ['apple', 'cherry', 'banana']

######################################################
from collections import Counter
a=3
b=[1,2,3,3,2,1,2,3,1,2,3,3,2,1,2,3,1,1,2]
g=Counter(b)
print(g)
# e=[]
# if a==1:
#     c=set(b)
#     d=list(c)
#     print(d)
# elif a==2:
#     for i in b:
#         if i not in e:
#             e.append(i)
#         else:
#             if i in e:
#                 f=e.count(i)
#                 #print(f)
#                 if f<2:
#                     e.append(i)
#                     #print(i)
#                 else:
#                     continue
#     print(e)
    
# elif a==3:
#     for i in b:
#         if i not in e:
#             e.append(i)
#         else:
#             if i in e:
#                 f=e.count(i)
#                 print(f)
#                 if f<3:
#                     e.append(i)
#                     #print(i)
#                 else:
#                     continue
#     print(e)
    


