# import re
# pattern = "ba*"
# texts = ["b", "ba", "baa", "baaa"]
# for text in texts:
#     match = re.findall(pattern, text)
#     print(f"Pattern {pattern} matches {text}: {match}")

##########################################
# import re
# pattern = "ba+"
# texts = ["b", "ba", "baa", "baaa"]
# for text in texts:
#     match = re.findall(pattern, text)
#     print(f"Pattern {pattern} matches {text}: {match}")

# ###############################################
# import re
# pattern = "colou?r"
# texts = ["color", "colour",'colouur']
# for text in texts:
#     match = re.findall(pattern, text)
#     print(f"Pattern {pattern} matches {text}: {match}")

###############################################################
# import re

# txt = "The rain in Spain"

# #Find all lower case characters alphabetically between "a" and "m":

# x = re.findall("[a-m]", txt)
# print(x)

########################################################
# import re

# txt = "hello planet"

# #Search for a sequence that starts with "he", followed by two (any) characters, and an "o":

# x = re.findall("he..o", txt)
# print(x)

########################################################
# import re

# txt = "hello planet"

# #Check if the string starts with 'hello':

# x = re.findall("^hello", txt)
# print(x)

#########################################################
# import re

# txt = "hello planet"

# #Check if the string ends with 'planet':

# x = re.findall("planet$", txt)

# print(x)

#####################################################
# import re

# txt = "The rain in Spain falls mainly in the stays plain!"

# #Check if the string contains either "falls" or "stays":

# x = re.findall("falls|stays", txt)

# print(x)
##############################################

"""
\d: Matches any digit (equivalent to [0-9]).
\w: Matches any alphanumeric character (equivalent to [a-zA-Z0-9_]).
\s: Matches any whitespace character.
\D, \W, \S: Match any character that is not a digit, alphanumeric, or whitespace 

"""
##########################################################
# import re
# pattern = "\d"
# text = "Today is April 24, 2024"
# match = re.findall(pattern, text)
# print(f"Pattern {pattern} matches in {text}: {match}")

# ################################################################
# import re
# pattern = "\w"
# text = "Hello, world! How are you? 7889"
# match = re.findall(pattern, text)
# print(f"Pattern {pattern} matches in {text}: {match}")
# # #############################################################
# import re
# pattern = "\s"
# text = "Hello, world! How are you?"
# match = re.findall(pattern, text)
# print(f"Pattern {pattern} matches in {text}: {match}")
# ##################################################################
# 
# import re
# patterns = ["\D", "\W", "\S"]
# text = "Hello, 123 world!"
# for pattern in patterns:
#     match = re.findall(pattern, text)
#     print(f"Pattern {pattern} matches in {text}: {match}")

#############################################
# import re

# txt = "The rain in Spain"

# #Return a match at every NON white-space character:

# x = re.findall("\S", txt)

# print(x)


# ##############################################
# import re

# txt = "The rain in Spain aaa44"

# #Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character):

# x = re.findall("\w", txt)

# print(x)

################################################
# import re

# txt = "The rain in Spain!"

# #Return a match at every NON word character (characters NOT between a and Z. Like "!", "?" white-space etc.):

# x = re.findall("\W", txt)

# print(x)

# import re

# txt = "hello planet"

# #Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":

# x = re.findall("he.{2}o", txt)

# print(x)
