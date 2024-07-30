"""
##############Extended Regular Expressions:
Extended regular expressions include additional features such as grouping, alternation, and quantifiers.
Grouping is =====achieved by enclosing part of the pattern in parentheses ().
Alternation is======= represented by the | symbol, which matches either the expression on the left or the expression on the right.
Quantifiers ========include {m} (matches exactly m occurrences), {m,} (matches m or more occurrences), and {m,n} (matches between m and n occurrences).

#######python
#######Copy code
import re

# Match words that start with "c" or "s" and end with "at"
pattern = "(c|s)at"
text = "The cat sat on the mat."
matches = re.findall(pattern, text)
print(matches)  # Output: ['cat', 'sat', 'mat']
Extended regular expressions allow for more complex pattern matching and manipulation of text data in Python. They are especially useful when dealing with structured text data or performing more advanced text processing tasks.

"""