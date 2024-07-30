"""

###match functions
This function attempts to match the pattern at the beginning of the string.
If the pattern matches at the beginning of the string, it returns a match object; otherwise, it returns None.
*****It only checks for a match at the beginning of the string.


The Match object has properties and methods used to retrieve information about the search, and the result:

.span() returns a tuple containing the start-, and end positions of the match.
.string returns the string passed into the function
.group() returns the part of the string where there was a match
"""
######################################################
# import re

# pattern = r'foo'
# string = 'ball is my favourite game foo'

# # Try to match pattern at the beginning of string
# match = re.match(pattern, string)
# print(match)
# print(match.start(),match.end())
# print(match.span())
###########################################################
# import re

# pattern = r'game'
# string = 'fooball is my favourite game'

# Try to match pattern at the beginning of string
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
###########################################################
# import re

# pattern = r'foo'
# string = 'my favourite game is football'

# # Try to match pattern at the beginning of string
# match = re.match(pattern, string)
# print(match)
# if match:
#     print("Match found:", match.group())
# else:
#     print("No match")

###########################################################
# import re
# line = "Cats are smarter than dogs"
# matchObj = re.match( r'Cats', line)
# print (matchObj.start(), matchObj.end())
# print ("matchObj.group() : ", matchObj.group())
##########################################################
#Print the position (start- and end-position) of the first match occurrence.

#The regular expression looks for any words that starts with an upper case "S":

# import re

# txt = "The rain in Spain"
# x = re.search(r"\bS\w+", txt)
# print(x.span())

##############################################################

#Print the string passed into the function:

# import re

# txt = "The rain in Spain"
# x = re.search(r"\bS\w+", txt)
# print(x.string)

#######################################################
#Print the part of the string where there was a match.

#The regular expression looks for any words that starts with an upper case "S":

# import re

# txt = "The rain in Spain"
# x = re.search(r"\bS\w+", txt)
# print(x.group())

#############################################