# Dictionaries:
# A dictionary is a collection which is unordered, changeable and indexed. In Python
# dictionaries are written with curly brackets, and they have keys and values.
# • Key-value pairs
# • Unordered
# We can construct or create dictionary like:
# X={1:’A’,2:’B’,3:’c’}
# X=dict([(‘a’,3) (‘b’,4)]
# X=dict(‘A’=1,’B’ =2)

# Methods that are available with dictionary are tabulated below. Some of them have already
# been used in the above examples.
# Method Description
# clear() === Remove all items form the dictionary.


# copy() ===Return a shallow copy of the dictionary.
# fromkeys(seq[, v]) ===Return a new dictionary with keys from seq and value equal to v (defaults to None).
# get(key[,d])===Return the value of key. If key doesnot exit,return d (defaults to None).
# items()===Return a new view of the dictionary's items (key, value).
# keys() ===Return a new view of the dictionary's keys.
# pop(key[,d])
# Remove the item with key and return its value
# or d if key is not found. If d is not provided
# and key is not found, raises KeyError.
# popitem() ===Remove and return an arbitary item (key,value). Raises KeyError if the dictionary isempty.
# setdefault(key[,d])===If key is in the dictionary, return its value. Ifnot, insert key with a value of d andreturn d (defaults to None).
# update([other])===Update the dictionary with the key/value pairsfrom other, overwriting existing keys.
# values()=== Return a new view of the dictionary's values