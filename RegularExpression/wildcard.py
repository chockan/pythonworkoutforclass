"""
Wildcards in Python
A wildcard is a symbol that can be used in place of or in addition to one or more characters. In computer programmes, languages, search engines, including operating systems, wildcards are used to condense search criteria. The question mark (?) and the asterisk () are the most popular wildcards.

Types of wildcards
The Asterisk (*)===='*'Matches any sequence of characters (including the empty sequence)
The Question Mark (?)===='?'matches any single character

Text = "baaabab",
Pattern = “*****ba*****ab", output : true
Pattern = "baaa?ab", output : true
Pattern = "ba*a?", output : true
Pattern = "a*ab", output : false 

"""
###################################################################
# import re

# # Add or remove the words in this list to vary the results
# wordlist = ["color", "colour", "work", "working",
#             "fox", "worker", "working"]

# for word in wordlist:
#         # The . symbol is used in place of ? symbol
#         if re.search('col.r', word) : 
#                 print (word)

##############################################################
# import re

# # Add or remove the words in this list to vary the results
# wordlist = ["color", "colour", "work", "working",
#             "fox", "worker"]

# for word in wordlist:
#         # The .+ symbol is used in place of * symbol
#         if re.search('work.+', word) : 
#                 print (word)

############################################################
# import fnmatch

# strings = ['data1.txt', 'config.ini', 'data23.csv', 'image.png']
# pattern = 'data*.txt'

# filtered = fnmatch.filter(strings, pattern)
# print(filtered)  
# # Outputs: ['data1.txt']
############################################################
# import fnmatch

# strings = ['report1.doc', 'slide.ppt', 'report12.pdf', 'summary.doc']
# pattern = 'report?.doc'

# filtered = [s for s in strings if fnmatch.fnmatch(s, pattern)]
# print(filtered)  # Outputs: ['report1.doc']

###################################################################
import re

strings = ['hello_world.py', 'helloWorld.py', 'hi_world.py','hellow.py']
pattern = re.compile(r'hello.*\.py')

filtered = [s for s in strings if re.match(pattern, s)]
print(filtered)  # Outputs: ['hello_world.py']

################################################################