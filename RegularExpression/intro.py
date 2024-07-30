"""
#regular expression
A regular expression is a special sequence of characters that helps you match or find other strings or sets of 
trings, using a specialized syntax held in a pattern.

#applications
Large scale text processing in data science projects requires manipulation of textual data.
##############################
##Raw Strings
Regular expressions use the backslash character ('\') to indicate special forms or to allow special characters to be used without invoking their special meaning.

normal="Hello"
print (normal)
Hello
raw=r"Hello"
print (raw)
Hello

>>> normal="Hello\nWorld"
>>> print (normal)
Hello
World
>>> raw=r"Hello\nWorld"
>>> print (raw)
Hello\nWorld
#########################################
###Meta characters
Meta characters are characters having a special meaning, similar to * in wild card.

Here's a complete list of the metacharacters −

. ^ $ * + ? { } [ ] \ | ( )
################################
##Match functions
re.match() Function
This function attempts to match RE pattern at the start of string with optional flags.

Here is the syntax for this function −

re.match(pattern, string, flags=0)
########################

Matching Vs Searching
Python offers two different primitive operations based on regular expressions :match checks for a match
 only at the beginning of the string, while search checks for a match anywhere in the string .
 


"""
import re

x=re.search(r'^Eat', "Eat cake!").group()

#y=re.search(r'^eat', "Let's eat cake!").group()
y=re.search(r'eat', "Let's eat cake!").group()
z=re.search(r'eat', "Let's eat cake!")
print(x)
print(y)
print(z)