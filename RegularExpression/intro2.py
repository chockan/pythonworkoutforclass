"""
[] - Square brackets

Square brackets specifies a set of characters you wish to match.

Expression	String	Matched?
[abc]	      a	    1 match
             ac	    2 matches
         Hey Jude	No match
        abc de ca	5 matches
###########
import re

txt = "The rain in Spain"

#Find all lower case characters alphabetically between "a" and "m":

x = re.findall("[a-m]", txt)
print(x)

#################################################
        
You can also specify a range of characters using - inside square brackets.

[a-e] is the same as [abcde].
[1-4] is the same as [1234].
[0-39] is the same as [01239]
###############################################
You can complement (invert) the character set by using caret ^ symbol at the start of a square-bracket.

[^abc] means any character except a or b or c.
[^0-9] means any non-digit character.
###################################################
. - Period

A period matches any single character (except newline '\n').

Expression	String	Matched?
..	           a	No match
              ac	1 match
             acd	1 match
             acde	2 matches (contains 4 characters)

#######
import re

txt = "hello planet"

#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":

x = re.findall("he..o", txt)
print(x)
#################################################
^ - Caret

The caret symbol ^ is used to check if a string starts with a certain character.

Expression	String	Matched?
^a	           a	1 match
             abc	1 match
             bac	No match
^ab	         abc	1 match
             acb	No match (starts with a but not followed by b)
############
import re

txt = "hello planet"

#Check if the string starts with 'hello':

x = re.findall("^hello", txt)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")
###################################################
             
$ - Dollar

The dollar symbol $ is used to check if a string ends with a certain character.

Expression	String	Matched?
a$	           a	1 match
           formula	1 match
             cab	No match
########
import re

txt = "hello planet"

#Check if the string ends with 'planet':

x = re.findall("planet$", txt)
if x:
  print("Yes, the string ends with 'planet'")
else:
  print("No match")

#####################################################
* - Star

The star symbol * matches zero or more occurrences of the pattern left to it.

Expression	String	Matched?
ma*n	      mn	1 match
             man	1 match
            maaan	1 match
            main	No match (a is not followed by n)
            woman	1 match
#######
import re

txt = "hello planet"

#Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":

x = re.findall("he.*o", txt)

print(x)
#################################################
+ - Plus

The plus symbol + matches one or more occurrences of the pattern left to it.

Expression	String	Matched?
ma+n	      mn	No match (no a character)
             man	1 match
            maaan	1 match
            main	No match (a is not followed by n)
           woman	1 match
########
import re

txt = "hello planet"

#Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o":

x = re.findall("he.+o", txt)

print(x)
#################################################
? - Question Mark

The question mark symbol ? matches zero or one occurrence of the pattern left to it.

Expression	String	Matched?
ma?n	      mn	1 match
             man	1 match
           maaan	No match (more than one a character)
            main	No match (a is not followed by n)
           woman	1 match
#######
import re

txt = "hello planet"

#Search for a sequence that starts with "he", followed by 0 or 1  (any) character, and an "o":

x = re.findall("he.?o", txt)

print(x)

#This time we got no match, because there were not zero, not one, but two characters between "he" and the "o"
######################################################
{} - Braces

Consider this code: {n,m}. This means at least n, and at most m repetitions of the pattern left to it.

Expression	String	       Matched?
a{2,3}	    abc dat	       No match
           abc daat	      1 match (at daat)
          aabc daaat	2 matches (at aabc and daaat)
         aabc daaaat	2 matches (at aabc and daaaat)
#######
import re

txt = "hello planet"

#Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":

x = re.findall("he.{2}o", txt)

print(x)
#########################################################
Expression	         String	       Matched?
[0-9]{2,4}	       ab123csde	1 match (match at ab123csde)
               12 and 345673	3 matches (12, 3456, 73)
                   1 and 2	    No match
#####################################################
| - Alternation

Vertical bar | is used for alternation (or operator).

Expression	  String	Matched?
a|b	            cde	    No match
                ade	    1  match (match at ade)
              acdbea	3 matches (at acdbea)
###########
import re

txt = "The rain in Spain falls mainly in the plain!"

#Check if the string contains either "falls" or "stays":

x = re.findall("falls|stays", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
##################################################
() - Group

Parentheses () is used to group sub-patterns. For example, (a|b|c)xz match any string that matches either a or b or c followed by xz

Expression	        String	      Matched?
(a|b|c)xz	        ab xz	    No match
                    abxz	    1 match (match at abxz)
                  axz cabxz	    2 matches (at axzbc cabxz)
########################################################
\ - Backslash

Backlash \ is used to escape various characters including all metacharacters. 
For example,

\$a match if a string contains $ followed by a. Here,
 $ is not interpreted by a RegEx engine in a special way.

 ######1
 import re

# Pattern to match if a string contains the literal sequence \d+
pattern = r"\\d\+"
text = "This string contains the sequence \\d+ and some other text."
matches = re.findall(pattern, text)
print(matches)

######2
import re

# Pattern to match if a string contains $ followed by a
pattern = r"\$a"
text = "This string contains $a and some other text."
matches = re.findall(pattern, text)
print(matches) 
###########################################################
Special Sequences

Special sequences make commonly used patterns easier to write. Here's a list of special sequences:

\A - Matches if the specified characters are at the start of a string.

Expression	     String	        Matched?
\Athe	        the sun	         Match
               In the sun	     No match
#########
import re

txt = "The rain in Spain"

#Check if the string starts with "The":

x = re.findall("\AThe", txt)

print(x)

if x:
  print("Yes, there is a match!")
else:
  print("No match")
##########################################################
\b - Matches if the specified characters are at the beginning or end of a word.

Expression	            String	       Matched?
\bfoo	             football	       Match
                   a football	      Match
                   afootball	     No match
#########
import re

txt = "The rain in Spain"

#Check if "ain" is present at the beginning of a WORD:

x = re.findall(r"\bain", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
###########
foo\b	           the foo	         Match
                the afoo test	     Match
                the afootest	   No match
##########
import re

txt = "The rain in Spain"

#Check if "ain" is present at the end of a WORD:

x = re.findall(r"ain\b", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
##############################################################
\B - Opposite of \b. Matches if the specified characters are not at the beginning or end of a word.

Expression	              String	         Matched?
\Bfoo	                  football	          No match
                          a football	       No match
                           afootball	        Match
########
import re

txt = "The rain in Spain"

#Check if "ain" is present, but NOT at the beginning of a word:

x = re.findall(r"\Bain", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
#########
foo\B	                   the foo	           No match
                           the afoo test	    No match
                             the afootest	    Match 
#########
import re

txt = "The rain in Spain"

#Check if "ain" is present, but NOT at the end of a word:

x = re.findall(r"ain\B", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
###########   
##############################################################           
\d - Matches any decimal digit. Equivalent to [0-9]

Expression	           String	       Matched?
\d	                   12abc3	       3 matches (at 12abc3)
                        Python	        No match
#########
import re

txt = "That will be 59 dollars"

#Find all digit characters:

x = re.findall("\d", txt)
print(x)
##########
import re

txt = "The rain in Spain"

#Check if the string contains any digits (numbers from 0-9):

x = re.findall("\d", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
############################################################
\D - Matches any non-decimal digit. Equivalent to [^0-9]

Expression	           String	         Matched?
\D	                  1ab34"50	        3 matches (at 1ab34"50)
                        1345	        No match
#########
import re

txt = "The rain in Spain"

#Return a match at every no-digit character:

x = re.findall("\D", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

###############################################################
\s - Matches where a string contains any whitespace character. Equivalent to [ \t\n\r\f\v].

Expression	           String	           Matched?
\s	                 Python RegEx	       1 match
                       PythonRegEx	        No match

#########
import re

txt = "The rain in Spain"

#Return a match at every white-space character:

x = re.findall("\s", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
###############################################################
\S - Matches where a string contains any non-whitespace character. Equivalent to [^ \t\n\r\f\v].

Expression	                  String	           Matched?
\S	                            a b	           2 matches (at  a b)
 	                                           No match
###########
import re

txt = "The rain in Spain"

#Return a match at every NON white-space character:

x = re.findall("\S", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
############################################################
\w - Matches any alphanumeric character (digits and alphabets). Equivalent to [a-zA-Z0-9_]. By the way, underscore _ is also considered an alphanumeric character.

Expression	             String	             Matched?
\w	                       12&": ;c 	     3 matches (at 12&": ;c)
                           %"> !	         No match
###########
import re

txt = "The rain in Spain"

#Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character):

x = re.findall("\w", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
##############################################################
\W - Matches any non-alphanumeric character. Equivalent to [^a-zA-Z0-9_]

Expression	            String	                Matched?
\W	                      1a2%c	              1 match (at 1a2%c)
                          Python	            No match
###########
import re

txt = "The rain in Spain"

#Return a match at every NON word character (characters NOT between a and Z. Like "!", "?" white-space etc.):

x = re.findall("\W", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
##############################################################
\Z - Matches if the specified characters are at the end of a string.

Expression	           String	              Matched?
Python\Z	        I like Python	          1 match

               I like Python Programming	  No match
                Python is fun.	              No match
###########
import re

txt = "The rain in Spain"

#Check if the string ends with "Spain":

x = re.findall("Spain\Z", txt)

print(x)

if x:
  print("Yes, there is a match!")
else:
  print("No match")
############################################################
"""