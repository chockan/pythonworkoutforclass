
"""
In python, collections are the containers used for storing the data. 
The built-in data structures in python are tuples, lists, sets and dictionaries. 
The collections class will provide additional data structures apart from the built-in data structures.
Some of the data structures in the ‘collections’ module −

Counter

namedTuple

orderedDict

defaultDict

Deque

chainMap

#######

Counter
It is the type of collection in which the 
elements will be stored as dictionary keys and the counts will be stored as dictionary values.

########
namedtuple() function
The namedtuple() will allow us to create tuples with named fields. So, 
instead of accessing the items using the indices, we can access them using the dot notation.

#########
OrderedDict
OrderedDict is a dictionary which can remember the order of its items. 
It is used for preserving the order in which the items will be added into the list.

##############
defaultdict
The defaultdict has all the functionalities of a dictionary with 
the additional feature where it will never give a KeyError.

###############
ChainMap. 
It basically returns a list of several other dictionaries. Suppose you have two dictionaries 
with several key value pairs, 
in this case ChainMap will make a single list with both the dictionaries in it.

###############
deque
deque pronounced as deck is an optimized list to perform insertion and deletion easily.

"""
################################################
#counter
# from collections import Counter
# a="tutorialspoint"
# result=Counter(a)
# print(result)

# ############################################
# from collections import Counter
# a=["apple","mango","cherry","apple","mango","mango"]
# result=Counter(a)
# print(result.values())

# ###########################################
# from collections import Counter
# a=["apple","mango","cherry","apple","mango","mango"]
# result=Counter(a)
# print(result.most_common(1))
# print(result.most_common(2))

###########################################

# from collections import namedtuple
# person=namedtuple("person",["name","place","sex","age"])
# id=person("kavya","Hyderabad","F","21")
# print(id)
# print(id[1])
# print(id[3])
# print(id.place)
# print(id.age)
#############################################
from collections import OrderedDict
d=OrderedDict()
d['sachin']=100
d['Dhoni']=90
d['Rohit']=110
d['Kohli']=95
print(d)
############################################
# from collections import OrderedDict
# d=OrderedDict([('sachin',100),('Dhoni',90),('Rohit',110),('Kohli',95)])
# print(d)
# print(d.keys())

##############################################
from collections import defaultdict
d=defaultdict(int)
d['Sachin']=90
d['Dhoni']=80
d['Virat']=95
print(d)
print(d['Dhoni'])
print(d['Rohit'])

#################################################
from collections import defaultdict
d=defaultdict(float)
d['Sachin']=90
d['Dhoni']=80
print(d)
print(type(d))
print(d['Rohit'])
print(d['Dhoni'])

###############################################

from collections import ChainMap
a = { 1: 'edureka' , 2: 'python'}
b = {3: 'data science' , 4: 'Machine learning'}
c = ChainMap(a,b)
print(c)
# #the output will be ChainMap[{1: 'edureka' , 2: 'python'} , {3: 'data science' , 4: 'Machine learning'}]
# a1 = { 5: 'AI' , 6: 'neural networks'}
# c1 = c.new_child(a1)
# print(c1)
# #the output will be ChainMap[{1: 'edureka' , 2: 'python'} ,
# # {3: 'data science' , 4: 'Machine learning'}, { 5: 'AI' , 6: 'neural networks'}
##################################################
# #creating a deque
from collections import deque
 
a = ['d' , 'u' , 'r' , 'e' , 'k']
a1 = deque(a)
print(a1)
print(type(a1))
# #the output will be deque([ 'd' , 'u' , 'r' , 'e' , 'k' ])
# a1.append('a')
# print(a1)
# # the output will be deque([ 'd' , 'u' , 'r' , 'e' , 'k' , 'a' ])
# a1.appendleft('e')
# print(a1)
# # the output will be deque(['e' , 'd' , 'u' , 'r' , 'e' , 'k' , 'a' ])
# a1.pop()
# print(a1)
# #the output will be deque([ 'e' , 'd' , 'u' , 'r' , 'e' , 'k' ])
# a1.popleft()
# print(a1)
# #the output will be deque([ 'd' , 'u' , 'r' , 'e' , 'k' ])
#####################################################