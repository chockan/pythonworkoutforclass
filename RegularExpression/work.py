

"""
findall()
search()==return match object
    methods==start,span,strings
sub()

"""
###################################
# import re
# a="happy learning"
# result=re.findall("le",a)
# print(result)


#####################################
# import re
# a="happy learning"
# b="happy"
# result=re.findall(b,a)
# print(result)

#####################################
# import re
# a="happy learning"
# result=re.findall("abc",a)
# print(result)

####################################

# import re
# a="happy learning"
# result=re.search("le",a)
# print(result)
# print(result.start())
# print(result.span())
# print(result.group())
# print(type(result.group()))

##################################
# import re
# a="happy learning"
# result=re.search("abc",a)
# print(result)

################################

# import re
# a="happy learning"
# result=re.search("le",a)
# print(result.start())

# ##################################

# import re
# a="happy learning"
# result=re.search("le",a)
# print(result.span())

####################################
# import re
# a="happy learning"
# result=re.search("le",a)
# print(result.string)

######################################
# import re
# a="happy learning"
# result=re.split("",a)
# print(result)
####################################
# import re
# a="happy learning"
# result=re.split("r",a)
# print(result)

######################################
# import re
# a="happy learning"
# result=re.split("r",a)
# print(result)

#####################################
# import re
# a="happy learning, have a great day"
# result=re.split(" ",a,3)
# print(result)

#####################################
# import re
# a="happy learning, have a great day"
# result=re.sub(" ","#",a)
# print(result)

###################################
# import re
# a="happy learning, have a great day"
# result=re.sub("h","H",a)
# print(result)

##############################

# import re
# a="happy learning, have a great day"
# result=re.sub("h","H",a,1)
# print(result)

##################################
# import re
# a="happy learning, have a great day"
# result=re.sub("a","A",a,2)
# print(result)

##################################
# import re

# pattern = r'foo'
# string = 'fooball is my favourite game'

# # Try to match pattern at the beginning of string
# match = re.match(pattern, string)
# print(match)
# print(match.start(),match.end())
# print(match.span())
###########################################################
# import re

# pattern = r'game'
# string = 'fooball is my favourite game'

# # Try to match pattern at the beginning of string
# match = re.match(pattern, string)
# print(match)
# print(match.start(),match.end())
# print(match.span())
###########################################################
# import re

# pattern = r'foo'
# string = 'fooball is my favourite game'

# # Try to match pattern at the beginning of string
# match = re.match(pattern, string)
# print(match)
# if match:
#     print("Match found:", match.group())
# else:
#     print("No match")


###############################
# import re

# txt = "The rain in Spain"

# #Find all lower case characters alphabetically between "a" and "m":

# x = re.findall("[a-m]", txt)
# print(x)

###############################################################
# import re

# txt = "hello planet hell"

# #Search for a sequence that starts with "he", followed by two (any) characters, and an "o":

# x = re.findall("he..o", txt)
# print(x)

#################################################################
# import re

# txt = "hell planet"

# #Check if the string starts with 'hello':

# x = re.findall("^hello", txt)
# print(x)
# # if x:
# #   print("Yes, the string starts with 'hello'")
# # else:
# #   print("No match")

##############################################################
# import re

# txt = "hello planet"

# #Check if the string ends with 'planet':

# x = re.findall("planet$", txt)
# print(x)

#############################################################
# import re

# txt = "hello planet"

# #Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":

# x = re.findall("he.*o", txt)

# print(x)

###########################################################
# import re

# txt = "hello planet"

# #Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o":

# x = re.findall("he.+o", txt)

# print(x)

########################################################
# import re

# txt = "hello planet"

# #Search for a sequence that starts with "he", followed by 0 or 1  (any) character, and an "o":

# x = re.findall("he.?o", txt)

# print(x)

######################################################
# import re

# txt = "hello planet"

# #Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":

# x = re.findall("he.{2}o", txt)
##########################################################

# import re

# txt = "The rain in Spain falls mainly in the plain!"

# #Check if the string contains either "falls" or "stays":

# x = re.findall("falls|stays", txt)

# print(x)

###########################################################
# import re

# # Pattern to match if a string contains the literal sequence \d+
# pattern = r"\\d\+"
# text = "This string contains the sequence \\d+ and some other text."
# matches = re.findall(pattern, text)
# print(matches)
######################################################

# import re

# txt = "The rain in Spain"

# #Check if the string starts with "The":

# x = re.findall("\AThe", txt)

# print(x)

#####################################################
# import re

# txt = "The rain in Spain"

# #Check if "ain" is present at the beginning of a WORD:

# x = re.findall(r"\bain", txt)

# print(x)
###################################################
# import re

# txt = "The rain in Spain"

# #Check if "ain" is present at the end of a WORD:

# x = re.findall(r"ain\b", txt)

# print(x)

#################################################

# import re

# txt = "The rain in Spain"

# #Find all lower case characters alphabetically between "a" and "m":

# x = re.findall("[a-m]", txt)
# print(x)

################################################
# import re

# txt = "hello planet"

# #Search for a sequence that starts with "he", followed by two (any) characters, and an "o":

# x = re.findall("he..o", txt)
# print(x)

##########################################################


# import re

# txt = "hello planet"

# #Check if the string starts with 'hello':

# x = re.findall("^h", txt)
# print(x)

# ######################################################
# import re

# txt = "hello planet"

# #Check if the string ends with 'planet':

# x = re.findall("planet$", txt)
# print(x)

