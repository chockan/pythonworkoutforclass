
import re

# pattern = 'foo'
# string = 'ball is my favourite game foo'

# # Try to match pattern at the beginning of string
# match = re.match(pattern, string)
# print(match)
# print(match.start(),match.end())
# print(match.span())
# print(match.group())

####################################################################
# import re
# line = "Cats are smarter than dogs"
# matchObj = re.search( 'ball', line)
# print(matchObj)
# print (matchObj.start(), matchObj.end())
# print (matchObj.group())

###########################################################################
# import re
# a="happy learning"
# result=re.findall("a",a)
# print(result)

####################################################################
# import re
# a="happy learning"
# result=re.search("le",a)
# print(result)
# print(result.string)

###########################################################
# import re
# a="happy learning"
# result=re.split(" ",a)
# print(result)

##############################################################
# import re
# a="happy learning, have a great day"
# result=re.sub(" ","#",a)
# print(result)

###############################################################
# import re
# a="happy learning, have a great day"
# result=re.sub("h","H",a,1)
# print(result)

#########################################################
# import re

# txt = "The rain in Spain"

# #Find all lower case characters alphabetically between "a" and "m":

# x = re.findall("[a-m]", txt)
# print(x)

#################################################################
# import re

# txt = "hello planet hell"

# #Search for a sequence that starts with "he", followed by two (any) characters, and an "o":

# x = re.findall("he..o", txt)
# print(x)

#####################################################################
# import re

# txt = " hello planet "

# #Check if the string starts with 'hello':

# x = re.findall("^hell", txt)
# print(x)

#################################################################

# import re

# txt = "hello planet"

# #Check if the string ends with 'planet':

# x = re.findall("planet$", txt)
# print(x)


##########################################################

# import re

# txt = "hello planet"

# #Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":

# x = re.findall("he.*o", txt)

# print(x)

#################################################################
# import re

# txt = "helo planet"

# #Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o":

# x = re.findall("he.+o", txt)

# print(x)

################################################
# import re

# txt = "hello planet"

# #Search for a sequence that starts with "he", followed by 0 or 1  (any) character, and an "o":

# x = re.findall("he.?o", txt)

# print(x)

######################################################################

# import re

# txt = "hello planet"

# #Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":

# x = re.findall("he.{2}o", txt)

# print(x)

####################################################################

import re

txt = "The rain in Spain falls mainly in the plain!"

#Check if the string contains either "falls" or "stays":

x = re.findall("falls|stays", txt)

print(x)





