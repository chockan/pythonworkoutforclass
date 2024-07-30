"""
The search() Function
The search() function searches the string for a match, and returns a Match object if there is a match.

If there is more than one match, only the first occurrence of the match will be returned:6+
"""
#######################################################
# import re

# txt = "The rain in Spain"
# x = re.search("\s", txt)

# print("The first white-space character is located in position:", x.start()) 
########################################################################

# import re
# line = "Cats are smarter than dogs"
# matchObj = re.search( r'than', line)
# print (matchObj.start(), matchObj.end())
# print ("matchObj.group() : ", matchObj.group())

#########################################################################
# import re

# txt = "The rain in Spain"
# x = re.search("Portugal", txt)
# print(x)
#######################################################

# import re

# txt = "The rain in Spain"
# x = re.split("\s", txt)
# print(x)

################################################
#Split the string only at the first occurrence:

# import re

# txt = "The rain in Spain"
# x = re.split("\s", txt, 1)
# print(x)
################################################

#Replace every white-space character with the number 9:

# import re

# txt = "The rain in Spain"
# x = re.sub("\s", "9", txt)
# print(x)

###################################################

#Replace the first 2 occurrences:

# import re

# txt = "The rain in Spain"
# x = re.sub("\s", "9", txt, 2)
# print(x)

##############################################
#Do a search that will return a Match Object:

# import re

# txt = "The rain in Spain"
# x = re.search("ai", txt)
# print(x)
###########################################