# from collections import OrderedDict
# d=OrderedDict()
# d['sachin']=100
# d['Dhoni']=90
# d['Rohit']=110
# d['Kohli']=95
# print(d)

# #################################################
# #counter
# from collections import Counter
# a="tutorialspoint"
# result=Counter(a)
# print(result)

####################################################
# from collections import Counter
# a=["apple","mango","cherry","apple","mango","mango"]
# result=Counter(a)
# print(result.values())
# print(type(result))
########################################################
# from collections import namedtuple
# person=namedtuple("person",["name","place","sex","age"])
# id=person("kavya","Hyderabad","F","21")
# print(id)
# print(id[1])
# print(id[3])
# print(id.place)
# print(id.age)

##########################################################

# from collections import defaultdict
# d=defaultdict(int)
# d['Sachin']=90
# d['Dhoni']=80
# d['Virat']=95
# print(d)
# print(d['Dhoni'])
# print(d['Rohit'])

########################################################
# from collections import ChainMap
# a = { 1: 'edureka' , 2: 'python'}
# b = {3: 'data science' , 4: 'Machine learning'}
# c = ChainMap(a,b)
# print(c)

###################################################
from collections import deque
 
a = ['d' , 'u' , 'r' , 'e' , 'k']
a1 = deque(a)
print(a1)
print(type(a1))