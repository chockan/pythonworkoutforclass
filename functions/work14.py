import re
# a="happy learning happy"
# result=re.findall("happy",a)
# print(result)

# #######################################
# pattern = 'ball'
# string = 'ball is my favourite game foo'

# # Try to match pattern at the beginning of string
# match = re.match("foo", string)
# print(match)
# print(match.start(),match.end())
# print(match.span())

# ######################################
# import re

# pattern = 'foo'
# string = 'fooball is my favourite game'

# # Try to match pattern at the beginning of string
# match = re.match(pattern, string)
# print(match)
# if match:
#     print("Match found:", match.group())
# else:
#     print("No match")
    
########################################
# import re
# line = "Cats than are smarter than dogs than"
# ma= re.search( 'than', line)
# print(ma)
# print (ma.start(), ma.end())
# print ("matchObj.group() : ", ma.group())

####################################################
# import re
# line = "Cats are smarter than dogs"
# matchObj = re.match( r'dogs', line)
# if matchObj:
#    print ("match --> matchObj.group() : ", matchObj.group())
# else:
#    print ("No match!!")
# searchObj = re.search( r'dogs', line)
# if searchObj:
#    print ("search --> searchObj.group() : ", searchObj.group())
# else:
#    print ("Nothing found!!")
   
#######################################################

#Split the string only at the first occurrence:

# import re

# txt = "The rain in Spain"
# x = re.split("\s", txt)
# print(x)

#################################################

# import re

# txt = "The rain in Spain"
# x = re.sub("\s", "9", txt)
# print(x)

##########################################

# import re

# txt = "The rain in Spain"
# x = re.sub("\s", "9", txt, 2)
# print(x)

# ##############################################
# import re
# a="happy learning, have a great day"
# result=re.findall("[a]",a)
# print(result)

# ######################################
# import re
# a="let us see what is meta characters"
# result=re.findall("[ta]",a)
# print(result)

########################################
# import re
# a="let us see what is meta characters"
# result=re.findall("^let",a)
# print(result)

# ###################################
# import re
# a="9195959595"
# result=re.findall("^91",a)
# print(result)

###############################
# import re
# a="let us see what is meta characters"
# result=re.findall("ers$",a)
# print(result)

#########################
# import re
# a="abc@gmail.com"
# result=re.findall("@gmail.com$",a)
# print(result)
# # ###############################
# import re
# a="let us see "
# result=re.findall("l..",a)
# print(result)

# ##################################
# import re
# a="let us see what is meta characters"
# result=re.findall(".e",a)
# print(result)

# #######################################
# import re
# a="let us see what is meta characters"
# result=re.findall("e*",a)
# print(result)
###################################
# import re
# a="let us see what is meta characteeeers"
# result=re.findall("ee*",a)
# print(result)

###############################################
# import re
# a="let us see what is meta characteeeers"
# result=re.findall("et+",a)
# print(result)

#########################################
# import re
# a="let us see what is meta characteers dee"
# result=re.findall("e{2}",a)
# print(result)

# #####################################
# import re

# txt = "hello planet"

# #Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":

# x = re.findall("he.{2}o", txt)

# print(x)

# ############################################
# # import fnmatch
# import re

# strings = ['report1.doc','reporta.doc' 'slide.ppt', 'report12.pdf', 'summary.doc']
# pattern = 'report?.doc'

# filtered = [s for s in strings if fnmatch.fnmatch(s, pattern)]
# print(filtered)  # Outputs: ['report1.doc']

# # #################################################

# import re

# strings = ['hello_world.py', 'helloWorld.py', 'hi_world.py','hellow.py']
# pattern = re.compile(r'hello.*\.py')

# filtered = [s for s in strings if re.match(pattern, s)]
# print(filtered)  # Outputs: ['hello_world.py']

# ##################################################
# import re
# pattern = "\d"
# text = "Today is April 24, 2024"
# match = re.findall(pattern, text)
# print(f"Pattern {pattern} matches in {text}: {match}")

# ##################################################
# import re
# pattern = "\w"
# text = "Hello, world! How are you? 7889"
# match = re.findall(pattern, text)
# print(f"Pattern {pattern} matches in {text}: {match}")

# ##################################################
# import re
# pattern = "\s"
# text = "Hello, world! How are you?"
# match = re.findall(pattern, text)
# print(f"Pattern {pattern} matches in {text}: {match}")

# # #####################################################
# import re
# patterns = ["\D", "\W", "\S"]
# text = "Hello, 123 world!"
# for pattern in patterns:
#     match = re.findall(pattern, text)
# #     print(f"Pattern {pattern} matches in {text}: {match}")
# # #################################################################
# ######################################
# import re

# txt = "The rain in Spain aaa44"

# #Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character):

# x = re.findall("\w", txt)

# print(x)

# #########################################
# import re

# txt = "The rain in Spain falls mainly in the stays plain!"

# #Check if the string contains either "falls" or "stays":

# x = re.findall("falls|stays", txt)

# print(x)

# #########################

# from collections import Counter
# a="tutorialspoint"
# result=Counter(a)
# print(result)

# #################################
# from collections import namedtuple
# person=namedtuple("person",["name","place","sex","age"])
# id=person("kavya","Hyderabad","F","21")
# print(id)
# print(id[1])
# print(id[3])
# print(id.place)
# print(id.age)

# ####################################################
# from collections import OrderedDict
# d=OrderedDict()
# d['sachin']=100
# d['Dhoni']=90
# d['Rohit']=110
# d['Kohli']=95
# print(d)

# ################################################
# from collections import defaultdict
# d=defaultdict(int)
# d['Sachin']=90
# d['Dhoni']=80
# d['Virat']=40
# print(d)
# print(d['Dhoni'])
# print(d['Rohit'])

##########################################


# from collections import ChainMap
# a = { 1: 'edureka' , 2: 'python'}
# b = {3: 'data science' , 4: 'Machine learning'}
# c = ChainMap(a,b)
# print(c)

###########################################
from collections import deque
 
a = ['d' , 'u' , 'r' , 'e' , 'k']
a1 = deque(a)
print(a1)
print(type(a1))
#the output will be deque([ 'd' , 'u' , 'r' , 'e' , 'k' ])
a1.append('a')
print(a1)
# the output will be deque([ 'd' , 'u' , 'r' , 'e' , 'k' , 'a' ])
a1.appendleft('e')
print(a1)
# the output will be deque(['e' , 'd' , 'u' , 'r' , 'e' , 'k' , 'a' ])
a1.pop()
print(a1)
#the output will be deque([ 'e' , 'd' , 'u' , 'r' , 'e' , 'k' ])
a1.popleft()
print(a1)
#the output will be deque([ 'd' , 'u' , 'r' , 'e' , 'k' ])